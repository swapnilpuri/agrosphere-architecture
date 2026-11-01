# II-1 local implementation and verification — 2026-10-31

The owner-approved incident/inspection increment is implemented locally across independent Contracts, Operations, Gateway, Infrastructure and Web repositories. Architecture records approvals/evidence. This is a SIMULATED-only, local/unpublished implementation, not production, REAL-data or owner functional acceptance. The existing developer stack was not upgraded or reseeded.

See [design approval](INCIDENT_INSPECTION_APPROVAL.md), [exact executable approval](INCIDENT_INSPECTION_CONTRACT_APPROVAL.md), [reviewed design](INCIDENT_INSPECTION_REVIEW.md) and [local evidence](INCIDENT_INSPECTION_LOCAL_EVIDENCE.json). Approved package SHA-256 remains `79944183a963bdddd4008557e2a8eb1e15acff739b612fb0d2e95d9d4f7da8e8`; executable manifest remains `e04a8b289682dcfe1e6b38f490cb867ca67fd7db7717348f40a30758be9307bd`. Historical pending labels in the unchanged reviewed artifacts are superseded by dated approvals.

## Delivered behavior

Contracts 0.7.0 locally promotes the exact eleven artifacts: 58-operation API (42 preserved + 16), four minimal crop-health/v1 schemas, four SIMULATED event examples, seven request shapes and fourteen negative fixtures. Prior 0.6.0 API/VERSION are archived byte-for-byte; earlier archives/events/examples remain intact. Accepted OpenAPI info.version stays its historical 0.2.0, separate from repository release metadata. Operations and Web independently pin the accepted bytes.

Operations adds completed block inspections, atomic first FOLLOW_UP incident creation, direct reports, manager triage/amend/resolve/reopen/correct/void, immutable revisions, scoped pages/history, durable original-success receipts and four minimal outbox families. Additive V5 preserves V1–V4 and all old modules. Dedicated signed-JWT positive permissions, delegated bounded Estate validation, paired inspection→incident locking, current-scope/permission replay checks and unconditional SIMULATED guards enforce accepted semantics. Runtime grants and deferred evidence/link/outbox constraints are verified on disposable resources.

Gateway adds only the two accepted route families. Infrastructure adds an explicit bounded durable crop-health sink/DLQ and a generated-only full-platform drill retaining 3A/3B/WA-1. Web 0.5.0 local adds inspections/incidents lists, filters/paging, create/detail/linked navigation, manager actions and protected history, estate-local display, explicit offset entry, identical-key retry, conflict comparison and dirty/session/narrow-layout protection. No report data/tokens persist in browser storage.

Guides: Operations [implementation/recovery](../../../agrosphere-operations-service/docs/CROP_HEALTH_IMPLEMENTATION.md), Web [screen guide](../../../agrosphere-web/docs/CROP_HEALTH.md). No attachments, personnel cases, account linking, offline/bulk/export, automatic diagnosis, notification delivery, new geometry or Analytics consumer. The projection policy is exercised in a test harness only.

## Actual checks

| Repository/check | Result |
|---|---|
| Contracts main validator and all three deterministic builders | PASS; exact promotion/manifest, legacy archives and semantics retained |
| Contracts tests | PASS; 36 cases (24 retained + 12 II-1) |
| Operations full `mvnw.cmd verify -Pintegration` | PASS; 128 unit/security/domain plus 91 full-profile integration cases, zero failures/errors/skips |
| Operations subsequent targeted CropHealthStoreIT | PASS; nine cases, including newly added populated II-1 backup/restore into a separate disposable DB. Integration XML inventory is now 92 passing cases; this was not a second full-profile 92-case run. Last addition changes tests only. |
| Actual runtime/API/event/response validators | PASS; all 58 actual operations, seven closed II-1 HTTP shapes, 24 actual II-1 envelopes covering four families; six workforce shapes/24 envelopes, retained tapping and collection exports also validate |
| Projection/comparison harnesses | PASS; four crop-health, two workforce, five collection and three comparator tests |
| Real Git checkout byte regression | PASS; autocrlf false/true, using disposable indexes only |
| Gateway Maven verification | PASS; 14 route/security cases, including both new path families and idempotency/body forwarding |
| Infrastructure offline validator | PASS; retained topology plus bounded explicit crop-health queue/DLQ |
| Generated-only full-platform `verify_crop_health.py` | PASS; independent Operations/Estate/Gateway image builds, real Keycloak PKCE/JWT → Gateway → Operations → Estate, retained 3A/3B/WA-1, linked lifecycle/history, role/REAL denial, original receipt replay and broker outage/recovery; all four minimal event families received |
| Web locked `npm ci` | PASS; 604 packages installed. Audit findings are recorded separately below. |
| Web lint/format/types/API pins | PASS |
| Web final unit/component suite | PASS; 56 tests in 16 files |
| Web final mocked browser UI suite | PASS; 20 cases, one worker, including six II-1 cases |
| Web separate graphics suite | PASS; one retained Cesium ingestion/route-remount case |
| Narrow layout | PASS at 390 px, no horizontal overflow; target/crop-health-narrow.png visually reviewed |
| Independent production builds/packages | PASS; Web build, final Operations local Docker image and Web public-source allowlist image. No owner's configuration/private files copied into Web image. |
| Architecture workspace audit/diff/preservation checks | PASS; fifteen ADRs, twelve independent product roots, no parent build/submodule; approved bytes, old migrations/events and Web config/index retained |

