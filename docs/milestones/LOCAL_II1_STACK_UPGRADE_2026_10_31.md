# Authorized local II-1 stack upgrade — 2026-10-31

Status: COMPLETE locally. The owner explicitly requested the previously described backup-preserving local upgrade. This supersedes the existing-stack/private-configuration exclusion only for this action. No production, REAL-data, Git publication, destructive migration, credential/role provisioning or AEO change is authorized or performed.

## Actual actions and evidence

Used existing local configuration and saved development account without displaying secrets. Independently built Operations/Gateway, stopped only Operations for a consistent custom-format backup, validated the archive with pg_restore --list, added only the new crop-health queue/DLQ/four bindings, then recreated Operations/Gateway with --no-deps --no-build. Service-owned Flyway applied additive V5; V1–V4 and all old records remain.

Backup: Infrastructure `target/local-backups/operations-before-ii1-20261031T171624Z.dump`. Exact archive checksum/size, pre/post table counts and business/evidence fingerprints, source/revision/index/config fingerprints, broker inventory and container states are in ignored Infrastructure `target/ii1-local-upgrade.json`. Do not publish that operational evidence or the backup. No business payloads, credentials or bearer tokens are reproduced here.

Running Operations image: `sha256:d26489eb4b567e0ce82a79b9bea6237ed8d0e9d4eb62100673a69ab9d09ab62a`; Gateway: `sha256:49837d13a49da5c0478f6476a8fb7aac09d071c899f925feecaee265282168bb`. Existing Compose image/version labels remain their independent application labels; these rebuilt local images now contain II-1.

PASS: all nine services healthy. Only Operations/Gateway were recreated; other container identities/images/start times and PostgreSQL/RabbitMQ volume mounts are unchanged. All legacy Operations table counts and business/evidence fingerprints are unchanged (outbox relay metadata is allowed to advance). Estate/Spatial business records match pre-upgrade fingerprints. Existing runtime/migration/broker/OIDC environment fingerprints, database role attributes, private configuration/saved-account file hashes, Web config/index and all six product Git indexes remain unchanged. V5 adds only its accepted table grants to the existing restricted runtime role; no role, password, account or realm provisioning occurred.

Broker verification preserved every pre-existing queue configuration and binding. New bounded durable `agrosphere.dev.crop-health.v1` and its DLQ, plus the four explicit bindings, are present. RabbitMQ reports an additional default `x-queue-type=classic`; the initial exact-dictionary comparison paused before migration and was corrected to verify that explicit default plus every requested argument. A retained-service-inventory variable in the continuation also paused post-upgrade verification; only read-only verification was resumed. Backup was retained, no migration/deployment was repeated and no destructive rollback occurred. Final verification passes.

## Read-only functional checks

Existing-account real PKCE/JWT queries through Gateway return HTTP 200 for both inspections and incidents for SIM-GA-DEMO and SIM-MW-DEMO. Both estates still have two rubber fields and four explicitly SIMULATED spatial features each. Observed database totals after upgrade: **0 inspections and 0 incidents**. These are measured empty totals, not invented crop observations; no report or other business record was seeded/created.

A real headless browser independently verified all four estate/module combinations, enabled Record simulated inspection / Report simulated incident controls, and two active field choices in each draft. Drafts were discarded. All business HTTP writes were blocked, and none was attempted. No trace, screenshot, video, token or report content was recorded. Ignored browser evidence: Web `target/ii1-local-browser.json`. Existing credentials/roles were used unchanged.

Refresh localhost:4200/inspections or /incidents and select the estate. Empty-state text is expected until the owner creates a SIMULATED record through the UI. CLEAR saves an inspection only; FOLLOW_UP atomically creates its first linked incident; an incident can also be reported directly. Boundaries/field metadata do not automatically generate crop observations. Incident filters default to OPEN/IN_REVIEW; use all statuses to inspect resolved/voided reports.

II-D07/08, WA D08/D09, REAL collection, M2 performance and production acceptance remain open. No more stack upgrade or repeated approval is needed for this completed action. Preserve the backup, current records/volumes/config/roles and all staged changes. Future report creation is an explicit user action; do not seed demos or enable REAL automatically.
