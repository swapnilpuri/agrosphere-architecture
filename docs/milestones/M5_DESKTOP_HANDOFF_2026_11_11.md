# M5 desktop handoff — 2026-11-11

The local Unreal desktop prototype is implemented, built and exercised on the owner's PC. Physical VR remains explicitly deferred. **Full M5 engineering and owner functional acceptance remain OPEN** because the broader verification gaps below are retained. This report supersedes historical pending implementation/package labels in the discovery, checkpoint and [execution record](M5_DESKTOP_VERIFICATION_2026_11_10.md); it does not close unrelated milestones.

## Working result

Immersive 0.2.0 supplies external-browser PKCE sign-in, an authorized estate picker with automatic single-estate load, canonical generated block surfaces, mouse selection, camera focus/navigation, recorded metadata, geometry provenance and illustrative primitive trees. It uses the independently pinned existing Estate/Spatial contracts and Cesium georeference. No terrain/imagery provider or ion token is needed. [Run instructions](../../../agrosphere-immersive/README.md) and [fixture instructions](../../../agrosphere-infrastructure/docs/M5_OWNED_FIXTURE.md) explain the packaged executable and new disposable sign-in.

Installed combination actually used: UE 5.8.4 build 58902052, Cesium 2.30.0, MSVC 14.50.35726 (directory 14.50.35717), SDK 10.0.22621.0. The renderer selected NVIDIA GeForce RTX 5090 **Laptop** GPU, driver 592.02; CPU Intel Core Ultra 9 275HX; 64 GB RAM. NullRHI automation reports Intel Graphics because it does not exercise the rendering adapter; actual D3D12 logs establish the NVIDIA selection.

## Actual verification

| Check | Executed result |
|---|---|
| Editor module | Build PASS with the installed combination. |
| Windows package | Development build, cook, stage and archive PASS; standalone launches without editor. Exact final identities are in the [evidence inventory](M5_DESKTOP_EVIDENCE_2026_11_11.json). |
| Native tests | `target/automation-handoff/index.json`: five Success, zero failed/warnings/notRun after the recovery-status correction. Tests cover geometry/topology, Cesium/ECEF frame agreement, actual mesh construction/clearing, endpoint isolation, signed identity/lifecycle and native HTTP probes. |
| Independent review | [Final review](M5_CLIENT_REVIEW_FINAL_2026_11_10.md) resolves the seven initial findings and corroborates the reviewed rebuild/tests. The subsequent single-line change restores the status message on a successful API read; its new source identity and tests are recorded separately. |
| Actual desktop | Fresh generated browser sign-in, 12 rendered blocks, 288 illustrative trees, selected UUID/metadata and focus; logout removes scene/details and browser IdP logout exercised. Earlier Web/native walkthrough selected identical M5_B09 UUID/version/GENERATED/SIMULATED values. |
| Actual outage/recovery | Stop only the owned Gateway, revalidate a selected block: unavailable status, no geometry or details remain. Restart that Gateway and refresh: estate returns. Observed stale unavailable text was corrected and repackaged. |
| Desktop frame target | Actual viewport 1920×1080; 5-second warmup, 30-second wall-frame capture, 7,773 samples; p95 **6.044403 ms**, maximum **19.063797 ms**, 12 blocks/288 trees. Proposed p95 <=33.3 ms target passes for this generated scene. |
| Useful view | Warm local run: **0.190952 s** from successful native sign-in to scene; **0.097948 s** loading. This excludes human login time and engine startup and is not a cold-cache benchmark. |
| Repository checks | Immersive descriptor/exact pins, Infrastructure validator/Python syntax, Architecture validator and twelve-root audit PASS. Final diff checks and hashes are in the evidence inventory. No hosted CI or new Web source build is claimed. |

Frame captures are desktop wall-clock samples, not separate CPU/GPU/compositor measurements. Earlier runs are retained: Windows-clamped 1423×889 was not accepted as 1080p; another true-1080p run included a 622.6389 ms transition stall. A foreground reload measured p95 5.771 ms and maximum 8.972198 ms, but its login-to-scene interval included 42.73 seconds of manual delay and is not used for the login target. No failed or inconvenient capture was silently replaced with a universal performance claim.

## Fixture lifecycle and preservation

The previous `agrosphere-m5-a77d64dd440e` verifier was interrupted during the usage-limit/session break. On resumption its process was absent and containers stopped; READY was stale. The new recovery script verified exact labels/stopped state/image IDs and resolved generated paths, removed only its owned resources, and recorded `INTERRUPTED_CLEANED` with cleanup PASS. Its nominal four-hour lifetime was exceeded while the verifier was absent; the finally loop was not an independent lifetime guarantee. This failure and corrective recovery remain explicit.

The fresh `agrosphere-m5-3b2a0a253977` fixture independently passed health/ownership, six-read/12-canonical-DTO agreements, foreign estate/object and missing-role/token denials, VIEWER write denial and exact public-client/S256 registration. It owns only generated accounts/data and random loopback ports. Final normal stop/cleanup results are recorded in the evidence inventory. Existing developer stacks, private configuration, roles and data were excluded. The temporary workspace credential copy and the two known M5 test crash exports are removed; sanitized failure descriptions remain.

Original approved M5 package SHA-256 remains `8e5d1571c13863b5e48320d2c870345cc6c5e7032717545441b7e9bbd9d0bb38`; M4 package remains `befbee78062c2fcef6af0ea394fcc81be3e7638053deca142f136c66bc7cc93d`. Existing HEAD/index state had advanced between sessions without agent staging/commit/reset commands; it was preserved. No production/REAL/AEO action, external publication, installer, purchase or license acceptance was performed. Available installed Cesium license/dependency notices are retained in the local package; redistribution rights/full transitive license audit are not inferred.

## Remaining verification and acceptance

- Physical VR/controller input, 90 Hz CPU/GPU/compositor metrics, recenter/physical scale and human comfort are DEFERRED; OpenXR stays disabled.
- [MR feasibility](M5_MR_FEASIBILITY_2026_11_10.md) is complete as an assessment only; no surveyed registration, passthrough, anchors or field accuracy is verified.
- The full rendered negative matrix (empty/no geometry/malformed or oversize service replies, live stale-response races, occupied callback port/partial callback timing), actual refresh failure/revocation/key rotation, maximum-scene stress, sustained input assessment and renderer-to-renderer numerical comparison remain unverified. Component tests and UUID agreement do not silently close them.
- Single-audience fixture ID tokens only, bounded generated geometry and conservative topology rules are supported. Polar/antimeridian edges, arbitrary GIS scale, REAL/offline/production/provider streaming are outside this implementation.
- Owner functional acceptance requires an explicit later response after trying the delivered desktop behavior. Package approval and these engineering results are not that response. No repeated implementation approval is required to continue the already authorized verification gaps.

The executable is `agrosphere-immersive/target/M5-Windows/Windows/AgroSphere.exe`. A new owned fixture is needed after cleanup; follow the README rather than reusing expired generated credentials or stopped fixture endpoints.
