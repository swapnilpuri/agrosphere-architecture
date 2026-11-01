# Alerts/privacy operating evidence and recovery handoff

Date: 2026-11-01 (America/Chicago). Status: **PLANNING ONLY; OR01–06 OPEN**.

This companion makes the [readiness review](ALERTS_PRIVACY_OPERATING_READINESS.md) and [generated maintenance package](ALERTS_PRIVACY_MAINTENANCE_PACKAGE.md) actionable without inspecting or changing an existing target. It neither supersedes the approved conditional stack plan nor authorizes AP-T08. PM04 has generated-fixture policy evidence; PM01/02 SQL and privilege review, PM03 runner, PM05 database integration and live monitoring remain open. No deployed control is inferred from a document or a passing fixture.

All client questions and provisional choices are maintained only in the [single client decision register](ALERTS_NOTIFICATIONS_CLIENT_DECISIONS.md), including OP01–04 for this handoff. Named operators, providers, locations, schedules and evidence destinations remain unassigned. No client answer or legal conclusion is inferred.

## Evidence record to complete after scoped authorization

Create a separate dated record for each generated drill or later authorized environment review. Keep generated evidence separate from selected-environment evidence. The fields below are an unpopulated record definition, not a claim that inspection occurred.

| Field | Required content / initial value |
|---|---|
| Scope and authority | Record ID, generated drill or selected environment, owner/date/exact authorized actions; selected environment: NOT AUTHORIZED / NOT INSPECTED |
| Identity | Explicit target alias, independently verified project/database/schema identity, UTC start/end; target fingerprint alone is not authentication |
| Artifacts | Independent HEADs and dirty-source hashes, policy revision, runner/observer/watchdog hashes, exact migration chain and effective privilege review |
| Responsible functions | Operator, responder, recovery owner, reviewer, escalation destination and access-controlled evidence destination: UNASSIGNED |
| Collection | Collector identity/version, source, observation time, collection time, UTC clock/skew validation and integrity check; UNKNOWN if provenance cannot be verified |
| Scenario and expected result | OR/PM-AC IDs, fixed input boundaries or actual generated load, expected component states and denial/preservation assertions |
| Actual result | PASS / FAIL / UNKNOWN / NOT RUN, exit status, duration, measured removal delay, counts and separately protected evidence reference |
| Copies and recovery | Copy inventory references, expiry evidence, current-ledger checkpoint and reconciliation evidence; UNKNOWN until independently verified |
| Preservation | Before/after source/index/config fingerprints, immutable artifacts, stable estate/block and geometry checks; no sensitive bodies in this repository |
| Review | Reviewer/date, accepted scope, unresolved failures and next action; no automatic gate closure from process exit or template completion |

Keep identity-bearing ledger contents, raw logs, credentials, command bodies and private target details out of tracked evidence. Aggregates still require restricted handling. Hashes demonstrate byte identity, not authorization, authenticity, completeness or actual expiry.

## Minimum gate evidence and rejection rules

| Gate | Evidence bundle required | Reject closure when |
|---|---|---|
| OR01 authority | Exact owner/search path/object definitions; effective PUBLIC/inherited/role privileges; intended calls succeed and runtime/monitor/cleanup denials match PM-AC01 | A broad table/DDL privilege is used, identity data reaches telemetry, or exact SQL/privileges are not reviewed |
| OR02 unattended cleanup | Independent scheduling/collection evidence; all PM-AC02–08 outcomes; locked-root and ledger-only observations; capacity and deadline-to-removal measurements | Zero processed roots substitutes for observation, unknown eligibility age is treated as zero, or fixture results substitute for an installed collector |
| OR03 log expiry | One row per application/access/security sink, driver, spool, index, archive and export; creation-time expiry and outage/replay boundary evidence | A dependent copy is missing, replay resets the retention clock, or configured retention substitutes for verified deletion lag |
| OR04 recovery | Full/incremental/snapshot/replica/export dependency inventory; oldest recoverable-data bound; independent current-ledger protocol and isolated restore PM-AC09 | Ledger is only from the restored backup, freshness/completeness is unknown, or a backup chain can recover older data beyond the provisional bound |
| OR05 subject/deployment | Register answers needed for the environment; accountable contact/basis/location facts; reviewed English/French notice and verified request-channel procedure | Invented facts, untranslated outline or generated-account tests substitute for client/reviewer evidence |
| OR06 preflight | Separate exact inspection authority, target manifest, preservation baseline, tested protected backup, stop/rollback review and fresh artifact comparison | Inspection is treated as upgrade authorization, V6 is nonempty without reviewed conversion, or target/config/data preservation cannot be proved |

Use a separate copy-inventory row for each actual copy with: copy alias/class, accountable function, parent/dependent copies, location/transfer, creation clock, retention origin/duration, deletion mechanism, access boundary, last verified expiry/lag, oldest recoverable-data time and evidence reference. Until authorized collection, every actual-copy field remains NOT INSPECTED; an empty inventory is not evidence of no copies. Accepted provisional durations remain in PR09/10; this handoff adds none.

