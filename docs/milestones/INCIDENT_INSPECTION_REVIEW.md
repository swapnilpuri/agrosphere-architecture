# Incident and inspection management review — II-1

Date: 2026-10-30 (America/Chicago). Status: PROPOSED, FOR OWNER REVIEW. Inspection and planning only are authorized. No new executable contract, migration, application code, realm configuration or business record has been created. The provisional roadmap label is 3C; II-1 is a bounded increment and does not close parent Milestone 3.

## Recommendation and inspected baseline

Proceed next with Operations-owned, block-level field inspection evidence and manually managed crop-health incidents, initially SIMULATED-only, after the decisions below are approved. This follows FR-06, backlog M3-01 and the [3C handoff](MILESTONE_3C_PLANNING_HANDOFF.md). The backlog's intervening priority was WA-1; [WA-1 verification](WORKER_ATTENDANCE_VERIFICATION.md) and current source show that capability is locally delivered as Web 0.4.0. No dependency requires implementing MQTT or Analytics first. This recommendation establishes the next suitable functional module, not production readiness or approval to implement it.

| Inspection | Finding / implication |
|---|---|
| Requirements and roadmap | FR-06 combines inspections/incidents with justified alerts. POC Milestone 3 also contains MQTT, overlays and alerts. Delivering this bounded increment leaves notification delivery and those other capabilities explicitly incomplete. PRODUCT_VISION limits the POC to rubber and excludes autonomous agronomic decisions. |
| Existing Operations | Tapping, collections/DRC and workforce ports/adapters, command receipts, immutable revisions and outbox are available patterns. Flyway currently ends at V4; Java 25 / Boot 4.0.9 / JUnit 5 remain constraints. Reuse mechanisms after feature-specific tests, without sharing workforce domain classes or broad legacy role unions. |
| Existing Contracts | Local release 0.6.0; Operations has 42 accepted operations. `events/v1/CropHealthIncidentDetected.schema.json` is a foundation placeholder requiring blockId and summary, with LOW/MEDIUM/HIGH/CRITICAL and source `operations-service`. It lacks aggregate revision/lifecycle semantics. Preserve it and its example byte-for-byte; no silent promotion or dual publication. |
| Existing Web and Gateway | Web has administration, digital twin, workers and attendance routes; no incident/inspection feature. Gateway routes tapping/workers/attendance to Operations, without either proposed new family. |
| Existing broker and other services | Public RabbitMQ definitions have spatial/tapping/collection/workforce acceptance bindings, no crop-health binding. Telemetry and Analytics remain foundation scaffolds; neither is a required implementation dependency here. No shipped incident projection/notification handler was found. |
| Existing Estate / Spatial | Estate owns canonical estate/division/block relationships and timezone; Spatial owns geometry. A block's missing geometry must not prevent textual evidence entry. Do not depend on division lifecycle events, which do not exist. No cross-service SQL or replicated business master model. |
| Documentation discrepancies | Architecture README still describes WA-1 as domain-only/pending release; FR and broad roadmap retain historical foundation/future labels. Use dated approval, verification and current source together. Neither those labels nor an old schema prove missing WA-1 or accepted incidents. Do not rewrite the previously approved WA-1 package. |

Inspected sources, observed HEADs/status and protected hashes are in [assessment evidence](INCIDENT_INSPECTION_ASSESSMENT_EVIDENCE.json). Ten relevant Git roots were inspected independently. Only Architecture had a pre-existing change: the checkpoint, with 32 added lines in the initial diff at HEAD `51e4ce2eaa41b530f726547fc3df2fefd95c7ed9`. External commits advanced Architecture during inspection: the machine-readable capture subsequently observed clean HEAD `b74090943eb01651b36c9e3c349e4aa4781a855f`, then validation-time inspection observed `6fa55348f26bc6f7fdf62816c5b9a44c420ead8b` with the evidence file already committed externally. This session did not perform those Git mutations. Preserve that history and refresh status before implementation. Web was clean at inspection; its configuration is still protected regardless of prior staging history. No service runtime or database was queried in this assessment; local upgrade/geometry results are recorded historical evidence, not repeated live verification.

## Scope and exclusions

Proposed requirements:

