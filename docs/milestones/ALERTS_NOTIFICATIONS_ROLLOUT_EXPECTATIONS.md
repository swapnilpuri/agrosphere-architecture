# AN-D08 rollout expectations — 2026-10-31

Status: PARTIAL — owner inputs recorded; server disconnection confirmed; scope reconciliation and measurable acceptance remain OPEN. This is planning documentation, not implementation/rollout/functional acceptance. Prior design/executable approvals persist within their scope.

## Owner inputs

The owner supplied the following answers and invited reasonable planning refinements. Preserve these as supplied expectations rather than replacing unknowns with invented plantation facts or silently lowering requirements.

| Item | Owner answer | Planning interpretation / current state |
|---|---|---|
| Initial rollout | For now Local Simulated | Local SIMULATED demonstration only; no REAL/cloud rollout authorised. Existing user accounts remain subject to AN-D07. |
| Estates | Unknown | Actual estate count undecided. Existing SIM-GA-DEMO/SIM-MW-DEMO illustrations may inform the demo plan without recreation, reseeding or treating their count as a real rollout fact. |
| Users / roles | Unknown | Actual user count/roster unknown. Keep the accepted access matrix; no new accounts or role changes. |
| Concurrent sessions | 2-3 users for each role | Proposed synthetic test envelope: 10–15 simultaneous sessions if each of the five alert role labels has 2–3 distinct sessions (PLATFORM_ADMIN, ESTATE_ADMIN, ESTATE_MANAGER, FIELD_SUPERVISOR, AUDITOR). This is a derived load assumption, not an actual staff count. Overlapping roles must not be double-counted as people. |
| Daily report volume | Unknown | No daily ingestion/growth assumption accepted. Small fixtures cannot establish sustained-load or long-term storage acceptance. |
| Existing history | 10 records for each category | Owner requests a small initial history. Meaning of category (module/list versus incident category) remains to be specified before fixture design. Proposed planning interpretation: roughly ten records per demonstrated resource/list. This is neither retention duration nor a maximum data cap; create test fixtures only in separately owned disposable environments. |
| Languages | English, French | Both requested for the initial experience. Current alert screens have English literals and no French alert localisation was found in inspected source/config. French remains an implementation/review gap, including labels, errors, help, dates and policy/user notices. |
| Connectivity | Mostly offline; devices are often disconnected from the AgroSphere server too (owner clarification) | Fully disconnected device use is a confirmed need. Current AN-1 requires server reachability and does not provide offline persistence/queues. Offline behavior needs separate review; no offline-first design or implementation approval is inferred. |
| Alert delay | ASAP | Fast visibility requested; no numerical budget supplied. See proposed target and current mismatch below. No measured delay guarantee accepted. |

Earlier policy context remains: initial users in Gabon, South Africa/India only tentative hosting candidates. No provider/exact region selected. Local SIMULATED demonstration does not establish a cloud hosting decision.

## Compatibility with delivered AN-1

The [accepted review](ALERTS_NOTIFICATIONS_REVIEW.md) excludes offline browser persistence/queues, SSE/WebSocket and external channels. The delivered [Web guide](../../../agrosphere-web/docs/ALERTS.md) and [poller](../../../agrosphere-web/src/app/features/alerts/alert-inbox.ts) confirm memory-only state, polling while visible/online, immediate refresh requests on context/focus/online transitions, approximately 30–35 seconds between healthy polls and failure backoff/Retry-After. Login and API services must be reachable. No notification is delivered to disconnected/absent users.

No Internet and no server connection are different operational conditions. A local-network demonstration could be viable only with required API/login/assets reachable; LAN-only behavior and the browser online guard still need explicit tests. Fully disconnected operation needs a separate reviewed design for cached data, sign-in/expiry, device privacy/storage, pending writes, idempotency/reconciliation, conflicts and reconnect behavior. Do not enable storage or queue commands under the existing approval.

English/French and mostly-offline needs must not be declared satisfied by the existing English connected UI or prior generated integration tests. They also affect informed-user policy material under AN-D07.

## Proposed measurable plan — not yet accepted or implemented

1. Connectivity clarification received: "No—devices are often disconnected from the AgroSphere server too." Define which tasks must work offline (for example viewing previously loaded information versus creating reports), permitted device data and reconnect behavior in a bounded review. Fresh server changes cannot arrive while disconnected; distinguish disconnected time from online visibility delay.
2. Use generated disposable sessions at ten and fifteen concurrent sessions as a starting test envelope, subject to the role-count interpretation above. Keep estate count/daily volumes unknown; separately exercise paging boundaries and larger synthetic datasets without presenting them as actual workload inputs.
3. Treat ASAP as a proposed **within five seconds of source commit** visibility goal while authenticated, foreground and connected to a healthy API, under an agreed test load. This is an engineering discussion target, not a supplied/accepted SLA or achieved measurement. Existing 30–35-second polling does not satisfy that proposed goal. Immediate reconnect refresh means an immediate request attempt, not guaranteed instantaneous data or delivery while disconnected.
4. Prepare a concrete review of faster refresh/reconnect behavior and English/French localisation. Fully disconnected use is now confirmed as a need; include the separate offline/privacy/contract consequences before any implementation. Existing accepted AN-1 scope cannot silently expand to real-time streams or offline persistence.
5. Finish outstanding AN-D07 policy decisions and reviewed implementation before non-generated account demonstration or rollout. Any existing-stack action requires its own backup-preserving plan/authorisation. Keep the current connected AN-1 implementation available for generated tests with its documented limits; do not claim it meets the new expectations.

No delay, language, connectivity or workload change is implemented by this document. The owner's invitation to refine estimates permits clearly labelled planning assumptions, not fabricated facts, erased requirements, notification sending, production approval or closure of other gates.

