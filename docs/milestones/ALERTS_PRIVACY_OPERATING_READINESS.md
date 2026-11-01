# Alerts/privacy operating-readiness review

Date: 2026-10-31 (America/Chicago). Status: **PLANNING COMPLETE; OPERATING GATES OPEN; EXISTING-STACK EXECUTION NOT AUTHORIZED**.

This companion updates the current-state interpretation of the immutable [conditional stack plan](ALERTS_PRIVACY_LOCAL_STACK_PLAN.md). Its opening unimplemented labels are historical: exact Contracts 0.9.0 release/pins and generated runtime checks are recorded in [approval](ALERTS_PRIVACY_APPROVAL.md) and [verification](ALERTS_PRIVACY_VERIFICATION.md). Preserve that plan's approved bytes. Neither document authorizes an upgrade, inspection of private configuration or existing databases, a maintenance grant, or activation for existing accounts.

This increment changes Architecture documentation only. Existing-account/REAL enablement remains disabled. All client questions and provisional retention choices remain in the single [client register](ALERTS_NOTIFICATIONS_CLIENT_DECISIONS.md), `AN_PRIVACY_PROVISIONAL_1`; no client answer, hosting fact, legal basis or compliance conclusion is supplied here. II-1 remains complete; WA/II/M2, offline/French/five-second and owner functional gates stay independent.

## Current evidence and gaps

The [Operations guide](../../../agrosphere-operations-service/docs/ALERTS_PRIVACY_IMPLEMENTATION.md), V7 migration and runtime verification establish local generated enforcement, restricted maintenance functions and isolated restore tests. Prior test counts are historical evidence, not rerun results for this planning increment. They do not establish an unattended scheduler, selected provider retention settings or a current external ledger service.

| Gate | Accountable function to assign | Required evidence before closure | Current disposition |
|---|---|---|---|
| OR01 maintenance authority | Operations/security owner | Exact database/schema/function owner, restricted job principal, approved privilege diff, secret reference/access/rotation process; runtime denial and job authorization checks in generated isolation | OPEN; no principal/grant/credential provisioned |
| OR02 cleanup and overdue response | Service operator plus responder | Reviewed job/monitor artifacts; success, missed-run, lock contention, partial batch, capacity and outage-recovery drill; measured deadline-to-removal delay | OPEN; routine tested, job/monitor absent |
| OR03 logs | Logging/security owner | Every sink/agent/export and actual 14-day ordinary/90-day security expiry configuration; minimization and expiry tests including collector outage/replay | OPEN; no selected-environment inventory |
| OR04 backups/current ledger | Recovery owner | Full copy/dependency inventory, 35-day recoverability limit, independently current protected removal ledger, freshness checks and isolated restore drill | OPEN; generated database restore evidence only |
| OR05 subject/deployment policy | Client/controller and reviewer | PR01–17 answers where needed, accountable contact, applicable basis, locations/transfers, English/French notices and verified request channel | OPEN; facts remain unknown |
| OR06 existing-stack preflight | Owner plus release operator | Exact authorized inspection scope, target manifest, protected tested backup, migration/image/source fingerprints, preservation comparison and stop/rollback review | OPEN; no existing targets inspected or upgrade executed |

Named people, selected providers, alert destinations and operational evidence locations must be supplied for the chosen environment. Functional labels above assign responsibility to resolve; they are not assertions that an operator exists. AP-T07 remains locally evidenced with external operating gaps; AP-T08 execution and AN-D07 actual-subject acceptance remain open.

## Proposed protected job and monitoring contract

The following is a reviewable engineering recommendation, not an installed configuration or change to the accepted retention policy.

