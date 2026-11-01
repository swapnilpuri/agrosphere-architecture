# AgroSphere project completion checklist

As of 2026-11-01 (America/Chicago). This is the reconciled progress index for the original rubber-plantation POC and remaining operating/rollout work. It supplements the historical [milestones](MILESTONES.md) and [backlog](IMPLEMENTATION_BACKLOG.md); their early foundation-only/pending-client labels do not override newer exact verification/approval records. Current execution state remains in the [checkpoint](../milestones/DEVELOPMENT_CHECKPOINT.md).

No percentage or completion date is assigned: remaining scope, staffing, device measurements, hosting and client facts are unresolved. Local generated verification, running-stack delivery, owner functional acceptance and production readiness are distinct. A checked item below means only the explicitly stated evidence exists. It does not accept a parent milestone or authorize the next one.

## Evidence-backed starting point

| Capability | Current evidenced state | Evidence / acceptance still needed |
|---|---|---|
| Independent foundation and Estate/GIS | Local implementation/integration recorded | [M1C](MILESTONE_1C.md); real plantation details/surveys, selected-environment controls and operational acceptance remain separate |
| Web/Cesium and estate administration | Local UI implemented; geometry correction and administration checks recorded | [Checkpoint](../milestones/DEVELOPMENT_CHECKPOINT.md); [Web administration verification](../../../agrosphere-web/docs/ESTATE_ADMINISTRATION_VERIFICATION.md); reference-device M2 performance remains OPEN |
| Tapping | Locally implemented/verified | [3A completion](../milestones/milestone-3a-completion.md); actual rollout/functional acceptance separate |
| Collections/DRC | Locally implemented/verified | [3B verification](../milestones/MILESTONE_3B_LOCAL_VERIFICATION.md); production/owner sign-off not inferred |
| Workers/attendance | SIMULATED-only local implementation/verification | [WA verification](../milestones/WORKER_ATTENDANCE_VERIFICATION.md); WA D08 workload and D09 actual privacy/retention remain OPEN |
| Inspections/incidents | SIMULATED-only local implementation/verification; separate II-1 stack upgrade recorded | [II verification](../milestones/INCIDENT_INSPECTION_VERIFICATION.md), [II upgrade](../milestones/LOCAL_II1_STACK_UPGRADE_2026_10_31.md); II-D07/08 remain OPEN; do not repeat II-1 |
| Alerts/privacy | Generated-only runtime/API/Web/restore verified; existing alert/privacy stack upgrade not performed by current work | [Privacy verification](../milestones/ALERTS_PRIVACY_VERIFICATION.md); OR01–06 and AN-D07/08 still OPEN |
| Offline capture/sync, French, faster refresh | Confirmed needs; implementation/acceptance not delivered by connected UI | [Owner rollout inputs](../milestones/ALERTS_NOTIFICATIONS_ROLLOUT_EXPECTATIONS.md), [single client register](../milestones/ALERTS_NOTIFICATIONS_CLIENT_DECISIONS.md) |
| MQTT telemetry | Foundation only; device/ingestion use cases not delivered | [Telemetry README](../../../agrosphere-telemetry-service/README.md); source inventory contains foundation/security/package declarations and V1 messaging infrastructure |
| Materialized analytics | Foundation only; test projection harnesses are not a shipped Analytics service | [Analytics README](../../../agrosphere-analytics-service/README.md), [3B verification](../milestones/MILESTONE_3B_LOCAL_VERIFICATION.md) |
| Forecasts/anomalies/assistant | Foundation only; liveness is not inference/authenticated business capability | [AI README](../../../agrosphere-ai-service/README.md) |
| Unreal/VR/MR | Foundation descriptor/architecture only; no validated editor/client/VR implementation | [Immersive README](../../../agrosphere-immersive/README.md) |

These are document/source observations, not fresh execution of every historical suite. Telemetry/Analytics business source inventories and AI inbound source were inspected in this increment; no runtime is started. Preserve original reports with their original dates and limitations.

## Stage 1 — make the current connected application operable