## Dependencies and next actions

- Connectivity resolved: devices are often disconnected from AgroSphere itself. Next clarify essential offline tasks and prepare a bounded follow-up review, including device storage/privacy, authentication expiry, command reconciliation and reconnection acceptance.
- Then review a bounded follow-up scope/acceptance plan for the language, timing and any offline gaps. Clarify categories and the session-count assumption before revising generated fixtures or running workload acceptance.
- Personal read tracking and its 30-day inactive-period marker rule remain approved. Acknowledgement/receipt/audit/log/backup retention, policy/user notice, final hosting and implementation interactions remain open under AN-D07.
- AN-D08 is now partially supplied, not unanswered and not closed. It does not resolve WA D08/D09, II-D07/08, M2, REAL or owner functional acceptance. Shared rollout facts may later inform those reviews without automatically satisfying their different domains.

Documentation-only work in Architecture. No code/contracts/configuration/private environment/account/role/credential/data/volume/geometry/stack/Git staging/commit/push/publish/deploy or AEO change. No existing demo records are created/reseeded and no notifications sent.

## Documentation verification — 2026-10-31

PASS: `python scripts/validate.py --workspace C:\Projects\agrosphere` (architecture layout, sixteen ADRs, workflow structure, twelve independent Git roots, YAML and heuristic secret/ignore checks); `git --no-optional-locks diff --check`. Architecture HEAD remains `6fa55348f26bc6f7fdf62816c5b9a44c420ead8b`; raw index SHA-256 matches the pre-edit baseline. Prior checkpoint bytes are retained verbatim as a suffix. No application behavior changed or application/load/offline tests run.

## Further owner clarification — field and office connectivity, 2026-10-31

"In fields there is no network. Only in office the connectivity to network is available."

Confirmed operating pattern: no field network; office connectivity only. Office login/API reachability still requires verification. The earlier disconnected-device clarification is now more specific. Offline tasks, device ownership/sharing, field duration and exact synchronization expectations remain open.

Recommended workflow for review, not approval or delivered capability: prepare/download permitted information at office; perform agreed offline field tasks; reconnect and authenticate at office; submit/reconcile pending records with clear success/conflict status; refresh server-generated alerts. Alerts based on field reports can only be generated after those reports reach the server. Fresh server alerts cannot arrive in the field without connectivity. Any local warning rules would require a separate design and must not be presented as server-generated alerts.

Next owner decision: must inspections/incidents be recorded directly in AgroSphere on the disconnected field device, or entered at the office after returning? This determines the minimum offline scope. The current AN-1 implementation does not deliver offline capture/persistence/synchronization. No specific offline actions, cache contents, queued read/ack actions or new scope are approved by the connectivity statement.

Clarification checks: PASS `python scripts/validate.py --workspace C:\Projects\agrosphere` and `git --no-optional-locks diff --check`; raw Architecture index unchanged and prior checkpoint bytes preserved verbatim. No application/offline tests run for this documentation-only update.

## Owner workflow selection — direct offline field entry, 2026-10-31

Owner: "I recommend direct field entry to avoid duplicate paperwork."

The preceding field-entry choice is resolved: inspections/incidents should be entered directly into AgroSphere on disconnected field devices, then synchronized at the office. This is a business workflow selection; detailed offline scope/design/contracts/device persistence are not yet reviewed or approved for implementation. Historical pending language above is superseded for this choice only.

Planning scope to review: office preparation and minimum permitted reference data; offline inspection/incident drafts with clear durable-save and pending status; observation time distinct from server acceptance time; office authentication, current estate/role authorization, retry/duplicate prevention, conflict/rejection resolution and unambiguous server confirmation. Local drafts must not appear as successfully submitted reports. Server-generated alerts use server-accepted reports and refresh once connected. The existing connected AN-1 implementation does not satisfy offline capture or synchronization.

Next business input: device types (Android phone/tablet, iPhone/iPad, laptop or other) and whether individually assigned or shared. Device storage/privacy, offline access expiry, maximum disconnected period, draft retention, loss/recovery expectations and sync behavior need review. Recommended initial boundary for that review: keep shared alert acknowledgement online; no implied offline read/ack queue, offline attendance, attachments, local diagnosis/warnings or expansion of roles. These are proposals, not accepted exclusions from future business requirements.

All existing AN-D07/08, WA/II/M2/REAL and owner functional acceptance gates remain independently open. No new module contracts/code, cache/queue, data creation/reset or runtime changes were made.

Workflow-selection checks: PASS `python scripts/validate.py --workspace C:\Projects\agrosphere` and `git --no-optional-locks diff --check`; raw Architecture index unchanged and previous checkpoint bytes retained verbatim. Documentation only; no application/offline tests run.

## Owner device input — Android phones and tablets, 2026-10-31

Owner: "Staff uses Andriod phones and tablets."

Confirmed field hardware categories: Android phones and tablets. These are the target devices for planning direct disconnected inspection/incident entry with office synchronization. Historical pending device-type questions above are resolved for these categories. No Android version, browser/version, model, minimum specification, ownership, native-app/browser/PWA choice or verified offline capability is inferred.

Next input remains whether devices are individually assigned or shared across staff/shifts. The offline review must address account/estate isolation, draft ownership, offline unlock and session expiry, handover, storage/retention, device loss and recovery. Supported device/browser versions and offline behavior require explicit validation before claiming support. All prior scope and policy/rollout gates persist; this is documentation only, with no new contracts/code/storage/runtime/data changes.

Device-input checks: PASS `python scripts/validate.py --workspace C:\Projects\agrosphere` and `git --no-optional-locks diff --check`; raw Architecture index unchanged and previous checkpoint bytes retained verbatim. Documentation only; no Android/offline/application tests run.