Final functional platform project: `agrosphere-3a-check-7bed467a`; earlier `agrosphere-3a-check-b629cbca` also passed. Both finally-cleanup paths completed; read-only Docker inspection found no remaining containers/volumes for either project. Test fixtures were not copied into any existing database. The final Swagger-only documentation correction was subsequently verified by full HTTP/runtime comparison and packaged independently; no business behavior changed after the functional platform pass.

Final local images: Operations `agrosphere-operations-service:ii1-local`, `sha256:46e0c782f71a111a627415523e430b1c6c3c79094a6d18e16b99348a5fe946cf`; Web `agrosphere-web:0.5.0-local`, `sha256:14d38ac3c2d03b36775ea0f6026f9b73e2c5d59baf688a12796298c8bce64769`. The additional populated-restore test postdates Operations packaging; shipped runtime code is unchanged. Gateway packaging passed in the independent platform build. None of these images was started against an existing stack.

## Acceptance traceability and open gates

| Criteria | Evidence/state |
|---|---|
| II-AC01–03 | Pure rules, real scoped HTTP/DB lifecycle, atomic links, versions/races, immutable history, offset/backdate/timezone/DST and retained resolution chronology pass. |
| II-AC04–06 | Signed JWT/direct service/Gateway, role/estate/foreign-ID/history/replay/REAL denial, closed shapes, normalized receipts, stale/paired versions and frozen browser retry pass. No production identity provisioning asserted. |
| II-AC07–08 | V5 fresh/upgrade/failed-DDL rollback, restricted runtime/evidence denial, paired atomic rollback, prior-WA image with retained V5 and separate populated restore pass. Fail-closed delegated reference scenarios pass; geometry is not a prerequisite. |
| II-AC09–11 | Exact accepted contracts/old bytes, actual 58-operation comparison and response/event schema/identity checks pass. Real delivery recovery and retained generic relay fault regressions plus test-only dedup/reorder/gap/tombstone/conflict/link policy harness pass. Scoped lists/counts/filter bounds pass. |
| II-AC12–13 | Web unit/UI/keyboard labels/focus/role/history/conflict/retry/dirty/narrow and existing administration/workforce/Cesium regression pass. Real generated platform and independent packaging pass. Mocked UI is not a live browser mutation test. |
| II-AC14 / II-D08 | OPEN: actual report volumes, concurrent users, languages/connectivity and budgets are not supplied/measured. WA D08 and M2 reference-device performance remain independent. |
| II-AC15 / II-D07 | SIMULATED-only candidate restriction verified. REAL purpose/access/retention/deletion across reports/evidence/receipts/logs/broker/DLQ/backups remains OPEN; WA D09 remains OPEN. No policy or national compliance claim is invented. |
| II-AC16 / II-T09 | Local guides, independent versions/pins/changelogs, exact checks/hashes and safe continuation recorded. Owner functional sign-off, production, hosted CI and remote publication are not asserted. |

II-T01–07 implementation and II-T08 functional disposable verification are complete locally. Overall production/REAL/load acceptance is open. Notifications remain deferred FR-06 scope, so parent Milestone 3 is not closed.

## Resolved failures and verification limits

Real-clock testing caught a per-call timestamp drift between roots/revisions; command time now freezes once and the full signed HTTP suite passes. Reference error ordering was corrected to distinguish inactive/mismatched (422) from malformed/unavailable (503). The approved JSON-formatted OpenAPI contains a JSON exponent that PyYAML's YAML 1.1 resolver misread; validators now parse JSON as JSON without modifying approved bytes. Swagger Schema.setRequired dropped a conditional sibling-defined required field; the documentation adapter restores that exact accepted constraint, with a serializer regression and strict actual comparison.

Legacy tests expecting four migrations were updated for additive V5; their initial failures cascaded into dependent fixtures. One later full run encountered transient legacy RabbitMQ EOF connection errors; the final sequential full-profile rerun passed without weakening assertions. Browser checks exposed a region name and a wrapping-label locator mismatch; explicit region labeling and the accessible combobox locator were corrected, then all 20 cases passed. Sandbox subprocess/Docker/temp-index limitations were resolved through approved escalation. An automatic approval-review usage-limit failure initially prevented the platform command from executing; after the owner's resume, authorized retries succeeded. No unresolved approval-review block remains.

Fresh npm audit reports **28 moderate development-tool dependency entries**, zero high/critical, and **zero findings with `--omit=dev`**. The dependency set is unchanged except local package version metadata. Reports are retained under ignored Web target/ii1-npm-audit*.json. Remediation of existing toolchain advisories remains maintenance work; no automatic `npm audit fix`, downgrade or breaking dependency change was applied. This is not a security certification.

No live browser business mutation, existing-stack upgrade, production/REAL/performance acceptance, hosted CI run or new diagram rendering is claimed. Existing Cesium CommonJS/JVM test-tool warnings remain. Existing data/volumes, SIM-GA-DEMO/SIM-MW-DEMO boundaries/two fields each, Web configuration/index, existing credentials/roles and AEO were untouched. Generated credentials/roles and destructive cleanup were limited to new disposable test resources.

## Safe continuation

Owner reviews the SIMULATED workflows and supplies II-D07/08 and WA D08/D09 inputs when ready. No need to repeat design or exact executable acceptance. Existing-stack upgrade is separately authorized: before any such action, prepare a concrete backup-preserving Operations/Gateway/new-binding plan retaining existing records/volumes/config/roles and verify the module through existing accounts without seeding. No automatic upgrade, REAL onboarding, role/credential change, commit/tag/push/publish, production/destructive migration or AEO action follows from local implementation success.