- II-R01: Record a completed, one-block inspection with explicit observation time, outcome and provenance. A clear finding is positive inspection evidence; no inspection never means healthy.
- II-R02: Report a crop-health incident directly or atomically from a FOLLOW_UP inspection, retaining distinct inspectionId and incidentId and a stable evidence link.
- II-R03: Managers triage, resolve, reopen and void incidents through explicit commands; preserve every accepted revision and action reason. Correct inspection evidence without erasing its earlier state.
- II-R04: Provide scoped, paged lists, detail, protected history and filters; distinguish current incident status from the original linked inspection finding.
- II-R05: Apply independent JWT validation, positive role permissions and trusted estate scope on every query, command and receipt replay. New mutation paths accept SIMULATED only.
- II-R06: Publish minimal versioned snapshots through the existing transactional outbox and demonstrate at-least-once recovery using an isolated durable sink.
- II-R07: Preserve legacy contracts, migration bytes, records, geometry and current Web behavior/configuration; keep independent repository builds and release pins.

Exclude inspection scheduling/checklist templates, recurring tasks, worker assignment/account linkage, anonymous reporting, personnel injury/safeguarding cases, payroll/disciplinary records, chemical recommendations/treatment approval, automatic diagnosis/severity, disease certainty, cost/yield-loss estimates, counts of affected trees, photos/files/URLs, GPS traces or new geometries, offline queues, bulk import/export, notifications by email/SMS/push/SSE/WebSocket, alert acknowledgement/escalation, automatic IoT incidents, Analytics/AI consumers and Cesium heatmaps. Display crop observations as reports requiring human review. Use no actual plantation facts or worker details.

SIM-GA-DEMO and SIM-MW-DEMO already have explicitly SIMULATED estate/division boundaries and two rubber fields each. Preserve them, all existing records and volumes. Future acceptance fixtures belong in new disposable environments; do not reseed, replace polygons or create demo records in the existing stack.

## Screen flows

Proposed navigation adds **Inspections** and **Incidents** alongside current pages, visible only for allowed roles. Every page shows selected estate and a persistent SIMULATED label. The current estate/block selector supplies IDs; missing/inactive master data and unavailable geometry are separate states.

| Flow | Concrete behavior |
|---|---|
| Inspections list → record | Require estate, active block, observedAt, outcome CLEAR/FOLLOW_UP and findings. Show estate-local time plus offset; convert explicitly to UTC. CLEAR saves inspection only. FOLLOW_UP requires category, severity and incident summary and saves inspection + one linked OPEN incident atomically. Success opens the inspection with its incident link; ambiguity offers identical retry. |
| Inspection detail → correct / void | Show original observation, latest revision, linked incident/current status and version. Managers correct findings/outcome/time with reason or void with reason; identity, block and provenance cannot change. History shows before/after and actor only to authorized history readers. A linked inspection cannot become CLEAR or be voided while its incident is nonvoided; direct the manager to review/void that incident first. Corrections never silently resolve it. |
| Incidents list → report | Filter by block, category, severity, status and observation range; default OPEN + IN_REVIEW, explicit toggle for resolved/voided. Direct report accepts active block, observation time, category, severity, summary and details; creates OPEN without inventing an inspection. No assignee or worker selector. |
| Incident detail → triage | Show linked inspection when present, original report, current summary/category/severity and status timeline. Managers may amend details, move OPEN → IN_REVIEW, resolve OPEN/IN_REVIEW with resolution note + resolvedAt, reopen RESOLVED → OPEN with reason, or void any nonvoided status. No generic status dropdown permitting arbitrary transitions. |
| Conflict / network / auth | Every save freezes its key and normalized request while pending; unknown outcome retries identical bytes. A 409 shows submitted versus current version and explicit reload/review, with no automatic overwrite. Session expiry keeps unsaved data only in component memory and clears protected state on logout. Estate/route change with dirty forms prompts discard; failed loads never appear as empty successful lists. |
| Read-only / narrow layout | Supervisors read current records and create today's evidence; managers receive action controls; auditors read detail/history. Keyboard labels, focus restoration, error summary and 390px layout are acceptance targets. No text/body/token in browser storage, telemetry, traces or console. No alert-delivery claim from a colored severity badge. |

History and paged lists require loading/empty/denied/unavailable states. Lists contain identifiers, block label, time, outcome/status/category/severity and summary; protected detail adds notes, not actor identities. Navigation is convenience, never server authorization. Screens are a review specification, not implemented mockups.

## Data model and invariants

