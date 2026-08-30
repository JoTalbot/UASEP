"""Runtime health state."""


def health_status() -> dict:
    return {"status": "ok", "service": "uasep-runtime"}