## Local response procedure for future drills

These steps define expected drill behavior. They install no scheduler, create no responder or send any message. Any selected-environment intervention needs its own authority.

| Result | Required response and evidence |
|---|---|
| HEALTHY | Retain component states and fresh trusted observation. Record eligible work that is still within budget; HEALTHY does not mean every copy was removed or a gate is closed. |
| WARNING | Examine missed-run versus backlog/removal components; record deadline margin and lock/capacity/outage cause. Use only bounded eligible cleanup under the existing reviewed privilege boundary. |
| ERROR | Preserve the failed-run outcome even if backlog is empty. Establish which batches committed and obtain a fresh independent observation before claiming recovery. |
| UNKNOWN | Restore trusted collection/clock/target evidence first. Do not infer an empty backlog or retry against an unverified target. An ambiguous commit requires re-observation, not fabricated success. |
| BREACH | Record original deadline, actual delay, affected copy classes and remaining work. Recover through reviewed maintenance; preserve the breach history after recovery. No deadline reset, grant expansion or claim of on-time deletion. |

Retain the evaluator's priority BREACH > UNKNOWN > ERROR > WARNING > HEALTHY and each component result; one component must not hide another. Existing warning/breach boundaries are unchanged. No human response-time promise is added. If suppression/access correctness is uncertain, the future authorized operator must isolate alert access while investigating; this document does not change a running feature flag.

Recovery evidence must include a fresh observation, the final job outcome and scheduler/collection recovery, remaining eligible classes and the measured late-removal interval. A healthy sample cannot erase an earlier breach or prove scheduler reliability. Record repeat samples spanning the failure/recovery scenario; production acceptance duration remains to be selected with the operator.

## Independent current-ledger protocol to design and test

This is a requirement for later implementation review, not an implemented synchronization service or a public contract. Preserve the accepted removal semantics and 66-day post-completion bound.

1. Assign a protected ledger authority independent of the backup being restored. Define authenticated access, writer/reconciler separation, destination ownership and retention. Actual storage/provider/credentials remain undecided. A digest or target alias alone is insufficient proof of a trusted ledger.
2. Require a complete ordered checkpoint: source identity, lineage/epoch, monotonically increasing committed sequence, original request/cutoff/completion/expiry metadata and an integrity-protected snapshot bound to that sequence. Detect gaps, rollback and conflicting lineage. A recently written empty file or a recent timestamp alone does not prove current or complete.
3. Review atomic publication and failure ordering. No verified-removal request may be reported safely recoverable until its durable independent representation is confirmed. A crash between database and independent-store commits needs explicit retry/deduplication/reconciliation evidence; a backup plus a best-effort export is insufficient. No distributed transaction or new API is presumed delivered.
4. Isolate a new restore destination with alert readers/writers disabled. Verify backup identity, dependency chain, original deadlines and a trusted complete current checkpoint. Reconcile all applicable requests through a defined high-water sequence, apply eligible cleanup and test old keys/read/history plus first-ack/version continuity. Keep identity-bearing comparison data inside the owned restricted fixture.
5. Close the restore race explicitly: before enabling access, obtain a final consistent checkpoint and prove there were no unreconciled requests during restore/reconciliation. Use a reviewed barrier or equivalent protocol and test a request arriving during reconciliation. A one-time snapshot at restore start cannot establish this property. Access remains blocked if the barrier/provenance/completeness check fails.
6. Test unavailable/stale ledger, skipped sequence, rolled-back checkpoint, conflicting source/epoch, interrupted publication and late removal requests. Capture denial and retry/recovery results without logging subject identities. PM-AC09 generated evidence does not certify a selected external store.
7. Before discarding suppression metadata, prove backup/key bounds and copy provenance still justify expiry. Unknown provenance or an over-retained copy requires isolation and a concrete exception review. Do not silently extend retention, discard suppression early or change V7 to satisfy this plan.

No arbitrary numeric ledger-freshness limit is selected here. The watchdog's 300-second observer freshness applies to aggregate monitoring, not independent-ledger completeness or permission to restore. Exact synchronization acknowledgement, checkpoint/barrier semantics and failure behavior must be reviewed before ledger integration.

## Next eligible engineering and acceptance sequence

Continue PM01/02 by reviewing the exact Operations-owned observer SQL, owner/search path and effective privileges before applying any additive migration even to a generated fixture. Check every V7 eligibility branch and whether original eligibility times are derivable; unresolved ages stay UNKNOWN. Then implement PM03 and real PM05 failure/recovery integration under applicable repository guidance. Keep the tested PM04 evaluator contract intact or explicitly review any change.

Generated maintenance completion can contribute to OR01/02/04 only. Actual unattended jobs, log/backup providers, trusted ledger service and selected-environment preflight need their own evidence. OR01–06, AP-T08, actual-subject/REAL, owner functional, WA/II/M2 and offline/French/five-second gates remain open independently. The reference-device question already recorded in the register is not repeated. No upgrade, existing-stack inspection, private configuration read, grant/credential change, account activation, external delivery, Git publication or AEO action is performed.
