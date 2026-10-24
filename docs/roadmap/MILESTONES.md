# Milestones and exit gates
| Milestone | Scope | Exit gate |
|---|---|---|
| 0 Foundation | Independent repos, standards, contracts, docs, CI, infrastructure definitions | Validation report records executed checks and unavailable runtime tests |
| 1 Estate/GIS | Estate/block identity, PostGIS geometry, synthetic rubber GeoJSON, API/query integration | Isolated credentials, geometry validity, JWT authorization and duplicate/outbox tests pass |
| 2 3D web | Angular/Cesium terrain, selection, gateway, KPI detail | Canonical selection, provenance, attribution and reference-device frame budget verified |
| 3 Operations/IoT | Tapping, collections/DRC, incidents, MQTT simulator, overlays, alerts | Unit consistency, authentication, replay/dedup and observation timestamps verified |
| 4 AI | KPI projections, forecasts, anomaly evaluation, assistant/evidence links | Time-aware holdout, model registry/evidence and predicted labels; no fabricated agronomic certainty |
| 5 Immersive | UE/Cesium exploration, API client, VR prototype, MR feasibility | Same estate/block IDs as browser, supported device/runtime and performance evidence |

No automatic continuation beyond M0. Schedule and staffing are deliberately uncommitted.

Milestone 1A is authorized separately for Estate Service only; see MILESTONE_1A.md and ADR-0008. Milestone 1B/GIS work requires a new request.

Milestone 1B is authorized by its separate request and implemented in Spatial Service; see MILESTONE_1B.md and ADR-0009. This does not authorize Milestone 1C.

Milestone 1C local integration is implemented; see MILESTONE_1C.md, ADR-0010 and the infrastructure completion report for executed evidence. Client implementation remains future scope.
