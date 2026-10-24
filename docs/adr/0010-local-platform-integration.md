# 0010: Milestone 1C local platform integration

Status: Accepted for the requested Milestone 1C implementation
Date: 2026-10-24 (America/Chicago)

The infrastructure repository owns shared local Compose orchestration. Each application remains an independent repository, Maven project, Docker image, CI pipeline and version. Local Compose may build sibling Docker contexts; released-image integration uses independently published image references and no sibling source checkout. No shared parent, submodule, deployment unit or persistence library is introduced.

Reuse the existing PostgreSQL/PostGIS server with separate service-owned databases and non-superuser roles rather than duplicating/moving existing data. PUBLIC database access is revoked by the existing fresh-volume bootstrap. Automated live tests verify Estate credentials cannot connect to Spatial and vice versa. Flyway migrations and persistence remain owned by each service. Never reset populated volumes to apply infrastructure changes.

Retain Spring Cloud Gateway MVC on compatible Boot 4.0.9/Cloud 2025.1.4 (Gateway 5.0.4), Java 25; Estate remains Java 25 and Spatial remains Java 21. Routes preserve existing /api/v1 paths. Gateway handles JWT, correlation, structured access logs, exact-origin CORS, configurable connect/read timeout and safe downstream 503 responses. The JDK client request factory is explicitly configured and exercised by real HTTP timeout tests; no automatic write retry is added.

The local gateway applies a bounded in-process fixed-minute limiter by verified JWT subject. This avoids a new Redis dependency for one local gateway. The limit is per process, resets on restart and is unsuitable as a distributed quota. A shared limiter store requires a separate production decision.

Keycloak supplies a local public Authorization Code/PKCE S256 Angular client and trusted audiences/roles/estate_ids. No demo users or secrets are committed. estate_ids is administrator-editable only. Each service validates RS256 signature, exact public issuer, audience and lifetime. A separate internal OIDC_JWK_SET_URI resolves the container/public hostname difference without accepting another issuer. Existing standalone issuer discovery remains supported. Local HTTP endpoints bind loopback; production TLS and identity hardening remain future work.

RabbitMQ imports durable diagnostic spatial-event bindings only after initial user/broker creation. Spatial owns its existing Estate v2 queue/DLQ; Estate starts after Spatial readiness. Existing transactional outboxes, mandatory confirms, deduplication and revision checks are reused. The spatial diagnostic queue is capped at 10,000 events and is a development sink, not a new business consumer. No contracts or migrations changed. Division lifecycle remains inferred from existing block snapshots; authoritative lifecycle/reconciliation still requires a future contract release.

HTTP W3C tracing passes through the observed gateway RestClient to Estate/Spatial, then through OpenTelemetry Collector to Jaeger. Live acceptance asserts the three service names on a known trace. Async outbox relays retain event correlation but do not promise parent-child trace spans. Jaeger uses ephemeral in-memory storage; the collector exports traces only. Retained metrics/logs, production backup/restore, image digest policy and workload SLAs remain outside this milestone.

The apps profile includes applications, identity and observability; infrastructure can run independently. Health checks and completed topology initialization gate startup. All published ports are loopback-only; application services and management health ports remain internal. Service restarts and broker outages are exercised without deleting volumes. Full verification evidence and exact per-repository changes reside in infrastructure docs/MILESTONE_1C_REPORT.md.
