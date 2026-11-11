# M5 desktop client review disposition — 2026-11-10

**Initial seven review findings resolved in source; reviewed native security/geometry automation PASS for the recorded tested snapshot.** This accepts those engineering corrections for the bounded local SIMULATED desktop client. Subsequent metadata/deadline refinements below are source-reviewed but awaiting rebuilt execution evidence. This does not certify every M5 exit, owner acceptance, broad OIDC compatibility, production security or deferred physical VR. [Initial review](M5_CLIENT_REVIEW_INITIAL_2026_11_10.md) remains unchanged as historical evidence. [Existing contract acceptance](M5_CONTRACT_REVIEW_2026_11_10.md) remains applicable.

Reviewer: independent delegated contract/security review agent. Inspected actual current EstateSession.cpp/h, EstateGeometry.cpp, EstateViewer.cpp, EstateTests.cpp, EstateSecurityTests.cpp and existing native build/automation outputs. Did not rerun a stack, mutate fixtures, inspect private config or change implementation in this final review. The reviewer previously authored the separate native security test file; implementation fixes were authored by the parent engineer.

## Corroborated execution

Immersive `target/automation-final/index.json` SHA-256 `01e77f5cefaf6687bca69f2a61e65456b7d41aeb16e020b1bd385b3c92b87be7` reports five Success, zero failures, zero warnings and zero unrun tests. `target/m5-automation-final.log` independently records completion of all five and queue-empty exit. Report timestamp is 2026-11-11 05:29 UTC, corresponding to 2026-11-10 America/Chicago.

| Native test | Executed coverage |
|---|---|
| AgroSphere.Geometry.CesiumFrames | Independent WGS84 ECEF versus Cesium within 1 cm, round trips in both hemispheres/near antimeridian, shifted origins and metre-to-centimetre scale |
| AgroSphere.Geometry.RenderAndClear | Actual procedural mesh construction, both triangle windings, bounded illustrative instances and removal of geometry/picks/selection/details |
| AgroSphere.Geometry.Validation | Hole area exclusion, foreign-estate rejection, malformed/open/3D/polar/antimeridian/crossing/exterior-hole/overlapping-hole input rejection and REAL disabled |
| AgroSphere.Security.EndpointIsolation | Approved loopback configuration and rejection of representative external/userinfo/query/invalid-port endpoints |
| AgroSphere.Security.SignedIdentityAndLifecycle | Genuine ephemeral RSA signatures and claim/key/signature negatives; subject continuity; reconfiguration/expiry/request cancellation; real loopback invalid/duplicate/replayed/oversize callbacks; latent WinHTTP 307 redirect trap, 128 KiB identity-body abort, transient GET recovery/three-attempt ceiling and no 401 retry |

These are native Unreal automation tests, not merely Python replicas. The automation device report names Intel Graphics; it is not RTX 5090 frame-performance evidence. Parent engineer separately reports observing actual standalone login, generated render/selection, identical Web UUID and logout. Those observations must be cited to the parent's demonstration/artifact evidence; this reviewer did not independently repeat the live walkthrough.

## Initial finding closure

1. Transport uses WinHTTP with redirects, cookies and automatic authentication disabled before send; no proxy. The native redirect trap passes.
2. Receive loop bounds bytes before append: 128 KiB identity and 10 MiB API response. Oversized identity response abort passes; viewer separately limits aggregate scene bytes/features/vertices.
3. Configure clears credentials, requests and protected presentation; generation prevents late session completions. Native lifecycle assertions pass.
4. Geometry validates ring area/simplicity, hole containment/nonoverlap and conservative outer-component overlap before triangulation. Native malformed topology cases and hole area pass.
5. The former Unreal ProcessRequest false-path omission is removed by replacement transport; each uncancelled native attempt delivers a terminal result. Native transport failure/response tests exercise this path structure; not every OS allocation failure is injected.
6. Signature verifier enforces issuer, RS256, key use/algorithm, single audience, nonce, nonempty subject, time claims, optional nbf/azp and subject continuity on refresh. Genuine signature/claim negatives pass. Unsupported audience arrays fail closed.
7. Required nullable sourceReference type/length and geometryType correspondence are checked. Selection revalidates canonical estate/block/feature IDs, version, actual polygon rings and provenance before displaying details; transport failures clear protected scene.

## Remaining limits and follow-up

