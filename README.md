# agrosphere-architecture

Architecture decisions through implemented Milestone 3A and owner-accepted Milestone 3B design for the AgroSphere Rubber Plantation Digital Twin.

This is an independent project and Git root. Version: 0.5.0; use independent SemVer tags and CHANGELOG.md. License decision: LICENSE.md (all rights reserved pending selection).

See AGENTS.md for scope and engineering rules. This scaffold provides no business APIs or production features. Architecture lives in the sibling agrosphere-architecture repository; versioned API/event definitions live in agrosphere-contracts. Do not add path dependencies to sibling projects.

## Architecture index

- docs/requirements: vision, POC scope, functional and nonfunctional requirements.
- docs/architecture: seven PlantUML diagrams, XR roadmap and integration/reliability patterns.
- docs/adr: thirteen accepted foundation and milestone decisions.
- docs/DEPENDENCIES.md: selected versions, source links and compatibility caveats.
- docs/roadmap: milestones, implementation backlog and exact next Codex prompt.
- docs/VALIDATION_REPORT.md: executed checks and limitations.

## Validate

Python 3.12+: python -m pip install -r requirements-dev.txt; python scripts/validate.py. Optional full local structure audit: python scripts/validate.py --workspace C:\Projects\agrosphere (requires Git on PATH). The audit reads sibling structure only; projects build independently.

C4 macros v2.12.0 are vendored under docs/architecture/includes with their MIT license. CI downloads pinned PlantUML with checksum verification and runs -checkonly. For local diagrams: java -jar target/plantuml.jar -tsvg -o ../../target/diagrams "docs/architecture/*.puml". PlantUML uses Smetana; Graphviz installation is unnecessary. The jar and rendered artifacts are ignored. Diagrams describe target architecture; M0 does not implement the depicted domain flows.

Milestone 1A estate implementation is recorded in docs/adr/0008-estate-management.md and docs/roadmap/MILESTONE_1A.md. Milestone 1B is recorded separately in ADR-0009.

Requested Milestone 1B spatial implementation is recorded in docs/adr/0009-spatial-digital-twin.md and docs/roadmap/MILESTONE_1B.md. Spatial Service targets Java 21 as explicitly requested; Estate retains its existing Java 25 build. Milestone 1C local integration is recorded in ADR-0010/0011 and docs/roadmap/MILESTONE_1C.md.

## Milestone 3B design package (proposed)

Design-only work, 2026-10-27: [requirements](docs/milestones/MILESTONE_3B_REQUIREMENTS.md), [technical design](docs/milestones/MILESTONE_3B_DESIGN.md), [implementation plan](docs/milestones/MILESTONE_3B_IMPLEMENTATION_PLAN.md), [acceptance criteria](docs/milestones/MILESTONE_3B_ACCEPTANCE_CRITERIA.md), [validation limitations](docs/milestones/MILESTONE_3B_VALIDATION.md) and [proposed ADR 0013](docs/adr/0013-latex-collection-and-drc.md). Six proposed PlantUML sources live under diagrams/milestone-3b. This package does not implement 3B, approve its business defaults, modify AEO or close Milestone 2 performance acceptance. Existing 3A evidence remains in docs/milestones/milestone-3a-completion.md.

## Continuous application development

Start with the [persistent workflow](docs/milestones/APPLICATION_DEVELOPMENT_WORKFLOW.md) and [current checkpoint](docs/milestones/DEVELOPMENT_CHECKPOINT.md). The [3B readiness review and consolidated decision package](docs/milestones/MILESTONE_3B_READINESS_REVIEW.md) records the outstanding approval gate. These are the resume entry points; the legacy NEXT_CODEX_PROMPT.md is historical. Milestone 3B remains proposed and Milestone 2 performance acceptance remains open.

## Milestone 3B owner disposition

The project owner accepted D01â€“D12, ADR 0013 and the design package with R01/R02 on 2026-10-27: [approval and boundaries](docs/milestones/MILESTONE_3B_APPROVAL.md). Earlier proposed-status descriptions are historical. Implementation is authorized in dependency order but T00 Git/validation baseline remains blocked by command process creation failure. ADR 0013 is accepted at its existing proposed path pending verified canonical inventory promotion. No feature implementation or runtime acceptance is claimed.

## Milestone 3B T00/T01/T02 progress

ADR 0013 now lives in the accepted docs/adr inventory. CI and validation cover thirteen ADRs and all six 3B diagrams. Workspace validation, PlantUML syntax/render and visual inspection passed. Contracts candidate authoring and pure Operations domain/calculation work are implemented and locally checked; collection APIs/persistence are not enabled. See [current checkpoint](docs/milestones/DEVELOPMENT_CHECKPOINT.md) for independent contract review/release and Docker availability gates. Earlier proposed-path and execution-blocked statements in historical records describe prior increments.