- [x] Prepare alerts/privacy operating-readiness review with open owners/evidence and stop conditions.
- [x] Prepare [generated-only maintenance implementation package](../milestones/ALERTS_PRIVACY_MAINTENANCE_PACKAGE.md) and parameter specification; these are proposed artifacts, not installed controls.
- [ ] Implement and verify PM01–06: restricted aggregate observation, bounded cleanup runner, independent watchdog and failure/permission/recovery drill in new disposable resources.
- [ ] Assign actual operating/recovery/security responsibilities and select log/backup/current-ledger controls; verify selected-environment OR01–04 evidence rather than relying on generated tests.
- [ ] Resolve actual-subject notice/controller/basis/hosting/request facts through PR01–17; preserve delegated provisional development defaults without presenting them as client/legal acceptance.
- [ ] Prepare exact authorized existing-stack preflight and protected isolated restore evidence; nonempty V6 requires a separate preservation-focused conversion review.
- [ ] Obtain separate authorization for the exact existing-stack upgrade actions; execute only those actions, retain data/config/volumes/geometry and leave accounts disabled unless separately governed.
- [ ] Conduct separately scoped connected SIMULATED owner walkthrough and record pass/fail per feature. This is distinct from production or offline/French acceptance.

Dependency: generated implementation can proceed without knowing production hosting, but generated success cannot close selected-environment controls. Backup/inspection/grant/demo-write permissions must be explicit in the later target-specific proposal. The current request does not execute that upgrade.

## Stage 2 — deliver the actual field workflow

- [x] Record owner choices: direct offline inspection/incident field entry, office synchronization, Android phones/tablets, English/French. These are requirements, not delivered functionality.
- [x] Record owner answers: individually assigned Android devices; one normal workday away from office connectivity (2026-11-01). These do not set offline access expiry or draft-deletion deadlines.
- [ ] Identify a first reference device; review offline access, draft retention, exceptional outages and loss/recovery expectations one input at a time in the existing register.
- [ ] Review a bounded offline design: permitted office-prepared reference data; encrypted/minimized device storage; ownership/account/estate isolation and handover; offline unlock/session expiry; clear saved draft/pending/server-confirmed states.
- [ ] Independently review executable contracts where changed; implement sync with current office authentication/authorization, original observation time, duplicate prevention and explicit conflict/rejection recovery. No offline alert read/ack queue, attendance or attachment expansion is assumed.
- [ ] Implement/review English/French UI and user information, dates/numbers/errors and accessibility; verify both languages on supported Android devices.
- [ ] Agree connected alert-delay/workload target; implement and measure foreground delivery/reconnect behavior. Proposed five seconds remains unaccepted/unmeasured; current healthy 30–35-second polling does not meet it.
- [ ] Verify restart/storage pressure, shared-device isolation, field-to-office reconnection, expired/revoked access, conflict, duplicate/unknown upload outcome and device-loss handling on named supported Android/browser versions.

Do not ask again whether direct field entry or Android devices are required; both are already answered. The first reference-device model is the next requested input; individually assigned devices and one normal workday away are now supplied. This does not stop independent generated maintenance work. Fresh server alerts require office connectivity/server-accepted reports; no field delivery without connectivity is promised.

## Stage 3 — accept workload, device performance and real onboarding

- [ ] Resolve WF03 record-category and role/session interpretation; obtain real estate/user/volume/growth inputs when available. Ten-per-category and 10–15 generated sessions are labelled scenarios, not client capacity facts.
- [ ] Measure M2 frame time/assets/memory and supported Android behavior on named hardware; validate agreed API latency/concurrency and recovery targets. Keep proposed targets in [nonfunctional requirements](../requirements/NONFUNCTIONAL_REQUIREMENTS.md) separate from achieved results.
- [ ] Close WA D08/D09, II-D07/08 and AN-D07/08 against their own requirements/evidence; shared inputs do not automatically close all three domains.
- [ ] Collect owner-confirmed plantation identities/divisions/fields/hectares/timezones and owner-supplied survey geometry; validate units/provenance/UUID continuity. No invented names/counts/boundaries or replacement with fixtures.
- [ ] Approve actual-data collection/retention/access and onboarding scope before real worker/operational records or account enablement; validate existing-data preservation and recovery.

These acceptance tasks may overlap Stage 2 when inputs exist; stage numbering is priority/dependency guidance, not an instruction to stall all independent work.

## Stage 4 — finish Operations/IoT and analytics

