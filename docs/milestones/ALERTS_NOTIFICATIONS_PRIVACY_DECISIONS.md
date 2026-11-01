# AN-D07 privacy decisions

Status: PARTIAL — access arrangement, explicit personal read tracking and P04a read-marker retention confirmed; remaining privacy decisions OPEN. Decisions are being collected step by step through the owner conversation. This record does not enable alerts or authorise non-generated account rollout, REAL data or an existing-stack upgrade.

## P01 — Access arrangement confirmed, 2026-10-31

Reviewer: project owner. Exact response to the role-access table:

> Keep the approved access arrangement

Retain the positive role matrix in the [approved AN-1 package](ALERTS_NOTIFICATIONS_REVIEW.md), SHA-256 `22d8c98ede00c4e912f98922f944417aca54bc585a48efe7beb74f59d1364251`:

| Role | Permitted capability, subject to the remaining policy/rollout gates |
|---|---|
| Estate-scoped ESTATE_ADMIN / ESTATE_MANAGER | View alerts, mark own read state, acknowledge for the estate team, view protected history |
| Estate-scoped FIELD_SUPERVISOR | View alerts and mark own read state; no shared acknowledgement or protected history |
| Estate-scoped AUDITOR | View alerts, mark own read state and view protected history; no shared acknowledgement |
| PLATFORM_ADMIN | Same alert capabilities as managers; explicit estate selection for lists/counts, no automatic all-estate subscription |
| Other roles alone | No alert access; an additional explicitly permitted role can grant its stated capability within estate scope |

Signed subject/issuer and existing trusted estate scope remain authoritative. No account, role, credential, recipient directory or worker/account linkage is added. There is no endpoint to inspect other users' read markers, choose recipients or edit the rule. Ordinary views omit acknowledgement actor identity; protected acknowledgement history remains available only to managers/admins/auditors with the applicable scope.

P01 confirms who may exercise each capability when the policy and rollout gates are satisfied. P01 alone does not decide collection of personal read receipts or any retention/deletion period; the later P02 decision below addresses collection. Existing approved design/executable bytes remain unchanged.

## P02 — Explicit personal read tracking allowed, 2026-10-31

Reviewer: project owner. Exact response:

> Allow personal read tracking

The owner permits the explicit Mark read receipt described in the preceding conversation: trusted issuer/account subject, alert/attention episode and server read time, supporting that user's persistent personal unread state. Opening or fetching an alert alone does not record a read. Other users cannot inspect the individual's read markers through the application. Shared manager acknowledgement remains a separate action and protected evidence record under P01.

This records the collection decision within that stated scope. It does not authorise staff attendance/performance monitoring, additional tracking, other channels, a retention/deletion duration, legal/policy compliance claims or non-generated account activation. Purpose/policy context, how actual users are informed, retention/deletion and implementation review remain open. No runtime switch or configuration is changed by this record.

## P03 — Initial locations supplied, 2026-10-31

Reviewer/source: project owner. Exact response:

> The initial users will be in Gabon. Agrosphere data will be hosted in appropriate cloud region . May be in South Aftrica or India.

Confirmed planning input: initial users will be located in **Gabon**. Intended hosting is a suitable cloud region; **South Africa or India are tentative candidates only** (normalised spelling of South Africa). No cloud provider, exact region, final hosting country, data residency arrangement, backup/log/identity/support-access locations or deployment has been selected or authorised. This statement supplies initial user geography, not actual estate identity, plantation facts, REAL-data onboarding or cloud provisioning approval.

P03 remains PARTIAL/OPEN: final hosting/data-flow locations, remaining purpose/policy context and how actual users are informed still need review. No jurisdictional applicability, cross-border transfer permission or compliance conclusion is inferred. Region/provider comparison is future planning, not a decision made by this record. Retention/deletion and AN-D07 completion remain open.

## P04a — Personal read-marker retention proposal, 2026-10-31

Status: PROPOSED FOR OWNER REVIEW, not accepted or implemented. The owner requested help choosing a retention period; this is no deletion, migration, rollout or runtime authorisation.

