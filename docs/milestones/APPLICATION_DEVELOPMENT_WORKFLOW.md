# Continuous application development workflow

Effective: 2026-10-27 (America/Chicago). This is the persistent engineering procedure requested by the project owner, not acceptance of proposed domain decisions or permission to deploy. Keep this document and the [checkpoint](DEVELOPMENT_CHECKPOINT.md) together. AEO is paused: do not modify agrosphere-orchestrator source, configuration, databases, approvals, recovery classifications or persisted runs. Product approval evidence must not be inferred from AEO observations.

## Start or resume a session

1. Read the owner's latest instructions, the affected repository's AGENTS.md and contribution/security instructions. Each of the twelve product repositories remains an independent Git root. Read sibling documentation for coordination; implement only in the repository that owns the change. No parent Git/build, shared database, cross-service SQL, submodules or sibling runtime source dependencies.
2. Read DEVELOPMENT_CHECKPOINT.md, its linked review/evidence files, current milestone requirements/design/acceptance and accepted ADRs. The checkpoint is an index of evidence, not independent proof of acceptance. Verify that evidence applies to current source before relying on it.
3. Probe safe command execution once. When available, run git status --short, git rev-parse HEAD and git diff --stat separately in each affected root. Preserve unrelated changes; never reset, clean, stash or overwrite them automatically. Read migration heads and pinned release versions. Record observed revisions plus working-tree status. If process creation fails, record the exact error and requested command. Use permitted file inspection/document edits only; do not attempt child-process, alternate-token or sandbox bypasses. Reading .git/HEAD/refs is a limited revision observation, not Git status or proof of a clean tree.
4. Check recorded approvals against the exact package revision/hashes, scope and reviewer identity. Proposed plans, ADR filenames, old completion checkboxes and commit subjects are not approvals. If instructions appear stale, use specific accepted milestone evidence to understand delivered behavior, but do not silently broaden an affected repository's authorization.
5. Select the next eligible task using dependencies and approval gates below. Update active task before substantive work. Resume independently through authorized increments; do not require a new prompt for each task.

## Source and progress map

