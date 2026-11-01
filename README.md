# agrosphere-architecture

Architecture decisions through implemented Milestone 3A and owner-accepted Milestone 3B design for the AgroSphere Rubber Plantation Digital Twin.

This is an independent project and Git root. Version: 0.5.0; use independent SemVer tags and CHANGELOG.md. License decision: LICENSE.md (all rights reserved pending selection).

See AGENTS.md for scope and engineering rules. This scaffold provides no business APIs or production features. Architecture lives in the sibling agrosphere-architecture repository; versioned API/event definitions live in agrosphere-contracts. Do not add path dependencies to sibling projects.

## Architecture index

- docs/requirements: vision, POC scope, functional and nonfunctional requirements.
- docs/architecture: seven PlantUML diagrams, XR roadmap and integration/reliability patterns.
- docs/adr: sixteen accepted foundation and milestone decisions.
- docs/DEPENDENCIES.md: selected versions, source links and compatibility caveats.
- docs/roadmap: milestones, implementation backlog and exact next Codex prompt.
- docs/VALIDATION_REPORT.md: executed checks and limitations.

## Validate

Python 3.12+: python -m pip install -r requirements-dev.txt; python scripts/validate.py. Optional full local structure audit: python scripts/validate.py --workspace C:\Projects\agrosphere (requires Git on PATH). The audit reads sibling structure only; projects build independently.

C4 macros v2.12.0 are vendored under docs/architecture/includes with their MIT license. CI downloads pinned PlantUML with checksum verification and runs -checkonly. For local diagrams: java -jar target/plantuml.jar -tsvg -o ../../target/diagrams "docs/architecture/*.puml". PlantUML uses Smetana; Graphviz installation is unnecessary. The jar and rendered artifacts are ignored. Diagrams describe target architecture; M0 does not implement the depicted domain flows.

Milestone 1A estate implementation is recorded in docs/adr/0008-estate-management.md and docs/roadmap/MILESTONE_1A.md. Milestone 1B is recorded separately in ADR-0009.

Requested Milestone 1B spatial implementation is recorded in docs/adr/0009-spatial-digital-twin.md and docs/roadmap/MILESTONE_1B.md. Spatial Service targets Java 21 as explicitly requested; Estate retains its existing Java 25 build. Milestone 1C local integration is recorded in ADR-0010/0011 and docs/roadmap/MILESTONE_1C.md.

## Milestone 3B

The owner accepted [requirements](docs/milestones/MILESTONE_3B_REQUIREMENTS.md), [design](docs/milestones/MILESTONE_3B_DESIGN.md), [acceptance](docs/milestones/MILESTONE_3B_ACCEPTANCE_CRITERIA.md), ADR 0013 and R01/R02. Contracts 0.5.0 was accepted for local release/pinning; scoped credential wiring permits tracked placeholders and generated disposable tests only. See [approval](docs/milestones/MILESTONE_3B_APPROVAL.md), [workflow](docs/milestones/APPLICATION_DEVELOPMENT_WORKFLOW.md) and [current checkpoint](docs/milestones/DEVELOPMENT_CHECKPOINT.md) for implementation, exact evidence, outstanding checks and safe continuation. Six diagrams are under diagrams/milestone-3b and covered by validation/CI. Earlier design-only reports are historical. Milestone acceptance requires current AC01-AC28 evidence; Milestone 2 performance stays open. No production deployment, private environment access, existing-stack provisioning, remote publication or AEO change is authorized.

## Worker registration and attendance (WA-1)

The owner accepted [WA-1](docs/milestones/WORKER_ATTENDANCE_APPROVAL.md) on 2026-10-29. ADR 0014 and the checkpoint govern implementation; isolated executable contracts await their independent release gate. Pure domain/ports are implemented, not a delivered UI/API. D08 workload inputs and D09 actual privacy/retention policy remain acceptance gates.

## Current WA-1 and II-1 status — 2026-10-31

Earlier domain-only/pending-release WA-1 descriptions are historical: [WA-1 verification](docs/milestones/WORKER_ATTENDANCE_VERIFICATION.md) records delivered Web 0.4.0/API/Contracts 0.6.0. D08/D09 remain open.

The owner accepted [II-1 design](docs/milestones/INCIDENT_INSPECTION_APPROVAL.md) on 2026-10-31; ADR 0015 is the fifteenth accepted ADR. An isolated executable candidate and pure domain/ports are prepared; no incident UI/API/migration is delivered. Independent exact executable acceptance precedes release/pinning. See the checkpoint for current checks and retained SIMULATED/privacy/workload gates.

## AN-1 approval and independent preparation — 2026-10-31

The owner accepted the exact [alert review](docs/milestones/ALERTS_NOTIFICATIONS_REVIEW.md); see [approval](docs/milestones/ALERTS_NOTIFICATIONS_APPROVAL.md) and accepted ADR 0016. Operations-owned SIMULATED in-app estate alerts are authorized by dependency. Four executable candidate artifacts await independent acceptance/local release; pure domain/ports are prepared, with no runtime alerts delivered. AN subject-policy/workload and WA/II/M2/REAL/functional gates remain open; see checkpoint for exact checks. Earlier II-1 pending-delivery descriptions above are historical; II-1 and its separate local upgrade are complete.

## AN-1 locally implemented and verified — 2026-10-31

See docs/milestones/ALERTS_NOTIFICATIONS_VERIFICATION.md and the current checkpoint for accepted 0.8.0 executable release/pins, implemented local behavior, generated tests and preserved gates. Earlier preparation/pending labels are historical. No owner functional acceptance, non-generated subject rollout, REAL/production/M2 acceptance or existing-stack upgrade is inferred.
