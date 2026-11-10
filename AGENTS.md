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


## Owner-approved TLM-01 preparation — 2026-11-01

Architecture docs/milestones/MQTT_POC_APPROVAL.md records acceptance of exact MQTT_POC_REVIEW.md SHA-256 84ba22535e81de2296d76746c612325571ea6364962bb42d7fe2138716dd3dbd. Authorizes isolated Contracts candidate and Telemetry pure domain/ports/tests only, SIMULATED. Exact executable acceptance/local release precedes promotion/pins/adapters; broker ACL/provisioning/migrations need later scoped review. Preserve all old release bytes, V1, indexes/config/data and independent builds. No live MQTT, database, actual account, role/credential, private configuration, REAL, Git publication/deployment or AEO action.


## TLM-01 exact local release/pins approved — 2026-11-01

Architecture MQTT_POC_CONTRACT_APPROVAL.md records owner acceptance of all eight artifacts in manifest 174140bc1db129ab879d9e431e9065a6715746c31c70fa0ec2bb7992063f01b0 and local Contracts 0.10.0 archive/promotion/release metadata plus exact Telemetry API/MQTT/event pins. Historical pending labels are satisfied only for this scope. Preserve exact candidate/review/archive/old artifacts and all existing indexes/config/data. Prepare broker ACL/provisioning/migration review before adapters; no live stack, role/credential, private configuration, REAL, Git publication/deployment or AEO action.


## TLM-01 adapters authorized — 2026-11-01

Architecture MQTT_POC_ADAPTER_APPROVAL.md accepts exact package 389f1d3cfa6ca80fd602c2f945b9f23965723b53d5ca169919f7e11099e2bc75. Implement Telemetry SIMULATED ingestion/persistence/outbox/latest API, Gateway telemetry route only and Infrastructure generated-only owned disposable drills. Exact SQL/ACL/client engineering review and generated fixture credentials included. No repeated domain/executable approval. Preserve Contracts 0.10.0 pins, old migrations/config/data/indexes, existing stacks/private config/roles/credentials, REAL/Git/deployment/AEO exclusions.


## Owner-approved TLM-02 — 2026-11-04

Architecture MQTT_POC_OVERLAY_APPROVAL.md accepts exact review 0d8a67aef15b295dbca267adad300ab0c94c2c88ec37cbff0c6a69c1ff7a49c9. Implement bounded deterministic SIMULATED fixture publisher and read-only selected-block Web detail/freshness overlay using unchanged Contracts 0.10.0 pin. Generated-only disposable verification, no new schema/role, no repeated executable approval. Preserve existing UI/config/index/data and all original gates; no existing-stack/private config/REAL/production/Git/deployment/AEO action.


## Owner-approved ANL-01 preparation — 2026-11-05

Architecture ANALYTICS_POC_APPROVAL.md records acceptance of exact review SHA-256 3f4b8ee7c521502e0a29196ab647d84598dcb09aa91700856ef1bdc36e452342. Isolated Contracts candidate/validation and Analytics pure domain/ports/tests only, SIMULATED. Preserve reviewed/released bytes, V1, configuration/data/indexes and independent builds. Exact executable acceptance/local release precedes promotion/pins; runtime SQL/consumer/queue/security/provisioning needs subsequent bounded review. No adapters, running API/broker/database, existing-stack/role/credential/private configuration, REAL, Git publication/deployment or AEO action.


## ANL-01 exact local release/pins approved — 2026-11-05

Architecture ANALYTICS_POC_CONTRACT_APPROVAL.md accepts exact manifest 43d9e5f7b328002c735cdf85da3f6ed5e0c9ff41a2f74aaccdcc0b8e8a396998 for ten artifacts/four unchanged inputs, local Contracts 0.11.0 archive/promotion and independent Analytics pins only. Preserve old bytes/reviews/data/config/indexes. Concrete runtime SQL/consumer/queue/security/provisioning review remains required; no runtime/Gateway/Web/existing-stack/REAL/Git/deployment/AEO authority. Do not repeat satisfied preparation/executable approvals.


## ANL-01 bounded runtime continuation — 2026-11-05

Owner instructed "please resume" immediately after the bounded runtime/dashboard approval request. Architecture ANALYTICS_POC_ADAPTER_APPROVAL.md records that continuation authority for exact review 855fe1894c530cf7942d3175e7a3eae850d0b34abff976a5e6bf7ba87a5618f3: SIMULATED materialized Analytics, Analytics-only Gateway route, read-only Web dashboard and new owned disposable verification. Existing 0.11.0 contracts/pins unchanged; exact SQL/grant engineering review precedes new-fixture installation. No existing-stack/private config/data/roles/credentials, REAL, production/Git/deployment/AEO action. Preserve indexes/prior features and original owner/field/milestone gates.


## ANL-01 finite admission approved

Owner approved exact admission review SHA-256 5c9a6787f0ebf2ad0d3d172e5fc3ac2ebb9d83ea9936c3664331fa81fe8629f8. Architecture ANALYTICS_POC_ADMISSION_APPROVAL.md records finite generated profile, bounded parser/diagnostic/test changes and new owned disposable verification. Prior approvals satisfied; preserve exact contracts, migrations, indexes/private config/data and all owner/field/REAL/AEO/Git/deployment exclusions.


## ANL-02 preparation approved; new-session start

Owner approved exact environmental preparation review SHA-256 c15ac50638feb09b176a44b5b16033d50e1b7365cbbe4467550f25d5910a17e9 and requested starting in a new session. See docs/milestones/ANALYTICS_ENVIRONMENT_POC_APPROVAL.md and current checkpoint. Isolated Contracts candidate/Analytics pure rules/ports/tests only; no repeated preparation approval, runtime/executable release or existing-target authority. Implementation remains unstarted at handoff.


## ANL-02 exact local release/pins approved — 2026-11-05

Architecture ANALYTICS_ENVIRONMENT_CONTRACT_APPROVAL.md records owner acceptance of manifest 1759e5d95fb3602b623b995e4650f035b67dbb550760116587f46c031ca7d111: fourteen artifacts/three unchanged inputs, local independent Contracts 0.12.0 archive/promotion/release metadata and Analytics API/Telemetry input pins only. Preserve old candidates/reviews/releases, four collection-v2 inputs, V1/V2/config/data/indexes. Preparation/executable gates satisfied; runtime/SQL/AMQP/HTTP/Web/queue/security/provisioning remains separately gated under ANL02_ADAPTER_REVIEW.md. No existing-target/private config/account/role/credential, REAL, Git publication/deployment or AEO authority.


## ANL-02 bounded runtime approved — 2026-11-05

Architecture ANALYTICS_ENVIRONMENT_ADAPTER_APPROVAL.md records owner acceptance of exact runtime/SQL manifest afff8ff5a13e1167d53ab569f0ea28c5f003def01fab9318db455f291f537ea8. Implement SIMULATED environmental parser/immutable persistence/consumer/scoped API, read-only Web with independent 0.12.0 pin and new owned disposable verification; generated fixture credentials included. Exact SQL/grant engineering review before installation. No new producer/role or Gateway prefix widening. Preserve old artifacts/V1/V2/config/data/index and all original gates. No existing-stack/private config/account/role/credential, REAL, Git publication/deployment or AEO action. Historical pending labels are superseded only for this scope.
