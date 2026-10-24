# Milestone 1B — Spatial Digital Twin

Requested implementation: independent Spatial Service 0.2.0; independent contracts 0.3.0. See ADR-0009 and the spatial repository docs/MILESTONE_1B_REPORT.md for concrete source, schema, endpoints, actual test results, run commands and limitations.

Delivered scope includes WGS84 features/history, spheroidal areas, bounded spatial queries, GeoJSON import/export, layers/assets, estate v2 projections, spatial v1 events/outbox, estate-scoped JWT policy and independent deployment artifacts. All fixtures are SIMULATED and require no deployed Estate Service.

Milestone 1C is now recorded separately in MILESTONE_1C.md and ADR-0010. Recommended integration tasks are trusted identity provisioning, coordinated contract release, projection replay/reconciliation (especially division lifecycle), gateway/client contract adoption and monitored outbox/DLQ operations. No remote release or cloud deployment is included.
