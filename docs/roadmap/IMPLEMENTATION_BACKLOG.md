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
