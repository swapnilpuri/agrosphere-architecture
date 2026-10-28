# AgroSphere application development checkpoint

## GitHub Actions contract-byte repair - 2026-10-28

Owner-reported failure emails were inspected through the connected GitHub tools. Operations run 40636359295 / commit 69290f7 passed Maven (75 unit/security + 52 integration) then failed the exact artifact hash for operations-service.yaml. The approved Windows CRLF bytes had been normalized to LF in Git. Operations and source Contracts now mark their exact byte-pinned artifacts as -text; accepted raw hashes are unchanged. Isolated Git checkout regressions and all post-Maven validations passed on Linux, including source Contracts checks. See Operations docs/CI_CONTRACT_BYTE_PRESERVATION.md. Changes remain local and must include the artifact files when eventually committed/pushed; no product Git index, commit, remote notification settings, running application, production or AEO state was changed. Hosted CI has not rerun with this repair.

## Digital Twin map correction - 2026-10-28

The owner reported an empty-looking map and missing-geometry warning. Existing local data includes sparse test estates and complete synthetic estates with 13 boundaries. Web now reapplies selection after an asynchronous geometry load, clearing stale warnings and restoring the selected camera target; genuine missing geometry remains explicit. See Web docs/DIGITAL_TWIN_GEOMETRY_LOADING_FIX.md for implementation and checks: 32 unit/component tests, lint/format/types/API/build, two UI tests, one graphics test, two real local live-browser cases (one-feature and 13-feature estates), and independent Docker packaging all passed. The running development server rebuilt. No business data, backend/private configuration, production or AEO changes; M2 device performance remains open.

## Subsequent local startup authorization - 2026-10-28

The owner explicitly authorized using existing local configuration and necessary local updates to bring up the application. See [local startup record](LOCAL_APPLICATION_START_2026_10_28.md). The existing local stack is now running, including Operations with the restricted runtime role and V1/V2/V3 migrations; all nine backend containers are healthy and the frontend is available at http://localhost:4200. Existing-account PKCE and read-only Gateway requests pass. A local database backup was saved before migration; only the missing private runtime credential was added, without displaying values or changing other passwords. No business records were created. This scoped local-start authorization supersedes the earlier disposable-only/private-environment exclusion below for this action; historical 2026-10-27 evidence remains unchanged. Production/AEO, destructive operations and remote publication remain excluded.

Updated: 2026-10-27 (America/Chicago). Milestone 3B T00-T09 LOCAL IMPLEMENTATION AND VERIFICATION COMPLETE. See [verification report](MILESTONE_3B_LOCAL_VERIFICATION.md) and [exact evidence](MILESTONE_3B_LOCAL_EVIDENCE.json). Final owner product sign-off and production readiness are not asserted.

## Authority and boundaries

Read [workflow](APPLICATION_DEVELOPMENT_WORKFLOW.md), [owner design approval](MILESTONE_3B_APPROVAL.md), and [scoped credential authorization](MILESTONE_3B_CREDENTIAL_WIRING_APPROVAL.json). The owner accepted D01-D12, ADR 0013, R01/R02, and authorized T01-T09 in dependency order; the executable Contracts candidate and local 0.5.0 release/pins were subsequently accepted. Credential wiring is authorized for tracked placeholders and generated credentials only in disposable tests. These approvals persist; no repeated per-task prompt is needed.

Do not read/modify private environment files, provision existing/running stacks, change production/AEO state, perform destructive migrations, commit/tag/push or publish remotely. All database/broker/Compose drills use exclusively new disposable resources with generated credentials. AEO remains paused and untouched. Milestone 2 performance remains independently OPEN/PARTIAL.

## Task state

