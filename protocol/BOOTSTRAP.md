# Bootstrap Resolution

The bootstrap prompt is only a loader. The full protocol must be resolved from the strongest available source in this order:

1. Project-local `.uasep/` matching a compatible version.
2. Trusted UASEP source repository.
3. Bundled protocol supplied by the runtime.
4. Minimal embedded bootstrap behavior.

The agent must report which source was actually loaded. If no full protocol can be loaded, it may operate in degraded bootstrap mode but must not claim full UASEP compliance.

A project-local protocol may add project-specific rules but must not silently weaken core safety, truth, evidence, or integrity requirements.
