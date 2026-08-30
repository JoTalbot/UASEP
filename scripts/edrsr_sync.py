#!/usr/bin/env python3
"""Sync official Ukrainian EDRSR open-data archives to a Hugging Face Dataset.

This first-stage implementation deliberately preserves the official ZIP as a
raw artifact and records provenance. Parsing into structured Parquet is a
separate stage because the archive schema must be verified against the current
official README before transforming millions of records.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import tempfile
import urllib.request
from datetime import datetime, timezone
from typing import Any

from huggingface_hub import HfApi

DATASET_IDS = {
    2026: "16ab7f06-7414-405f-8354-0a492475272d",
    2025: "ediniy-derzhavniy-reestr-sudovih-rishen-za-2025-rik_879",
}
CKAN_API = "https://data.gov.ua/api/3/action/package_show?id={dataset_id}"


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_resource(year: int) -> tuple[str, str, dict[str, Any]]:
    dataset_id = DATASET_IDS.get(year, f"ediniy-derzhavniy-reestr-sudovih-rishen-za-{year}-rik")
    url = CKAN_API.format(dataset_id=dataset_id)
    with urllib.request.urlopen(url, timeout=60) as response:
        payload = json.load(response)
    if not payload.get("success"):
        raise RuntimeError(f"data.gov.ua CKAN request failed for {year}")
    resources = payload["result"].get("resources", [])
    expected = f"edrsr_data_{year}.zip".lower()
    for resource in resources:
        name = str(resource.get("name", "")).lower()
        if expected in name and resource.get("url"):
            return resource["url"], dataset_id, resource
    raise RuntimeError(f"Could not find {expected} in data.gov.ua metadata")


def download(url: str, destination: pathlib.Path) -> None:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "UASEP-EDRSR-Sync/1.0"},
    )
    with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as output:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            output.write(chunk)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--repo", default=os.environ.get("HF_DATASET_REPO", ""))
    parser.add_argument("--token", default=os.environ.get("HF_TOKEN", ""))
    parser.add_argument("--source-url", default="")
    args = parser.parse_args()

    if not args.repo:
        raise SystemExit("HF_DATASET_REPO is required")
    if not args.token:
        raise SystemExit("HF_TOKEN is required")

    source_url, dataset_id, resource = resolve_resource(args.year)
    if args.source_url:
        source_url = args.source_url

    with tempfile.TemporaryDirectory(prefix="uasep-edrsr-") as tmp:
        archive = pathlib.Path(tmp) / f"edrsr_data_{args.year}.zip"
        download(source_url, archive)
        digest = sha256_file(archive)
        now = datetime.now(timezone.utc).isoformat()
        manifest = {
            "dataset": "Єдиний державний реєстр судових рішень",
            "year": args.year,
            "source": source_url,
            "source_catalog": f"https://data.gov.ua/dataset/{dataset_id}",
            "resource_name": resource.get("name"),
            "source_updated": resource.get("last_modified") or resource.get("metadata_modified"),
            "downloaded_at": now,
            "size_bytes": archive.stat().st_size,
            "sha256": digest,
            "stage": "raw",
            "notes": "Official source archive preserved without transformation.",
        }

        api = HfApi(token=args.token)
        api.upload_file(
            path_or_fileobj=str(archive),
            path_in_repo=f"raw/edrsr_data_{args.year}.zip",
            repo_id=args.repo,
            repo_type="dataset",
            commit_message=f"data: sync EDRSR {args.year}",
        )
        api.upload_file(
            path_or_fileobj=json.dumps(manifest, ensure_ascii=False, indent=2).encode("utf-8"),
            path_in_repo=f"manifests/{args.year}.json",
            repo_id=args.repo,
            repo_type="dataset",
            commit_message=f"data: add EDRSR {args.year} manifest",
        )

    print(json.dumps(manifest, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