Recommended product-policy starting point:

- Retain the latest personal read marker while its alert is ACTIVE, supporting the user's unread state.
- Target expiry 30 days after the alert becomes INACTIVE (resolved, voided or below the approved alert threshold). The clock starts at the transition to INACTIVE, not at the first read or an unrelated later edit.
- If the alert reactivates before expiry, cancel the pending inactive-period expiry; its next transition to INACTIVE starts a new 30-day period. Existing attention rules still make a new episode unread.
- At expiry, delete the personal marker rather than keeping an identifiable read-history archive. The operational rationale is a short post-closure/support window; this marker is not the manager acknowledgement or evidence that follow-up was completed.

Thirty days is an engineering/product recommendation, not a statutory duration or compliance determination. Article 70 of the law published on [Gabon APDPVP's official site](https://www.apdpvp.ga/textes-et-decisions/) states the purpose/necessity-based retention principle. It does not establish this proposed 30-day number. Source inspected 2026-10-31. Applicable obligations still require review before non-generated rollout.

This proposal covers the personal read-marker rows only. Shared acknowledgements, command receipts (which may include related identity/read-response information), audit evidence, logs and backups have separate pending retention/deletion decisions. No claim is made that deleting a marker removes all related data from every store. Deletion execution timing, reads of old inactive alerts after expiry, account removal and restore/replay handling must be reconciled during the policy implementation review. No existing data is purged.

P04 remains OPEN; await the owner's acceptance/revision of this proposal, then collect the other data categories' rules. AN-D07 and rollout remain open overall.

## P04a — Owner acceptance, 2026-10-31

Reviewer: project owner. Exact response to the proposed rule:

> Approve 30 days after an alert becomes inactive.

This accepts the personal read-marker rule in the preceding P04a proposal (section SHA-256 `28b241c535865ee7f890fe899e930c2d8769f189f1cd04d8212da6495cd0793a`). Preserve the original proposal as historical review evidence; its pending labels are superseded for this parameter only.

Accepted scope: retain the latest personal read marker while the alert is ACTIVE, then expire/delete that marker 30 days after the alert transitions to INACTIVE (resolved, voided or below the approved threshold). An unrelated inactive-state edit does not restart the clock. Reactivation before expiry cancels that deadline; its next INACTIVE transition starts a fresh 30-day period. Existing attention rules still make a new episode unread. No identifiable read-history archive is authorised after marker expiry.

This records an approved policy parameter, not an implemented deletion mechanism or a legal-compliance conclusion. It supplies no retention period for shared acknowledgements, command receipts, audit evidence, logs or backups. Related personal information in those stores must be addressed separately. Deletion execution timing, inactive-alert reads after expiry, account removal and restore/replay interactions remain to be reviewed in P05 before implementation/activation. No existing data is deleted, no running stack/configuration/role/credential is changed, and alerts remain disabled for existing accounts. AN-D07 remains OPEN overall.

## Decision status

| Item | State / input still required |
|---|---|
| P02 Personal read tracking | CONFIRMED for explicit Mark read receipts and personal unread state, as recorded above. No implicit view tracking or access to others' read markers. Remaining purpose/context/retention/rollout gates still apply. |
| P03 Purpose and account-subject policy context | PARTIAL: initial users in Gabon confirmed; South Africa/India tentative hosting candidates, provider/exact region/final data-flow locations undecided. Remaining purpose/policy context and user information are OPEN; no policy, legal basis or transfer permission inferred. |
| P04 Retention/deletion | PARTIAL: P04a accepted for latest read marker while ACTIVE plus 30 days after transition to INACTIVE, with the stated reactivation rule. Acknowledgements/receipts/audit/logs/backups, execution timing and copy/restore/replay handling remain undecided. No purge performed or live deletion enabled. |
| P05 Completed policy review and implementation | OPEN: consolidate actual decisions, review remaining gaps and implement/test the agreed policy before any non-generated account rollout. |

AN-D07 remains OPEN overall. AN-D08, WA D08/D09, II-D07/08, REAL, M2, owner functional acceptance and separately authorised rollout remain independent gates. Alerts remain disabled for existing accounts. This increment records documentation only; no code/contracts/configuration/data/index/stack/AEO change or external notification is authorised or performed.

## Documentation checks

2026-10-31: Architecture `python scripts/validate.py --workspace C:\Projects\agrosphere` and `git diff --check` PASS. Architecture HEAD/index match the fresh baseline, the entire prior checkpoint remains a verbatim suffix, and the relative review-package link resolves. No application tests were run for this documentation-only decision record.

P02 recording, 2026-10-31: Architecture workspace validator and `git diff --check` PASS; HEAD/index remain identical to the fresh baseline, and the entire prior checkpoint is retained verbatim. No application tests or runtime changes for this documentation-only update.

P03 location recording, 2026-10-31: Architecture workspace validator and `git diff --check` PASS; HEAD/index and prior checkpoint bytes preserved. Documentation only; no application tests, region recommendation, private configuration access or runtime change.

P04a proposal recording, 2026-10-31: Architecture workspace validator and `git diff --check` PASS; HEAD/index and prior checkpoint bytes preserved. Documentation only; no application tests, data deletion or runtime changes.

P04a acceptance recording, 2026-10-31: Architecture workspace validator and `git diff --check` PASS; HEAD/index, approved proposal section and entire prior checkpoint preserved. Documentation only; no application tests or deletion/runtime changes.

## Owner delegates provisional missing decisions — 2026-10-31

The owner cannot currently obtain business input and authorizes reasonable provisional choices and progress, with questions/choices in one document for later client answers and corresponding code updates. See the dedicated [client decision register](ALERTS_NOTIFICATIONS_CLIENT_DECISIONS.md), policy `AN_PRIVACY_PROVISIONAL_1`. Earlier “await owner parameters” statements are superseded by this delegation for local policy development only; original explicit P01/P02/P04a decisions are preserved. PR04–PR17 record assumptions, copy/receipt/restore interactions and facts that cannot be invented. No client/legal acceptance is inferred.

Provisional local durations: acknowledgement and alert audit history while ACTIVE plus 365 days INACTIVE; command receipts 30 days after original completion, READ copies capped by the marker expiry; ordinary logs 14 days, security logs 90 days, backups 35 days from creation. Logical expiry at the deadline, daily live cleanup within 24 hours in healthy operation, restore expiry before access. The dedicated register is authoritative for questions/rationale/limits and pending client answers; avoid duplicating a second questionnaire here.

Pure Operations `AlertPrivacyPolicy` calculations and eight boundary/lifecycle/receipt/log/backup tests are implemented, without runtime wiring or deletion authority. Existing alert domain/input plus new tests: 33 PASS, zero failures/errors/skips. Existing completed receipts and ack/history are immutable; exact new expiry/replay/redaction semantics require a new independent executable review before pinning. No historical migration or old released artifact is changed. AN-D07 is now provisionally specified for development, not enforced or closed; non-generated rollout stays disabled. No private configuration, stack, role/credential, data/volume, external notification, Git publication or AEO action.

## Approved local privacy implementation status — 2026-10-31

The owner accepted the exact technical package/candidate in ALERTS_PRIVACY_APPROVAL.md. Contracts 0.9.0 promotion/archive/pins and generated-only runtime enforcement/cleanup/restore/Web verification are recorded in [privacy verification](ALERTS_PRIVACY_VERIFICATION.md). Prior individual approvals persist and business defaults remain provisional pending client answers. Unattended maintenance authority/scheduling, actual log/backup controls, controller/basis/notice/hosting facts, existing-stack execution and owner functional acceptance remain open; AN-D07 is not closed for actual subjects. No existing data/config/volumes/geometry/accounts/roles/credentials/AEO change or external notification occurred. This status supersedes earlier unimplemented labels only within its evidenced local scope; no duplicate client questionnaire is introduced.
