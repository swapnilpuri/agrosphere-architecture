# Integrated POC Verification and Acceptance - proposed follow-on milestone

Prepared 2026-11-11. Identifier: **POC-CLOSE**. The original roadmap remains M0-M5; this is a proposed delivery milestone for their remaining integration, verification and acceptance work, not an invented original M6. Preparing this prompt does not start execution or approve a new package.

Current starting point: [M5 desktop handoff](../../milestones/M5_DESKTOP_HANDOFF_2026_11_11.md) delivers a working desktop prototype while retaining incomplete desktop verification and deferred physical VR. [M4 acceptance](../../milestones/M4_OWNER_ACCEPTANCE_2026_11_10.md) remains valid for its bounded package. The [existing checklist](../PROJECT_COMPLETION_CHECKLIST.md) is the sole completion tracker.

## Complete milestone prompt

Copy the entire block into a new task when selecting this milestone.

```text
AgroSphere - POC-CLOSE: Integrated POC Verification and Acceptance

Role and objective
Act as lead integration engineer and verification owner. Work exclusively on
closing the remaining agreed local SIMULATED POC integration and verification
requirements across the existing independent repositories. Deliver a reproducible
connected demonstration of the implemented platform, correct defects within the
approved scope, and produce an evidence-based owner acceptance handoff.

Start from the existing implementation. Do not rebuild completed milestones or
add unrelated features. Treat original M0-M5 acceptance, engineering completion
and explicitly deferred capabilities as distinct states.

1. Read and inspect before changes

Read these Architecture documents:
- docs/milestones/DEVELOPMENT_CHECKPOINT.md
- docs/milestones/APPLICATION_DEVELOPMENT_WORKFLOW.md
- docs/roadmap/MILESTONES.md and PROJECT_COMPLETION_CHECKLIST.md
- docs/milestones/M5_DESKTOP_HANDOFF_2026_11_11.md
- docs/milestones/M5_DESKTOP_EVIDENCE_2026_11_11.json
- docs/milestones/M5_DELIVERY_APPROVAL_2026_11_10.json and its exact package
- docs/milestones/M5_CLIENT_REVIEW_FINAL_2026_11_10.md
- docs/milestones/M5_MR_FEASIBILITY_2026_11_10.md
- docs/milestones/M4_OWNER_ACCEPTANCE_2026_11_10.md and M4 delivery evidence
- docs/milestones/ALERTS_NOTIFICATIONS_CLIENT_DECISIONS.md

Read AGENTS.md, README/build/test instructions and relevant accepted decisions in
each affected repository. Inspect actual source, public contracts, migration/pin
versions and current Git state. Historical test reports are evidence to assess,
not fresh execution. Preserve prior reviewed package/report bytes.

2. Scope and authority

Selecting this prompt authorizes discovery, evidence reconciliation and preparation
of one concrete consolidated POC-CLOSE delivery package. Existing M5 approval still
authorizes its stated desktop verification work; do not ask for that approval again.
New combined fixture execution and broader changes must be covered by the concrete
POC-CLOSE package before execution. Do not assume that adding prior approvals
together authorizes a new data flow or fixture lifecycle.

Consolidate only genuinely unresolved product, contract, privacy/security,
workload/performance, license/provider and cost decisions. Include exact fixture
ownership/copy/cleanup boundaries and delegated engineering gates. After approval,
continue autonomously through all included phases. Resolve routine reversible
engineering choices without asking. Stop dependent work only for a material
decision outside approved scope or a genuine blocker; continue independent
authorized work where useful.

Preserve twelve independent Git roots, builds, versions and service-owned databases.
No parent repository/build, sibling runtime source dependency, shared persistence
entities or cross-service SQL. Preserve existing Git work, data, volumes, private
configuration, prior migrations and accepted contract archives. No staging,
commit, reset, push, publication, production deployment, REAL-data enablement,
existing-stack/account/role/credential mutation or AEO changes. Use approved new
owned disposable generated fixtures only. No new installations, purchases,
license acceptance, external notifications or provider spend by inference.

3. Repository responsibilities

- Architecture: decisions, requirement/evidence mapping, demo guide and checkpoint.
- Contracts: public APIs/events/examples, compatibility, exact local release/pins
  only if a demonstrated correction requires an approved change.
- Infrastructure: isolated fixture orchestration, public image/source identities,
  bounded generated credentials, failure injection, ownership and safe cleanup.
- Estate: authoritative canonical estate/block identity and lifecycle.
- Spatial: authoritative geometry, WGS84 longitude/latitude and spatial queries.
- Operations: tapping, collection/DRC, workforce, inspections/manual incidents,
  in-app alerts and their existing privacy/history semantics.
- Telemetry: generated device registry, MQTT validation and immutable readings.
- Analytics: service-owned production/environmental projections and history.
- AI: accepted observed-mass forecasts/anomalies, chronology, immutable records
  and deterministic evidence assistant. No new model/provider or agronomic action.
- Gateway: existing scoped routes and authentication integration.
- Web: existing administration, digital twin and operational/analytics panels.
- Immersive: delivered Unreal desktop client and outstanding desktop checks.

Make only necessary changes in each owning repository. Preserve each actual pinned
toolchain rather than forcing a global Java/Python/Node/engine upgrade.

4. Requirement and evidence reconciliation

Build a traceable mapping from the existing checklist to current implementation,
exact historical evidence, fresh checks needed and acceptance state. Keep the
existing checklist authoritative; do not create another competing completion list.
Classify each requirement as verified, failed, not run, explicitly deferred,
outside the approved scenario, or awaiting owner acceptance.

Resolve stale scheduling labels through dated status updates, preserving historical
reports. M4 bounded acceptance is already satisfied and must not be reopened simply
because integrated regression is needed. Connected ANL/TLM/alerts and broad earlier
milestone acceptance are not silently included in that M4 acceptance.

Reconcile the broad M1 company/division requirement with accepted ADR 0008 narrowing.
Identify whether each gap needs a scope disposition or implementation. Do not build
a company hierarchy, generalized GIS or a new feature family under a hardening label.

5. Finish the authorized M5 desktop verification

Use the actual packaged Unreal client, approved generated fixtures and rendered
execution where required. Do not replace a rendered requirement with a mocked or
NullRHI/component test. Cover the remaining handoff matrix:
- Empty estates/no geometry and malformed/oversize service responses.
- Live stale-response races across estate/selection/logout changes.
- Occupied callback port and partial callback timing.
- Actual refresh failure, revocation and signing-key rotation behavior.
- Maximum supported scene stress and sustained desktop input/navigation.
- Numerical Web-to-Unreal coordinate/geometry agreement against authoritative
  source geometry and an agreed measurable tolerance, not UUID agreement alone.

Define bounded fault injection in fixture-owned services/clients; never alter
existing identity providers or developer stacks. Record deterministic reproduction,
the actual UI/rendered outcome, source identities, failures, fixes and reruns.

Physical VR remains explicitly DEFERRED; keep OpenXR disabled under the current
desktop scope. MR remains assessment-only. Do not claim physical frame timing,
controller behavior, real-world scale, comfort or surveyed registration. These
remain original M5 requirements until separately verified or explicitly rescoped.

6. Connected generated demonstration

Prepare one coherent logical scenario with canonical estate/block identities and
an explicit mapping of generated users, source transactions, telemetry and evidence.
Use public APIs/events and service-owned projections; no cross-database joins.
Prefer existing verification helpers. If multiple owned fixtures are necessary,
state their boundaries and prove transfer/replay continuity; do not claim one
connected run from unrelated historical demonstrations.

The walkthrough must demonstrate:
a. Real signed login, role/estate scoping and canonical Estate/Spatial geometry.
b. Web estate navigation, block selection, details and provenance.
c. Tapping/attendance, latex collection and accepted wet/DRC/dry calculations,
   including correction history and missing-value behavior.
d. Manual inspection/incident, justified in-app alert, read/acknowledge,
   resolve/reopen/history and the reviewed privacy states.
e. Authenticated SIMULATED weather/soil MQTT ingestion, validation/deduplication,
   latest values/freshness and selected-block presentation.
f. Production/environmental history with explicit windows, units, observation and
   availability semantics; no inferred rainfall totals or causal yield claims.
g. Accepted forecast/comparator/anomaly, immutable model/evaluation records and
   deterministic assistant answer with inspectable same-scope evidence.
h. Unreal desktop loading/selection/details for the same canonical geometry/UUIDs,
   logout clearing and owned API outage/recovery.
i. Final cleanup of the owned resources and generated copies.

Preserve the distinction between M4's generated historical evaluation and its
actual live source availability. Never backdate live ingestion to manufacture
training history or replace worse-than-comparator evaluation results. Keep REAL,
SIMULATED, ESTIMATED and PREDICTED provenance explicit as applicable.

7. Security, privacy and fixture lifecycle

Consolidate demo-relevant WA D08/D09, II D07/D08 and AN D07/D08 dispositions in the
existing client decision register. Do not invent actual-subject/legal/retention
facts. Real-subject and production policies stay separately open; applicable
generated-demo privacy/copy conditions must still be satisfied.

Exercise missing/expired/wrong-role tokens, cross-estate/object access and
least-privilege DB/broker boundaries. Confirm protected UI state clears on
logout/denial/scope change and raw credentials/tokens do not enter evidence.

Specify owned resource labels, ports, source/image pins, account lifetime, copy
inventory and teardown for databases, brokers, logs, exports and any backups.
Do not assume a process finally block enforces expiry if that process disappears:
the M5 interrupted fixture exceeded its nominal lifetime. Reuse its ownership-safe
recovery lessons. Provide an approved bounded lifetime mechanism or supervised
stop/recovery procedure and state exactly what is and is not guaranteed. Stop on
uncertain target ownership. Do not delete resources by broad name patterns.

For exercised privacy expiry/recovery paths, verify suppression and no resurrection.
If backups/restores are included, review current-ledger/barrier and restore-before-
access controls. Do not claim operating-control or unattended deletion certification
from a short-lived fixture cleanup.

8. Performance and nonfunctional verification

Agree the remaining workload and acceptance budgets in the package: M1 query
concurrency/p95, M2 useful-view/frame/assets/memory, M5 maximum supported scene and
cross-renderer tolerance, and relevant connected update delays. Preserve existing
accepted targets. Do not introduce arbitrary new pass thresholds.

Use a named actual desktop/browser/GPU/runtime and report scene sizes, resolution,
warm/cold state, sampling windows, p50/p95/max where useful and observed stalls.
M5's existing 12-block/288-tree 1080p result does not establish Web performance or
maximum-scene capacity. Wall-frame timings are not CPU/GPU/compositor breakdowns.
Existing polling evidence does not accept a five-second delivery promise.

Verify outbox/consumer duplicate and restart behavior, projection rebuild where
applicable, unavailable-dependency handling and concurrent writes. Use additive
migrations only for approved defects; preserve existing migration bytes. Test
nonempty upgrade preservation if persistence changes. Do not rerun broad suites
without a dependency/change/remaining-evidence reason.

9. Contracts, builds and tests

Reuse accepted public contracts unless a reproduced defect requires a change.
For approved changes, specify operations/errors, event envelopes, idempotency,
compatibility and access rules; complete exact executable engineering review and
independent local release before consumer pins under delegated package authority.

Run affected domain, API, contract, migration, UI, native and integration checks.
Build each changed repository independently. Validate fixture scripts, public
packaging and architecture/workspace structure. Report actual hosted CI execution
separately from local workflow syntax checks. Record command, date, source/artifact
identity, pass/fail/not-run result and sanitized evidence location. Retain failures
and relevant retries; do not sum overlapping runs into misleading counts.

10. Execution phases

P1 - Discovery: inspect current source/evidence/authority and enumerate exact gaps.
P2 - Consolidated review: prepare one concrete POC-CLOSE package, scenario,
     decisions, delegated gates, performance criteria and cleanup boundaries.
P3 - Corrections: after approval, fix only evidenced in-scope gaps in owning repos.
P4 - Integration: assemble the approved owned fixture and connected scenario.
P5 - Verification: execute desktop/connected/security/recovery/performance checks,
     correct defects within scope and repeat only affected verification.
P6 - Reproducibility: document exact setup, walkthrough, artifacts/licenses,
     observed limitations, interruption recovery and owned cleanup.
P7 - Handoff: update existing checklist/checkpoint and deliver the working demo
     plus an owner acceptance review with satisfied and remaining gates explicit.

After package approval, proceed through all included phases without requesting
routine phase approvals. Stop after this milestone. Do not start Android/offline,
physical VR, production readiness, deployment or another feature track automatically.

11. Definition of Done and reporting

- Approved connected scenario runs against identified current artifacts.
- Included M5 desktop gaps and other agreed verification exits have actual evidence.
- Authorization/isolation/replay/recovery and reviewed privacy checks pass.
- Agreed performance targets are measured; misses remain visible.
- Independent builds and relevant regression checks pass or are explicitly blocked.
- Setup/replay/teardown is reproducible and all owned copies/resources are accounted for.
- Existing work/data/configuration and independent repositories are preserved.
- Checklist/checkpoint record capability-level engineering and acceptance states.

Report ENGINEERING COMPLETE / PARTIAL / BLOCKED for the approved POC-CLOSE scope,
separately from owner acceptance. Include changed repos/files, commands/results,
demo steps/results, artifacts, cleanup, failures/retries and remaining limitations.
An approved desktop-only demonstration may complete that bounded scope; it does
not complete original physical VR or other retained original-roadmap requirements.
Documentation alone does not satisfy implementation or verification exits.

Present one consolidated owner acceptance handoff. Record acceptance only from
an explicit owner response; "M5 seems done" is not a waiver of its remaining tests.
Recommend the next selectable track without starting it.
```