| Task | Current state |
|---|---|
| T00 | COMPLETE: accepted decisions/ADR, actual baseline and diagram inventory |
| T01 | COMPLETE: owner-accepted 26-file executable candidate, local Contracts 0.5.0 and five exact Operations artifact pins |
| T02 | COMPLETE: immutable domain, exact decimals/time/chronology/lifecycle and fixed-clock tests |
| T03 | COMPLETE locally: additive V3, scoped JDBC, actual separate generated runtime/Flyway logins, restricted privileges, upgrade/DDL rollback, separate backup/restore and pinned prior-3A image against retained V3 |
| T04 | COMPLETE locally: typed bounded/fail-closed Estate adapter, signed JWT role matrix and scoped SQL access; legacy port preserved |
| T05 | COMPLETE locally: durable normalized command reservation/receipt, atomic evidence/revision/adjustment/outbox, concurrency/fault tests; PostgreSQL 55P03 reservation timeout explicitly translated to retryable 409 |
| T06 | COMPLETE locally: nine HTTP operations, scoped history/measurements/list/summaries, exact calculations/provenance/coverage; strict runtime comparison passes all 27 operations |
| T07 | COMPLETE locally: four v2 full snapshots, actual schema/formula checks, real confirms/returns/nacks/timeouts/ACK-crash duplicate tests; tapping v1 retained |
| T08 | COMPLETE locally: final generated-only Compose workflow passed with real Keycloak/Gateway/Estate, original tapping assertions, collection lifecycle/scope, durable sink and outage recovery; labelled test containers and volumes absent after cleanup |
| T09 | COMPLETE locally: independent regressions/builds, six rendered/visually reviewed diagrams, runbooks, exact evidence and AC01-AC28 traceability. Application changelogs remain Unreleased; no remote publication/deployment |

## Current evidence and limits

Final Operations regression: 75 unit/security plus 52 integration tests, zero failures/errors/skips. Gateway 13 tests; Estate 39 unit plus 9 integration tests. Strict runtime comparison passes all 27 Operations and all 16 Estate operations; 10 actual legacy Operations and 78 Estate events pass validators. Five accepted Operations artifact pins, all 26 candidate hashes and 47 legacy hashes are unchanged. Four actual v2 families, four domain/JDBC snapshots and five HTTP response shapes pass schema/identity/formula checks. Five projection and three comparator tests pass. Contracts validator/builder and 12 boundary tests pass.

Infrastructure offline/public topology validation and actual generated-only role-provisioning checks pass. The final post-CORS full-stack project agrosphere-3a-check-4296d0ad passed, including original tapping assertions and complete collection/scope/outage checks; its own labelled containers and volumes are absent after cleanup. Separate Operations/Estate/Gateway image builds passed. Gateway permits Idempotency-Key preflight, without route or business-logic changes. Architecture/workspace, pinned PlantUML syntax/render, all six visual inspections and affected diff checks passed. See report/evidence for commands, source/report hashes, resolved failures and limits.

No private .env/local-secrets file was read or modified, no existing/running stack was provisioned, no production/AEO action or remote publication occurred. A reservation lock-timeout translation defect, expired disposable setup token and missing foreign-scope test fixture were corrected and reverified; earlier partial attempts are not passed acceptance. Documentation is contract-first and separate HTTP tests establish enforcement. Historical evidence remains historical. M2 performance remains open.

## Revisions and preservation

Repository HEADs advanced externally since the earlier checkpoint. Fresh observation during this increment: Architecture ed4e594069b7a54dcad048325393d304aee7b780; Contracts 73b2b7099e27b97515f98fe0efbf42f07e919955; Infrastructure fe306963262376d7daa3c23e100125235f54cf14; Operations 5cd5321d054b403c60ccf7449d3d26de28078d0a; Gateway fcf7daf66fa0d9efaf2d1aa72f8cc88c600ab6c0; Estate 7fdd691431a6962f5ac71fb08e9e3e09380bae00. Record final HEAD/status/source hashes again because the owner may commit while work continues. This agent did not manipulate Git indexes, commits, tags or remotes. Preserve unrelated/staged work.

## Exact safe continuation

1. Read this checkpoint, the verification report/evidence and authorization records. Do not ask the owner to repeat satisfied 3B/Contracts/credential approvals.
2. Observe current HEAD/status before future edits and preserve external/staged work. Revalidate hashes/tests only if source changed or new evidence warrants it. This agent made no Git index/commit/tag/remote changes.
3. Current credential wiring needs no further owner input or private values. Existing-environment provisioning/production deployment remains excluded and was not performed. Do not start the candidate against a developer stack automatically.
4. See [next planning handoff](MILESTONE_3C_PLANNING_HANDOFF.md). It is a proposal only, with required domain/security/contract decisions before any new milestone implementation. Current authorization covers 3B T01-T09, not an automatic expansion to incidents, IoT or Analytics.
5. Retain the independent M2 reference-device/performance gate, AEO pause, unreleased application status and all production/private-environment exclusions. No unsupported remote CI or owner sign-off claims follow from local verification.