Operations owns all new tables, migrations and transactions. UUID estateId/blockId remain canonical; division is derived reference context, not an independently editable scope. A proposed additive V5 is conditional on rechecking the migration head after approval. Do not amend V1–V4, run destructive down migrations or query Estate/Spatial databases.

| Record | Proposed fields and rules |
|---|---|
| Inspection root | id UUID; immutable estateId/blockId/dataProvenance; observedAt UTC microsecond instant; estateTimezone snapshot; outcome CLEAR/FOLLOW_UP; findings 1–2000 Unicode code points; state RECORDED/VOIDED; nullable linkedIncidentId; version int64 starting 0; createdAt/updatedAt and signed createdBy/updatedBy. First FOLLOW_UP requires the linked incident in the same transaction. CLEAR has none. |
| Incident root | id UUID; immutable estateId/blockId/dataProvenance/nullable inspectionId; observedAt and estateTimezone; category PEST_SIGNS/DISEASE_SIGNS/TREE_DAMAGE/OTHER_CROP_HEALTH; severity LOW/MEDIUM/HIGH/CRITICAL; summary 1–200; details 1–2000; status OPEN/IN_REVIEW/RESOLVED/VOIDED; nullable resolvedAt/resolutionNote (1–1000); version and audit metadata. Categories describe signs, not a diagnosis. |
| Revision evidence | Root ID + version primary key, action kind, before/after snapshot or full resulting snapshot with previousVersion, actor, server recordedAt, correlationId, mandatory reason 1–1000 on noninitial commands. Append-only; no delete/cascade of evidence through normal runtime commands. Prior versions retain private text and therefore require retention review. |
| Command receipt | Feature namespace + signed actor + UUID Idempotency-Key unique; normalized method/path/body hash and normalization version; successful original status/body/Location; created/completed timestamps. Reserve in the same transaction before root locks. Scope/permission is checked before replay. Separate feature receipts avoid collisions with existing workforce/collection keys. |
| Outbox | Existing owned outbox mechanism; stable eventId, type/version and minimal snapshot, tied atomically to root/revision/receipt. No notes/actor subjects in shared payload. Transactional creation of inspection + incident produces two events, not cross-service atomic delivery. |

All inputs are closed shapes. Reject unknown fields/enum values; trim surrounding Unicode whitespace, preserve interior spelling/case; reject inappropriate control characters. IDs, provenance and original links cannot be corrected in place: void and create a replacement if wrong. No hard-delete API and no special permission to relabel simulated evidence REAL. Only SIMULATED mutation is proposed; REAL/ESTIMATED/PREDICTED inputs are explicitly rejected, including corrections and transitions. A future REAL policy must cover incident text and identity metadata as well as existing D09 workforce obligations.

No future observation; accept RFC3339 offset time, normalize to UTC at microsecond precision, reject excess precision. Supervisor creation is restricted to today's date in canonical estate timezone; managers may backdate with a reason, no proposed fixed age cutoff. All server times use a fixed injectable Clock and monotone versioning. Resolution requires observedAt <= resolvedAt <= serverNow; reopen clears current resolution fields while history retains them. Resolve/reopen times are manager commands, not inferred from inspection times. Correction of an observedAt cannot invalidate retained resolution chronology.

New evidence requires active, correctly related estate/block references with delegated caller authentication and bounded fail-closed responses. Historical corrections/transitions may use retained canonical identity/timezone on inactive master records; ownership cannot be changed. No geometry dependency. Reference checks are point-in-time validation, not a distributed lock guaranteeing the block remains active after commit. Timezone corrections require explicit context review; stored historical local interpretation does not silently change when Estate timezone changes.

One inspection links to at most one incident, and vice versa in II-1. A direct incident has no inspection link; later linking and merging duplicates are excluded. No uniqueness by block/time: distinct observations can be legitimate; identical command retries deduplicate. Correct CLEAR → FOLLOW_UP creates its first incident atomically; FOLLOW_UP → CLEAR is allowed only once its linked incident is VOIDED, retaining the historical link. That retained link prevents a second linked incident; if a new concern emerges, record a new inspection. Incident void never voids the inspection automatically. Current outcome is interpreted together with incident state, never rewritten by an event consumer.

