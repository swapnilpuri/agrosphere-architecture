# Functional requirements
| ID | Requirement | Milestone / owner |
|---|---|---|
| FR-01 | Manage company, estate, division, block, crop/clone and planting identity using UUIDs | 1 / estate |
| FR-02 | Associate valid WGS84 geometry with canonical estate/block IDs; spatial search and layers | 1 / spatial |
| FR-03 | Fly to estate, select blocks and inspect authoritative details in a 3D browser | 2 / web + spatial |
| FR-04 | Record tapping, latex mass and DRC; calculate dry rubber with explicit units | 3 / operations |
| FR-05 | Register devices and normalize MQTT soil/weather observations, retaining observed and received times | 3 / telemetry |
| FR-06 | Record inspections and incidents; notify users of justified alerts | 3 / operations |
| FR-07 | Build historical and productivity projections from versioned events | 4 / analytics |
| FR-08 | Forecast rubber yield and detect anomalies with model/version/evidence metadata | 4 / AI |
| FR-09 | Provide evidence-backed assistant recommendations and hotspot links | 4 / AI + clients |
| FR-10 | Explore the same estate in Unreal with canonical block selection | 5 / immersive |
| FR-11 | Authenticate clients and independently validate JWTs at gateway and services | Before domain endpoints / each backend |
| FR-12 | Label REAL, SIMULATED, ESTIMATED, PREDICTED data in transport and presentation | All milestones |

All domain endpoints and authorization policies are future work. SSE/WebSocket notifications require a delivery/reconnect design before adoption.

## Accepted WA-1 increment — 2026-10-29

The sentence above describes the historical foundation baseline, not current implementation status. The owner accepted worker registration/daily attendance requirements WA-R01–WA-R08 in the [reviewed package](../milestones/WORKER_ATTENDANCE_REVIEW.md); see [approval and retained gates](../milestones/WORKER_ATTENDANCE_APPROVAL.md) and ADR 0014. These requirements extend the product scope independently of FR-04. Acceptance criteria WA-AC01–18 are not yet passed. D08 workload inputs and D09 actual privacy/retention policy remain open gates; only SIMULATED development is eligible until real-data enablement is reviewed and verified.

## Accepted II-1 increment — 2026-10-31

The owner accepted II-R01–07, II-D01–10 and II-T01–09 in the [incident/inspection package](../milestones/INCIDENT_INSPECTION_REVIEW.md); see [approval](../milestones/INCIDENT_INSPECTION_APPROVAL.md) and ADR 0015. This delivers a bounded part of FR-06: completed block inspection evidence and manually managed crop-health incident lifecycle, with scoped permissions, immutable evidence and minimal events. Notification delivery, MQTT and Analytics are deferred. II-AC01–16 require independent implementation evidence; II-D07/08 and WA D08/D09 remain open downstream gates and REAL collection remains disabled. The checkpoint records current source/test state; historical WA acceptance labels above are not current verification results.

## Accepted AN-1 increment — 2026-10-31

The owner accepted AN-R01–05 / AN-D01–10 in the [alerts package](../milestones/ALERTS_NOTIFICATIONS_REVIEW.md); see [approval](../milestones/ALERTS_NOTIFICATIONS_APPROVAL.md) and ADR 0016. This adds a bounded SIMULATED crop-health estate inbox, polled badge, own read and shared manager acknowledgement to FR-06. No addressed/external delivery, MQTT or Analytics. Independent executable acceptance/local release and implementation evidence remain required. AN-D07/08 and existing WA/II/M2/REAL gates remain open; design acceptance is not functional acceptance.
