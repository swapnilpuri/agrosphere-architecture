# Nonfunctional requirements
| Area | Initial target / verification gate |
|---|---|
| Independence | Each repo builds/tests without sibling source paths, shared JPA models or a parent build; CI per repo |
| Security | TLS outside loopback, OIDC PKCE clients, issuer + audience validation, role/estate authorization and audit before domain release |
| Isolation | Service-specific database roles/migrations; no cross-database queries; verify access denial in integration tests |
| Reliability | At-least-once events, transactionally deduplicated consumers and outbox confirms; replay/DLQ tests before shipping handlers |
| API performance | Proposed POC p95 <500 ms for indexed block metadata queries, 20 concurrent local-demo users; benchmark in M1, not measured yet |
| Visualization | Proposed 30 fps minimum on a named reference desktop; streaming/LOD and assets budget set in M2/M5 |
| Data quality | Geometry validity, provenance, units, UTC instants, stable UUIDs, explicit observed/ingested timestamps |
| Observability | Structured logs, correlation/trace propagation, metrics and health; collector retention/export design before shared environment |
| Recovery | Proposed RPO 24h / RTO 4h for POC shared environment; restore rehearsal before relying on backups |
| Testability | Unit/use-case tests + PostgreSQL/PostGIS Testcontainers + contract/event replay tests per capability |
| Privacy | Minimize worker/location identifiers; define access, retention and deletion with product owner before collection |
| Licensing | Ownership/license undecided; asset, terrain and third-party notices reviewed before redistribution |

Targets are engineering hypotheses, not achieved SLAs. Tenant isolation, retention, availability and hosting budgets need explicit future ADRs.