## Individual phase prompts

These are optional controls for working on one phase at a time. The complete prompt runs all approved phases autonomously. Each block inherits the complete specification above.

### P1 - Discovery

```text
Select AgroSphere POC-CLOSE P1 only. Read the complete specification in
agrosphere-architecture/docs/roadmap/prompts/POC_CLOSE.md and the current checkpoint.
Inspect actual source, approvals, M5 handoff and M0-M5 evidence. Map remaining
requirements to verified/failed/not-run/deferred/acceptance states in the existing
tracker. Preserve M4 acceptance and physical VR deferral. Report concrete gaps and
dependencies, update the checkpoint and stop after discovery. Do not run a new
combined fixture or infer new implementation authority.
```

### P2 - Consolidated review

```text
Select AgroSphere POC-CLOSE P2 only. Apply the complete POC_CLOSE.md specification.
Use verified P1 findings to prepare one concrete delivery package: scope, scenario,
product/contract/security/privacy/provider/license/cost decisions, exact fixture
ownership and copy lifetime, performance criteria, delegated engineering gates,
verification exits and exclusions. Reuse satisfied approvals. Make the review
ready for one owner decision; update the checkpoint and stop before unapproved work.
```

### P3 - Corrections

```text
Select AgroSphere POC-CLOSE P3 only. Read POC_CLOSE.md and the recorded package
approval. Fix only approved evidenced defects in their owning independent repos,
including remaining M5 desktop issues where applicable. Preserve accepted APIs,
data and historical artifacts; follow delegated release/migration gates for any
necessary changes. Run relevant tests and report source/check evidence and remaining
dependencies. Update the checkpoint and stop after this phase.
```

