# AgroSphere application development checkpoint

Updated: 2026-10-27 (America/Chicago). Current state: 3B OWNER DESIGN APPROVAL RECORDED; command execution RESTORED; T00 COMPLETE, T01 locally RELEASED/PINNED 0.5.0; T02 domain complete; T03 COMPLETE including authorized generated-only credential wiring; T04 components verified. Milestone 3B acceptance remains incomplete.

Start with [workflow](APPLICATION_DEVELOPMENT_WORKFLOW.md), [owner approval](MILESTONE_3B_APPROVAL.md) and [current approval evidence](MILESTONE_3B_APPROVAL_EVIDENCE.json). [Earlier evidence](DEVELOPMENT_CHECKPOINT_EVIDENCE.json) remains historical and its output hashes describe the pre-approval documentation, not current files.

## Milestone, authority and boundaries

D01–D12, ADR 0013, requirements, design, acceptance specification and REST/event design were explicitly accepted by the project owner in chat. All 14 reviewed package hashes matched the prior baseline before edits. R01/R02 are applied to owning design/contract/acceptance text. T01–T09 are authorized in dependency order subject to required validation and independent contract review/release gates. No further per-task prompt is required within that scope.

Production deployment, destructive migrations, existing private environment/credential access and AEO changes remain unauthorized. The owner explicitly authorized the reviewed tracked placeholder wiring and generated credentials only in disposable tests; see MILESTONE_3B_CREDENTIAL_WIRING_APPROVAL.json. Do not modify or query orchestrator runtime/approval/run state. The separate scoped credential-wiring authorization is now recorded and verified; it does not allow provisioning running stacks or altering real credentials. Milestone 2 performance remains independently OPEN/PARTIAL; reference-device frame/useful-view measurements and initial-view budget confirmation remain outstanding.

## Completed work and task state

| Work | Current evidence/state |
|---|---|
| DOC-01–03: discovery, consolidated review, persistent workflow and initial checkpoint | Historical readiness review, workflow and DEVELOPMENT_CHECKPOINT_EVIDENCE.json |
| GOV-01: owner acceptance recorded | MILESTONE_3B_APPROVAL.md quotes exact instruction; approval evidence binds 14 pre-edit package hashes |
| GOV-02: R01/R02 and current document status | Owning Architecture requirements/design/acceptance/plan/ADR and Contracts wire design updated; no executable artifact modified |
| T00 decisions | COMPLETE for owner acceptance; no additional external approval falsely asserted |
| T00 Git/validation baseline | COMPLETE: current Git/compatibility baseline, accepted ADR 0013 promoted, thirteen-ADR/3B CI inventory updated, Architecture/workspace validation and all six diagrams syntax/render/visual review passed. |
| T01 | COMPLETE: owner accepted exact 26-file executable candidate and local release/pinning. Contracts VERSION 0.5.0; five accepted runtime artifacts pinned; no remote publication. |
| T02 | COMPLETE for pure domain scope; current full unit/security suite has 70 passing tests. |
| T03 | COMPLETE for local implementation: V3/schema/JDBC, actual restricted runtime versus Flyway-owner connections, generated-only provisioning proof, upgrade/DDL rollback and prior-3A image rehearsal passed. |
| T04 | Reference/access components verified; collection HTTP/query/replay enforcement will be exercised in T05/T06. |
| T05 | ACTIVE: durable command replay and atomic root/evidence/receipt/outbox orchestration. |
| T06-T09 | Next dependent tasks; no new per-task authorization needed inside existing scope. |

The owner accepted the exact credential-wiring proposal for tracked placeholders and generated disposable tests. [Authorization](MILESTONE_3B_CREDENTIAL_WIRING_APPROVAL.json) and [evidence](MILESTONE_3B_CREDENTIAL_WIRING_EVIDENCE.json) record the scope/proof. Full current regression: 70 unit/security plus 28 integration tests pass. Infrastructure actual provisioning SQL and generated-only Compose configuration pass. No private .env was read/changed and no running stack was provisioned.

Active task is T05, followed by T06/T07/T08/T09 in dependency order. Earlier review-pending/NOLOGIN-only notes below and in historical reports describe the preceding increment; the credential gate is now satisfied within its stated scope. Existing-environment operations remain excluded. Current strict runtime OpenAPI comparison still fails on the nine unimplemented collection routes until T06; do not weaken it.

## Current observed revisions

Fresh Git CLI HEAD/status and local VERSION observations on 2026-10-27. Detailed dirty/staged state is in the current evidence; preserve it. No Git index, commit, tag or remote was modified.

