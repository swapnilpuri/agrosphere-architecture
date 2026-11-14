# POC-CLOSE rendering progress and restart handoff — 2026-11-13

**POC-CLOSE PARTIAL; reported Digital Twin failure UNRESOLVED; owner acceptance OPEN.** Original exact cleanup now passes. A subsequent generated browser attempt failed in its test harness and left a Windows-protected profile. The owner plans a system restart later. No fresh fixture may start until exact private-copy cleanup passes. Existing approvals, historical failures and deferrals remain effective.

## Recovery and actual browser evidence

- Original run `39166eb7f43c41b68afafa967eef8ac6`: owner deletion independently verified. Docker Desktop was stopped, then its installed engine was started. Exact recovery PASS, private root absent, empty container/volume/network inventories. Historical missed supervision/lifetime remains recorded.
- Generated browser-only run `769c0ce7a13643d0a64a75e19d1a77f2`: one installed Edge/WebGL smoke test PASS (8.5 seconds), cleanup PASS. Snapshots cover initial 3D, 3D→2D→3D, 2D focus, eight rapid custom-mode/focus/resize sequences and route re-entry, with no retained render-error events. This was **isolated generated mocked identity/API, not the owner's reported environment**. Adapter: ANGLE Intel Graphics/D3D11; canvas: 1077×620. This is not NVIDIA reference-performance evidence or complete picking/console/frame-continuity acceptance. Wrong 2D-focus extent remains a separate observation, not established causality for the frustum exception.
- Expanded run `8d4b7d52fe7246aa8fdbc881e978896e`: FAILED in the harness. Its role selector excluded deliberately hidden viewer buttons, reaching the 120-second test timeout. The implementation agent manually stopped the exact owned Node/browser tree to avoid repeated hangs, interrupting graceful browser teardown. Northern samples contain no render errors, but native-picker2D was still MORPHING at the fixed wait. The additional geometry-route pattern was also incorrect. **Do not claim southern/origin/hidden coverage passed.** Revised harness NOT RUN.

The expanded run has no active recorded client identity or owned Docker resource. Exact cleanup is BLOCKED by WinError5 at `playwright-temp/playwright_chromiumdev_profile-4yzNak/Default/AutofillAiModelCache/LOCK`. Its private root is:

`C:\Users\Owner\AppData\Local\Temp\agrosphere-poc-close-8d4b7d52fe7246aa8fdbc881e978896e-ba5c8op7`

The owner said, “I will have to restart the system. I wil do that later.” No further fixture was started. Computer-use native pipe was unavailable after retries/reset; no UI action occurred. No automatic approval-review rejection occurred.

## Source changes and investigation

Owner clarification: the error appears on opening Digital Twin, after choosing2D/3D. Root cause/fix remains UNRESOLVED; no speculative camera/morph correction was made.

- Web `src/app/features/digital-twin/cesium-viewer.service.ts`: read-only camera/frustum, mode/morph, canvas/container dimensions and bounded render errors behind the existing explicit loopback verification-run gate. Destroy removes both listeners and the probe. Normal camera behavior is unchanged.
- Web `e2e/digital-twin-rendering.spec.ts`: bounded hardware reproduction scaffold. Revised hidden-role selectors, actual estate-feature route and completed-mode polling; added opening-time toggles and layout restoration on failure. Current expanded version NOT RUN.
- Web `playwright.config.ts`: installed Edge hardware reproduction project, tracing off.

Review is sequential implementation-agent self-review, not independent review. Executed source hashes remain in each run's owner manifest. [Current evidence](POC_CLOSE_RENDERING_PROGRESS_2026_11_13.json) records current unrun source identities. The ignored orchestration is Infrastructure `target/twin-rendering/run.py`; public run reports are under `target/poc-close/<runId>/`. Private raw logs await exact cleanup. Original reviewed packages and configuration remain unchanged.

## Actual independent checks

Web lint, formatting, typecheck, API generation comparison and diff checks PASS. All112 unit tests and production build PASS, repeated successfully after dependency restoration. Existing Cesium CommonJS warnings remain. Broad UI/graphics suites, Docker Web packaging, corrected connected capture and remaining native/performance/numerical/security criteria are NOT RUN in this increment.

`npm ci --ignore-scripts --no-audit --no-fund` FAILED with EPERM because a separately active owner `ng serve` compiler held esbuild. No owner server was stopped. `npm install --ignore-scripts --no-audit --no-fund` restored dependencies (exit0). Parsed lockfile identities were unchanged; newline normalization was reverted to the exact original bytes/hash. No dependency version changed. Four ignored stale native-binary directories under `node_modules/@esbuild`, `@msgpackr-extract`, `@lmdb` and `@rollup` remain held until restart; clean locked restoration remains pending. Do not claim npm ci PASS.

Twelve roots retain HEADs and empty cached diffs against HEAD. Eleven raw index hashes match prior evidence. Web's raw index hash differs after restored-lockfile timestamps/ordinary status refresh; a stat-cache explanation is plausible, not independently proven. No staged-content change, index restoration, staging, commit, reset or push occurred. AEO was untouched.

## Resume after restart

