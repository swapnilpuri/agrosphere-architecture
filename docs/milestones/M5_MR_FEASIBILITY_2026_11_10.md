# M5 MR feasibility — assessment only

The approved desktop demonstration is feasible with the installed Unreal/Cesium toolchain. Plantation-aligned MR is **not verified**. Physical VR is explicitly deferred by the owner; no headset, passthrough, spatial anchor, camera/room capture or outdoor trial was performed.

Cesium supplies transformations between longitude/latitude/ellipsoidal height, ECEF and the Unreal frame. Those transformations allow numerical coordinate agreement; they do not locate a headset in a surveyed plantation. See the [Cesium georeference API](https://cesium.com/learn/cesium-unreal/ref-doc/classACesiumGeoreference.html).

OpenXR LOCAL/STAGE are runtime tracking reference spaces. LOCAL can be recentered; tracking loss can yield inferred poses, and recovery can move the reported pose. STAGE describes a runtime-defined floor rectangle. Neither establishes a WGS84 survey origin. See [Khronos reference-space definitions](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrReferenceSpaceType.html) and the [OpenXR specification](https://registry.khronos.org/OpenXR/specs/1.1-khr/html/xrspec.html). The following are engineering implications and proposed prerequisites, not measured device capabilities.

| Concern | Requirement for a later authorized trial |
|---|---|
| Registration | Surveyed control points and a measured rigid transform between tracking and geodetic frames, including heading, units and handedness; independent check points rather than fitting and testing the same points. |
| Height | Identify ellipsoidal versus orthometric height and any geoid conversion. The current 0 m ellipsoid display is illustrative and cannot align to ground. |
| Drift/relocalization | Measure repeatability over distance/time, restart and tracking loss; detect changes and suppress misleading overlays until registration is restored. |
| Calibration/occlusion | Verify eye/camera/display calibration and depth/occlusion support on the actual device. Primitive estate surfaces cannot establish real trees/buildings or safe obstacles. |
| Outdoor environment | Test illumination, shadows, foliage movement, weather, texture and tracking limitations with a human operator and a controlled area. No outdoor suitability is claimed. |
| Anchor persistence | Confirm supported runtime extensions and persistence behavior across sessions/devices. An anchor is not automatically a surveyed geographic coordinate. |
| Privacy and permissions | Separately authorize camera, room/scene capture, storage, retention and any cloud anchor processing; none is enabled here. |
| Offline | Current authenticated clients deliberately clear/hide protected data on failures; there is no authorized offline estate cache. Offline MR needs its own reviewed data/access policy. |

Before implementation, name the device/runtime, permitted SDK/license use, operator, environment, surveyed ground truth and acceptance error budget. Measure translation/rotation errors and uncertainty against that ground truth. Desktop centimetre-level arithmetic tests and frame timing are not field accuracy, tracking accuracy, comfort or physical scale evidence. No MR implementation or numerical field-accuracy claim is delivered.
