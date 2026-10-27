# Milestone 3B — Consolidated readiness and decision package
## Subsequent owner disposition — 2026-10-27

The project owner accepted D01–D12, ADR 0013 and the requirements/design/acceptance/wire design, including R01/R02, and authorized T01–T09 subject to validation and independent contract review/release gates. See [approval record](MILESTONE_3B_APPROVAL.md) and its exact reviewed hashes. Statements below about an open human approval gate describe the earlier review state; they are not current blockers. T00 Git/validation baseline remains blocked by CreateProcessAsUserW access denied. No implementation or acceptance-test pass is claimed. Production deployment, destructive migrations, secret-handling changes and AEO changes remain unauthorized.


Review date: 2026-10-27 (America/Chicago). Status: REVIEW PREPARED; NOT APPROVED; IMPLEMENTATION NOT STARTED. This review concerns the local proposed documents fingerprinted in [checkpoint evidence](DEVELOPMENT_CHECKPOINT_EVIDENCE.json). No AEO approval/run state was consulted or changed.

## Readiness verdict

The package is sufficiently detailed for a consolidated business/architecture/security review. Implementation is not eligible yet: D01–D12 and ADR 0013 explicitly require acceptance, and the task plan puts their resolution in T00 before T01/T02. No acceptance record for these decisions was found in the inspected package or product instructions. The owner's continuous-development request explicitly preserves this gate and authorizes implementation only after the applicable review process accepts the relevant decisions. It does not accept the proposed defaults by itself.

Inspected: all four 3B requirements/design/task/acceptance documents, proposed ADR 0013, owning proposed REST/event specification, all six PlantUML sources, prior validation record, accepted ADR 0012, 3A completion/reconciliation, roadmap/backlog, twelve product AGENTS files and relevant Operations source/configuration. This is source/document inspection, not fresh functional certification.

## One consolidated human decision

Requested disposition: accept or revise the rows below together with the linked [requirements](MILESTONE_3B_REQUIREMENTS.md), [technical design](MILESTONE_3B_DESIGN.md), [acceptance specification](MILESTONE_3B_ACCEPTANCE_CRITERIA.md), [ADR 0013](../adr/0013-latex-collection-and-drc.md) and [wire specification](../../../agrosphere-contracts/docs/milestone-3b/API_EVENT_DESIGN.md). Record the responsible reviewer(s), date, exact reviewed revision/hashes and any conditions using the project's applicable process. These recommendations are not adopted defaults.

| Decision IDs | Proposed choice for acceptance or explicit replacement | Why a human decision is needed |
|---|---|---|
| D01–D02 | A separately weighed lot belongs to one completed, nonzero-tree execution; multiple lots allowed; permanent execution/normalized-reference uniqueness; no pooling | Defines production eligibility and physical duplicate responsibility; changes allocation/domain identity |
| D03 | No future collection; unlimited historical entry with reason for a prior estate-local date, including workers' own entries | Changes observable backdating authority and historical production boundaries |
| D04 | Wet 0.001..999999.999 kg, DRC 0.00..100.00%; exact decimal product /100; dry kg HALF_UP to 3 places; totals sum rounded lot values, measured-only weighted DRC uses exact products | Production arithmetic; two tiny lots can sum to 0.002 kg versus 0.001 kg if rounded after summation |
| D05 | Missing DRC remains null/pending; direct lot measurements only; no estimated/default/pooled DRC | Determines reported completeness and known production |
| D06–D07 | Supervisor/management first DRC; workers weight only; manager/admin correction/void; same person may record and approve; no four-eyes queue | Authorization and approval separation are security/business boundaries |
| D08 | Immutable execution worker attribution and creation-time division/timezone/master snapshots; later reparenting does not regroup history | Determines historical reporting meaning |
| D09 | Retain observations, revisions, subject identifiers, command results and events indefinitely for this increment; define production privacy/retention policy before external deployment | Evidence/privacy/storage decision; indefinite local retention is not a production policy approval |
| D10–D11 | REAL/SIMULATED observations only, measurement must match collection; segregated summaries; pending/calculated/terminal voided; no payment/inventory certification | Defines provenance, irreversible void behavior and limits of calculated production |
| D12 | Stable actor/key command receipts, immutable versions and same-ID outbox recovery; never retry ambiguous creation with a new key | Defines externally visible replay/receipt and recovery contract |
| ADR/API/events | Operations-owned aggregate and append-only evidence; nine additive REST operations; four collection v2 snapshots; preserve all old event bytes/18 tapping operations; no legacy dual publishing | Published-contract review and independent release/pinning required; the specification is not yet an OpenAPI/schema release |
| Security/persistence extension | Operations-only restricted runtime login separate from migration owner; append-only grants/guards in proposed V3; additive operator provisioning and isolated upgrade/rollback rehearsal | Changes authorization/database privilege and credential wiring boundaries; no active provisioning or secret-handling change is authorized by this review |

