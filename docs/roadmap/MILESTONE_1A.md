# Milestone 1A Estate Service

Implementation resides only in agrosphere-estate-service, with coordinated contracts 0.2.0 and ADR-0008. No Milestone 1B implementation is included.

- [x] Pure domain models, DTOs, ports/adapters and service-owned migrations
- [x] Estate/division/block/clone REST API and paginated scoped queries
- [x] Validated JWT issuer/audience/roles/estate scope
- [x] Atomic outbox, confirmed RabbitMQ delivery, retries and replay guidance
- [x] Domain/security/messaging tests and PostgreSQL/RabbitMQ integration checks
- [x] V1 event preservation and additive v2 schemas/OpenAPI
- [x] Reproducible runbook and synthetic example requests
- [x] Java 21 verification: 47 tests passed, no skips
- [x] Docker image built successfully; see service completion report

Runtime verification results and limitations are recorded in the service's docs/MILESTONE_1A_REPORT.md, not inferred from implementation checkboxes. Central infrastructure and all other service repositories remain unchanged.
