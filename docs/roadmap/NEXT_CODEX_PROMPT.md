# Current prompt selection - 2026-11-10

Bounded M4 is [owner accepted](../milestones/M4_OWNER_ACCEPTANCE_2026_11_10.md). Choose a complete milestone, individual phase or increment from the [prompt library](prompts/README.md). [M5](prompts/M5.md) is the next original-roadmap implementation candidate; it is not selected or approved yet. The older 1B prompt below is retained as history, not current scheduling.

---

# Recommended Milestone 1B prompt (not executed)

Implement AgroSphere Milestone 1B Spatial Service and estate identity projection only. Read affected AGENTS.md files, architecture ADR-0008, the completed Estate Service report, infrastructure configuration and contracts 0.2.0 first. Preserve independent Git roots and service-owned databases. Consume the Estate Service v2 snapshots with transactional consumer_name/eventId deduplication, revision-aware updates, retry/DLQ/replay and reconciliation. Implement spatial-owned PostGIS geometry and RFC 7946 WGS84 API contracts, using canonical estate/block UUIDs without cross-database access. Reject new operational use of inactive blocks and label synthetic fixtures SIMULATED. Add contract/security/PostGIS integration and duplicate/out-of-order event tests. Validate builds, migrations, permissions and Docker, document actual results and blockers, and stop after Milestone 1B. Do not add operations, telemetry, AI, web/immersive functionality or deploy to Azure.