Lock order: command reservation, inspection root (if linked), incident root. All linked corrections/transitions use that order, including incident void, so inspection-versus-incident races preserve link and state invariants. Root CAS checks expectedVersion; paired operations check both versions. One local transaction writes every changed root, its revision/event and one receipt, or rolls back all. Runtime grants permit only required root changes, insert-only evidence/receipts and existing relay operations; deny DDL, root/evidence deletion and evidence rewrites. Do not create/change roles or credentials under this proposal; return any necessary privilege expansion to scoped review.

## Proposed authorization

Use a dedicated incident/inspection policy over validated realm roles, signed subject and canonical trusted `estate_ids`; do not inherit legacy Access.admin(), which includes PLANTATION_ADMIN. PLATFORM_ADMIN is global but lists still require an explicit estateId. No new roles, account provisioning or division entitlements are proposed.

| Role within trusted estate scope | Current list/detail | Create inspection/direct incident | Amend / triage / resolve / reopen / void | History with reasons/actor |
|---|---|---|---|---|
| PLATFORM_ADMIN | Yes, explicit estate | Yes | Yes | Yes |
| ESTATE_ADMIN / ESTATE_MANAGER | Yes | Yes, manager backdate rule | Yes | Yes |
| FIELD_SUPERVISOR | Yes, no actors/revision reasons | Today only | No | No |
| AUDITOR | Yes | No | No | Yes |
| FIELD_WORKER / VIEWER / PLANTATION_ADMIN alone / unknown | No | No | No | No |

Positive permissions combine across mixed roles, but never broaden estate scope. No creator-only editing shortcut. This policy intentionally needs owner acceptance: WA-1 personal-data permissions do not automatically apply to crop reports. No anonymous endpoint. Resolve minimal ownership before protected object read; missing or foreign-scope ID returns a uniform 404 after feature-role validation, while an explicit unauthorized estate filter returns 403. Apply the same behavior to links, counts, histories and receipt replay. History page sizes are bounded; lists require one estate, deterministic ordering and scoped count predicates. Supervisor response schemas omit actors, correction reasons and revision snapshots; replay after permission downgrade is denied rather than returning an old fuller response.

## Proposed API design (documentation only)

All calls go through Gateway; Operations independently validates JWT issuer/audience/expiry and scope. These **16 operations** are a proposed design, not files to author in Contracts before approval. No new production endpoint exists.

| Method / path under /api/v1 | Command/query and result |
|---|---|
| POST /inspections | Create CLEAR or atomic FOLLOW_UP + incident; 201, Location, inspection + nullable incident state/version |
| GET /inspections | Estate-scoped page; filters blockId,outcome,state,observedFrom,observedTo,provenance,page,size |
| GET /inspections/{id} | Current permitted inspection view, linked incident reference/status |
| GET /inspections/{id}/history | Manager/auditor paged immutable revisions |
| POST /inspections/{id}/corrections | Expected inspectionVersion, optional linked incidentVersion where required, reason + full mutable observation fields; 200 |
| POST /inspections/{id}/void | Expected version(s), reason; 200 |
| POST /incidents | Direct report only (cannot provide inspectionId); 201 + Location |
| GET /incidents | Estate-scoped page; blockId,category,severity,status,observedFrom,observedTo,provenance,page,size |
| GET /incidents/{id} | Current permitted incident detail |
| GET /incidents/{id}/history | Manager/auditor paged immutable revisions |
| POST /incidents/{id}/amendments | expectedVersion, reason, complete mutable observation/category/severity/summary/details; no identity or status change; OPEN/IN_REVIEW only |
| POST /incidents/{id}/triage | OPEN → IN_REVIEW, expectedVersion, reason |
| POST /incidents/{id}/resolve | OPEN/IN_REVIEW → RESOLVED, expectedVersion, resolvedAt, resolutionNote and reason |
| POST /incidents/{id}/reopen | RESOLVED → OPEN, expectedVersion, reason |
| POST /incidents/{id}/void | Any nonvoided → VOIDED, expectedVersion, linked inspectionVersion when linked, reason |
| POST /incidents/{id}/corrections | Manager evidence correction in OPEN/IN_REVIEW/RESOLVED; expectedVersion, reason, full mutable observation fields; preserves status/resolution chronology. VOIDED is immutable. |

