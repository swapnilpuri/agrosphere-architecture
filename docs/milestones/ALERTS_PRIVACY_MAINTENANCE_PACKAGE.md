# Generated-only alerts/privacy maintenance implementation package

Date: 2026-11-01 (America/Chicago). Package: `AP_MAINTENANCE_1`. Status: **PREPARED FOR IMPLEMENTATION REVIEW; NO JOB INSTALLED**.

The owner requested proceeding with the generated-only maintenance/monitoring package and whole-project completion checklist. This package makes the next implementation concrete under the [operating-readiness review](ALERTS_PRIVACY_OPERATING_READINESS.md). It does not execute AP-T08, inspect the existing stack/private configuration, change existing roles/credentials, enable actual subjects, modify retention periods or reopen accepted Contracts 0.9.0 approval. Approved reviews, V1–V7, old events, runtime API pins, source data and Web configuration stay intact. The machine-readable [specification](ALERTS_PRIVACY_MAINTENANCE_SPEC.json) describes proposed behavior, not deployed configuration.

## Proposed artifact set and dependency order

Paths below are deliverables to implement in their owning independent repositories; they are not claims that these files already exist. Read that repository's guidance before editing. No sibling runtime source dependency or common build is introduced.

| Task | Owner / proposed files | Deliverable and exit evidence |
|---|---|---|
| PM01 | Operations `docs/ALERTS_PRIVACY_MAINTENANCE.md`, tests `PrivacyMaintenanceServiceIT.java` | Freeze privilege/output/eligibility design below; capture V1–V7/pin hashes; prove generated runtime/maintenance/monitor role separation |
| PM02 | Operations additive `V8__alert_privacy_observation.sql` | Aggregate-only `privacy_observe()` with PUBLIC execution revoked, explicit schema resolution and no mutation; exact V7 eligibility parity and read-only grants tested; no edit/replacement of V7 cleanup |
| PM03 | Infrastructure `scripts/privacy_maintenance.py`, `scripts/test_privacy_maintenance.py` | Explicit-target one-shot runner; transaction/run budgets, sanitized results, retries and durable atomic heartbeat; no scheduler auto-install or ambient connection defaults |
| PM04 | Infrastructure `scripts/privacy_maintenance_watchdog.py` and tests | Independent heartbeat/observer evaluation; no external notification sending; breach/unknown/warning exit status and bounded aggregate output |
| PM05 | Infrastructure `scripts/verify_privacy_maintenance.py` | Exclusively new labelled project/database/volume, generated principals/fixtures; real DB permissions, lock/failure/capacity and recovery drill; exact owned-resource cleanup verification |
| PM06 | Infrastructure `docs/PRIVACY_MAINTENANCE.md`; Architecture increment evidence/checkpoint | Proposed hourly schedule artifact/invocation guidance, recovery and copy-inventory handoff; exact commands/artifact hashes/results; keep OR01–06 open for selected environment |

PM01/02 precede PM03 database integration; PM04 can be developed independently with generated observations; PM05 follows all four. A V8 observer is a new internal security surface: review exact SQL and effective grants before applying it even in the generated integration fixture. No public API/event change is proposed; if one becomes necessary, stop and use independent Contracts review instead. Do not bypass Maven checks by calling this merely a script change when a migration is added.

## Authority design for generated tests

Use unique generated login names and credentials only inside the owned disposable fixture. Do not add grants to the existing stack. Migration owner installs V8 in the service-owned schema; runtime is unchanged and cannot call cleanup/observation/removal functions or DELETE/DDL. Normal inherited/PUBLIC privileges must be included in effective-permission assertions.

The cleanup principal receives CONNECT to its exact database, USAGE on its exact schema and EXECUTE only on `privacy_cleanup(integer)` and the aggregate observer. The monitor principal receives CONNECT/USAGE and EXECUTE only on the observer; it cannot clean or request removal. Neither receives schema CREATE, table SELECT/DELETE, owner membership or `privacy_request_removal(text,text)` execution. A separately generated verified-removal test operator exercises that function without exposing identity in process output. Existing V7 routine behavior and search-path capture are verified, not silently rewritten. Remove PUBLIC schema CREATE in the owned test fixture where needed to prove no untrusted object substitution; no such change is made to an existing database.

