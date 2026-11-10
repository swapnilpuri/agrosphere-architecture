# Current M4 acceptance and prompt handoff - 2026-11-10

[Owner acceptance](../milestones/M4_OWNER_ACCEPTANCE_2026_11_10.md) closes the delivered bounded M4 functional acceptance. Prior OPEN labels below are historical for that package only; separate ANL and other tracked gates persist. [Milestone/phase prompts](prompts/README.md) are ready for owner selection. No next milestone has started.

# M4 engineering handoff — 2026-11-10

The owner's single approved remaining-M4 package is implemented and locally generated-verified; [delivery and actual evidence](../milestones/M4_DELIVERY_VERIFICATION_2026_11_10.md). D07's deterministic provider and D01's bounded dry/wet observed-mass interpretation were explicitly accepted. Owner functional acceptance remains OPEN. This backlog grants no authority to start another milestone: wait for the owner's milestone prompt. Prior pending/preparation/Ollama scheduling labels below are historical within their scope; all original M0–M5/field/REAL requirements remain in the sole checklist.

# Milestone delivery anchor — 2026-11-05

Use the [consolidated remaining-M4 package](../milestones/M4_DELIVERY_PACKAGE.md) as the one proposed delivery review. It covers all remaining M4 capabilities through a working generated demonstration, with explicit bounded yield and deterministic-provider scope decisions. Approval is pending; this file grants no implementation authority. Old priority rows and Ollama expectation below are retained historical requirements; D07 proposes their explicit POC disposition rather than silently treating an LLM as delivered. Existing original-milestone/field/REAL gates remain in the sole completion checklist.

# Current sequencing anchor — 2026-11-01

The [original M0–M5 roadmap](MILESTONES.md) and [completion checklist](PROJECT_COMPLETION_CHECKLIST.md) now govern progress and the finite SIMULATED local POC finish line. The [checkpoint](../milestones/DEVELOPMENT_CHECKPOINT.md) owns next action/authorization. Offline Android capture/sync and English/French remain confirmed field-release requirements; real-data/production operating readiness is tracked separately. All accepted requirements/approvals persist. Foundation-only/future-work/old-priority statements below are historical, superseded for current status and scheduling; they grant no new implementation authority.

# Implementation backlog
| Priority / ID | Work | Owner | Acceptance / dependency |
|---|---|---|---|
| P0 M1-01 | Define estate/block OpenAPI commands/queries and error envelope | contracts + estate | Contract review, pagination, UUIDs, validation, authorization; no geometry in estate |
| P0 M1-02 | Implement estate domain/use cases/adapters and business migrations | estate | Company/estate/division/block tests with Java 25 and PostgreSQL Testcontainers |
| P0 M1-03 | Create synthetic rubber estate/block GeoJSON with provenance | spatial | RFC 7946, closed valid polygons, explicit accuracy and canonical UUID fixtures |
| P0 M1-04 | Implement geometry ingestion/bbox/intersection contract and PostGIS adapters | spatial | CRS/SRID 4326, geometry validity, no cross-DB lookup, spatial Testcontainers tests |
| P0 M1-05 | Provision identity realm/PKCE clients and audience/estate authorization | infrastructure + services | Deny wrong issuer/audience/estate, unauthenticated commands and expired tokens |
| P0 M1-06 | Implement outbox relay and idempotent identity consumer | estate + spatial | Confirm/crash/redelivery tests; no loss or duplicate effect; DLQ/replay documented |
| P0 M1-07 | Verify database isolation, migrations and backup procedure | infrastructure | Each role denied other service DB access; fresh/upgrade migration tests |
| P1 M1-08 | Add gateway routes, limits, correlation and contract integration tests | gateway | No domain logic; choose limiter store first; rate-limit and JWT tests |
| P1 M1-09 | Reproducible local estate/GIS demo guide | architecture | Health, sample data, calls and teardown documented; no production deployment |
| P1 M2-01 | Cesium asset/worker pipeline, terrain and block selection | web | Licensing, provenance, IDs, source accuracy and performance measured |
| P1 M3-01 | Tapping/latex/DRC and crop incident use cases | operations | Explicit kg/percent, valid ranges and unique event identity |
| P1 M3-02 | Authenticated MQTT normalization and simulated sensors | telemetry | Device ownership, timestamp policy, units, event contract and replay tests |
| P1 M4-01 | Materialized projections and historical KPIs | analytics | Eventual consistency, rebuild/reconciliation and projection schema ownership |
| P1 M4-02 | Baseline forecasting/anomaly evaluation and model registry | AI | Chronological holdout, baseline metrics, evidence/model version, predicted labels |
| P2 M4-03 | Ollama adapter and assistant evidence links | AI | Provider boundary, prompt/versioning, evaluation and authorization |
| P2 M5-01 | UE authoritative API adapter/georeference/selection | immersive | Install matching licensed toolchain, no claimed surveyed procedural trees |
| P2 M5-02 | VR prototype and MR feasibility | immersive | Supported device, comfort/frame-time evidence, tracking accuracy limitations |

Before the first business endpoint: confirm license/ownership, tenancy assumptions, authorization model and current dependency security status.

## Owner-approved WA-1 — 2026-10-29

Prioritize the estate worker register and daily attendance before the proposed incident/inspection increment. Follow WA-T00–WA-T09 in the [accepted review package](../milestones/WORKER_ATTENDANCE_REVIEW.md), with [dated approval](../milestones/WORKER_ATTENDANCE_APPROVAL.md), independent executable-contract review/release/pinning, and D08/D09 acceptance gates. This is a separate capability; do not silently rename provisional 3C or claim parent Milestone 3/M2 performance completion. Current task/evidence state belongs in DEVELOPMENT_CHECKPOINT.md.

## Owner-approved II-1 — 2026-10-31

WA-1 is locally delivered; II-1 is the next accepted bounded Operations increment (provisional 3C). Follow [II-T00–09](../milestones/INCIDENT_INSPECTION_REVIEW.md) and [dated approval](../milestones/INCIDENT_INSPECTION_APPROVAL.md). Executable candidate review/local release/pinning remains independent; REAL/privacy/load/M2 gates and deferred alert delivery remain visible. Do not interpret parent M3/M4 rows as authorization to implement MQTT/Analytics alongside it.

## Owner-approved AN-1 — 2026-10-31

II-1 and its separately authorized local stack upgrade are complete. Proceed with the [accepted AN-1 tasks](../milestones/ALERTS_NOTIFICATIONS_REVIEW.md) by dependency; see [approval](../milestones/ALERTS_NOTIFICATIONS_APPROVAL.md). Isolated executable candidate review/release precedes runtime pins. Generated-only pure rules/ports can proceed independently. Keep subject-policy/workload, WA/II/M2/REAL and functional acceptance gates open; MQTT/Analytics and external notification delivery remain separate scopes.
