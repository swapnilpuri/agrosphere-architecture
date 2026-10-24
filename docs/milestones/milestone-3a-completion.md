# AGROSPHERE MILESTONE 3A COMPLETION REPORT

Status: COMPLETE — implemented and verified locally on 2026-10-24. No commit, push, remote CI run or shared-environment deployment was performed. Milestone 3B was not started.

## Executive summary

Rubber tapping is implemented in the independently buildable Operations service, from draft schedules through bounded, duplicate-safe dated assignments, owned-worker execution, missed reasons, cancellations, live summaries and atomic outbox events. PostgreSQL migrations and real RabbitMQ publication/retry have executed successfully. A disposable full Compose stack verified real Keycloak PKCE, Gateway routing, Estate HTTP validation, scoped worker execution, auditor denial, summaries and confirmed events.

## Repository changes

| Repository | Version | Changes |
|---|---|---|
| agrosphere-operations-service | 0.2.0 | Domain, application ports/services, DTO API, JDBC/Flyway, JWT authorization, Estate adapter, outbox/metrics, tests, pinned contracts, Docker and CI |
| agrosphere-estate-service | 0.2.2 | Small read-only authorization extension for scoped operational roles; existing GET master-data APIs reused; regression tests |
| agrosphere-api-gateway | 0.2.1 | Tapping route and bearer/query/correlation forwarding tests |
| agrosphere-contracts | 0.4.0 | Full Operations OpenAPI, six versioned schemas/examples, compatibility validation; existing event schemas unchanged |
| agrosphere-infrastructure | 0.3.0 | Operations Compose service, role/audience/subject configuration, durable development event sink, safe additive realm setup, isolated acceptance test |
| agrosphere-architecture | 0.5.0 | Discovery, ADR 0012, seven PlantUML diagrams, development guide, this report, updated validators/CI |

All twelve requested Git roots were inspected on main. Only Web had pre-existing uncommitted changes; no Web files were changed. Spatial, Telemetry, Analytics, AI and Immersive remain unchanged. No parent build, shared persistence model or sibling runtime source dependency was introduced.

## Implemented domain and persistence

TappingSchedule supports DRAFT/ACTIVE/SUSPENDED/CLOSED and versioned edits/lifecycle. TappingAssignment supports PLANNED/IN_PROGRESS/COMPLETED/MISSED/CANCELLED, scheduled/ad hoc creation, worker reassignment and explicit transitions. TappingRecord stores planned/actual trees, worker/estate/block/date, execution instants, notes and recording actor; missed reasons store validated code, remarks and authenticated actor. Audit instants are UTC; canonical estate timezone controls business dates. No latex weight or DRC exists.

V1__messaging_foundation.sql is preserved. V2__rubber_tapping.sql creates four operational tables, internal assignment/schedule/record/reason foreign keys, UUID keys, numeric/status constraints, version/audit fields and filter indexes. Schedule/date uniqueness permanently prevents regeneration; a partial worker/block/date index prevents duplicate noncancelled work. V2 adds outbox retry state/index and preserves existing published history (upgrade test executed). Estate/block UUIDs have no cross-service foreign keys.

## REST inventory

All paths start /api/v1/tapping. There are 18 HTTP operations across 15 paths.

| Method | Path | Behavior |
|---|---|---|
| POST / GET | /schedules | Create (201) / scoped page |
| GET / PATCH | /schedules/{id} | Read / replace draft editable configuration |
| POST | /schedules/{id}/activate | Activate or resume |
| POST | /schedules/{id}/suspend | Stop generation |
| POST | /schedules/{id}/close | Final schedule closure |
| POST | /schedules/{id}/generate-assignments | Bounded anchored recurrence, permanent occurrence deduplication |
| POST / GET | /assignments | Authorized ad hoc creation (201) / scoped filter page |
| GET | /assignments/{id} | Assignment plus execution/missed detail |
| PATCH | /assignments/{id}/worker | Reassign PLANNED work |
| POST | /assignments/{id}/start | Create execution and begin |
| POST | /assignments/{id}/complete | Validate actual trees and finalize |
| POST | /assignments/{id}/mark-missed | Required reason, today/past estate-local date |
| POST | /assignments/{id}/cancel | Management-only immutable cancellation |
| GET | /records | Scoped paginated execution records |
| GET | /summary | Total, worker or block counts/trees; grouped pagination |

Requests use Bean Validation and observed versions. Invalid transitions and contradictory retries return 400; authentication 401, authorization 403, missing objects 404, uniqueness/version conflicts 409, invalid Estate references 422, unavailable/malformed dependencies 503. Responses carry correlation UUIDs and structured problem details. Contracts are pinned independently in Operations resources; the validator compares request/response schemas, parameters and HTTP operations with runtime OpenAPI.

## Event inventory

Operations namespace events/operations/v1 contains TappingScheduleActivated, TappingAssignmentCreated, TappingAssignmentStarted, TappingCompleted, TappingMissed and TappingAssignmentCancelled. All use eventVersion=1, established timestamp/source/provenance metadata, aggregateId/version and stable eventId/correlationId. SIMULATED examples accompany every schema. Publish on agrosphere.domain with routing agrosphere.<eventType>.v1.

Domain changes and outbox insert share one local transaction. A scheduled relay locks committed due rows with SKIP LOCKED, sends persistent mandatory messages, waits for positive confirms/no returns, and marks publication only afterward. Bounded exponential retries retain failed rows and stable IDs. Broker acknowledgment followed by database failure can redeliver: consumers must atomically deduplicate eventId. Backlog/failure gauges, health/readiness, bounded pooling and graceful shutdown are configured.

## Security and dependency integration

