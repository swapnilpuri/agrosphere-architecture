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

## Owner-approved II-1 — 2026-10-31

See docs/milestones/INCIDENT_INSPECTION_APPROVAL.md and accepted ADR 0015. II-D01–10 and dependency-ordered II-T01–09 are accepted for block inspections and manually managed crop-health incidents. Preserve reviewed package bytes. Isolated executable contracts need exact independent acceptance/local release before pinning; pure domain/ports may proceed independently. II-D07/08 and WA D08/D09 remain open downstream gates; SIMULATED-only development, existing data/configuration and production/Git/role/credential/AEO exclusions persist.

## Owner-approved AN-1 — 2026-10-31

See docs/milestones/ALERTS_NOTIFICATIONS_APPROVAL.md and accepted ADR 0016. AN-D01–10 and dependency-ordered AN-T01–09 are accepted for the SIMULATED in-app crop-health estate inbox. Preserve reviewed package bytes; exact executable acceptance/local release precedes pins. Pure rules/ports may proceed independently; persistence follows stable reviewed schema. AN-D07/08 subject-policy/workload and WA/II/M2 gates stay open. No non-generated rollout, REAL, existing-stack/private configuration, roles/credentials, external delivery, Git/deployment/destructive or AEO change.

## AN-1 exact executable accepted — 2026-10-31

Architecture ALERTS_NOTIFICATIONS_CONTRACT_APPROVAL.md records owner acceptance of the exact four artifacts, local Contracts 0.8.0 release and Operations/Web pins. Continue accepted AN-T03–09 by dependency; preserve prior features/artifacts and reviewed bytes. Generated-only verification; AN-D07/08 and WA/II/M2 gates remain open. No non-generated account rollout, REAL, existing-stack/private configuration/role/credential/external delivery/Git/deployment/destructive/data-reset/AEO action. Gateway adds only /api/v1/alerts/**; Infrastructure generated-only drills reuse existing topology without a new alert queue.

## AN-1 local verification state — 2026-10-31

Architecture ALERTS_NOTIFICATIONS_VERIFICATION.md records local implementation and generated-only checks after exact executable acceptance. Earlier preparation labels are historical. Preserve 0.8.0 pins/old bytes/V1–V5/Web config/index and existing data/volumes. Default-disabled subject-policy gate, AN-D07/08, WA/II/M2 and no non-generated rollout/REAL/live-stack/private configuration/role/credential/Git/deployment/AEO exclusions remain.

## Owner-approved AN privacy extension — 2026-10-31

Architecture ALERTS_PRIVACY_APPROVAL.md records exact five-artifact privacy candidate acceptance (manifest ea6402a205d1da7a0801090b0acabac58ae164ba6544b474d709d8a4a608286b), local independent Contracts 0.9.0 release/archive/pins and generated-only AP-T02–07 implementation. Preserve accepted bytes, V1–V6, old events/records and all staged work/Web config. Additive privacy storage and narrowly scoped maintenance may be tested only in separately owned disposable generated databases. No existing-stack/private configuration/actual-account/REAL/existing role or credential/destructive migration/historical conversion/external delivery/Git publication/deployment/AEO action. AP-T08 local-stack execution remains separately gated; do not repeat II-1. Prior approval/pending labels remain historical within their scope; do not ask again for this exact acceptance.
