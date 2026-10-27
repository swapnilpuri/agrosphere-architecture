# Milestone 3B — Design inspection and validation record
## Subsequent owner disposition — 2026-10-27

The project owner accepted D01–D12, ADR 0013 and the requirements/design/acceptance/wire design, including R01/R02, and authorized T01–T09 subject to validation and independent contract review/release gates. See [approval record](MILESTONE_3B_APPROVAL.md) and its exact reviewed hashes. Statements below about an open human approval gate describe the earlier review state; they are not current blockers. T00 Git/validation baseline remains blocked by CreateProcessAsUserW access denied. No implementation or acceptance-test pass is claimed. Production deployment, destructive migrations, secret-handling changes and AEO changes remain unauthorized.


Date: 2026-10-27 (America/Chicago). Scope: documentation only. This is an inspection record, not acceptance of an implemented feature or an authenticated business approval.

## Delivered package

- [Requirements](MILESTONE_3B_REQUIREMENTS.md): B3-01–B3-13 and twelve explicit proposed business decisions.
- [Design](MILESTONE_3B_DESIGN.md): aggregate/invariants, calculation, role matrix, replay algorithm, persistence/upgrade/rollback and recovery.
- [Implementation plan](MILESTONE_3B_IMPLEMENTATION_PLAN.md): exact repository areas, T00–T09 dependencies and release verification.
- [Acceptance criteria](MILESTONE_3B_ACCEPTANCE_CRITERIA.md): AC01–AC28, proposed executable targets and required evidence.
- [Proposed ADR 0013](../adr/0013-latex-collection-and-drc.md): owned collection aggregate, immutable evidence and versioned compatibility decisions.
- [Contracts design](../../../agrosphere-contracts/docs/milestone-3b/API_EVENT_DESIGN.md): nine REST additions, exact data shapes/filters/errors/replay and four collection v2 snapshot event contracts.
- Six sources under ../../diagrams/milestone-3b: domain.puml, workflow.puml, rest-sequence.puml, persistence.puml, event-ownership.puml and correction-reconciliation.puml.

README indexes and Unreleased changelog entries in Architecture and Contracts identify the proposed package. No VERSION bump, release, commit, push or deployment was performed. All mutations are Markdown or PlantUML; only these two independent repositories were edited.

## Inspection findings

3A completion and ADR 0012 agree with inspected source: TappingRecord can exist for aborted execution, so collection eligibility must inspect completed assignment/completedAt and not merely presence of a record. The accepted tapping types, routes, summaries and six event schemas need no modification. Operations currently has V1/V2 migrations, JDBC transaction boundaries, problem details and confirmed retrying outbox.

Estate OpenAPI already exposes block divisionId and canonical timezone/master versions. Add a typed collection-specific validation result while preserving the 3A string-zone validation method. Spatial remains the geometry owner and is not a production validation dependency. Historical division is a collection snapshot, not authoritative division lifecycle.

Foundation LatexCollectionRecorded.v1 is a real existing schema with nonnullable DRC and source=operations-service. The proposed operations/v2 collection family avoids changing its route/schema; existing tapping remains operations/v1. Events.java currently hardcodes v1; the plan includes an additive version-aware writer. OutboxDispatcher already uses stored event_version in routing. Rabbit definitions currently bind six tapping v1 event types only; a separate bounded collections v2 acceptance sink is required in implementation.

The Gateway wildcard already covers collection routes. Current Operations Flyway/runtime credentials use one database owner role; append-only evidence protection requires the proposed Operations-only restricted runtime login plus migration-owner separation and tested guards/grants. These are planned changes, not current capabilities.

Existing Architecture scripts/validate.py asserts exactly twelve accepted ADR files and seven 3A diagrams. Proposed ADR 0013 is stored under docs/adr/proposed so this documentation-only pass does not break the accepted-ADR count or edit validation code. Existing CI explicitly validates main architecture and 3A diagrams only; the six new sources are not covered until the planned CI inventory change. Review/promotion later must move ADR 0013 into the accepted inventory and update validator counts/diagram coverage deliberately. Its existence is not acceptance.

## Checks actually performed

| Check | Actual result and limit |
|---|---|
| Filesystem inspection | Read request attachment, applicable AGENTS instructions, 3A docs/ADR/source/migrations/contracts, Estate/Spatial OpenAPI, roadmap/FR-04, reconciliation/open M2 gate, diagrams, gateway predicate and broker/DB configuration through Node filesystem access. No AEO source or persisted run was edited. |
| Existing-file fingerprint baseline | Captured SHA-256 for 416 existing non-log/non-cache files in the seven inspected product repositories before writing. Final comparison permits changes only in Architecture/Contracts README and CHANGELOG. Other inventoried source, migrations, APIs, event schemas, examples, VERSION files and configuration remain byte-identical. This is a per-session filesystem comparison, not Git status or repository provenance certification. |
| Local link checks | Resolved Markdown file links in all package/index/changelog outputs and the C4 include; all targets exist after writing this record. Links were checked for file existence, not external availability or rendered anchors. |
| Diagram source checks | Six sources each have one start/end delimiter; vendored C4 include exists and defines the used queue macro. This is structural inspection only, not PlantUML syntax validation/rendering. |
| Decimal documentation examples | Independently checked five measured vectors using exact integer arithmetic in Node (kg thousandths, percentage hundredths, HALF_UP); all documented rounded values agree. Missing DRC null semantics and the sum-of-rounded example were inspected. No Java BigDecimal implementation/test exists in this pass. |
| Scope/traceability review | Requirements map to domain/API/persistence and 28 proposed acceptance scenarios; implementation tasks name owning repositories and dependencies. All business defaults and ADR remain proposed. |

## Unavailable or not run

The shell tool failed to create a process with CreateProcessAsUserW access denied on both attempts (including the alternate-shell request). No successful shell execution occurred. Continued permitted inspection/document writing with filesystem access as requested. Git status/diff, Maven, Python validators, PlantUML -checkonly/render, Docker, Flyway/PostgreSQL upgrades and broker/identity acceptance were not executed. No new test pass, diagram render, runtime compatibility or database upgrade result is claimed. Full Markdown rendering was not inspected. Historical 3A results remain historical.

Before implementation acceptance, run all checks in the implementation plan and AC table in disposable environments; produce current reports rather than reusing this record as proof. No active database was accessed or modified. No application/feature code, executable migration, released OpenAPI/event schema, infrastructure config or consumer was created here. Milestone 2's performance gate remains open. AEO remains paused and its persisted run untouched.