### P4 - Integration

```text
Select AgroSphere POC-CLOSE P4 only. Apply POC_CLOSE.md and the approved package.
Assemble the approved separately owned SIMULATED scenario through real public APIs,
events, Gateway/auth, Web and Unreal. Prove canonical identity/source continuity,
least privilege and fixture ownership. Record lifecycle/copy inventory and safe
stop/recovery instructions. Clean up unless an explicit approved supervised handoff
allows bounded retention. Update the checkpoint and stop after this phase.
```

### P5 - Verification

```text
Select AgroSphere POC-CLOSE P5 only. Apply POC_CLOSE.md and the approved package.
Execute the required rendered M5 fault/auth/race/stress/coordinate checks, connected
workflow, isolation/replay/recovery/privacy checks and agreed named-device performance
measurements. Fix in-scope defects and rerun affected checks. Preserve failures and
not-run/deferred results, including physical VR. Verify owned cleanup, update the
checkpoint and stop after this phase; do not infer owner acceptance.
```

### P6 - Reproducibility

```text
Select AgroSphere POC-CLOSE P6 only. Apply POC_CLOSE.md. Use actual P3-P5 evidence to
produce exact independent build/setup/walkthrough/teardown instructions, artifact
and license-notice inventory, interruption recovery and limitations. Validate
documentation and links. Do not convert documentation into an unexecuted test pass.
Update the checkpoint and stop after this phase.
```