| Need | Authoritative starting point |
|---|---|
| Current work, blockers and next action | [Checkpoint](DEVELOPMENT_CHECKPOINT.md), then linked evidence and source |
| Product scope and nonfunctional gates | ../requirements/{PRODUCT_VISION,POC_SCOPE,FUNCTIONAL_REQUIREMENTS,NONFUNCTIONAL_REQUIREMENTS}.md |
| Roadmap | ../roadmap/MILESTONES.md and IMPLEMENTATION_BACKLOG.md; reconcile broad/stale entries with specific milestone reports |
| Accepted decisions | ../adr/*.md with explicit Accepted status; ../adr/proposed remains proposed |
| Current 3B package | [Requirements](MILESTONE_3B_REQUIREMENTS.md), [design](MILESTONE_3B_DESIGN.md), [task plan](MILESTONE_3B_IMPLEMENTATION_PLAN.md), [acceptance](MILESTONE_3B_ACCEPTANCE_CRITERIA.md), [readiness review](MILESTONE_3B_READINESS_REVIEW.md) |
| REST/events and compatibility | Owning agrosphere-contracts repository: openapi/, events/, examples/, docs/COMPATIBILITY.md and docs/milestone-3b/API_EVENT_DESIGN.md; runtime copies are independently pinned artifacts |
| Architecture diagrams | ../architecture/*.puml; ../../diagrams/milestone-3a and milestone-3b; read source and render before acceptance |
| Historical implementation evidence | milestone-3a-completion.md and reconciliation-1a-3a/ACCEPTANCE_MATRIX.md; service source/tests/reports corroborate delivered scope |
| Validation commands | Each affected README, CI workflow, scripts and current milestone acceptance plan |

The old ../roadmap/NEXT_CODEX_PROMPT.md recommends already-delivered 1B and is not the session entry point. Several repository scopes and the Architecture README introductory scope also predate 3A. Record such discrepancies; do not infer missing implementation or permission from them. Architecture AGENTS now references this workflow for owner-authorized application coordination. Preserve every repository-specific security/toolchain rule until explicitly reviewed.

## Task eligibility and genuine decisions

A task is eligible only when its prerequisites have implementation/test evidence, its exact scope is authorized and all required requirements/design/contract/security decisions are accepted through the applicable review process. For 3B use T00–T09; T00 is incomplete while D01–D12/ADR 0013 remain proposed. T01 and T02 follow T00; integration follows their dependencies. Do not mark a task complete because its plan exists.

The inspected product documentation uses explicitly accepted ADRs and reviewed independent contracts; it does not establish an additional authenticated product approval tool or named reviewer roster. Ask the owner to identify a required approver if their process requires one. Never manufacture an approval or modify the paused AEO system to obtain it. Record actual reviewer, date, decision, exact package revision/hash and any conditions. A scoped decision recorded in this workflow/checkpoint does not itself satisfy an external review process.

Resolve reversible internal choices autonomously when they do not change observable behavior, domain semantics or security: documentation placement, test organization within existing conventions, local evidence filenames. Record those choices. Consolidate unresolved decisions about domain meaning, production/money arithmetic, retention, authorization/security, published contracts or irreversible migration into one concrete review package with recommendation, consequence and affected tasks. Do the safe review/document preparation before asking. Do not substitute silence for acceptance or repeatedly ask already answered questions.

Current 3B owner acceptance is recorded in [the approval record](MILESTONE_3B_APPROVAL.md), including exact reviewed hashes and R01/R02. The readiness review is the historical decision package. D01–D12 and ADR 0013 are accepted; T00 is complete and the owner accepted the executable candidate/local Contracts 0.5.0 release and Operations pinning. See the current checkpoint for the remaining explicitly excluded credential-wiring scope; do not repeat satisfied approvals. Milestone 2 performance acceptance is an independent open gate; backend 3B planning does not close it or prove sequential milestone completion.

## Implement one coherent increment

1. Establish owners and baseline: affected Git roots, current revisions/dirty files, migration chain, pinned contracts and SHA-256 of compatibility-protected artifacts. Preserve Java/toolchain choices (Operations/Estate Java 25; Spatial Java 21 as documented). Do not create a common multi-service build.
2. Define the observable change and acceptance IDs. Review the owning ports/adapters, established test patterns and transaction/security boundaries. Preserve canonical UUIDs, GeoJSON longitude/latitude, service-owned migrations and REAL/SIMULATED/ESTIMATED/PREDICTED vocabulary with milestone-specific restrictions.
3. Implement the smallest dependency-complete change with automated tests for its actual risks. Contracts are authored/reviewed/versioned in Contracts; producers/consumers pin reviewed release artifacts, never sibling source paths. Preserve old schema bytes and route behavior; breaking changes require a reviewed independent version/release.
4. Run the affected repository's required checks. 3B needs exact decimal/domain tests, signed-JWT scope tests, contract checks, concurrency/rollback/upgrade tests, real broker confirms and isolated full-stack verification as mapped by AC01–AC28. Reuse disposable Testcontainers/Compose patterns (verify_tapping.py and platform_support.py), random projects, separate ports/volumes/credentials and SIMULATED fixtures. Never reset an authoritative or active database. Browser suites run sequentially.
5. Inspect authorization before queries/aggregation/replay, input precision, audit retention, idempotency, compatibility and failure behavior. Compare root/revision/outbox identities and versions. Do not treat unit tests as proof of broker/DB/identity integration.
6. Update diagrams, runbooks, independent changelogs and release pins when appropriate to the authorized change. Do not move proposed ADR 0013 into the accepted inventory before actual review. Update validators/CI inventory deliberately when promotion is authorized. No commit/push, remote release, deployment, secret-handling change, destructive migration or irreversible Git operation follows automatically.
7. Persist exact commands, date/environment, exit/results and artifact paths/hashes. Separate passed, failed, unavailable, skipped and historical checks. Review the change inventory against the baseline and update the checkpoint before selecting the next eligible task. If checks cannot run, continue safe authorized review/documentation, but do not accept implementation or declare the milestone complete.

## Durable checkpoint and stopping rules

After every meaningful increment record: milestone and acceptance state; completed tasks with source/test evidence; all affected repository revisions and working-tree limits; active and next eligible tasks; dependency/blocker list; unresolved decisions and actual approval references; exact test commands/results and unverified checks; files awaiting review; and exact safe resume steps. Keep evidence append-only by dated increment where practical; preserve earlier results as historical rather than silently upgrading their status. Never record tokens, passwords, private environment content or sensitive payloads.

At a genuine gate, provide one consolidated decision request and a self-contained report of completed work, changed repositories/files, actual checks, blockers and next eligible task. A decision gate is a valid stopping point after all independent authorized work is complete. If no gate remains, continue without asking for another engineering prompt.

Only close 3B after current evidence covers every AC or a specifically reviewed scope change. Produce an evidence-backed completion report, update the checkpoint, then inspect the roadmap and prepare the next authorized planning increment. Implementation of that next milestone still needs its applicable decisions/authorization. Keep Milestone 2 performance and broader nonfunctional debt visible until measured and accepted independently.