Issuer/audience/cryptographic JWT validation follows the existing platform. Roles and trusted estate_ids are enforced inside Operations for individual objects and collection queries. PLATFORM_ADMIN/PLANTATION_ADMIN are global; ESTATE_ADMIN/ESTATE_MANAGER manage scoped schedules and assignments; FIELD_SUPERVISOR manages scoped assignments; FIELD_WORKER executes only own scoped assignments using signed sub; AUDITOR/VIEWER read only. Additional read roles do not remove a worker's own execution permission or grant writes to others.

Operations delegates the authenticated bearer token to the real Estate GET estate/block APIs, using bounded timeouts, no redirects, canonical timezone, active RUBBER ownership checks and explicit denial/unavailability mapping. No external database access or fabricated success fallback exists. Estate operational roles receive scoped master-data reads only; existing master-data write permissions remain enforced.

Real Keycloak testing exposed two prerequisites hidden by synthetic JWTs: the custom default scope omitted canonical sub, and administrator-managed estate attributes needed the supported profile configuration step. Infrastructure now supplies an explicit subject mapper; disposable acceptance applies configure_identity.py and asserts signed sub/estate_ids before exercising work. Existing local realms require that documented additive setup.

## Tests actually executed

| Check | Actual result |
|---|---|
| Operations Maven verify -Pintegration, Java 25 | PASS: 34 unit/security tests + 10 Testcontainers integration tests, no failures/errors/skips |
| Estate Maven verify -Pintegration | PASS: 39 unit/security tests + 9 PostgreSQL/RabbitMQ integration tests, no failures/errors/skips |
| Gateway clean Maven verify | PASS: 12 tests, including real signed-JWT forwarding for tapping routes |
| Operations contract validation | PASS: 18 operations aligned with runtime request/response/parameter schemas; all six event types from actual outbox exports pass strict JSON schema and negative cases |
| Contracts full validation | PASS: old v1/v2/Spatial compatibility, six Operations schemas/examples and all OpenAPI documents |
| Infrastructure validator / Compose config | PASS: identity, service isolation, health dependencies, broker and Compose syntax |
| Architecture/workspace validator | PASS: 12 independent Git roots, workflow/YAML checks, ignore/secret-pattern scan, twelve ADRs and seven new diagram sources |
| PlantUML -checkonly | PASS: all seven Milestone 3A diagrams |
| Independent Docker builds / isolated apps profile | PASS: Operations, Estate and Gateway images; healthy PostgreSQL, RabbitMQ, Keycloak, Estate, Spatial, Operations and Gateway with observability services |
| Full-stack acceptance | PASS: PKCE, actual trusted subject/estate claims, Gateway → Operations → Estate, generation retry, worker start/complete/retry, auditor write denial, correct summary and four confirmed outbox events |

Tests cover recurrence anchoring/bounds, DST/date boundaries, invariants/terminal states, execution requirements, missed reasons/future prevention, role/estate/worker isolation, stale versions, simultaneous generation/start, DB uniqueness/check constraints, schema upgrades, rollback of domain+outbox, broker confirms/mandatory returns/backoff/exhaustion/stable retry IDs, malformed/down/denied/missing Estate responses and API failures. Operations runtime artifacts are in ignored target/events, target/openapi-runtime.json and Surefire/Failsafe reports. Exact commands are in service READMEs.

Intermediate failures were corrected: malformed YAML nesting; unused Hibernate scanning on Windows (removed JPA starter in favor of the intended JDBC adapter); Docker wrapper tar/zip checksum mismatch (use the already pinned Maven image executable); Python validator version conflict (reuse Contracts' pinned versions); incomplete disposable Keycloak profile updates; missing subject/scope prerequisites. No failed intermediate check is represented as passing.

## Definition of Done

- [x] Existing capabilities inspected/documented; independent boundaries preserved.
- [x] Schedule management and duplicate-safe generation.
- [x] Authorized worker/supervisor workflows, persisted execution and required missed reason.
- [x] Accurate summary calculations with documented denominator and dates.
- [x] PostgreSQL/Flyway migrations and constraints executed, including upgrade.
- [x] RabbitMQ transactional outbox publication and real retry verified.
- [x] OpenAPI/event contracts aligned and validated.
- [x] Object and estate authorization enforced.
- [x] Unit, PostgreSQL and RabbitMQ tests passed.
- [x] Docker local integration and independent service build verified.
- [x] CI configuration updated; YAML and invoked checks validated locally.
- [x] Seven PlantUML diagrams validated and documentation updated.
- [x] No direct cross-service database access.

Hosted GitHub Actions execution and deployment to shared/production environments: **NOT VERIFIED** and not performed. Local CI-equivalent build/test/contract/Docker checks passed; this report does not claim remote runs or production rollout.

## Decisions, limitations and recovery

ADR 0012 defines recurrence, cancellation, UTC/local dates, retry/version policies, roles, summary semantics and at-least-once delivery. The intentionally bounded recurrence vocabulary is DAILY/EVERY_N_DAYS:n, not arbitrary RFC 5545. One schedule occurrence covers one worker/date. Create requests do not promise exactly-once replay: reconcile ambiguous responses with list queries. Terminal reopening, worker identity provisioning, UI workflows, downstream analytics, latex collection and DRC are outside 3A.

No unresolved implementation prerequisite remains for local Milestone 3A acceptance. Existing local realms must apply the additive reviewed identity update; private passwords remain external. Failed outbox rows require fixing broker/routing and resetting selected rows to PENDING without replacing IDs. See the development guide and Operations README for API examples, security matrix and recovery.

## Milestone 3B recommendation

Readiness: READY for planning the separately authorized next milestone. Preserve Operations ownership and immutable assignment/execution IDs; version future contracts independently and deduplicate all consumed events. No Milestone 3B feature was implemented.
