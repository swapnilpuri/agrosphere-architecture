# Milestone 3B — T00/T01 candidate/T02 progress

Date: 2026-10-27 (America/Chicago). Status: PARTIAL IMPLEMENTATION; NOT MILESTONE ACCEPTANCE. See [checkpoint](DEVELOPMENT_CHECKPOINT.md) and [owner authorization](MILESTONE_3B_APPROVAL.md).

## Delivered increments

T00 is complete: owner decisions/R01/R02 recorded, current Git roots and V1/V2 Operations migration chain inspected, legacy contract baseline captured, accepted [ADR 0013](../adr/0013-latex-collection-and-drc.md) moved into the canonical inventory, links aligned, thirteen-ADR validation and CI coverage of six 3B diagrams added. No Git staging/reset/commit/push was performed. Existing staged and unstaged changes were preserved.

The workspace validator initially failed on the removed, still-indexed proposed ADR path. It now explicitly recognizes Git-reported working-tree deletions while validating remaining files, without changing the index. The corrected full workspace audit passed. Historical approval manifests retain the pre-promotion path/hashes intentionally.

T01 candidate authoring is complete. [Independent contract review package](../../../agrosphere-contracts/docs/milestone-3b/CANDIDATE_REVIEW.md) describes nine additive REST operations, four v2 event schemas, examples, seven persisted negative fixtures, deterministic generation and strict semantic/compatibility checks. Existing 47 event/example files are byte-identical; old 18 Operations operations/components and metadata are semantically unchanged. The candidate is not released; Contracts VERSION remains 0.4.0 and Operations pins remain unchanged. [Candidate manifest](../../../agrosphere-contracts/docs/milestone-3b/CANDIDATE_0_5_0.json) hashes the exact review artifacts.

T02 pure domain/calculation is implemented in Operations: CollectionRules, LatexCollection, DrcMeasurement, CollectionRevision and CollectionAdjustment. Immutable attribution/master snapshots, normalized ASCII references, observed-time precision, decimal input/range validation, exact product/HALF_UP kg calculation, measured-zero versus missing, initial DRC, reasoned correction/replacement and terminal void are covered by fixed-clock tests. Corrections construct new values and preserve old evidence; revisions/adjustments bind consecutive root versions and signed actor/time context.

These are domain types, not HTTP DTOs. Application authorization, durable idempotency, uniqueness, JDBC persistence, outbox serialization, summaries and runtime OpenAPI export remain later tasks. No collection endpoint, V3 migration, runtime role/config change or contract pin was introduced. Existing tapping domain/application and migrations are unchanged.

## Actual validation

| Repository / command | Result |
|---|---|
| Architecture: python scripts/validate.py --workspace C:/Projects/agrosphere | PASS: thirteen ADRs, diagram/workflow layout, twelve independent roots, YAML/ignore/heuristic secret checks |
| Architecture: pinned local PlantUML jar -checkonly across main, 3A and 3B sources | PASS; jar SHA-256 matches CI pin |
| Architecture: PlantUML -tpng -o ../../target/diagrams-3b diagrams/milestone-3b/*.puml | PASS: all six PNGs rendered and visually inspected; no clipped text or syntax-error panels |
| Contracts: .venv/Scripts/python.exe scripts/validate.py | PASS: existing/new schemas, examples, semantic checks, exact decimal inputs, 47 old hashes, all OpenAPI documents and 27-operation inventory |
| Contracts: .venv/Scripts/python.exe scripts/build_collection_contracts.py --check | PASS: five deterministic executable contract artifacts |
| Contracts: .venv/Scripts/python.exe -m unittest discover -s scripts -p test_collection_contracts.py -v | PASS: 12 tests, zero failures/errors; includes mutation subcases and seven persisted negatives |
| Operations: ./mvnw.cmd verify, JAVA_HOME=C:/myprograms/jdk-25.0.2 | PASS: Java release 25, 56 unit/security tests (22 collection + 34 existing), zero failures/errors/skips; packaged jar |
| Affected repositories: git diff --check | PASS; Git emits existing CRLF normalization notices |
| Docker availability: docker version --format '{{.Server.Version}}' | FAILED: dockerDesktopLinuxEngine named pipe absent; no integration containers launched |

Operations Surefire XML and rendered PNGs are retained under ignored target directories; durable evidence records hashes and test counts. Existing Mockito/deprecation warnings did not fail Maven. The initial default Python environment lacked openapi_spec_validator; the repository's existing venv supplied the pinned tooling. A speculative Python timezone dependency could not be installed and was removed; the final implementation uses existing dependencies and Java's timezone rules for domain tests. No failed attempt is represented as a pass.

NOT RUN in this increment: Maven integration profile, live runtime OpenAPI/exported event comparison, Docker packaging, disposable real PostgreSQL/RabbitMQ/Keycloak acceptance, upgrade/rollback and CI hosted execution. The contract OpenAPI file is a validated candidate document; it is not evidence of 27 running endpoints. No full AC01–AC28 completion claim is made.

## Next gate and owner actions

Review/accept the executable contract candidate through the applicable independent contract process and authorize local 0.5.0 release metadata/artifact pinning (or name the required reviewer). This is the specific contract gate retained by the owner's implementation authorization, not a repeat request for D01–D12 approval. No remote publishing is requested.

Make Docker Desktop's Linux engine available before integration/container checks. Do not reset existing volumes or databases. After the contract gate, continue T03 persistence and T04 reference/security in dependency order, deferring any excluded secret-handling portion until separately authorized. Milestone 2 performance remains open; AEO remains paused and untouched. No production operations or irreversible Git action occurred.
