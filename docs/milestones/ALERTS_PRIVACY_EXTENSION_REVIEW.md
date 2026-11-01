# AN privacy extension — concrete implementation review

Date: 2026-10-31. Status: READY FOR REVIEW, NOT IMPLEMENTED OR RELEASED.

The owner delegated provisional business choices in the [single client decision register](ALERTS_NOTIFICATIONS_CLIENT_DECISIONS.md) and requested the next steps. This package specifies the new technical behavior required to enforce those choices. Original AN-1 design and exact Contracts 0.8.0 approvals remain valid; this is a new compatibility and maintenance review. Nothing here approves an existing-stack upgrade, real accounts, REAL data, client functional acceptance or new offline functionality.

## Scope and decision requested

Review the isolated [Contracts privacy candidate](../../../agrosphere-contracts/docs/alerts-privacy/CANDIDATE_REVIEW.md), its exact manifest and five artifacts, plus the storage/security design and acceptance criteria below. Proposed local Contracts release: **0.9.0**, with a coordinated Operations/Web update after exact acceptance. Version 0.x does not make breaking changes safe: v2 alert representations/keys and privacy-mode v1 retirement require updated clients.

Requested review scope: accept/revise the new executable candidate and authorize local promotion/pinning and dependency-ordered generated-only implementation of this extension. Persistence authoring and narrowly scoped retention maintenance may be tested in separately owned disposable databases only. Existing tables/rows, roles/credentials, private configuration, current stack, V1–V6 migrations and prior contract bytes remain preserved. No maintenance may target an existing database under this approval. If new persistence authority exceeds this reviewed scope, stop at that specific gate rather than weakening database controls.

Implement read-marker expiry, acknowledgement/alert-history attribution expiry, bounded receipts and retry semantics, account-removal processing and restore suppression for the provisional policy. Logs and backups need explicit operating controls/tests as separate completion items. No claim that in-process logic rotates external logs or expires provider backups.

Exclusions: offline browser storage/queue/Android application changes; French localization implementation; faster polling/SSE/WebSocket; attendance/workforce/source incident retention; source history rewrites; data backfill; historical privacy-data conversion; external notifications; real plantation details; rollout enablement; existing-stack roles/credentials; Git publication/deployment/AEO actions.

## API and screen flows

Six new `/api/v2/alerts` operations mirror inbox, counts, detail, read, acknowledgement and history. Preserve the positive estate/role matrix, paging bounds, SIMULATED provenance, no-store responses and no implicit reads. No event/broker schema changes. Existing 58 non-alert operations and all old component definitions remain structurally unchanged in the candidate; released files remain byte-identical. The six v1 alert operations gain documented 410 retirement responses only in the candidate. In privacy mode they cannot provide a legacy bypass. Legacy generated-test mode is mutually exclusive with privacy mode and remains unavailable to actual accounts.

