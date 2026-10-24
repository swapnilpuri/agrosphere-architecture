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