The observer should use a locked-down SECURITY DEFINER owner/search path with explicitly qualified service tables and no dynamic caller SQL or caller-provided cutoff. It returns one aggregate result at database time. Fail on unexpected schema/function owner, privilege drift or V1–V8 migration fingerprint. Observation remains private operator data, not a new HTTP endpoint or public health detail. Exact generated role provisioning and owner choices are implementation artifacts to review in PM01.

## Observation design

Return only database UTC observation time; eligible root count; oldest eligible instant/age by copy class; eligible read/receipt/ack/evidence counts; pending verified-removal count and oldest requested time; expired ledger count/oldest expiry; and observer/policy revision. No estate/root/command/request IDs, issuer/subject, tokens or content. Counts/ages are still restricted operational information.

Match **every** V7 root-selection and delete predicate: inactive + 30-day reads; inactive + 365-day evidence/ack attribution; read/history expired-through watermarks after reopening; orphaned acknowledgement condition; command `expires_at`; verified-removal cutoff for reads/receipts; and global ledger completion/expiry. Do not approximate eligible work with `inactive_since` alone or assume all receipts live thirty days. Each class needs a real eligibility instant derived from original deadline/watermark/removal metadata. If a faithful instant cannot be derived, return UNKNOWN for age, block the on-time-deletion claim and review additive metadata; do not invent a timestamp or mutate old rows.

Pending removal has a separate PR13 request + 30-day deadline; normal expiry can require earlier removal. Report both physical eligibility age and request deadline. A request still pending before five-minute future-skew cutoff must not be reported completed from one empty observation. Observe original metadata and cleanup transaction results. Tests must include requests with no remaining copies and old/new keys around the cutoff.

Observer and cleanup observe separate committed snapshots. Use repeated observations for progress; do not assert a globally quiescent database from one result. Read-only observation must see locked eligible roots that cleanup skips. A zero cleanup return, zero roots with pending ledger work, timeout or missing sample cannot become an all-clear.

## Runner and watchdog behavior

Use a one-shot standard-library orchestrator invoking reviewed database tooling with parameterized inputs or a reviewed driver; select the mechanism in implementation without changing this security boundary. Private connection values use protected transient credential material, never command-line passwords, tracked files, logs or printed subprocess exceptions. Do not read existing `.env` files. Reject missing explicit host/port/database/schema/generated project identity; verify live target identity before any call. Generated-target ownership is a mandatory restriction of this first implementation, not an easily omitted `--force` convention.

Proposed generated defaults: hourly trigger, 200 roots/call, 30-second statement timeout, 2-second lock timeout, 120-second run budget, at most 100 batches and two transient retries with 1/2-second backoff. These are testable starting budgets, not measured capacity or accepted SLAs. Set transaction-local timeouts and leave no open transaction/connection after a run. Stop before the budget is exceeded, rollback only the current failed transaction, and preserve committed previous batches. Use a monotonic clock for local budgets; database UTC for eligibility. Unknown commit outcome causes re-observation and safe eligible cleanup, never fabricated success. Function idempotence/eligibility, not saved command bodies, makes this recovery safe.

Write a sanitized heartbeat atomically to a protected generated output directory: version, target alias/fingerprint, run ID, process start/end, last committed batch, root/batch counts, database observation time, last verified no-overdue observation, and outcome (`SUCCESS`, `PARTIAL`, `ERROR`, `UNKNOWN`). Constrain permissions and preserve the previous complete file on write failure. Bind it to the target/revision and reject future/stale/malformed/foreign heartbeats. No backup or removal-ledger identity data belongs in the heartbeat.

Watchdog runs independently of the runner and reads its heartbeat plus a fresh observer result. Recommended initial thresholds: two missed hourly runs or 12-hour oldest eligible age warns; 24-hour age breaches the healthy physical-cleanup objective; a verified-removal deadline breach is also a breach. Unknown observation/clock skew/invalid heartbeat is UNKNOWN, never healthy. A failed recent job must remain visible even if backlog currently happens to be empty. Separate scheduler liveness, physical backlog and removal deadline states in the output. Prioritize BREACH, UNKNOWN, ERROR, WARNING, HEALTHY; use stable distinct exit codes and include component states. This emits local results only; routing/email/webhooks need later explicit authorization.

