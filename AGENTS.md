# Repository instructions

Work only within this independent Git repository. No parent repository, submodules, shared persistence models, cross-service SQL or multi-service Maven parent.

Current scope: Architecture through requested Milestone 1C; document local integration decisions and actual validation. No service code here.

Use ports/adapters and service-owned migrations. APIs and events are designed in agrosphere-contracts; coordinate breaking changes through a versioned contract release, never a source path dependency. UUID estateId/blockId remain stable across clients. Mark data REAL, SIMULATED, ESTIMATED or PREDICTED. GeoJSON is WGS84 longitude/latitude (RFC 7946). Procedural trees are illustrative.

Never commit credentials, local environment files, generated datasets or large geospatial assets. Use environment examples containing placeholders only. No remote creation, push or cloud deployment is authorized.

Run repository checks documented in README.md. Report actual checks separately from unavailable checks. Version independently using SemVer and CHANGELOG.md; changes to 0.x contracts can still break consumers and require review.

## Continuous application development

The owner request dated 2026-10-27 authorizes application-development coordination and Milestone 3B readiness documentation in this repository, supplementing the historical scope above. Read [APPLICATION_DEVELOPMENT_WORKFLOW.md](docs/milestones/APPLICATION_DEVELOPMENT_WORKFLOW.md), then [DEVELOPMENT_CHECKPOINT.md](docs/milestones/DEVELOPMENT_CHECKPOINT.md) at the start of every session. Preserve all security, repository independence and contribution rules above. Follow the checkpoint to verify actual implementation and approvals; proposed 3B decisions are not accepted by this reference. AEO remains paused and untouched. Service implementation requires its applicable reviewed decisions and authorization. The owner accepted the 3B package and authorized T01–T09 on 2026-10-27; see [approval record](docs/milestones/MILESTONE_3B_APPROVAL.md). Follow dependencies and validation gates; production deployment, destructive migrations, secret-handling changes and AEO changes remain unauthorized.

## Scoped credential-wiring authorization - 2026-10-27

The owner authorizes the reviewed Operations-only runtime/Flyway wiring, tracked placeholders and provisioning-tool implementation, and generated credentials only in disposable tests. This supplements earlier secret-handling exclusions only for that scope. Do not read/modify existing private environment files, provision existing/running stacks, or change production/AEO state. See Architecture docs/milestones/MILESTONE_3B_CREDENTIAL_WIRING_APPROVAL.json and continue authorized T03-T09 in dependency order.

## Owner-approved WA-1 — 2026-10-29

See docs/milestones/WORKER_ATTENDANCE_APPROVAL.md and accepted ADR 0014. The owner accepted D01–D10 and authorized WA-T01–T09 in dependency order. Preserve the reviewed proposal bytes; the dated approval supersedes its historical status labels. Independent executable-contract acceptance/local release must precede pinning. D08 rollout/load inputs and D09 actual privacy/retention parameters remain acceptance gates; no REAL workforce collection is enabled. Preserve current Web changes/config and all production/AEO/Git exclusions.
