# Milestone 3B — Local release, persistence and access progress

Date: 2026-10-27 (America/Chicago). Status: PARTIAL IMPLEMENTATION, NOT MILESTONE ACCEPTANCE. [Checkpoint](DEVELOPMENT_CHECKPOINT.md), [evidence](MILESTONE_3B_T03_T04_EVIDENCE.json), [remaining credential-wiring scope](MILESTONE_3B_CREDENTIAL_WIRING_REVIEW.md).

## Accepted local contract release

The owner explicitly accepted the executable candidate and authorized local Contracts 0.5.0 metadata and Operations artifact pinning, with no remote publication. All 26 accepted candidate hashes matched before changes. Candidate manifest SHA-256: 1fa837922afa69e2cff42d33e3a5bff5dade7efc18d91ec52e4126fff442f543. [Release record](../../../agrosphere-contracts/docs/milestone-3b/RELEASE_0_5_0.json) preserves the owner's instruction and exact accepted artifact hashes.

Contracts VERSION is now 0.5.0; local metadata, compatibility notes and indexes are updated. Operations pins the exact accepted OpenAPI and four operations/v2 schemas in version-specific directories, with a local hash lock. All existing v1 event pins and V1/V2 migrations are preserved. No commit, tag, push, publication or running service deployment occurred. The candidate manifest remains an immutable pre-release observation; the separate release record supplies current disposition.

## Implemented preparation

T03 schema/JDBC preparation: V3 creates collection roots, measurements, revisions, adjustments and command receipts; permanent lot/reference uniqueness; completed-execution ownership guard; current-revision and selected-child deferred FKs; immutable root attribution, append-only evidence/completed receipts; deferred command completion; indexes and restricted grants. The role must already exist with no elevated flags, inherited roles or migration-object ownership. No login or password is provisioned by V3.

CollectionStore joins one application transaction for conditional writes and evidence appends. It applies estate/worker predicates before reads, pagination, counts and history. Decimal history parsing remains exact. CollectionSnapshots explicitly maps domain records into the accepted closed wire shape; domain record layout is not exposed as an HTTP DTO. Database-rounding does not replace request/domain precision validation.

T04 components: CollectionAccess supplies positive read/create/initial-DRC/correct/void/replacement policies, including mixed-role protection, trusted estate claims and signed subject ownership. CollectionScope is immutable. EstateHttpClient adds a typed MasterSnapshot port for canonical IDs, division, timezone, versions and validation time while retaining the original 3A timezone method/constructor. Required malformed metadata fails 503, invalid/inactive ownership 422, denied delegation 403; HTTP requests remain bounded and never follow redirects.

These components are not yet a collection application service or HTTP API. T05 must add atomic replay/state/history/outbox/receipt orchestration, T06 HTTP/summaries, and T07 v2 event writing. Repositories alone do not prove the whole command transaction. Initial collection writes are not enabled.

## Current passing evidence

| Check | Result |
|---|---|
| Contracts full validator, deterministic artifact check, boundary unittest suite | PASS: 12 tests; accepted artifact hashes and 47 legacy event/example hashes preserved |
| Operations ./mvnw.cmd verify -Pintegration, Java 25 | PASS: 70 unit/security tests plus 25 integration tests; zero failures/errors/skips |
| CollectionSchemaIT | 8 passed: fresh schema/grants, role inheritance rejection, uniqueness/void, execution ownership, selected-child/revision constraints, command completion/immutability, V2 upgrade and failed-DDL rollback |
| CollectionStoreIT | 7 passed: roundtrip/scoped pagination/history, immutable snapshot audit, required transaction/scope, rollback, stale writer cleanup, competing conditional writers, actual adapter writes under SET LOCAL ROLE |
| TappingServiceIT | 10 passed after additive V3; original tapping behavior assertions retained. Migration inventory now expects three versions and explicitly retains V1/V2. |
| Signed-JWT and reference tests | Production JWT decoder verifies issuer/audience/lifetime/signature before policy tests; malformed/null scopes, mixed roles, revoked estate, typed master errors, no-redirect and timeout/down behavior checked |
| Operations python scripts/validate_collection_pins.py --snapshots target/collection-snapshots | PASS: five exact release artifacts and four actual serialized JDBC/domain snapshots validate against the pinned CollectionView schema |
| Operations independent Docker build | PASS: separate local review image agrosphere-operations-service:3b-schema-review; runtime remains non-root. No running stack modified. |

Docker Desktop is available (engine 29.8.2). The sandbox denied access to its named pipe; normal tool approval allowed Docker-backed commands outside the sandbox. No manual sandbox bypass or disabling occurred. Testcontainers created only disposable PostgreSQL/RabbitMQ fixtures and cleaned those containers. Existing private environments, authoritative databases and AEO were not accessed.

Intermediate failures are retained honestly: PowerShell split an unquoted Maven -D property; the corrected quoted command ran. Two schema assertions initially counted Flyway's schema-creation row as a versioned migration; queries now check actual version rows. A package-private JWT configuration factory required moving its test into the matching package, not changing production visibility. The existing tapping suite's two-migration count stopped its first ordered test and caused dependent failures; the inventory was updated for V3 without weakening behavioral checks, and all ten then passed. Public Markdown encoding/newline errors introduced during metadata writing were corrected; no private files were involved.

## Required failing or deferred checks

The unchanged strict runtime validator scripts/validate_contracts.py currently **FAILS**: the accepted/pinned document describes 27 operations while the actual runtime export has the existing 18 tapping operations. The nine missing collection routes are the entire difference. This is recorded as incomplete T06 implementation; the validator and CI gate are not disabled or weakened. Artifact pin validation is not runtime endpoint acceptance.

T03 is **PARTIAL**: production-shaped separate login/Flyway credential wiring, actual restricted-login proof and previous-3A-image rollback rehearsal are not complete. The disposable privilege tests use a NOLOGIN role via SET ROLE, not a fabricated runtime-login success. Current application/Compose credential wiring is unchanged and V3 fails closed if its required role is absent. Do not launch this intermediate build against an existing stack before operator provisioning/configuration.

T04's reusable reference/security components are tested; complete collection HTTP object/history/query/replay enforcement still requires T05/T06 integration. Full disposable Keycloak/Gateway collection acceptance, summary queries, v2 outbox publication, operational provisioning, hosted CI and milestone AC01–AC28 acceptance remain incomplete.

## Specific owner decision now needed

The implementation authorization explicitly states: “Production deployment, destructive migrations, secret-handling changes and AEO changes remain unauthorized.” The next T03 portion changes how runtime and migration credentials are supplied, so it cannot be inferred from contract acceptance. [Concrete proposal](MILESTONE_3B_CREDENTIAL_WIRING_REVIEW.md) shows exact variable/configuration changes, affected files, provisioning/test scope and exclusions.

Requested extension: implement placeholder-only public credential wiring/provisioning tools, and test with new generated credentials in disposable environments only. Do not read/change existing private environment files, provision existing/running stacks, rotate real credentials, deploy, publish or alter AEO. No credential values are needed in chat. Once accepted, complete T03 and continue T05–T09 in dependency order without per-task prompts. Milestone 2 performance remains independently open.
