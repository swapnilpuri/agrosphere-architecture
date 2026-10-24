# agrosphere-architecture

Architecture and implementation decisions through Milestone 1C for the AgroSphere Rubber Plantation Digital Twin.

This is an independent project and Git root. Version: 0.4.0; use independent SemVer tags and CHANGELOG.md. License decision: LICENSE.md (all rights reserved pending selection).

See AGENTS.md for scope and engineering rules. This scaffold provides no business APIs or production features. Architecture lives in the sibling agrosphere-architecture repository; versioned API/event definitions live in agrosphere-contracts. Do not add path dependencies to sibling projects.

## Architecture index

- docs/requirements: vision, POC scope, functional and nonfunctional requirements.
- docs/architecture: seven PlantUML diagrams, XR roadmap and integration/reliability patterns.
- docs/adr: eleven accepted foundation and milestone decisions.
- docs/DEPENDENCIES.md: selected versions, source links and compatibility caveats.
- docs/roadmap: milestones, implementation backlog and exact next Codex prompt.
- docs/VALIDATION_REPORT.md: executed checks and limitations.

## Validate

Python 3.12+: python -m pip install -r requirements-dev.txt; python scripts/validate.py. Optional full local structure audit: python scripts/validate.py --workspace C:\Projects\agrosphere (requires Git on PATH). The audit reads sibling structure only; projects build independently.

C4 macros v2.12.0 are vendored under docs/architecture/includes with their MIT license. CI downloads pinned PlantUML with checksum verification and runs -checkonly. For local diagrams: java -jar target/plantuml.jar -tsvg -o ../../target/diagrams "docs/architecture/*.puml". PlantUML uses Smetana; Graphviz installation is unnecessary. The jar and rendered artifacts are ignored. Diagrams describe target architecture; M0 does not implement the depicted domain flows.

Milestone 1A estate implementation is recorded in docs/adr/0008-estate-management.md and docs/roadmap/MILESTONE_1A.md. Milestone 1B is recorded separately in ADR-0009.

Requested Milestone 1B spatial implementation is recorded in docs/adr/0009-spatial-digital-twin.md and docs/roadmap/MILESTONE_1B.md. Spatial Service targets Java 21 as explicitly requested; Estate retains its existing Java 25 build. Milestone 1C local integration is recorded in ADR-0010/0011 and docs/roadmap/MILESTONE_1C.md.