After these are accepted, the current owner request supplies the instruction to continue eligible implementation; no fresh prompt is needed per task. Record scope explicitly (T01–T09 as gated by their dependencies). Contract release/publication, credential changes and any migration/deployment action still require their applicable authorization; this package does not authorize remote release or production operations.

No named product approver roster or separate authenticated approval mechanism was established by the inspected product instructions. Have the owner identify any required architecture/security/business approvers rather than inventing acceptance or using the paused orchestrator as an approval system. A chat acceptance must not be represented as an external approval it did not satisfy.

## Engineering findings and implementation conditions

| ID | Finding / disposition | Follow-up and proof |
|---|---|---|
| R01 | Timestamp wording needs one precise interpretation: design says at most six fractional digits and reject excess nonzero precision; wire text says at most six nonzero fractional digits. A token with zeros interspersed beyond microseconds must not lose information. | During review confirm value-exact microsecond normalization: accept extra trailing zeros only when the instant is exactly representable; reject any nonzero digit beyond the sixth fractional position. This is a proposed clarification, not a silently changed wire contract. Add offset/precision boundary tests in T01/T02/T06. |
| R02 | AC14's phrase 'missing date-pair/list' is ambiguous; proposed wire contract explicitly permits unbounded lists while summary requires paired bounds. | Proposed clarification: list accepts neither bound, rejects exactly one; summary rejects either missing bound. Both enforce from<=to and difference<=366. Confirm with the package review; encode four boundary cases in T01/T06. |
| R03 | New diagram sources are structurally present but current Architecture CI checks main and 3A diagrams only; validator counts twelve accepted ADRs. | Preserve existing checks now; when promotion/implementation is approved, explicitly add 3B syntax/render coverage and update ADR inventory. No CI/render pass claimed. |
| R04 | Current Events.emit hardcodes v1; relay constructs routes from stored event_version. Current Estate validation returns only timezone; runtime/Flyway share credentials. | T04/T07 need additive typed snapshot and version-aware writer preserving old signatures; T03 needs tested role separation. These are planned capabilities, not already delivered. |
| R05 | Current Access.workerOnly is a read filter and includes mixed-role behavior; reusing it as write authorization would widen access. | Use explicit per-operation policies as design requires. Test worker+viewer/auditor and revoked-scope receipt replay with real signed JWTs (AC09–12). |
| R06 | Source inventory has only tapping application/domain/controller and V1/V2 migrations; it does not contain a collection aggregate/controller/V3. | No 3B task implementation is credited. Before reserving V3, recheck current migration head and Git changes. Old 3A reports remain historical evidence. |

No source-level blocker was found that requires a new service, shared database or monolithic build. Cross-row/time/identity invariants are primarily application-enforced with SQL defenses, so their concurrency/rollback/grant tests are mandatory. The proposed API and event shapes remain unreleased and unvalidated by runtime export.

## Safe defaults actually adopted in this increment

Documentation stays under existing docs/milestones conventions; checkpoint links to a separate machine-readable evidence manifest; only Architecture AGENTS gains a narrow workflow reference. No proposed business, calculation, contract or permission default is adopted. Existing security/contribution instructions remain intact. No executable code, schema, migration, credential, runtime configuration or VERSION change is part of this increment.

## Execution and independent open gates

Two safe shell read attempts failed before process creation with CreateProcessAsUserW failed: 5 (Access is denied.). The second requested an explicit Windows PowerShell path with login=false; the tool still reported launching the WindowsApps pwsh.exe. No child-process workaround, elevation or sandbox bypass was attempted. Permitted Node filesystem operations support this review and documentation only.

Current-session inspection checks and precise limits are in [checkpoint](DEVELOPMENT_CHECKPOINT.md). Git status/diff, Python validators, Maven, Docker, Flyway/PostgreSQL, signed-JWT/broker/full-stack acceptance and PlantUML syntax/render checks are NOT RUN. Command execution must be restored for required implementation verification; no milestone completion is claimed.

Milestone 2 performance remains PARTIAL independently: reference desktop/GPU/browser, representative geometry/provider configuration and repeatable useful-view/frame measurements remain outstanding. Confirm the initial-view budget before treating the report's 10-second mention as an accepted threshold; 30 FPS is the recorded minimum frame target. Backend 3B planning has no documented GPU-performance dependency, but neither planning nor future backend tests close M2. Broader metadata-load/security/production acceptance debt remains as recorded in the reconciliation report.

## Next eligible task

Finish T00 by obtaining and recording the consolidated dispositions above, then re-establish Git/validation baseline in a working command environment. After acceptance and scope confirmation, T01 contract authoring is the first selected implementation task; T02 pure domain work is also dependency-eligible after T00. Do not begin T03+ out of order, publish the proposed contracts or alter AEO. Exact resumption steps are in the checkpoint.
