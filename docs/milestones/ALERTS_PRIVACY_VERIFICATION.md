# AN privacy extension — local implementation and verification

Date: 2026-10-31 (America/Chicago). Status: **GENERATED-ONLY RUNTIME VERIFIED; OPERATING/ROLLOUT GATES OPEN**.

The [owner approval](ALERTS_PRIVACY_APPROVAL.md) accepts the exact [technical package](ALERTS_PRIVACY_EXTENSION_REVIEW.md) and five-artifact manifest `ea6402a205d1da7a0801090b0acabac58ae164ba6544b474d709d8a4a608286b`. Original reviewed bytes and all previous approvals are retained. Earlier pending labels in those frozen documents are historical for the approved local implementation scope only. Business defaults remain provisional under the [single client decision register](ALERTS_NOTIFICATIONS_CLIENT_DECISIONS.md); the client has supplied no new answers and no legal/owner functional acceptance is inferred.

## Delivered locally

- Independent Contracts **0.9.0** promotion/archive/release metadata and exact Operations/Web pins. Previous 0.8.0 API/VERSION and producer/consumer snapshots are archived. Candidate/manifest/review and old event bytes remain unchanged. No remote release or publication.
- Operations: independent privacy root/lifecycle rules, UUIDv7 admission and hard retry ceiling, separate additive **V7** privacy storage, six v2 routes, explicit expiry/redaction/partial history, first shared acknowledgement and original authorized success replay. Root/evidence exclude actor copies; acknowledger attribution is separately retained. Old V1–V6 tables/guards/rows/grants are not modified.
- Read and receipt logical expiry, no old-marker/receipt resurrection across reopening, 365-day attribution/history expiry, verified-removal cutoff including allowed future skew, bounded removal ledger, owner-controlled eligible cleanup and isolated current-ledger restore evidence. Normal runtime cannot DELETE, invoke maintenance/removal functions or edit completed receipts/evidence.
- Privacy and legacy modes default off and are mutually exclusive; privacy requires an exact generated-subject allowlist and refuses nonempty V6 legacy alert storage. V1 alerts retire in privacy mode; no fallback or automatic historical conversion/backfill. Source transactions and existing module events/outbox remain independent of broker delivery.
- Web **0.7.0**: independently pinned v2 alert types/routes, memory-only frozen UUIDv7 keys, explicit expired read/attribution/history states, 410/unknown-409 refresh without automatic replacement commands, and narrowly extended Gateway token boundary. Gateway adds only the new alert route. Existing public config and previous modules remain preserved.
- Infrastructure generated-only drill uses a new random Compose project and existing topology, with real Keycloak/Gateway/Estate/Operations, retained 3A/3B/WA/II checks and own-project cleanup. No existing stack upgrade, credential/role change or data reset occurred.

Runtime detail and operating instructions: [Operations guide](../../../agrosphere-operations-service/docs/ALERTS_PRIVACY_IMPLEMENTATION.md). The reviewed [local-stack plan](ALERTS_PRIVACY_LOCAL_STACK_PLAN.md) remains conditional preparation, not authorization to execute it.

## Actual validation

| Area | Command/evidence | Actual result |
|---|---|---|
| Contracts | Existing `.venv` `python scripts/validate.py`; all `test_*contracts.py` | PASS, 59 tests (48 retained + 11 privacy); exact local 0.9.0/current and 0.8.0/archive bytes verified; 70 proposed/actual operations retain the old 58 non-alert operations and all old schemas. |
| Operations full profile | `mvnw.cmd verify -Pintegration`, ignored `target/privacy-final-verify.log` | PASS: 172 unit/security/domain tests and 113 real integration tests, zero failures/errors/skips. Includes the then-current ten-case privacy class and all retained modules/previous-image checks. |
| Final targeted privacy boundaries | `mvnw.cmd -Pintegration -Dit.test=PrivacyAlertServiceIT failsafe:integration-test failsafe:verify`, ignored `target/privacy-it-boundaries-final.log` | PASS: 12 cases. Adds exact removal-cutoff replacement and atomic failed-V7 rollback; validates the final inclusive cutoff predicate. This targeted run follows the full profile, not a claimed second full profile. |
| Operations API/pins | Collection, workforce, crop-health, legacy alert and new `validate_alert_privacy_runtime.py`, plus `validate_contracts.py` | PASS: 70 actual operations; ten real privacy HTTP shapes and expired/redacted/partial invariants; old actual HTTP/event shapes and exact archives retained. |
| Projection/comparison | Collection/workforce/crop-health projection scripts; comparator unit tests | PASS: 5/2/4 projection cases and 3 comparator cases. |
| Checkout bytes | `python scripts/test_contract_checkout.py` | PASS for actual Git autocrlf false/true in disposable repositories/indexes; new 0.9.0 pin and prior-0.8.0 archive included. No application-repository staging command. |
| Gateway | `mvnw.cmd test` | PASS: 16 cases, including v2 body/key/bearer/correlation transport. |
| Web dependencies and static checks | Locked `npm ci --no-audit --no-fund`; lint, format check, typecheck, API check | PASS. No dependency upgrades; package/lock version metadata moves to 0.7.0. |
| Web unit/build | `npm test`; `npm run build` | PASS: 66 tests; build retains known Cesium CommonJS optimization notices. |
| Browser | Sequential `npm run e2e`, then `npm run e2e:graphics` | PASS: 29 mocked UI cases and one software graphics smoke. Includes expired-read explanation, no replacement after 410 and expired/partial history. Not reference-device/offline/performance acceptance. |
| Web Docker | Public-source `scripts/build-public-image.ps1` | PASS: local image `sha256:fddb0fb79d6a9fa3f4ad8c1006d39493bf10cdb5cec1782e9d302a3fbbb0bd8a`, placeholder config only; owner's public/config.json never read/copied by the build script. |
| Generated platform | `python scripts/verify_alert_privacy.py`, ignored Infrastructure `target-privacy-platform-final.log` | PASS: real Keycloak/Gateway v2 lifecycle/read/ack/replay, default disabled/no backfill, role/REAL denial and broker-independent inbox; prior modules retained. Project `agrosphere-3a-check-47eab4d5` removed. This preceded the final one-character inclusive cutoff refinement, which is covered by the 12-case targeted backend recheck; no new wire shape was changed. |