Amendments record an operational reassessment; corrections explicitly replace erroneous report evidence. Both preserve revisions. No no-op version increments: identical current mutable values with a fresh key return 409; repeated original key returns original success. Invalid repeated lifecycle transitions return 409. Inspection corrections are allowed while RECORDED, including with resolved incident provided link/outcome and chronology invariants hold. VOIDED roots are terminal; replacement is a new root.

All POSTs require UUID Idempotency-Key and canonical expectedVersion on existing roots (plus paired version where specified). Original success replay returns original HTTP status/body/Location even if the root advanced; refresh via GET for latest state. A changed normalized command for the same actor/key returns 409. Authorize before reservation/replay; reserve + lock + CAS + evidence/outbox + receipt commit atomically. Broker failure does not roll back committed HTTP state. Ambiguous outcomes use identical retry; new key is for a consciously revised command.

List ranges are half-open UTC [observedFrom, observedTo); require both or neither; page >=0, size 1–100, default 25; newest observedAt then UUID descending. Provenance required and SIMULATED for this candidate. No unbounded export, full-text search or aggregate endpoint. Reference labels are current display context, not rewritten historical evidence. Empty pages/counts share one scoped snapshot; no global totals.

Errors use application/problem+json + correlationId: 400 malformed/unknown fields/precision/range; 401 invalid authentication; 403 role/explicit estate/backdate/provenance denial; 404 missing or inaccessible object; 409 stale/paired version, link invariant, illegal state, key mismatch, no-op or bounded lock timeout (timeout marked retryable); 422 missing/inactive/mismatched canonical reference; 503 bounded reference dependency failure. Never return SQL, protected bodies, foreign record details or raw downstream payloads. Exact shapes/error cases and normalization rules are subject to executable contract review.

## Proposed events and compatibility

Author new `events/operations/crop-health/v1` only after approval. Four new event names avoid collision with the legacy CropHealthIncidentDetected v1 placeholder. No existing event or old 42-operation behavior may change; any additional release must preserve accepted archives/hashes. A candidate local Contracts 0.7.0 is a recommendation only; release/version/pinning requires independent exact-artifact acceptance. API info.version versus repository release metadata must be explained, not silently edited in approved bytes.

| Event / routing key on agrosphere.domain | Trigger / minimal state |
|---|---|
| FieldInspectionRecorded / agrosphere.FieldInspectionRecorded.v1 | Initial version 0: id, estateId, blockId, observedAt, estateTimezone, outcome, state, linkedIncidentId, provenance, version |
| FieldInspectionChanged / agrosphere.FieldInspectionChanged.v1 | Correction/void; same full minimal snapshot + previousVersion, changeKind CORRECT/VOID |
| CropHealthIncidentReported / agrosphere.CropHealthIncidentReported.v1 | Initial version 0, direct or linked: id, estateId, blockId, inspectionId, observedAt, estateTimezone, category, severity, status, nullable resolvedAt, provenance, version |
| CropHealthIncidentChanged / agrosphere.CropHealthIncidentChanged.v1 | Amend/triage/resolve/reopen/void/correct; same minimal snapshot + previousVersion and explicit changeKind |

Envelope: eventId UUID, literal eventType, eventVersion=1, timestamp UTC server recordedAt, source=`agrosphere-operations-service`, correlationId UUID, estateId, blockId, dataProvenance, aggregateId, aggregateVersion, payload snapshot. Verify envelope/payload identities/provenance/version agree. Actor subjects, summaries, findings, details, reasons and resolution notes stay out of broker events. Private-only corrections still emit a new minimal version, even if its other fields are unchanged. Trace context stays transport metadata. All four mutations remain SIMULATED-only; REAL is not enabled by including a future vocabulary in design prose.

Reused outbox must prove confirms, mandatory returns, nacks, timeouts, bounded FAILED retention and ACK-crash redelivery with stable eventId. New bindings go only to an explicitly bounded durable acceptance queue/DLQ in disposable infrastructure. No notification or Analytics service ships here. Future consumers must atomically deduplicate eventId with projection writes, use aggregateVersion, retain VOIDED tombstones, quarantine equal-version conflicts and reconcile gaps through authorized APIs. Two linked events can arrive in either order; retain unresolved IDs, never fabricate the other root or assume two-root delivery atomicity. Exercise that policy in a test harness only. An event is evidence transport, not an alert delivered to a user.

## Business decisions requiring owner review

Every II-D row is pending. Recommendations are concrete defaults for review, not accepted policy. Existing WA D08/D09 remain open and are not renamed or closed by this table.