| Repository | Local VERSION | Observed HEAD |
|---|---|---|
| agrosphere-ai-service | 0.1.0 | cc92974049a50d64e6a5c1fb06868f01aa7f5def |
| agrosphere-analytics-service | 0.1.0 | 38725317675493237b2769ed38e1840b3991d69e |
| agrosphere-api-gateway | 0.2.1 | fcf7daf66fa0d9efaf2d1aa72f8cc88c600ab6c0 |
| agrosphere-architecture | 0.5.0 | edffdc19868b7d8d9139bc8272405a30ce28bb3d |
| agrosphere-contracts | 0.5.0 | 7e962552421f15ad5d1492276817db1e1692b104 |
| agrosphere-estate-service | 0.2.2 | 7fdd691431a6962f5ac71fb08e9e3e09380bae00 |
| agrosphere-immersive | 0.1.0 | 2bf7663e412f86956dbdb831184f2d0ab1a03c70 |
| agrosphere-infrastructure | 0.3.0 | 3268651e1d48a38f858351c105ab54b4103c3ded |
| agrosphere-operations-service | 0.2.0 | fbfda7e87dc0f650f013e6082d1f886df888b6c9 |
| agrosphere-spatial-service | 0.2.1 | 2a7dbda842141fca041510ca79481ea0454eaaf8 |
| agrosphere-telemetry-service | 0.1.0 | 8a3c888dea3e1f3c7a94baf5c55a61285b5bcb7a |
| agrosphere-web | 0.2.0 | 2a56f819cc653425e4c58bd6306872e352ee5c7a |

## Current checks and limits

- Operations Java 25 ./mvnw.cmd verify -Pintegration: PASS, 70 unit/security and 25 integration tests; zero failures/errors/skips.
- Current integration breakdown: 8 schema, 7 JDBC store and 10 tapping regression tests. PostgreSQL/RabbitMQ fixtures are disposable. Restricted privileges are tested via NOLOGIN/SET ROLE; no actual runtime-login success is claimed.
- Contract validator/builder and 12 boundary tests: PASS. Accepted 26-file candidate unchanged; five runtime pins exact; 47 legacy event/example files preserved. V1/V2 migrations and current application.yaml/.env.example are unchanged.
- Four actual JDBC/domain snapshots match the pinned CollectionView schema. Explicit wire mapping and exact decimal history verified.
- Independent Operations review Docker image: BUILD PASS, separate 3b-schema-review tag; no stack launch/replacement.
- Strict original runtime OpenAPI validator: FAIL, 9 collection operations pending T06 (18 actual versus 27 pinned). The validator/CI gate remains intact; artifact integrity is not runtime acceptance.
- Pinned PlantUML syntax checks: PASS; changed persistence diagram rendered/visually checked. Current workspace/YAML/link/diff checks are recorded in the evidence/report after final verification.

## Dependencies, exclusions and open decisions

1. T03 cannot be marked complete while actual migration/runtime credential wiring and restricted-login proof are excluded. The concrete review document specifies placeholder-only tracked changes and generated credentials in new disposable tests, with existing private .env/running stacks left untouched. No credential values are requested in chat.
2. After that scope decision, finish T03 and previous-image rehearsal, then T05/T06/T07/T08/T09 in dependency order. Complete real command replay, SQL summaries, HTTP scoping and v2 confirmed events before acceptance.
3. The strict runtime API mismatch is expected unfinished work, not waived. Full Gateway/Keycloak collection acceptance and hosted CI remain incomplete.
4. Milestone 2 performance remains OPEN/PARTIAL independently. No production deployment, destructive migration, real secret rotation, remote publication or AEO action is authorized.

## Changes awaiting review

- Contracts: accepted release record, local 0.5.0 VERSION/changelog/compatibility/index metadata; accepted executable artifacts unchanged.
- Operations: exact release pins, additive V3, scoped CollectionStore/ports/snapshot mapper, positive CollectionAccess/scope, typed Estate adapter extension, schema/store/reference/signed-JWT tests and pin/snapshot validator/CI step. Existing tapping production logic and V1/V2 migrations preserved; test fixture adds a NOLOGIN role and updates only migration inventory for V3.
- Architecture: release/persistence/reference progress evidence, updated persistence diagram, workflow/checkpoint and concrete credential-wiring proposal.
- Infrastructure: public configuration/instructions read for proposal only; no files or running resources changed.

No collection API/controller, application command replay or new event writer is enabled. This is not a milestone completion report. Do not start the intermediate application against existing environments: V3 requires operator-provisioned restricted role and the still-pending configuration step.

## Exact safe resumption

1. Read affected AGENTS, workflow, owner design acceptance, Contracts RELEASE_0_5_0.json, current progress/evidence and the credential-wiring review. Do not ask the owner to repeat satisfied approvals.
2. Verify current Git status/HEADs, accepted 26-file hashes, runtime pin lock and current source/report hashes; preserve staged and unrelated changes. Keep AEO untouched.
3. Obtain the specific extension for public credential-wiring/provisioning tooling and new disposable generated test credentials. Until then do not modify application/Compose secret bindings, read/change existing private .env files, or provision active stacks.
4. With that scope accepted, implement the reviewed Operations-only owner/runtime separation, test actual restricted login and migration-owner connection plus isolated upgrade/prior-3A compatibility, and complete T03. No real credentials should be supplied in chat.
5. Continue T05 durable command replay/transaction/audit/outbox, T06 HTTP/summaries, T07 v2 publication, T08 disposable full-stack checks and T09 independent closeout. Retain strict 27-operation runtime validation and old tapping regression. Use only scoped disposable database/broker fixtures.
6. Update checkpoint/evidence after each increment. Claim completion only with current AC01-AC28 evidence or explicit reviewed scope changes. Keep open M2 performance and all production/AEO exclusions.