- Follow-up source inspection found and the parent corrected a metadata-validation gap: Viewer Select now rejects fractional tree counts, non-RUBBER cropType and unsupported status enums before presentation. Native malformed metadata execution is not asserted by the older five-test report.
- The parent also replaced the per-attempt deadline with one deadline captured before worker dispatch, shared by retries/backoff, and clamps native send/receive timeouts to the remaining budget. Current source is reviewed; a precise end-to-end ten-second timing measurement is not established. Cancellation invalidates callbacks immediately but a blocking native call may run until its bounded timeout.
- The verifier intentionally supports the fixture's single-audience Keycloak profile; it is not a general reviewed third-party OIDC SDK. Key rotation, actual refresh failure/revocation, occupied login port, partial callback timeout, full HTTP denial/empty/unavailable rendered-state matrix and live late-response races are not established by the five tests alone. Separate executed evidence can close individual cases; absence here is not proof of runtime failure.
- Maximum-scene load, packaged GPU performance, exact packaged-source identity, provider/license notices and all owned-resource cleanup require the delivery evidence. The frame transform test checks numerical alignment; no surveyed or MR accuracy follows.
- Physical VR input, comfort and frame measurements remain explicitly deferred by the owner. MR is feasibility-only. Owner functional acceptance requires a later explicit response.

## Reviewed source fingerprints

| Source/AgroSphere file | SHA-256 |
|---|---|
| EstateSession.cpp | `c0b558e26b2475125a40394893f90e1b2f4830ca7af845b7f338f0a3520bee68` |
| EstateSession.h | `b257113af1139c11cecc85c56edf612482973b5eda01114361f622af31371b24` |
| EstateGeometry.cpp | `7d6a27d20f80446caf8be7fd6786f041d390e057be9152fcf9d0b23469265489` |
| EstateViewer.cpp | `9ce09c2f3c1484b234b8c501d2035367c919efb8522fc79f96a2d6e6c75df4d1` |
| EstateSecurityTests.cpp | `3553364b8558417f45ed65c7333a8b6d1a882c428f6f240cfa295370ee307424` |
| EstateTests.cpp | `68a031bcf957886842aecbb87bd4cf298413b6c98e782b0167be8917df154895` |

Later source changes need updated artifact association; historical test reports must not silently certify changed bytes.

Follow-up reviewed source (awaiting parent rebuild/retest association): EstateSession.cpp `d4dc58b7c242e7a2ee9c82109e2c2bbae15eceaf11991d199742aa53084b5998`; EstateViewer.cpp `7826e522a7b9fecb5069a3bf26ed5bca882f1c2f71b196d52fd7ac2a5967f774`. No remaining critical defect was identified in this bounded review. All unexecuted gates above remain separate.

## Rebuilt verification addendum — 2026-11-10 23:39 America/Chicago

The preceding pending-rebuild labels are now satisfied for the exact follow-up source fingerprints above. Independently reread `target/m5-review-fix-build.log`: **Result: Succeeded**, execution time 12.45 seconds, SHA-256 `1023499a57bf59ffaeb45bc6edb17e1fc3a6a1442160ec754720f6b22704ac63`. Current Session/Viewer hashes still match the follow-up review; Session.h, Geometry and both test-source hashes still match the table.

`target/automation-reviewed/index.json` SHA-256 `009acebde9bf8b66630c5da7b17bb78a602dcbe49f282be8755a66918cf27a46` reports the same **five Success, zero failed, zero warnings, zero notRun**, created 2026-11-11 05:39:13 UTC. `target/m5-automation-reviewed.log` SHA-256 `446db34a77dbde15e9b20f9f8b09c86afd5d4172a772f8656d66365d7cb92f12` corroborates each completion and queue-empty exit. It records actual editor arguments `-unattended -nop4 -nosplash -NullRHI -ExecCmds="Automation RunTests AgroSphere" -TestExit="Automation Test Queue Empty"`, with report/log paths in the owning Immersive target directory.

The five native tests therefore pass after the reviewed metadata/deadline changes. NullRHI automation verifies native logic, mesh construction and clearing; it does not measure actual GPU rendering or certify a packaged executable. Dedicated malformed metadata and ten-second timing fault tests are not newly claimed by this rerun. Parent-reported 1920x1080 capture (p95 5.800899 ms, maximum 622.6389 ms with a foreground/transition interval) belongs to separate performance evidence; this addendum neither hides the maximum nor independently certifies that capture. The packaged client was being rebuilt separately and is not certified by these editor tests. Deferred VR and all other stated unverified gates remain open.