| ID | Recommendation | Consequence / affected tasks |
|---|---|---|
| II-D01 Priority and boundary | Choose II-1 next: completed block inspections + manually managed crop-health incidents. Defer alert delivery/MQTT/Analytics/heatmaps. | FR-06 remains partially delivered until notification acceptance. If notification is required now, design channels, recipients, acknowledgement, retries and privacy before contracts. T00–T09. |
| II-D02 Identity and evidence | Distinct roots; one optional atomic linked incident per FOLLOW_UP inspection; CLEAR is explicit evidence, not inferred health. No later linking/merging. | Multiple concerns require new reports; owner must confirm this fits field work versus checklist/many-findings workflows. T01–T04,T07. |
| II-D03 Categories and severity | Four sign-based categories above. LOW=routine review; MEDIUM=prioritize review; HIGH=prompt manager attention; CRITICAL=highest manual priority. No SLA, numerical threshold, diagnosis or automatic response. | These are prioritization labels requiring operational owner validation, not established plantation practice. Additional categories/checklists or escalation deadlines change contracts. T01–T02,T07. |
| II-D04 Lifecycle and correction | OPEN/IN_REVIEW/RESOLVED/VOIDED, manager-only transitions, resolution evidence, direct reopen, terminal void; linked inspection guard and full revisions as specified. No second approver. | Managers have powerful correction/backdate authority; decide if approval queue, cutoff or closure evidence requirements differ. T01–T05,T07. |
| II-D05 Time and required fields | Explicit observed instant, server recorded instant, estate timezone snapshot, bounded text; today's supervisor entry, manager backdate with reason; active block required only for new evidence. | No GPS, attachment or affected-area/count measurements; confirm the minimal fields are operationally useful. T01–T04,T07. |
| II-D06 Access and responsibility | Approve the positive role matrix; no FIELD_WORKER/VIEWER/PLANTATION_ADMIN-only access; estate scope only; no assignees/anonymous reports or new roles. | If field workers must self-report, division isolation is needed or a named owner is mandatory, redesign authorization/identity before code. T01,T04,T06–T08. |
| II-D07 Privacy and attachments | No attachments, named people or personnel cases; minimal events; all new mutations SIMULATED-only until approved purpose/access/retention/deletion covers reports, revisions, receipts, logs, broker/DLQ and backups. | Notes and signed audit subjects can still be personal data. D09 workforce policy remains separately open; no national compliance or indefinite-retention assumption. T01,T03–T05,T07–T09. |
| II-D08 Connectivity and load | Online single-report saves; existing UI language with Unicode text; no offline/browser persistence, bulk or export. Obtain actual languages/connectivity, estates/blocks/report volume, concurrent users and latency budgets before performance acceptance. | WA D08 is still open; its worker inputs do not establish incident workload. No invented business load or M2 device-performance claim. T07–T09. |
| II-D09 API/events/release | Accept proposed 16 operations, four minimal families, new namespace and preservation of legacy placeholder. Independent executable candidate review and local release/pinning gate required. | Design approval permits candidate authoring only if implementation scope is explicitly authorized; it never accepts not-yet-authored contract bytes. T01,T04–T08. |
| II-D10 Implementation authorization | If accepted, authorize II-T01–T09 in dependency order with recorded gate conditions; retain all Git/production/credential/role/existing-data/AEO exclusions. | No module code/contracts before explicit acceptance. Existing-stack upgrade, REAL enablement and remote publication are separate actions. T00–T09. |

Owner can accept the recommendations together or revise individual II-D rows. Record actual reviewer/date, exact package SHA-256 and any conditions. No new personal records, credentials or real plantation details are needed for design approval. Missing D08/D09 inputs may remain downstream gates for an explicitly authorized SIMULATED implementation; they cannot be silently waived for acceptance or REAL use.

## Proposed acceptance criteria

None of these criteria has been implemented or executed for II-1. Existing WA-1 test totals are historical evidence of patterns, not tests of this proposal.