| Flow | Proposed behavior |
|---|---|
| Inbox/detail, active alert | Normal unread/read and shared acknowledgement controls. Show own personal state only. `readExpiresAt=null`; no other user's markers or ordinary-view actor identity. |
| Inactive alert before read expiry | Show fixed `readExpiresAt`; explicit read still possible for the current attention. Incidental edits do not extend it. |
| Inactive alert at/after read expiry | `readState=EXPIRED`, `readAttentionVersion=0`, `readAt=null`, `unreadForMe=false`; disable Mark read and explain expiry. Do not count as unread or create a new marker. `unreadOnly` excludes these results. |
| Shared acknowledgement attribution expires | Keep acknowledged operational status; return `acknowledgementState=REDACTED`, `acknowledged=true`, `acknowledgedAt=null`. Do not make the alert acknowledgeable again or manufacture an actor/time. This is attribution removal, not a claim that every linked business fact is anonymous. |
| Protected history expires | Return an empty 200 page with `retentionState=EXPIRED`, `lastExpiredAt` and `totalElements=0`. Before expiry COMPLETE; after later reopening/revisions, PARTIAL with the earlier expiry instant and newly retained entries only. Never fabricate missing history. |
| Command expiry | 410 closed problem with `ALERT_COMMAND_EXPIRED` or `ALERT_READ_RETENTION_EXPIRED`. Discard frozen retry state, refresh, explain expiry; never automatically submit a new action/key. No stored successful command on a failed/expired request. |
| Wrong/absent recent key | 400 malformed/noncanonical/non-v7 or excessive future clock skew; 409 absent older key still inside 30-day window, or key/body mismatch. Explain clock/unknown outcome and require refresh/explicit action. Do not guess command success. |
| Privacy-mode v1 access | After authentication and feature-role checks, 410 `ALERT_API_RETIRED` with no object information; client updates to v2. No v1 data read/mutation fallback. |
| Reactivation | New attention follows original AN rules. Before expiry, cancel relevant lifecycle deadlines. At/after expiry, purge/suppress old copies first, preserve the last history-expiry watermark, then start a new episode. Never revive an old personal read/actor/history from a retained row or receipt. |

The candidate adds `policyVersion`, `readState`, `readExpiresAt`, `acknowledgementState` to v2 ordinary views; history page adds `retentionState` and `lastExpiredAt`. Existing v1 schemas stay intact. Error response is a closed no-store 410 problem without subject, alert/estate identifiers or command body. Normal 400/401/403/404/409/429/503 handling remains. Return foreign/missing-object 404 and explicit forbidden-estate 403 before any receipt/retention disclosure on v2.

Dates are server UTC instants; day durations are elapsed 24 hours. Physical deletion need not wait for another user query. Current healthy 30–35-second polling is retained and is not acceptance of the proposed five-second target or offline/French requirements.

## Retry design without indefinite personal tombstones

