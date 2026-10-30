# WA-1 local verification — 2026-10-30

The owner-approved worker registration and daily attendance increment is implemented locally across independent Contracts, Operations, Gateway, Infrastructure and Web repositories. Architecture records approvals/evidence. This is a SIMULATED-only candidate, not production acceptance, a deployed upgrade or authorization to collect actual personal data.

See [design approval](WORKER_ATTENDANCE_APPROVAL.md), [exact executable approval](WORKER_ATTENDANCE_CONTRACT_APPROVAL.md), [reviewed design](WORKER_ATTENDANCE_REVIEW.md) and [source/check evidence](WORKER_ATTENDANCE_LOCAL_EVIDENCE.json). The design and executable manifest hashes remain exactly those accepted. Historical pending labels in the original package/checkpoint are superseded by the dated approvals, not rewritten.

## Delivered scope

Contracts 0.6.0 locally promotes eleven exact artifacts: fifteen additive operations (42 total), four minimal workforce event schemas and their examples/requests/negatives. Prior 0.5.0 OpenAPI is archived and old event bytes/27 operations are preserved. Approved OpenAPI info.version remains its historical 0.2.0; repository release metadata is separate.

Operations adds immutable worker registrations/active periods, daily PRESENT/ABSENT/EXCUSED evidence, manager correction/void/re-record, protected revisions, scoped lists/coverage and original-success idempotent receipts. Additive V4 preserves V1–V3. Restricted runtime grants, permanent uniqueness, root locks and deferred consistency guards protect audit evidence. Positive workforce roles are separate from legacy unions; current scope is rechecked before receipt replay. A bounded, delegated Estate adapter fails closed. Four minimal event families omit names/codes/reasons/actors and use the existing reliable relay.

Gateway adds two path families. Infrastructure adds four explicit workforce bindings to a separate bounded durable sink and a generated-only full-platform drill. Web 0.4.0 (local/unpublished) adds workers and attendance screens, active-period flows, protected history, role/scope navigation, estate-local dates, explicit unmarked evidence, current-division coverage, original-version conflicts, frozen identical retries and dirty-state protection. Personal data is not persisted in browser storage. Estate administration and Cesium remain intact.

## Actual checks

| Repository/check | Result |
|---|---|
| Contracts validator and contract tests | PASS; 24 tests, accepted hashes and legacy compatibility |
| Operations full `mvnw.cmd verify -Pintegration` | PASS; 102 unit/security + 75 integration cases |
| Operations subsequent targeted CollectionCredentialsIT | PASS; 5 cases including new prior-3B-image/V4 retained-evidence drill; current integration XML inventory totals 76 passing cases, not a second full-profile run |
| Operations actual runtime/pin validators | PASS; 42 operations, six closed workforce response shapes, eight actual workforce envelopes covering four families; retained legacy exports validated |
| Operations comparison/projection harnesses | PASS; 3 comparison, 5 collection projection and 2 workforce projection tests; duplicate/reordering/gap/tombstone/conflict/atomic dedup policy, no shipped consumer |
| Operations exact artifact checkout regression | PASS for autocrlf false/true; no product index changes |
| Gateway Maven verification | PASS; 14 route/security tests |
| Infrastructure offline configuration | PASS; old topology retained plus four explicit workforce bindings |
| Disposable full-platform `python scripts/verify_workforce.py` | PASS; independent Docker builds, real Keycloak PKCE/JWT → Gateway → Operations → Estate, retained 3A/3B, worker lifecycle/history/coverage, scope/REAL denial, original receipt replay, broker outage/recovery and all four minimal event families received |
| Web locked install | PASS; 604 packages installed, audit reported zero vulnerabilities at execution time |
| Web lint/format/types/generated API pins | PASS |
| Web final unit/component tests | PASS; 49 tests in 15 files |
| Web final mocked UI suite | PASS; 14 cases including six workforce cases |
| Web production build | PASS; existing Cesium CommonJS warnings remain |
| Web graphics regression | PASS; one Cesium ingestion/route-remount case, run separately from UI |
| Web narrow layout | PASS at 390 px, no horizontal overflow; retained screenshot visually reviewed at `agrosphere-web/target/workforce-narrow.png` |
| Architecture workspace validation | PASS; fourteen ADRs, twelve independent product Git roots, no parent build/submodules, workflow/layout checks |

Final Web image status/hash is recorded in evidence/checkpoint after the public-source allowlist rebuild. Packaging excludes the owner's configuration, private environments and Git metadata, using generated public defaults. Browser mocks are not a live browser mutation test; real HTTP/platform acceptance is separate. Neither software WebGL timing nor this platform drill establishes D08 workload latency or M2 reference-device performance.

The final successful Compose project was `agrosphere-3a-check-c21fb93d`. Its finally cleanup completed. Read-only Docker checks on 2026-10-30 found no containers/volumes for it or the earlier failed `agrosphere-3a-check-86c8515e`. Existing stacks were not reset, seeded, upgraded or restarted.

## Acceptance and remaining gates

| Criteria/tasks | State and evidence |
|---|---|
| WA-T01–T06; AC01–13 | Local implementation and relevant domain/database/signed HTTP/contract/broker/platform checks pass. Prior-image test uses pinned 3B with additive V4/evidence retained. |
| WA-T07; AC14 | Web functionality and automated role/retry/conflict/history/session/focus/dirty/narrow checks pass; existing UI/graphics regressions pass. Owner functional review remains separate. |
| WA-T08; AC15 | Disposable real-platform functional verification passes; final package evidence recorded separately. |
| AC16 / D08 | OPEN: owner must provide rollout languages/connectivity, expected worker/estate volumes, concurrent usage and response budgets. No invented business counts or performance acceptance. |
| AC17 / D09 | SIMULATED-only restriction verified at domain/HTTP/database. Actual purpose/access/retention/deletion policy across roots, evidence, receipts, logs, broker/DLQ and backups remains OPEN before REAL use. |
| WA-T09 / AC18 | Local docs, independent release/pin decisions and source/test evidence recorded. Overall production/REAL/performance acceptance remains OPEN. |

Operations, Gateway and Infrastructure application changes remain Unreleased; their existing independent VERSION values are not presented as new published releases. Contracts 0.6.0 and Web 0.4.0 are local/unpublished candidates. No commit/tag/push/publish/production deployment, destructive migration, existing-realm provisioning, private-environment access or AEO mutation occurred.

## Resolved verification issues and safe continuation

Browser tests caught the old login guard excluding scoped supervisors/auditors and navigation overflow after adding links; both were fixed and all affected checks rerun. Test expectations were corrected to the approved REAL denial (403). The prior-image test stopped streaming a partially consumed ZIP pipe and instead uses a generated isolated archive; migration metadata assertions use the migration-owner connection without weakening runtime grants. All three failures were followed by passing checks. An infrastructure unittest discovery command found no test files; it is not counted as a successful test suite.

The final image rebuild was initially prevented by automatic approval review hitting a usage limit; after resuming, Docker was stopped. The owner restarted Docker and the public-source rebuild was retried. Earlier successful image packaging predates the last responsive CSS change and must not be claimed as final-source packaging.

Next: owner reviews the local SIMULATED workflow and supplies D08 inputs/D09 policy when ready. Existing stack deployment/startup, Git publication and REAL onboarding remain separately authorized actions. Do not ask again for already accepted WA-1 contracts/design; do not enable REAL data, invent plantation details, or change AEO to satisfy an acceptance gate.
