# Immersive and XR architecture
The web and Unreal clients consume the same gateway/service API contracts and UUID estateId/blockId. Estate owns identity; spatial owns geometry and authoritative georeferenced asset references. Clients cannot query databases or invent authoritative identities.

Use Cesium georeferencing for WGS84/ECEF/world transforms, double precision and world-origin management. GeoJSON coordinates are longitude, latitude, optional altitude metres; vertical datum must be declared by each future dataset. Terrain, roads, buildings and illustrative rubber trees are representations with source/provenance/accuracy metadata. Procedural tree locations are never surveyed individual trees.

The Milestone 0 descriptor targets Unreal Engine 5.8 + Cesium for Unreal 2.30.0, whose release publishes a matching package. No editor build is claimed. OpenXR is engine-bundled and disabled until runtime/device support is validated. No plugin binaries, assets or gameplay are generated.

M5 separates transport/auth, domain selection state, geospatial adaptation and presentation/input modules. Test canonical block selection against the browser on identical GeoJSON. Cache only permitted data, refresh credentials through public-client PKCE/device-supported flow, never embed secrets. Asset URIs must be authorized, short-lived where needed and licensed.

VR prototype: select a supported headset/runtime, measure frame time, comfort, LOD/streaming and selection accuracy. AR/MR roadmap: evaluate geospatial anchors, outdoor tracking/GNSS accuracy, occlusion, terrain registration, offline constraints, device support and permission UX. OpenXR support does not guarantee MR capability. Device procurement and cloud/asset streaming costs require separate decisions.