| ID | Observable acceptance and required evidence |
|---|---|
| II-AC01 | CLEAR saves only an inspection; FOLLOW_UP creates exactly one linked OPEN incident atomically; direct report creates no inspection. IDs/identity/provenance are immutable and no missing evidence is presented as clear. Domain/API/UI tests. |
| II-AC02 | All permitted/forbidden state, amendment/correction, resolve/reopen/void transitions and linked outcome guards pass; original evidence survives; terminal void rejects mutation. Test inspection/incident races and paired versions on PostgreSQL. |
| II-AC03 | Fixed-clock UTC/offset/microsecond/future/backdate/estate-local date/DST and inactive-reference scenarios pass; resolution chronology survives corrections; timezones remain historical snapshots. |
| II-AC04 | Signed JWT role/mixed-role/estate/issuer/audience/expiry/invalid-claim matrix passes through Gateway and direct service; no legacy admin union leak. Test own/foreign ID, explicit estate filter, linked root, count/history and revoked/downgraded replay. |
| II-AC05 | Unknown fields, invalid/overlong Unicode text, controls, invalid enums/IDs, malformed filters, range/page bounds and provenance denials match exact contracts; errors expose no private or foreign payload. |
| II-AC06 | Actor/key normalized identical retry returns original success and Location, including atomic two-root create; changed command conflicts. Stale/paired CAS, two actors, lock timeout, crash after commit and new-key no-op are verified. |
| II-AC07 | Failure injection at each persistence stage proves root(s)/revision(s)/receipt/outbox all-or-nothing; runtime denies evidence mutation/deletion/DDL. Additive fresh/upgrade/failed-DDL rollback and pinned prior-WA-image with retained new evidence pass in disposable resources. V1–V4 unchanged. |
| II-AC08 | Delegated Estate validation denies inactive/mismatched new references and fails closed on malformed/denied/down responses; no geometry dependency, cross-service SQL or master copy; inactive historical correction uses retained context safely. |
| II-AC09 | Actual runtime operation set adds exactly 16 to the current 42 if approved; retained legacy semantics/artifact hashes and independently generated Web pins pass. New schema examples/negative cases cover roles, links, errors, normalization and field projections. |
| II-AC10 | Four actual minimal event families validate identity/version/provenance; no report text/actor in shared payload. Real confirm/return/nack/outage/ACK-crash tests pass; paired out-of-order, duplicate, gap, tombstone and conflicting-version behavior passes a harness without claiming a shipped consumer. |
| II-AC11 | Scoped paged lists/counts agree within a request snapshot; filters/half-open observation ranges/order work, no cross-provenance mixing, and current versus historical linked state is clearly presented. |
| II-AC12 | Web flows pass keyboard/focus/labels, role/denied/loading/empty/errors, dirty estate/navigation, session expiry, frozen retry, 409 review and 390px browser checks. Protected data absent from storage/logs/traces; existing administration/workforce/Cesium regressions pass. Browser suites sequential. |
| II-AC13 | Disposable real Keycloak→Gateway→Operations→Estate plus PostgreSQL/RabbitMQ verifies full lifecycle, linked atomicity, denial/replay and recovery; old tapping/collections/workforce regressions pass. Independent affected builds/packages and cleanup recorded. No existing stack writes or reseeding. |
| II-AC14 | Approved II-D08 workload and budgets measured in a named environment before incident performance acceptance. WA D08 and M2 remain independent, open until their own evidence is accepted. |
| II-AC15 | SIMULATED-only denial enforced at domain, signed HTTP and DB boundaries, not just UI. REAL remains disabled until approved implemented privacy/retention/deletion policy passes tests across all stores. WA D09 remains open. |
| II-AC16 | Exact approved package/candidate hashes, per-root revisions/status, actual results/limits, independent changelogs/pins and safe next actions recorded. Owner functional sign-off is distinct from local test completion; no prohibited publication/deployment/AEO/role action. |

## Dependency-ordered implementation plan

Only inspection and preparation of this package are complete. Every implementation task is BLOCKED ON OWNER APPROVAL. The table describes work to authorize, not work begun.

