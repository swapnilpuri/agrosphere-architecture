# POC-CLOSE rendering resume — 2026-11-12

POC-CLOSE engineering remains **PARTIAL; runtime blocked by incomplete expired-fixture private-copy cleanup; owner acceptance OPEN**. Existing C01–C07 and image/dependency approvals remain effective. No new implementation approval is needed. No Digital Twin fix or hardware acceptance is claimed.

## Ownership and exact recovery

At 2026-11-12 15:32:25 UTC (09:32 America/Chicago), run `39166eb7f43c41b68afafa967eef8ac6` was past its fixed 08:10:59.810202 UTC expiry. Its recorded operator PID/start-time identity was absent. The manifest still reported `COMPONENTS_PASS_RENDERED_CHECKS_PENDING` and cleanup `NOT_RUN`; those were stale. The supervised lifetime was missed after operator loss.

The existing `python scripts/verify_poc_close.py --recover target/poc-close/39166eb7f43c41b68afafa967eef8ac6/owner.json` first stopped on unrecorded generated native files. Sequential review matched the additional paths to native tooling: the dedicated native browser profile, command/state/browser inventory and native Saved/Config crash files. All paths were checked against the exact marked root and rejected if linked. The additional inventory was recorded before retrying recovery. No credential contents were inspected.

Exact cleanup removed all owned containers, volumes, networks and run-specific image tags. A subsequent label/identity check confirmed empty resource inventories and that all five recorded client process identities were absent. Recovery then failed with `PermissionError: [WinError 5] Access is denied` at `native-browser-profile/Default/AutofillAiModelCache/LOCK`. This zero-byte file is not read-only. Native PowerShell removal also failed. Attempts to restore explicit current-owner ACL rights returned Access Denied/unauthorized operation; no successful ACL repair is claimed. This is a Windows filesystem blocker, not an automatic approval-review rejection.

The exact remaining generated root is `C:\Users\Owner\AppData\Local\Temp\agrosphere-poc-close-39166eb7f43c41b68afafa967eef8ac6-_i2dnqau`. It still contains generated credentials/profile and other inventoried private copies. Do not report cleanup PASS or start another fixture until absence is verified. An asynchronous owner request asks for removal of this exact folder through their Windows account. No existing stack or user profile is targeted.

Public ignored recovery evidence: Infrastructure `target/poc-close/39166eb7f43c41b68afafa967eef8ac6/recovery-review-2026-11-12.json`, `recovery-blocker-2026-11-12.json` and `owner.json`. [Resume evidence](POC_CLOSE_RENDERING_RESUME_2026_11_12.json) preserves current source hashes, independent Git baselines and verification limits.

## Digital Twin investigation

Read the service, component/callers, layout, current graphics/component tests and installed Cesium 1.146.0 camera, flight, transition, uniform and frustum implementations. No owner browser/localhost application was accessed, and no generated WebGL reproduction was started because cleanup must precede a fresh fixture.

The installed frustum throws the reported message when `left > right`. Source inspection found a separate mode-dependent focus defect: `getRectangleCameraCoordinates` returns projected coordinates in 2D, whereas `bounds()` always feeds its result to `Cartographic.fromCartesian` as ECEF. Source also shows direct animated morph calls without application lifecycle coordination; concurrent loads/focus can encounter MORPHING, in which rectangle coordinates return undefined and camera flyTo is ignored. These are observations and hypotheses, **not an established root cause** for the owner's error. The empty/degenerate/zero-size cases and both mode controls still require actual timing reproduction.

An exploratory CPU-only script used the installed Camera/SceneTransitioner/TweenCollection in a synthetic scene. After accounting for nested transition durations, its tested 3D→2D→flight→3D→2D sequence did not reproduce the reported error. It has no browser, WebGL, render-error events, real layout or interactive canvas and cannot establish a rendered PASS. The exploratory script remains ignored under Web `target/digital-twin-investigation/camera-reproduction.mjs`.

No speculative product patch was made. The existing graphics test's immediate 2D/3D clicks and final page-error assertion do not establish completed modes or continued rendering. Add a focused regression after the actual invalid state is reproduced, with sanitized camera/frustum, scene mode/morph state, dimensions and triggering actions.

## Required resumption

1. Verify the exact private root is absent; rerun the existing exact recovery so the manifest verifies Docker absence and records cleanup PASS. Retain this failed recovery and missed-lifetime evidence.
2. Reproduce the Digital Twin error in a fresh, generated, owned fixture; distinguish it from the owner's environment. Implement and review the smallest demonstrated lifecycle fix, then run unit and actual WebGL regressions across the requested transitions, races, dimensions, selections and route remounts.
3. Run the corrected connected hardware harness with exact new source/run identities; preserve all prior failures and chronology. Finish the approved native negative/auth/race/security/coordinates and 1920×1080 performance protocols unchanged. Persist request-start proof for races and actual renderer coordinate exports.
4. Complete independent required checks, setup/recovery/teardown and all-copy cleanup. Present concrete owner acceptance results before requesting functional acceptance. Android/offline remains subsequent; AEO untouched, OpenXR disabled, physical VR/French deferred and bounded M4 acceptance preserved.

Twelve independent product Git roots were clean when inspected; source/index baseline hashes are in the evidence JSON. No staging, commit, reset, push, dependency change, production/REAL/existing-stack mutation or sub-agent was used. Only Architecture progress documentation changed; Infrastructure ignored manifests/recovery reports and Web ignored CPU diagnostic are evidence artifacts. No new product test/build results are asserted.

## Documentation validation

`python scripts/validate.py --workspace C:\Projects\agrosphere` PASS (architecture layout/16 ADRs/workflow YAML and 12-root structure/ignore/secret-pattern checks). `git diff --check` PASS. Final preservation check PASS: all twelve recorded Git index hashes unchanged, all eleven non-Architecture statuses unchanged, inspected Web source/dependency hashes unchanged. These checks do not verify application rendering or cleanup of the remaining protected private directory.
