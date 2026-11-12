# M5 desktop execution evidence — 2026-11-10

Historical execution record. The [2026-11-11 desktop handoff](M5_DESKTOP_HANDOFF_2026_11_11.md) supersedes pending package/performance/cleanup labels here and records the exact final artifacts. The owner approved D01–D10 with VR deferred; owner functional acceptance remains OPEN. Full M5 is not closed by desktop evidence. Preserve the original approved package bytes and prior M4 acceptance.

## Delivered implementation

Immersive 0.2.0 contains a native Windows module, independent exact Estate/Spatial pins, PKCE S256 external-browser authentication, bounded loopback WinHTTP transport, RS256 ID-token validation, paged identity/geometry reads, Cesium georeferencing, procedural block meshes, picking/focus and authoritative selected-block metadata. The single authorized estate loads automatically. Decorative primitive trees are deterministic and explicitly illustrative. OpenXR remains disabled. No imagery/terrain/ion token, production target or new public API was introduced.

Infrastructure adds a new random owned fixture runner and a temporary Web build server that supplies generated configuration without reading or modifying existing Web configuration. Estate, Spatial and Gateway source remain independent; fixture services use their existing APIs/migrations. MR is an [assessment only](M5_MR_FEASIBILITY_2026_11_10.md).

## Executed checks

- Native editor module builds with UE 5.8.4-58902052, Cesium 2.30.0, MSVC 14.50.35726 (directory 14.50.35717), SDK 10.0.22621.0.
- Windows Development BuildCookRun builds, cooks, stages and archives successfully; standalone executable launches without the editor.
- Final native automation: five tests PASS, zero test failures or warnings: Geometry.Validation, Geometry.CesiumFrames, Geometry.RenderAndClear, Security.EndpointIsolation, Security.SignedIdentityAndLifecycle. The final report is `agrosphere-immersive/target/automation-final/index.json`. Startup contains an upstream Cesium enum-initialization diagnostic outside the test results; this is retained, not reported as a clean engine log.
- Geometry tests cover holes, invalid topology/provenance/coordinates, independent WGS84/ECEF agreement and Cesium round trips within 1 cm, changed origins and metre/centimetre conversion. Renderer regression constructs actual mesh sections and verifies protected geometry/selection/details clearing. These are generated numerical checks, not survey accuracy.
- Security tests use real ephemeral RSA signatures, claim negatives, lifecycle clearing/expiry/reconfiguration, real loopback callback rejection/replay/size checks and WinHTTP redirect/receive-bound/retry probes. Redirect traps are not reached; GET retries are capped and 401 is not retried.
- Owned fixture `agrosphere-m5-a77d64dd440e`: six API reads and 12 canonical DTO agreements; signed role/estate/object isolation, unsigned/missing-token and read-only write denials; exact native public-client registration. Safe results are in Infrastructure `target/m5/a77d64dd440e4f8b80427ba28bacd3fe/results.json`.
- Actual UI: external browser sign-in, authorized estate loading, all 12 block surfaces/288 decorative trees, mouse picking, camera focus, selected canonical metadata, native logout clearing scene/details, and browser IdP logout prompt exercised. The next login required authentication again.
- Web actual independent built artifact and native client both selected `M5_B09`, UUID `fcaaeb42-f9d6-45ee-a67c-7779a920ce50`, estate `d0839f33-48ba-4a56-a21b-bd2e625f37ea`, geometry version 1, GENERATED/SIMULATED. Final native metadata agrees with Web: recorded area 1 ha, planted 100, tappable 80; clone/planting date not supplied. Web displays Spatial calculated area separately (1.19 ha). The generated recorded area is not a survey.

Geometry DTO SHA-256: `ba5c1e1eb9f06929f64ae63753f14a847c5e2204897b0122391427fa0db1a668`. Metadata DTO SHA-256: `f35358041db7b28ee7c99933e98d396879687419866d137a0083e6a69b257910`. Exact source/package/evidence hashes are recorded separately after final validation.

## Failures and corrections retained

Initial fixture authentication failed because a sparse user update discarded generated account attributes; full generated-user representation fixed it. A second fixture caught database timestamp precision differences between POST and persisted reads; verification now bounds that conversion to 2 microseconds and compares persisted list/detail responses exactly. Both failed owned runs cleaned up.

Native compile issues (OpenSSL/UE UI namespace collision and initial Slate/pawn typing) were corrected. An initial test world was initialized twice; the duplicate initialization was removed. Real rendering then exposed TArray self-reference during reverse triangle winding; indices are copied before append, and RenderAndClear now exercises that path. The observed crash is not hidden by earlier pure tests. A later relink failed while the unsent crash reporter held the module; closing it without submitting and retrying succeeded.

The first frame report lacked actual viewport dimensions. Added measurement revealed Windows resized the requested 1920x1080 window to 1423x889. That run achieved 4.729502 ms p95, 9.082299 ms maximum across 11,136 frames, and 0.099941 seconds from successful login to scene (0.060192 seconds loading). It does **not** prove the 1080p target. An explicit-resolution follow-up is tracked separately. Measurements use a 5-second warmup/30-second wall-frame capture, not GPU-only timing.

## Limits and remaining exits

Physical VR/controller navigation, 90 Hz CPU/GPU/compositor capture, physical scale/recenter and human comfort are DEFERRED by the owner. No MR physical alignment is verified. Owner functional acceptance is OPEN.

The exercised generated fixture is deliberately small and local. Broad production OIDC support, provider streaming, REAL data, offline access, arbitrary GIS topology and larger-estate scaling are excluded. Multi-audience ID tokens are explicitly rejected by this bounded client. Conservative component-overlap validation may reject some otherwise valid MultiPolygon layouts.

A complete UI-level negative/recovery matrix, independent final security disposition, sustained navigation/input evidence, exact 1080p measurement, and renderer-to-renderer numerical coordinate comparison must not be inferred solely from the component tests or matching UUID screenshot. Test coverage and remaining gates are recorded explicitly; no broad desktop or whole-M5 engineering completion claim is made until required exits are satisfied. The independent Web build used for comparison is an existing artifact, not a new Web source release or hosted CI run.

Installed upstream license/attribution files are preserved with the local package where available. This is not a completed redistribution/license audit or permission to distribute; no installer, purchase, EULA acceptance, deployment or Git publication occurred. Local machine cost is unmetered; no paid provider assets were requested.

## Reproduce

Use [Immersive README](../../../agrosphere-immersive/README.md) and [owned fixture instructions](../../../agrosphere-infrastructure/docs/M5_OWNED_FIXTURE.md). The local executable is `agrosphere-immersive/target/M5-Windows/Windows/AgroSphere.exe`; it requires a current owned fixture and generated sign-in. Screenshots are local ignored evidence (`target/m5-native-final.png`, `target/m5-web-selected.png`), not committed generated datasets. Cleanup status is recorded after the fixture stop sentinel is processed.