### P7 - Handoff

```text
Select AgroSphere POC-CLOSE P7 only. Apply POC_CLOSE.md. Reconcile current evidence
with the existing completion checklist and approved exits. Deliver the reproducible
demo instructions, actual pass/fail/not-run results, artifacts/cleanup, limitations
and one owner acceptance review. Distinguish the bounded desktop POC from deferred
physical VR and other original requirements. Preserve prior acceptance. Update the
checkpoint and stop; do not start a new track or record acceptance without a reply.
```

## Immediate M5-only alternative

If the owner wants to finish only the remaining approved M5 verification before selecting the broader follow-on, use:

```text
Resume only the already approved M5 desktop verification gaps listed in
M5_DESKTOP_HANDOFF_2026_11_11.md. Preserve the working prototype and exact package
approval; no repeated implementation approval. Exercise the rendered negative,
refresh/revocation/key-rotation/race, maximum-scene/input and numerical Web-Unreal
geometry checks against approved criteria. Fix in-scope defects and record actual
results, owned cleanup and limitations. Keep physical VR deferred and MR assessment-
only. Deliver an updated M5 acceptance handoff and checkpoint, then stop. Do not
start POC-CLOSE or another milestone automatically.
```

## Next feature track after the POC review

The recorded Android field release is the next feature candidate: offline inspections/incidents, office synchronization, individually assigned devices, one normal workday away, and English/French. It can also be prioritized independently by the owner; it does not require AI/VR completion. It needs its own package for offline storage/access/expiry, loss/recovery, sync/conflict contracts and physical-device verification. This prompt does not authorize that work, REAL data or production deployment.