## Required generated acceptance matrix

| ID | Scenario | Evidence required |
|---|---|---|
| PM-AC01 | Role boundaries and object substitution | Runtime denied new functions; monitor denied cleanup/removal and raw identity tables; cleanup denied removal/raw tables/DDL; intended calls succeed; captured search path safe |
| PM-AC02 | Exact eligibility boundaries | Before/at/after 30/365-day and receipt deadlines, inactive edits, reopened watermarks and orphaned ack match cleanup; identities never emitted |
| PM-AC03 | Locked root / misleading zero | Independent connection locks sole eligible root; cleanup returns zero; observer still reports eligible work; watchdog never HEALTHY from return count |
| PM-AC04 | Batches / large roots / ledger-only work | More than 200 roots; high child counts; pending request with no copies; expired ledger without eligible roots; measured duration and all-copy outcomes |
| PM-AC05 | Missed trigger / outage / commit ambiguity | Deterministic time-based watchdog tests and real DB connection interruption; preserve prior commits; restart/re-observe; no altered retention clocks |
| PM-AC06 | Budget / permission / wrong target | Statement and lock timeouts, retry exhaustion, wrong schema/project/database, checksum/privilege drift; fail closed without touching another target |
| PM-AC07 | Races / preservation | Concurrent read/ack/reopen/removal, future-skew cutoff, root/version/first-ack continuity, V1–V7/legacy/source-record hashes preserved |
| PM-AC08 | Monitoring evidence integrity | Missing/stale/future/foreign/malformed heartbeat, failed atomic write, stale observer and unknown eligibility age; explicit nonhealthy states |
| PM-AC09 | Independent ledger recovery | New isolated restore plus current ledger reconciliation, no old key/read/history resurrection; stale/missing ledger blocks access; bounded ledger expiry verified |
| PM-AC10 | Owned-resource lifecycle | Fresh generated project identity, no pre-existing volume/realm reuse, exact project-owned cleanup and absence proof; no actual-account flag or external send |

Use existing Operations integration patterns and independent build commands; preserve Java 25/Boot/JUnit conventions. PM05 reuses generated-only platform support without a new alert queue. Run relevant Python runner/watchdog unit tests, Operations `mvnw.cmd verify -Pintegration`, pin/runtime validators after migration work, Infrastructure validators/generated drill and Architecture workspace validation. Record actual command exits/counts, failed attempts, source fingerprints, independent HEADs/index preservation and remaining limitations. Test only generated resources; do not read production/private data for fixtures.

## Recovery controls and closure limits

PM-AC09 recovery testing above does not build a production current-ledger synchronization service. Specify separately the chosen protected store, atomic version/freshness/checkpoint semantics, authentication, ownership, retention and copy inventory before integrating it. Preserve the 66-day accepted bound and never silently extend it if copy provenance/backup rules fail. Missing current ledger isolates restore; logs/backup provider settings remain unknown until selected and authorized.

Completing PM01–06 supplies generated engineering evidence for parts of OR01/02/04. It does not close selected-environment OR01–06, privacy/legal/client acceptance, existing-stack AP-T08 or owner functional acceptance. The [completion checklist](../roadmap/PROJECT_COMPLETION_CHECKLIST.md) tracks those separately. Implementation authority is limited to reviewed generated-only scope; existing-stack execution always needs its own concrete proposal and separate authorization.


## PM01/02 candidate review increment — 2026-11-01

The [Operations review/candidate](../../../agrosphere-operations-service/docs/ALERTS_PRIVACY_MAINTENANCE.md) now supplies aggregate observer SQL outside runtime migrations and 13 passing generated integration cases. Full Operations verify passed 172 unit/128 integration; [dated observer evidence](ALERTS_PRIVACY_OBSERVER_EVIDENCE_2026_11_01.json) records exact artifacts and limits. PM01/02 remain partial: original watermark ages can be UNKNOWN, additive deadline metadata/V8 promotion is not performed, and effective NOLOGIN SQL-role checks do not establish real job-principal provisioning or full V7 hardening. Keep PM03 database integration gated on that review. PM04 fixture evaluator and all other PM/OR/AP-T08/REAL gates retain their scoped status; no existing-stack action is authorized.