Commands require canonical lowercase RFC-variant **UUIDv7** Idempotency-Key. Its timestamp layout is defined in [RFC 9562 section 5.7](https://www.rfc-editor.org/rfc/rfc9562.html#section-5.7); these admission/expiry rules are our proposed application policy. Timestamp bits are immutable within a given key. They are a bounded admission hint, never trusted observation/completion time or authorization. New keys must be within five minutes of the server clock; actual completion timestamps come from the server. No new client timestamp field is trusted.

Processing order: authenticate/feature gate/role, authorize estate/object, validate closed command/key shape, lock alert root, inspect receipt under the existing issuer/subject/key namespace, decide retention, then version/state checks and effect. Receipt reuse on a different resource/body conflicts after current authorization. Do not acquire source locks after alert locks.

1. Reject a key over five minutes in the future with 400. At `key timestamp + 30 days`, reject with 410 even if a stale receipt still exists.
2. A matching live receipt replays its original body only before the earliest of key-time + 30 days, completion + 30 days, personal-copy deadline or verified removal cutoff. Never extend any deadline through retry. Key-time cap can shorten the provisional completion window; this is a deliberate implementation refinement.
3. For an absent key within +/- five minutes, admit as new only after read-retention/removal checks. An absent key older than five minutes but under 30 days returns 409 unknown/expired outcome; a missing receipt must not be interpreted as success. At 30 days return 410. No action is re-executed from an old deleted key, even without a tombstone.
4. Early removal of a receipt inside the five-minute admission window is possible during account removal. The bounded removal ledger sets its key cutoff to verified request time **plus five minutes**, covering all future-skew keys previously admitted. It rejects keys at/before that cutoff, including after account reinstatement. While removal is pending, new personal-copy commands are denied; later explicit actions require completion and a key after the cutoff. It must not silently re-admit them. Retention-expired inactive reads are separately rejected before effects.

UUIDv4 keys from 0.8.0 are not converted or assigned invented issue times. A caller can choose a fresh v7 key for a genuinely new explicit action; this does not bypass expected attention/alert versions, first-shared-ack rules or current authorization. The Web client must support timestamp-correct v7 generation and retain frozen key/body only in memory for retry. Offline command queues are excluded.

## Data model, authority and physical deletion

Use proposed **additive V7** privacy tables in the Operations database; do not edit V1–V6 or replace the old immutable guards. No SQL in this package is executable against an existing database. New service-owned storage remains separate from legacy V6 alert tables so that preserving old evidence does not imply expiry has been enforced on it.

| Proposed record | Meaning and retention |
|---|---|
| Privacy alert root | Incident/rule uniqueness, immutable estate/block, source/alert/attention versions, minimal source facts and shared-ack boolean, true `inactive_since`, policy version, history-expiry watermark. No issuer/subject or historical private snapshots. Not automatically deleted with read expiry. |
| Read marker | Alert + trusted issuer/subject + attention + server time, with effective lifetime and removal cutoff. ACTIVE plus 30 days INACTIVE. No separate read event archive. |
| Acknowledgement attribution | Actor/time for acknowledged attention episodes, physically separate from root's operational boolean. ACTIVE plus 365 days INACTIVE. Ordinary responses never expose actor. |
| Alert evidence | History required fields and scoped minimal metadata; attribution joined from the retained attribution table. No duplicate private root snapshots/receipt bodies here. Whole eligible history/attribution expires together at 365 days. Keep only minimal non-actor continuity anchor needed for current version; no invented history row or identifying archive. |
| Receipt | Current issuer/subject/key, canonical request hash/path, original success, original completion, hard key deadline and current applicable copy expiry. No new response archive. ACK success includes personal read state and is treated as a personal copy too. |
| Removal ledger | Verified issuer/subject key cutoff (request time + five-minute skew) plus request/completion/deadline and opaque local request ID; no free-text personnel reason. Plan retains suppression metadata for 66 days after completed live removal, covering the 35-day backup and 30-day key window plus margin. Reject keys at/before cutoff; reapply on restore. This is still personal data, access-restricted and subsequently deleted. |
| Maintenance result | Policy version/run time/counts/status/oldest-overdue deadline, no personal row dump, subjects, key hashes or report text. Use bounded security-log retention; do not log raw SQL parameters. |

Precise `inactive_since` changes only on ACTIVE→INACTIVE and clears on reactivation; not on unrelated edits. Compare one server decision time per transaction. A source transition must materialize/suppress already expired data **before** cancelling deadlines. Persist evidence of expiry as non-personal watermark, not old marker identities. Source/alert/attention version changes remain business-rule changes; expiry does not forge source revisions or manager actions. Queries derive read/redaction state at their transaction time, even if physical cleanup is delayed.

Both read and ACK receipt copies are deadline-filtered and scrubbed on expiry/removal. Validate copies in root projections, attribution/history, receipts, JVM/browser caches, logs, database backups and exports. No hidden identifiable archive is allowed. Existing source incident/inspection histories remain governed by II-D07; this extension does not claim to erase identities in those other records.

The normal application keeps no broad DELETE/DDL or ability to edit immutable evidence. Proposed maintenance is a dedicated, non-HTTP, allowlisted operation that takes a bounded batch size, derives its cutoff from the database clock, locks selected roots in stable UUID order, rechecks eligibility under lock and deletes only eligible privacy-table rows. It cannot accept arbitrary SQL/cutoff/subject deletion from a request. Fixed schema/search path; revoke public execution; no user-settable bypass/session flag. Separate independently tested maintenance authority is required in disposable tests; no role/credential provisioning or grants on existing stacks. Any later actual grant/maintenance execution needs separately scoped authorization.

Normal writers, cleanup and removal use root→receipt/read/attribution/evidence lock order with bounded lock timeouts; maintenance retries locked roots without partially deleting one alert's copies. Account-wide removal proceeds root-by-root under a verified cutoff, denies re-creation of old markers/keys, and records completion only once all eligible copies are handled. Correlation IDs in retained evidence are removed with the evidence. Cleanup metrics must reveal no subjects.

**Legacy gate:** privacy enablement refuses when any of the five V6 alert tables is nonempty. Do not hide those rows, copy them into new storage or claim that they satisfy retention. A nonempty environment needs a separately reviewed conversion/expiry plan. Generated tests must verify fail-closed behavior with populated V6 and that every existing row remains unchanged. Empty V6 with populated V1–V5 can exercise new prospective alerts without altering old incidents or backfilling. Never run legacy and privacy writers simultaneously.

## Removal, restore, logs and backups

Account removal is a verified operator-supplied privacy request in the generated maintenance harness, not a new public recipient/account API or an invented identity-provider event. It creates a bounded cutoff; own-read and identifying receipt copies disappear within 30 days or sooner at normal expiry. Ack/audit follow 365-day attribution rules unless a specifically reviewed obligation changes them. Do not claim that a JWT makes identity-provider revocation instantaneous: server authorization is checked on every action, and token revocation/validity behavior must be verified separately before real accounts.

Logical access expiry is immediate at deadline; healthy physical cleanup completes within 24 hours. Logs: ordinary 14 days, narrowly defined security 90 days. Backups/copies: max 35 days from creation, including incremental chains and exports, with no automatic indefinite keep-last rule. Thus normal backup erasure can be deadline + 24 hours + 35 days; failures extend this and must be reported instead of claiming compliance.

Restore into a restricted isolated environment, preserve original deadlines/policy version and load the current removal ledger from a source not rolled back with the database. Reapply expiry and completed removal cutoffs, validate copies, then permit access. Never restore into an active database or automatically expose restored historical actors. A discarded 66-day ledger entry cannot be needed by a still-valid backup/key if the bounded backup/key policies were enforced; if backup provenance/retention cannot be established, keep access disabled. No restore is performed by this review.

The provider, cloud region, controller/contact, applicable basis and actual logging/backup system remain unresolved facts. Prepare English/French notices without inventing those facts; real-account enablement remains gated. All client questions/assumptions stay in the single client register; this technical package links them rather than opening another business questionnaire.

## Acceptance criteria and dependency plan

| ID | Required evidence before enforcement is accepted |
|---|---|
| AP-01 | Exact candidate hashes/OpenAPI/schema validation; old 58 non-alert ops and old schemas preserved; all released bytes/events/VERSION/pins remain unchanged until exact new acceptance. |
| AP-02 | Signed-JWT v2 HTTP matrix: estate/role/REAL denial before existence/expiry/replay disclosure; ordinary actor exclusion; all responses no-store; v1 cannot bypass privacy mode. |
| AP-03 | UTC boundary tests before/at/after 30/365 days; incidental inactive edits; reactivation before deadline cancels it; at/after expiry never resurrects data even before batch cleanup. |
| AP-04 | Exact success replay only while authorized and live; v7 shape/skew/30-day bounds; absent old key cannot re-execute; earlier copy expiry; body/path mismatch; malformed and legacy v4 keys; rollback and concurrent duplicate commands. |
| AP-05 | Physical all-copy deletion in new storage and bounded failure recovery; no legacy data/source-history alteration; root/first-ack/version continuity; expired history empty, later history PARTIAL; expired inactive read creates no marker/receipt. |
| AP-06 | Runtime cannot DELETE/DDL/bypass evidence guards; maintenance cannot delete ineligible data or use supplied arbitrary cutoffs/SQL; lock/race tests versus source/read/ack/removal; no partial erasure transaction. |
| AP-07 | Populated V1–V5 and V6 preservation; nonempty V6 prevents enablement; additive migration failure rolls back in disposable DB; disable/rollback retains data and cannot expose expired state through old API/image. |
| AP-08 | Verified removal cutoff and deadline; current removal ledger survives restore independently; no pre-removal key replay/re-admission or read-state resurrection after reinstatement; ledger expires at its bounded deadline. |
| AP-09 | Isolated backup/restore after expiry and after removal; actual log and backup copy inventory/rotation verified, never inferred from unit arithmetic. No access until restored eligibility checks pass. |
| AP-10 | Web v2 expired/read/history/retry/clock-error/narrow flows; no automatic new command after 410/unknown 409; no offline persistence; retained legacy modules/config unaffected. |
| AP-11 | Exact schema/runtime/pin validators, meaningful full service integration plus independent Web build/tests, generated platform drill, owner connected functional review recorded separately. |

1. **AP-T01 (this package):** inspect constraints, prepare design and isolated executable candidate/fixtures/validator/tests; freeze manifest. No release/pinning.
2. **AP-T02 (new exact acceptance gate):** accept/revise candidate and scoped disposable-maintenance design; independently promote/archive local Contracts 0.9.0 and pin exact artifacts only after acceptance.
3. **AP-T03:** extend pure domain/read/ack/version/privacy state, UUIDv7 admission, expiry/removal watermarks; unit/concurrency design tests. Prior policy calculator is reusable; no runtime enforcement claimed yet.
4. **AP-T04:** reviewed additive persistence, scoped maintenance harness and transaction adapters in generated disposable databases. Preserve every V1–V6 byte and populated legacy rows. No broad grant or bypass.
5. **AP-T05:** signed-JWT API/router and no-store errors, source transaction wiring and mode mutual exclusion; integration and contract runtime checks. No policy switch enabled for actual accounts.
6. **AP-T06:** v2 Web and Gateway routing, explicit expired/partial/clock/unknown-outcome handling; independent pinned contracts and sequential browser tests. Preserve public/config.json.
7. **AP-T07:** generated maintenance/restore/log/backup tests and runbooks, complete AP-01–11 engineering evidence; document unverified external deployment controls. Source-module/rollout gates remain independent.
8. **AP-T08:** prepare separately authorized local-stack upgrade and owner acceptance; use [conditional upgrade plan](ALERTS_PRIVACY_LOCAL_STACK_PLAN.md). It is not executable authorization and will not repeat II-1. Any nonempty legacy migration is another concrete gate.

## Current evidence and review limits

Only isolated candidate artifacts/scripts and review/checkpoint documentation are added in this increment. The previous pure Operations policy calculations are unchanged. Exact checks and candidate SHA-256 are recorded in the Contracts candidate review and Architecture checkpoint after execution. Contract oracle tests verify proposed semantics/fixtures; they are not evidence of implemented server authorization, expiry, deletion, backup or restore behavior. No full integration/browser tests are claimed for this review-only increment.

## Final review preparation checks — 2026-10-31

PASS Contracts `.\.venv\Scripts\python.exe scripts/validate.py`, isolated `scripts/alert_privacy_contract_validation.py`, and `-m unittest discover -s scripts -p 'test_*contracts.py'`: 59 tests (48 retained + 11 privacy), zero failures/errors. PASS Architecture `python scripts/validate.py --workspace C:\Projects\agrosphere`; PASS Architecture/Contracts/Operations `git --no-optional-locks diff --check`. New review links resolve. Existing pre-edit Contracts file hashes, all three observed HEADs/raw indexes, prior checkpoint bytes and Web public/config.json hash are preserved. No Operations runtime change or application/integration/restore/browser/stack test performed in this review increment. The initial global Python dependency failure was resolved by the existing independent Contracts virtual environment.

The new exact executable gate comes from [Contracts AGENTS.md](../../../agrosphere-contracts/AGENTS.md): "Exact executable acceptance and independent local release precede promotion/pinning." The new candidate changes observable retry/retention semantics, so that rule applies to it; old 0.8.0 acceptance is not being repeated. Maintenance/stack exclusions are also explicit owner constraints, not an inferred permission flow. See [machine-readable review evidence](ALERTS_PRIVACY_REVIEW_EVIDENCE.json) for artifact hashes and passed/unimplemented distinctions.