Architecture workspace validation, final diff/index/content preservation and machine-readable source hashes are recorded in [local evidence](ALERTS_PRIVACY_LOCAL_EVIDENCE.json) after execution. Neither raw unit calculations nor generated tests prove that a deployed scheduler, external log collector or backup provider enforces a retention rule.

## Failures found and corrected

- First release validation still expected 64 operations/old VERSION at some retained validators. Exact 0.8.0 archival projections and new-release checks were added; old constraints, manifests and candidate bytes remain verified rather than ignored.
- A Java wildcard Actor/Permission import failed compilation; explicit imports corrected it. Partial compiler output then lacked an old synthetic enum class; only generated classes/test-classes were moved aside under `target` and rebuilt, preserving source and previous generated outputs.
- Generated historical fixtures initially omitted a backdate reason, had inconsistent timestamp chronology and formatted session-local time as UTC. Explicit SIMULATED reason and UTC fixture times corrected the fixtures. No active-stack clock/data was changed; deliberate fixture trigger control applies only to new tables in owned disposable databases.
- First full profile found two retained previous-image tests still expecting migration head 6; assertions were updated to 7 without removing preservation checks. All seven credential/image checks passed on targeted recheck, then the full final profile passed.
- Browser tests initially lacked a background `/api/v2/alerts` mock outside the alert feature, causing retained tests to lose their mocked session; default disabled/no-store mock added. Stale-ack wording retained the expected explicit review instruction. The first failing browser run was stopped, then all 29 UI and graphics checks passed sequentially.
- Review identified stale receipt copies after reopening before physical cleanup; persistent expiry watermarks now suppress/delete those copies too. The final targeted database test covers that race and exact inclusive removal cutoff replacement.
- Windows sandbox denied Docker, npm/esbuild process launch and disposable temp-directory checkout tests. Scoped approved generated-only checks ran with escalation. No automatic-review rejection remains. Global Python lacked an OpenAPI validator; the existing Contracts virtual environment supplied verification tooling without adding a runtime/build sibling-source dependency.

## Acceptance and remaining gates

AP-T02–06 are implemented locally in generated scope. AP-T07 has generated API/database/Web/platform/restore evidence; real operating controls remain OPEN. AN-D07 is therefore **partially implemented and verified, not closed for actual subjects**.

| Gate | Remaining action |
|---|---|
| Daily physical cleanup | Select/authorize a protected maintenance principal and scheduler, arrange daily invocation/overdue monitoring, prove the 24-hour objective under failures. The cleanup routine is tested; no unattended job is installed against an existing database. |
| Logs and backups | Configure/inventory actual ordinary/security logs and all backup/replica/export chains; verify 14/90/35-day limits and current-ledger preservation through restore. These are not implemented provider settings or legal minimums. |
| Client/subject policy | Client confirmation, accountable organization/contact, applicable basis, user information/notices, actual hosting/data-flow locations and any evidenced exceptions remain open. Do not invent these facts or enable actual accounts through generated flags. |
| Existing data/stack | Obtain exact authorized preflight/targets, protected backup and accepted artifact/migration/maintenance plan. Nonempty V6 needs a separate preservation-focused conversion review. Current records/volumes/config/geometry stay intact; II-1 is not repeated. |
| Owner functional acceptance | Perform the explicitly scoped office-connected SIMULATED create/read/shared-ack/resolve/reopen review after a governed demonstration is available. Engineering success does not supply this decision. |
| Broader modules | AN-D08 workload/language/latency disposition, WA D08/D09, II-D07/08, M2, REAL and offline Android/French/faster-refresh requirements remain independently open. |

The next eligible work is an operating-readiness/preflight review using the [conditional plan](ALERTS_PRIVACY_LOCAL_STACK_PLAN.md), not another request to approve the already accepted design/candidate. No existing-stack action, actual accounts, REAL collection, external notifications, credential/role modification, Git commit/push/publication/deployment or AEO mutation follows automatically.

## Repository preservation

Six independent repository HEADs remain unchanged. All approved review/candidate bytes, old events and V1–V6 migrations remain byte-identical; the full pre-approval checkpoint is retained verbatim as a suffix and Web public/config.json working bytes remain unchanged. Local promotion deliberately replaces current contract copies while retaining prior exact releases in archives.

**Staging observation:** all six raw indexes/staged inventories changed during this run, including previously untracked prior work becoming staged. No root-repository staging/reset/commit command was executed by this implementation. Do not mistake this for a metadata-only refresh or claim initial raw-index identity; preserve the observed current index without undoing it. A fresh staged-entry baseline was captured read-only for final comparison. Source/data preservation and staged-state observations are reported separately in local evidence.

Final PASS: Architecture workspace validator; unstaged diff checks in all six roots; current staged entries match the read-only post-change baseline; review links resolve; no containers/volumes remain for agrosphere-3a-check-47eab4d5. Default staged diff checking reports pre-existing frozen CRLF contract lines; checks with temporary `-c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol` pass in all six roots without changing repository config, index or approved bytes. This distinction is recorded in local evidence. V1–V6, old events, reviews/candidate, Web config and the pre-approval checkpoint suffix remain preserved.