| Task | Dependencies / repository owner | Deliverable and exit gate |
|---|---|---|
| II-T00 Decision and baseline | This package; Architecture + owner | Resolve II-D01–10 and record reviewer/date/exact package hash/conditions. Define which performance/privacy inputs remain downstream gates. Refresh per-root status, source/artifact hashes, migration head and pins. Only then promote an ADR and requirements/backlog for accepted scope. |
| II-T01 Executable candidate | T00; Contracts | Isolated 16-operation/four-event candidate, positive/negative SIMULATED fixtures, normalization/security/error policy and legacy byte-preservation manifest. Run validator/candidate tests. Present exact hashes for independent review before any release/promotion/pinning. Proposed 0.7.0 is not pre-approved. |
| II-T02 Domain and application ports | T00; Operations; independent of executable release under accepted semantics | Immutable roots, explicit state commands, dedicated permissions, fixed-clock/linked invariants and command/reference/evidence ports. Pure tests AC01–06. Preserve existing domain and toolchain. |
| II-T03 Persistence | T02 + stable T01 semantics; Operations | Recheck V4 head; additive migration, scoped indexes/queries, link uniqueness, lock ordering, receipts/revisions/outbox and constrained grants. Disposable upgrade/role/race/atomicity/prior-image tests AC02,06–07. No role/credential mutation; raise any necessary expansion for separate scoped review. |
| II-T04 REST and authorization | T01 exact accepted local release/pins + T02,T03; Operations | Feature-specific identity/views, bounded Estate references, sixteen operations, original-success replay and runtime comparison. Signed-JWT/reference/privacy tests AC04–09,11,15. No broadening existing module policies. |
| II-T05 Events | T01 exact released/pinned + T03,T04 command transactions; Operations | Four minimal versioned snapshots and real broker fault/recovery/privacy checks AC07,10. Preserve old emits and placeholder bytes; no consumer. |
| II-T06 Routing and acceptance topology | T01 stable + T04; Gateway / Infrastructure independently | Add only /api/v1/inspections/** and /api/v1/incidents/**; retain audiences/CORS/correlation/idempotency/rate limits/timeouts. New bounded durable disposable acceptance bindings and cleanup checks. No running realm, credential or existing-stack changes. |
| II-T07 Web | T01 accepted independent pin + T04,T06; Web | Generated types, feature stores/permissions and specified screen flows. AC01,06,11–12. Preserve public/config.json and all existing features; package with a public-source allowlist. No live-data fixtures. |
| II-T08 Isolated verification and open gates | T03–T07; Infrastructure + affected owners | Real disposable platform lifecycle/fault/scope and retained legacy regressions AC01–13,15; approved incident load AC14 when supplied. Privacy acceptance/REAL enablement remains blocked until policy reviewed and implemented. Record cleanup/results separately from unavailable checks. |
| II-T09 Evidence and owner handoff | T08 functional evidence; Architecture + each affected repo | Acceptance matrix, runbooks, source/artifact hashes, diagrams/render review where needed, independent version/pin/changelog decisions and checkpoint AC16. Report outstanding D08/D09/M2 and owner functional sign-off explicitly. No automatic local-stack upgrade or publication. |

Implementation repository map: Architecture owns review/ADR/evidence; Contracts owns APIs/events; Operations owns domain/storage/HTTP/producer; Gateway owns routing/security transport; Infrastructure owns disposable topology/integration; Web owns screens and independent generated pins. Estate and Spatial are reference dependencies with no proposed changes. Telemetry, Analytics, AI, Immersive and Orchestrator receive no implementation work. Keep each Git root/build/DB independent, with no sibling source runtime dependencies.

When authorized, use actual repository README/scripts: Contracts validator plus candidate/compatibility tests; Operations `mvnw.cmd verify` and `mvnw.cmd verify -Pintegration`, API/event/pin validators and Docker; Gateway Maven verification/Docker; Infrastructure offline validator and a new generated-only disposable workflow retaining existing drills; Web locked install, lint, format:check, typecheck, api:check, unit tests, build, UI then graphics sequentially, and independent packaging. Architecture `python scripts/validate.py --workspace C:\Projects\agrosphere` validates structure/docs, not domain behavior. Do not run module implementation checks now and count legacy passes as II-1 acceptance.

## Review handoff

Immediate next action: owner reviews II-D01–10 and explicitly approves or revises the proposed scope and II-T01–T09 authorization. Until then, leave all new contracts and code untouched. On approval, fingerprint this package, record actual decision/conditions, refresh baseline and begin T01/T02 according to dependencies; the executable release gate remains separate. Existing WA/3B approvals do not authorize II-1.

Continue to preserve existing local records/volumes, SIMULATED demo geometry and Web configuration. No commit, push, publish, production deployment, destructive migration, credential/role change, data reset or AEO state change is included. D08 workload/language/connectivity, D09 privacy/retention, actual estate onboarding and M2 reference-device performance remain visible independent gates.