- [ ] Review Telemetry scope/contracts/ownership, device identity/estate mapping, authenticated MQTT, timestamp/unit/provenance rules and retention before implementing ingestion.
- [ ] Deliver generated sensor simulator, validation/normalization, replay/dedup, outage/DLQ recovery, scoped API and environmental overlays; preserve observation versus ingestion times and SIMULATED labels.
- [ ] Review Analytics KPI definitions, formulas, source contracts, history/correction rules, retention and authorization; keep service-owned projection storage.
- [ ] Implement event consumers with transactional dedup, correction/replay/rebuild/reconciliation and coverage/provenance; deliver authorized historical dashboards. No cross-service SQL or test harness presented as production analytics.
- [ ] Obtain functional/load/recovery acceptance of complete M3 capabilities and materialized analytics; do not mark M3 complete merely because tapping/incidents/alerts exist.

This is future capability scope requiring its reviewed decisions/authorization, not automatically authorized by maintenance planning. Analytics planning can proceed from accepted Operations events independently of Telemetry if the chosen KPI scope permits it.

## Stage 5 — evidence-backed AI

- [ ] Review prediction/anomaly use cases, lawful/minimized data inputs, chronological datasets, baseline metrics and acceptance thresholds.
- [ ] Implement time-aware evaluation, forecast/anomaly baselines and versioned model/evidence registry; retain PREDICTED labels and uncertainty/coverage.
- [ ] Deliver authenticated scoped inference and evidence-linked assistant through provider ports; test authorization, unsupported claims and prompt/model versioning.
- [ ] Accept evaluation/functional results; no autonomous agronomic decisions or fabricated certainty. Synthetic evaluation does not prove accuracy on real plantations.

Model/provider selection, spending, deployment and actual-data use need concrete decisions when reached. No model installation or service is started by this checklist.

## Stage 6 — shared Unreal estate and immersive feasibility

- [ ] Confirm licensed toolchain/assets/terrain and supported device/runtime, then validate the matching editor/plugin combination.
- [ ] Implement authoritative Gateway API integration, canonical estate/block identity, georeference/selection and provenance across Web/Unreal.
- [ ] Prototype VR with comfort/frame-time evidence on the selected hardware; record MR feasibility/accuracy limits separately.
- [ ] Accept POC immersive scope or record an explicit reviewed deferral. A deferral changes completion scope; it is not silent completion of original M5.

Unreal/VR belong to the original wider POC roadmap; production rollout can have a separately agreed narrower release boundary. Procedural trees remain illustrative, never a surveyed inventory.

## Release and production gate — cross-cutting

- [ ] Agree POC versus production release boundary and accountable acceptance/recovery owners; settle licensing/redistribution and relevant asset notices.
- [ ] Select hosting/identity/TLS/secret management, backup/log retention and data-flow locations; resolve applicable governance facts without guessing them.
- [ ] Produce environment-specific threat/access/isolation and dependency-security review, restore rehearsal, monitoring/runbooks, capacity and release/rollback evidence.
- [ ] Validate all acceptance criteria against exact source/pins/images and chosen device/environment; reconcile gaps/approved deferrals visibly.
- [ ] Obtain separate publication/deployment authorization; record owner functional and operational acceptance. Local checks do not assert hosted CI, deployment or security certification.

AEO remains paused and outside this product completion scope. No AEO change, Git commit/push/publication, cloud resource or deployment is authorized by the checklist. PM04 now has a tested generated-fixture policy evaluator; live observation/runner/scheduler integration and the remaining PM01–06 acceptance stay OPEN. The next single user input is the first reference-device model. All future requests for user action should name one specific action, one at a time.


### Observer review increment — 2026-11-01

PM01/02 now have an [Operations-owned reviewed SQL candidate and generated test suite](../../../agrosphere-operations-service/docs/ALERTS_PRIVACY_MAINTENANCE.md), outside automatic migrations. Original watermark eligibility ages can be unknown; source deadline metadata needs an additive design before an on-time claim. Effective SQL-role checks are not authenticated job-principal provisioning or V7 hardening. The initial 13-case candidate run passed; final regression/preservation results are in [observer evidence](../milestones/ALERTS_PRIVACY_OBSERVER_EVIDENCE_2026_11_01.json). PM01–06 and OR01–06 remain incomplete; no existing-stack inspection or upgrade is performed.

Reference-device availability update observed during final capture: the owner cannot provide a model now, as recorded in the single client register. Treat the question as answered unavailable and keep physical-device acceptance OPEN; do not repeat the device-model question.
