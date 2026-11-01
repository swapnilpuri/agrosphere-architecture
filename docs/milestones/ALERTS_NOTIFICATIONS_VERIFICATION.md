# AN-1 local implementation and verification — 2026-10-31

The owner-approved in-app alert increment is implemented locally across independent Contracts, Operations, Gateway, Infrastructure and Web repositories, with approval/evidence in Architecture. This is SIMULATED-source, generated-identity engineering verification, not non-generated account rollout, REAL enablement, production readiness or owner functional acceptance.

See [design approval](ALERTS_NOTIFICATIONS_APPROVAL.md), [exact executable acceptance](ALERTS_NOTIFICATIONS_CONTRACT_APPROVAL.md), [reviewed package](ALERTS_NOTIFICATIONS_REVIEW.md), [local evidence](ALERTS_NOTIFICATIONS_LOCAL_EVIDENCE.json) and Contracts [0.8.0 release record](../../../agrosphere-contracts/docs/alerts-notifications/RELEASE_0_8_0.json). Approved design SHA-256 remains `22d8c98ede00c4e912f98922f944417aca54bc585a48efe7beb74f59d1364251`; candidate manifest remains `d96a5885a60e4e16e2b6e196806d26c8e50a8b58d0243d06a8a6651962b3274c`. Historical pending labels in preserved review documents are superseded only within those dated approvals.

## Delivered scope

Contracts 0.8.0 locally promotes the exact four accepted artifacts: 64-operation API (58 preserved plus six alerts), two closed command shapes, nine positive response fixtures and twenty negatives. Prior 0.7.0 API/VERSION are archived byte-for-byte. All old events, prior archives and reviewed candidate/manifest bytes remain intact. No new shared event family or notification delivery receipt is invented. Operations/Web pin the accepted API independently; OpenAPI info.version remains its accepted historical value.

Operations adds deterministic local rule evaluation to accepted incident revisions in the same source-root/revision/outbox/original-receipt transaction. One incident/rule alert, versioned attention, explicit personal read, first shared manager acknowledgement, protected immutable history, stable scoped pages/counts and six signed-JWT endpoints implement the package. Additive V6 preserves V1–V5. Alerts do not assign/triage/resolve the incident. No backfill, source text/contact copy, worker linkage or broker consumer.

The feature is disabled by default. Generated tests require both explicit test mode and an exact allowlist of generated subjects. Existing accounts are not enrolled, contacted or tracked. The running developer stack was not changed or upgraded. Gateway adds only `/api/v1/alerts/**`. Infrastructure adds a generated-only drill and a guarded disposable-project enablement helper; existing broker topology is unchanged. Web 0.6.0 local adds the selected-estate badge, visible/online poller, inbox/detail/source link/history and explicit read/ack/retry/conflict/session/dirty-navigation/narrow flows.

Guides: Operations [implementation/recovery](../../../agrosphere-operations-service/docs/ALERTS_IMPLEMENTATION.md), Web [screen guide](../../../agrosphere-web/docs/ALERTS.md). MQTT, Analytics, external/targeted channels, escalation, diagnosis and REAL data remain excluded.

## Actual checks

| Check | Actual result |
|---|---|
| Contracts main validator, all four deterministic builders, exact promotion/pins/archives | PASS; exact manifest/candidate and prior 0.7.0 bytes preserved |
| Contracts tests | PASS; 48 cases, including 12 AN-1 cases |
| Operations full `mvnw.cmd verify -Pintegration` | PASS; 153 unit/security/domain cases plus 103 integration cases, zero failures/errors/skips |
| Final portable prior-II fixture rehearsal | PASS; separate targeted CollectionCredentialsIT, seven cases. This test-fixture-only revision postdates the full-profile pass; runtime code is unchanged. It does not represent a second full-profile run. |
| Actual runtime/HTTP schema comparison | PASS; all 64 actual operations, all six alert response shapes, retained seven crop-health/six workforce shapes, 36 actual crop-health + 36 workforce envelopes and ten legacy actual envelopes validate. No new shared events. |
| Retained projection/comparator/checkout harnesses | PASS; five collection, two workforce, four crop-health and three comparator tests; real autocrlf false/true checkout with disposable indexes |
| Gateway Maven verification | PASS; 15 cases including alert transport, query, body and idempotency forwarding plus retained security behavior |
| Infrastructure offline validator | PASS; existing bounded sinks/queues/DLQs retained; no alert queue introduced |
| Real generated-platform `verify_alerts.py` | PASS; independent Operations/Estate/Gateway builds and real Keycloak PKCE -> Gateway -> Operations -> Estate, default-disabled/no-backfill, source/read/ack/resolve/reopen/replay/role/REAL and broker-independent inbox; retained II/WA/3B/3A pass |
| Web locked install | PASS; final `npm ci`, 604 packages. Earlier Windows in-use binary failure and same-lock repair are recorded below. |
| Web lint/format/types/independent API pins | PASS |
| Web final unit suite | PASS; 63 cases in 17 files |
| Web final mocked UI suite | PASS; 26 cases with one worker, including six new AN-1 cases |
| Web separate retained graphics suite | PASS; one Cesium ingestion/route-remount case, software rendering only |
| Narrow visual inspection | 390px no horizontal overflow, detail keyboard focus and protected history; final screenshot visually inspected after Unicode corrections |
| Local packaging | PASS; independent Operations `an1-local` and public-source Web `0.6.0-local` images, with no owner configuration/private files in Web build context. No packaged image started against an existing stack. |
| Architecture/workspace/diff/preservation | PASS; sixteen accepted ADRs, twelve independent product roots, all thirteen HEADs/staged contents retained; Operations stat-cache refresh recorded below, prior data/config/source safeguards as recorded in evidence |