1. Check actual time and public manifests. Verify/delete only the marked/inventoried run8d4b7d52fe7246aa8fdbc881e978896e private root, then run Infrastructure `python scripts/verify_poc_close.py --recover target/poc-close/8d4b7d52fe7246aa8fdbc881e978896e/owner.json`. Require cleanup PASS, private absence and empty resource inventories. Preserve failures; do not extend/reuse leases, endpoints or profiles.
2. With the owner development server stopped, run Web `npm.cmd ci` at unchanged versions and required checks. Do not stop an owner server without authorization. Verify package/config/index preservation.
3. Review the current test and ignored wrapper. Increase its current180-second bound to cover three60-second tests plus graceful teardown before execution. Let bounded selector failures finish naturally; do not manually terminate early again. Record source identities; run browser suites sequentially in a fresh owned generated fixture.
4. Reproduce opening-time mode changes and the actual invalid state, implement only the demonstrated correction and add focused regression. Finish the requested frame/picking/overlay/console/render-event, both-control, geometry/load/selection/size/hidden and route matrix. Current scaffold remains incomplete acceptance coverage.
5. Resume the approved connected and native workflows, request-start-proven races, actual renderer ECEF comparisons and unchanged1920×1080/performance protocols. Complete all-copy cleanup and concrete owner package before requesting functional acceptance. Physical VR/French remain deferred, OpenXR disabled, bounded M4 accepted, Android/offline subsequent and AEO untouched.

Final documentation verification: Architecture `python scripts/validate.py --workspace C:\Projects\agrosphere` PASS (layout/16 ADRs/YAML, twelve independent roots, ignore/secret-pattern checks); Web and Architecture diff checks PASS, final Web format check PASS. These do not establish rendered acceptance or pending private-copy removal.

## Later Columbus-focus correction - 2026-11-13

The owner reported that Columbus view does not focus the selected field and displays imagery fallback with four spatial features. [Exact correction evidence](POC_CLOSE_COLUMBUS_FOCUS_2026_11_13.json) supersedes the earlier no-product-fix statement **for this focus defect only**. The original frustum error remains UNRESOLVED.

Installed Cesium returns projected map positions from getRectangleCameraCoordinates in Columbus/2D. The service incorrectly treated them as ECEF and reconverted them. Two regressions using the actual installed CPU camera/projection failed against that code and pass after preserving projected coordinates with convert:false. Original3D ECEF/terrain clearance remains. Scene morph-start cancels the prior flight; morph-complete refocuses the latest selected canonical field, otherwise reset/estate. Lifecycle listeners are removed on destroy.

New Web service unit file adds3 regressions, including latest-selection focus and listener teardown with actual Cesium events. Full115-test suite, lint/type/format/API/build/diff checks PASS. The initial test typing and global-module-mock hoisting failures are retained in JSON; final tests use no global Cesium mock. Browser scaffold adds native Columbus mode and expected focus-centre polling, but NOT RUN after the change. No new runtime was started because the private-profile cleanup/restart blocker persists. README/CHANGELOG explain the scoped correction and its browser-validation limit; no version/config/provider/contract changes.

The imagery status is emitted when the configured imagery provider reports an error and imagery layers are removed. No provider failure reason is established here, and four spatial features counts loaded records, not selected-field visibility or four block polygons. No imagery source was changed or provider request made by this increment.

After the already-recorded restart/cleanup/dependency steps, verify the corrected Columbus/2D focus, normal3D, both mode controls, initial-load transitions, picking/overlays/route teardown and original invalid-frustum reproduction in actual WebGL. POC-CLOSE remains PARTIAL and final acceptance OPEN.

## Owner-reported mode-view regression and replacement - 2026-11-13

The owner reported that the preceding focus correction made3D and Columbus appear2D and worsened previously available free globe navigation. This supersedes any implication that prior unit success established rendered correctness. [Exact replacement evidence](POC_CLOSE_MODE_VIEW_CORRECTION_2026_11_13.json) retains the prior source identity and owner rejection.

The prior morphComplete handler unconditionally focused selected-field/estate bounds using a straight-down pitch in every mode. That replaced native mode views with a close overhead view. The earlier coordinate assertions did not check orientation or unsolicited flights. This was an implementation mistake; no acceptance of that behavior is inferred.

The replacement removes unconditional transition refocus. Mode changes preserve Cesium's native3D/Columbus pose. Only a focus request received during MORPHING is queued and replayed, latest request wins; geometry generation changes and destroy clear it. Columbus field focus uses an oblique45-degree camera offset south of the field, aimed north/down at its centre.2D remains overhead. Existing3D explicit-focus/ECEF behavior and the projected-coordinate correction remain.

Focused tests use the actual installed CPU camera to check Columbus pitch and ground-ray intersection,2D overhead projection, latest queued focus, no automatic flight/native3D pose-frustum preservation and listener removal. Final115unit/lint/type/format/build/diff PASS. The gated browser probe/scaffold now checks actual ground-centre and pitch; browser NOT RUN because the same protected test-profile/restart cleanup remains pending. No new fixture/provider/config/dependency/Git/AEO action. The original invalid-frustum error and remaining rendered acceptance remain OPEN.

On resume, verify visually that switching modes alone does not zoom back into the field,3D orbit/zoom remains usable, explicit Columbus field focus is oblique and centred,2D remains overhead, and queued focus during initial transitions uses current geometry. Do not treat these CPU checks as rendered proof. All earlier exact cleanup/dependency/restart requirements remain.
