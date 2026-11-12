# Current POC-CLOSE decision — 2026-11-11

The owner selected full POC-CLOSE. [Revision1 C01–C07](../milestones/POC_CLOSE_DELIVERY_PACKAGE.md) and its [exact manifest](../milestones/POC_CLOSE_DELIVERY_MANIFEST_2026_11_11.json) are ready for the one new combined-scope decision. Preparation is PARTIAL engineering; no combined execution/owner acceptance inferred. Existing M5 desktop approval and bounded M4 acceptance persist; physical VR remains deferred. On approval proceed autonomously P3–P7; do not start another feature track. Earlier recommendations follow as history.

---

# Current prompt selection - 2026-11-11

M5's desktop prototype is delivered, but its [handoff](../milestones/M5_DESKTOP_HANDOFF_2026_11_11.md) retains desktop verification gaps, deferred physical VR and open owner acceptance. The owner asked for next steps and a similar next-milestone prompt; this is not acceptance or execution authorization.

Recommended follow-on: [POC-CLOSE - Integrated POC Verification and Acceptance](prompts/POC_CLOSE.md). Copy its complete prompt to select discovery and one consolidated review, followed by autonomous implementation/verification after approval. Seven phase prompts and an M5-only continuation alternative are included. The original M0-M5 numbering is unchanged. Android offline/English-French field release is the next separate feature candidate.

---

# Historical prompt selection - 2026-11-10

Bounded M4 is [owner accepted](../milestones/M4_OWNER_ACCEPTANCE_2026_11_10.md). Choose a complete milestone, individual phase or increment from the [prompt library](prompts/README.md). [M5](prompts/M5.md) is the next original-roadmap implementation candidate; it is not selected or approved yet. The older 1B prompt below is retained as history, not current scheduling.

---

# Recommended Milestone 1B prompt (not executed)

Implement AgroSphere Milestone 1B Spatial Service and estate identity projection only. Read affected AGENTS.md files, architecture ADR-0008, the completed Estate Service report, infrastructure configuration and contracts 0.2.0 first. Preserve independent Git roots and service-owned databases. Consume the Estate Service v2 snapshots with transactional consumer_name/eventId deduplication, revision-aware updates, retry/DLQ/replay and reconciliation. Implement spatial-owned PostGIS geometry and RFC 7946 WGS84 API contracts, using canonical estate/block UUIDs without cross-database access. Reject new operational use of inactive blocks and label synthetic fixtures SIMULATED. Add contract/security/PostGIS integration and duplicate/out-of-order event tests. Validate builds, migrations, permissions and Docker, document actual results and blockers, and stop after Milestone 1B. Do not add operations, telemetry, AI, web/immersive functionality or deploy to Azure.