Functional platform project `agrosphere-3a-check-e9d6a78c` completed its finally-cleanup path. Read-only Docker inspection found no remaining containers/volumes carrying that project label. No generated fixture was copied into an existing database. Platform verification preceded the final exact-decimal parser refinement, which subsequently passed the full real HTTP/database regression; transport/platform business semantics did not change. Final Operations local packaging includes the refined runtime. The later portable rollback-fixture adjustment changes tests/historical source inputs only.

Image IDs and final source/report hashes are in the local evidence. The Web image was rebuilt after encoding/polling corrections. Retained JVM/Mockito and Cesium CommonJS warnings remain limitations. No hosted CI, reference-device performance, live browser business mutation, real recipient delivery or new diagram rendering is claimed.

## Acceptance traceability and open gates

| Criteria | Evidence/state |
|---|---|
| AN-AC01–02 | Exhaustive pure severity/status/provenance rules, real direct/linked source lifecycle, same-severity edit/escalation, resolve/reopen and stale attention checks pass. CLEAR/low observations do not automatically create alerts. |
| AN-AC03 | Generated DB/HTTP tests prove source+alert atomic failure rollback, no duplicate linked alert, receipts and competing manager races; existing source receipt replay bypasses rule work. No network/broker call inside rule. |
| AN-AC04–05 | Signed service JWT/role/estate/foreign-ID/downgrade/no-store, own-read separation, first shared acknowledgement, stale versions, same-key canonical integer replay, unknown fields/duplicates/fractions/overflow and protected projections pass; real Gateway/Keycloak platform complements them. |
| AN-AC06 | Exact accepted promotion/archives/independent pins, strict 64-operation comparison and all actual alert response shapes pass. Old 58 operations/events retain semantics/bytes. |
| AN-AC07 | Fresh/populated-V5 upgrade, failed-V6 DDL rollback and no backfill pass; runtime DDL/evidence/receipt denial, populated separate alert/read/ack/receipt restore and prior-II runtime retaining V6 evidence pass. No destructive down migration. |
| AN-AC08 / AN-D08 | Scoped coherent pages/counts/bounds/indexes pass functionally. Actual volumes/concurrency/languages/network/latency/staleness budgets and measured workload acceptance remain OPEN. Proposed polling interval is not an SLA. |
| AN-AC09–10 | Web unit/mock UI/narrow/focus/session/cancel/hidden/offline/429/retry/conflict tests and real generated Keycloak/Gateway platform pass. Existing crop/workforce/admin/Cesium and source outbox behavior retained. |
| AN-AC11 / AN-D07 | OPEN: actual subject-purpose/access/retention/deletion policy across markers/ack/receipts/evidence/logs/backups is absent. Default-disabled plus exact generated-subject gate prevents implied live rollout. SIMULATED reports do not remove account-subject privacy obligations. |
| AN-AC12 / AN-T09 | Local guides/pins/changelogs/versions/checkpoint/check evidence recorded. Owner functional sign-off, non-generated rollout, REAL, production and M2 remain OPEN. |

AN-T01–07 implementation and AN-T08 generated functional verification are complete locally; AN-T09 local documentation/evidence is recorded. This does not close every overall acceptance criterion, FR-06's wider delivery needs or parent Milestone 3.

## Resolved failures and preservation

The first integration command needed PowerShell quoting for `-Dit.test`. Sandbox Docker/temp-directory/browser subprocess limitations required scoped escalation; generated-only checks then ran. Initial trigger evaluation accessed a field absent on another table's OLD record; nested table-specific dispatch corrected it, followed by real HTTP/DB verification. Old regression expectations of five migrations were updated for additive V6; their initial failures caused dependent fixture failures, not removed business assertions.

Browser tests caught focus scheduled before DOM render; focus now waits for Angular render. Visual inspection caught Windows default-decoding damage in edited Unicode text; original shell characters and the alert template/timestamp were restored, with a browser assertion and final rebuild/UI pass. `npm ci` initially hit an in-use esbuild binary; a same-lock package restoration preserved the running frontend, and the final locked install passed. The dependency graph is unchanged except Web version metadata. The audit still reports 28 moderate development-tool entries; no automatic dependency remediation was applied.

Existing staged/unstaged/untracked work is preserved. All repository HEADs and staged source contents are preserved, along with the Web `public/config.json` index entry/hash, V1–V5, old events, accepted packages/manifests, prior archives and AEO. Twelve raw Git indexes remain byte-identical. During final checks, Operations refreshed the stat-cache entry for the unchanged workforce validator after its original bytes were restored. The staged inventory/status did not change: 166 tracked staged blobs match initial working hashes (allowing Git EOL normalization), and all three initially MM documentation bodies were independently verified against reconstructed original working bytes. This covers every pre-existing staged change. The raw metadata refresh is recorded in evidence; no staging/commit/tag/remote action occurred. The previous checkpoint is retained verbatim as a suffix. No existing records/volumes/SIMULATED demo boundaries/two fields each were read/recreated/reseeded for this increment. No private environment/saved account was read; no existing stack/account/credential/realm-role change, external notification, commit/push/publish/deploy/destructive migration or AEO mutation occurred.

## Safe continuation

Do not ask for design or exact executable approval again. Owner reviews functional behavior separately when an appropriately governed demonstration is available. Supply AN-D07 subject-data policy and AN-D08 workload/language/connectivity/budget inputs, retaining WA D08/D09 and II-D07/08. Implement/test reviewed policy before non-generated account rollout; keep REAL disabled. Any future existing-stack upgrade requires a concrete separately authorized backup-preserving plan. Do not reuse test-mode flags for actual accounts or repeat the completed II-1 upgrade. No automatic backfill/reconciliation, real plantation invention or AEO operation follows from this result.