1. Run a separate non-HTTP maintenance process against one explicitly selected Operations database/schema. Recommend an hourly trigger with bounded retries to leave recovery margin inside PR11's 24-hour healthy physical-deletion objective. A once-daily trigger alone leaves no failure margin. Proposed warning thresholds are 12 hours of eligible-work age or two missed hourly runs; breach at 24 hours. Select/approve the actual schedule and routing with the operator.
2. Request only the exact schema access and `EXECUTE` needed for `privacy_cleanup(integer)`; do not reuse the application login or grant owner/superuser, broad table DELETE, DDL or schema CREATE. `privacy_request_removal(text,text)` is a distinct authority for a verified operator workflow, never a scheduler capability by default. V7 revokes PUBLIC function execution. Prove the final effective grants and SECURITY DEFINER owner/search-path safety in a generated target before proposing existing-role changes.
3. Start with the function's maximum 200 roots per call, commit between calls and enforce reviewed statement/lock/run budgets. Size those budgets from generated workload measurements; this review invents no throughput. The return value counts processed roots, not rows removed. Child rows per root and the ledger update/delete are not bounded by that root limit, so capacity/transaction-duration tests must cover large roots and removal backlogs.
4. Repeat within the run budget and defer remaining work to the next scheduled attempt. `FOR UPDATE SKIP LOCKED` can return zero while eligible locked work remains. A full batch does not establish how much remains, and a zero count is not a completion certificate. Use a separately reviewed read-only aggregate observer matching all V7 eligibility branches, including watermarks after reopening, receipt expiry, pending removal and ledger expiry. No observer/query/grant is implemented by this plan.
5. Record database UTC time, target alias, policy/artifact revision, run ID, start/end/outcome, batch/root counts, oldest eligible deadline, pending verified-removal age, last verified successful cleanup and observer freshness. Use aggregates; no issuer/subject, command IDs, row bodies, tokens or raw SQL parameters in telemetry. An unknown/stale observation is UNKNOWN, never zero backlog. Job success and verified absence of overdue work are separate signals.
6. Monitor outside the job itself so scheduler failure is observable. Retry transient failures within the remaining deadline budget; notify the assigned responder through a separately configured/authorized channel. Missing authority, wrong target/schema, unexpected migration checksum or expiry disclosure stops the job and keeps rollout blocked. No external message is sent by this review.
7. On overdue work, record actual delay and affected copy classes, preserve evidence, investigate lock/capacity/failure causes and recover through eligible bounded maintenance only after authorization. Do not move deadlines, disable evidence guards, expand grants or claim on-time deletion after a breach. Logical expiry remains enforced independently; it does not prove physical erasure. If suppression/access correctness is uncertain, disable/isolate alert access pending review.

Generated acceptance scenarios: before/at/after deadline; missed triggers then recovery; job killed between committed batches; locked eligible root with zero returned; large child-row/root backlog; observer unavailable; wrong target; runtime denied maintenance; cleanup principal denied request-removal; concurrent read/ack/reopen/removal; and minimal operational root/history continuity. Measure real removal delay and unchanged source/legacy data, not merely process exit status. Implementation of the job, observer or authority needs its own applicable repository guidance and scoped authorization.

## Logs, copies and recovery evidence

Use one inventory row per actual application/access log, identity/security log, container log driver, agent spool, collector/index/archive, full/incremental backup chain, snapshot, replica and exported/support copy. Capture owner, purpose/class, location/transfers, creation clock, dependent copies, access, deletion mechanism, configured duration, last verified expiry and evidence reference. Leave unknown fields unknown. Existing-stack inspection and any sample access require separate authorization; do not collect raw personal log contents into this repository.

PR09/10's 14/90/35 days are provisional limits, not legal minimums. Verify expiration at the boundary plus actual provider deletion lag. Rolling incrementals, replication, exports, failed jobs and keep-last settings must not retain a recoverable older personal copy indefinitely. Distinguish archive expiry from the age of the oldest recoverable data. Any unavoidable chain extension is a review failure/exception to resolve, not an implicit extension. Confirm ordinary logs omit identities, headers/tokens, read/ack details and identifying URL parameters; restrict/minimize exceptional security fields. Exercise offline collector spool/replay so forwarding does not restart retention clocks.

Keep the current removal ledger protected and independently recoverable through the backup/key recovery window. It contains personal identity metadata and needs restricted access and bounded expiry too. Define synchronization, atomic version/checkpoint, freshness observation, backup independence and failure recovery before use. A stale export or the old ledger bundled inside a backup is insufficient. The accepted 66-day post-completion ledger bound assumes the 35-day backup and 30-day key bounds were enforced; unknown copy provenance or a retention breach prevents relying on that arithmetic. Do not silently extend ledger retention or drop suppression early; isolate recovery and obtain a concrete exception/change review.

Restore acceptance requires an isolated destination with alert access/writers disabled, original UTC deadlines, verified current ledger reconciliation, eligible cleanup and tests that old keys/read state/history cannot reappear. Record backup provenance and timestamps, ledger checkpoint/freshness and reconciliation result, cleanup/expiry outcomes, access-denial evidence and destruction of the separately owned test resources. Fail closed if the ledger is unavailable or cannot be proven current. Never restore over existing data automatically. Normal all-copy lag may reach deadline + 24 hours + 35 days; failures can extend it and must be reported as actual delay.

## Notice and client fact handoff

Resolve PR16/17 in the existing register: accountable organization/contact, applicable basis, user countries, exact hosting/support/log/backup locations and transfers, request verification channel, exceptions and reviewers. Prepare English and French notices for review explaining explicit own-read actions, shared acknowledgement/history and permitted viewers, purposes, active/inactive retention clocks, receipt/key expiry, backup delay, removal scope and request handling. Distinguish alert copies from source incident/inspection/workforce retention. Translation/delivery/reviewer evidence is required; an outline does not deliver French readiness. Do not invent a consent choice or statutory obligation. No legal research or legal determination is part of this technical planning pass.

## Exact preservation-focused preflight handoff

The original plan remains the sequence/rollback authority for preparation. Use these additional fields to make a later execution proposal concrete. Every active-target field is currently **NOT INSPECTED / NOT AUTHORIZED**.

| Manifest group | Exact evidence required |
|---|---|
| Authorization | Owner/date/action scope; distinguish read-only inspection, backup/isolated restore, image build, service replacement, V7 migration, maintenance grant and any demo writes; identify excluded actions |
| Target | Compose project and source file identities, exact service/container IDs, database/schema and mapped named volume IDs; no ambient defaults or wildcard selection |
| Artifacts | Independent HEAD and dirty-source fingerprints, exact contract pins/accepted hashes, image IDs/digests and build inputs; freshness recheck immediately before execution |
| Migration/data | Flyway applied versions/checksums; local raw V1–V7 hashes plus tool-recorded migration checksums (different algorithms); non-sensitive counts/stable content and geometry fingerprints; every V6 alert table checked |
| Preservation | Web config working bytes and staged entry; all six repo staged inventories/indexes and prior changed/untracked source fingerprints; private config preserved in place without publishing values; estate/block IDs, fields, volumes and geometry retained |
| Recovery | Protected destination/access/encryption, archive checksum/size/inventory, isolated restore evidence, independently current removal ledger, recovery owner and downtime/stop criteria |
| Execution result | Before/after target, schema, health, scope denial, config/data/geometry comparison; alerts remain disabled unless a separate explicit account/mode decision permits enablement |

Any nonempty V6 alert table means STOP and a separate preservation-focused conversion review; no erase, hide, reseed or automatic historical conversion. Empty V6 does not authorize actual-account use through generated flags. Do not repeat completed II-1 provisioning, restart unrelated services, reset volumes, backfill alerts or fast-forward the active clock. Disable-and-isolate rollback retains additive schema/evidence and prevents old images/routes exposing expired copies; database restore remains a separate recovery decision.

## Safe continuation and review outcome

Planning is ready for review; all OR01–06 remain OPEN. Next eligible work is preparation of a generated-only job/observer and recovery-control implementation proposal, with exact artifacts and scoped authority; keep client answers in the existing register. Actual selected-environment evidence and separately authorized exact preflight must precede an upgrade proposal. Owner functional acceptance follows separately governed connected SIMULATED behavior. No repeat acceptance of Contracts 0.9.0 or the approved runtime package is needed.

Planning validation and source/index preservation observations are recorded in [increment evidence](ALERTS_PRIVACY_OPERATING_READINESS_EVIDENCE.json). This document does not execute any job, query an existing database, read private configuration, change roles/credentials, create demo records, send notifications, deploy, publish, commit, or touch AEO.


## Evidence and recovery handoff refinement — 2026-11-01

The [operating handoff](ALERTS_PRIVACY_OPERATING_HANDOFF.md) now specifies unpopulated evidence fields, per-copy inventory requirements, OR closure rejection rules, component-aware failure/recovery handling and a current-ledger checkpoint/final-barrier protocol for later implementation review. Provisional choices OP01–04 are recorded only in the existing client register. The fixture-tested PM04 evaluator does not provide live collection, ledger synchronization or unattended cleanup. No gate closes and no existing target is inspected or upgraded. Continue exact PM01/02 SQL/privilege review before generated fixture application, followed by PM03/PM05 integration.
