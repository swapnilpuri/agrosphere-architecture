# ADR 0016 — In-app crop-health alerts

Status: ACCEPTED by project owner, 2026-10-31. See [approval](../milestones/ALERTS_NOTIFICATIONS_APPROVAL.md) for exact package hash and conditions.

Operations owns a durable estate-scoped SIMULATED alert inbox for human-reported HIGH/CRITICAL incidents in OPEN/IN_REVIEW. In-app polling serves currently authorized signed-in estate users; it does not enumerate recipients or promise absent-user delivery. No external channels, diagnosis, worker-account linkage, sensor rules or Analytics dependency.

An incident/rule identity has versioned attention. Qualification/requalification or HIGH-to-CRITICAL escalation resets attention; same-severity edits do not. Personal explicit read and shared manager acknowledgement are distinct; neither changes source lifecycle. Current role/estate/subject authorization applies to queries/counts/history/commands and original-success receipt replay.

Deterministic evaluation joins the incident revision/outbox/receipt transaction through an internal application port. Alert persistence failure rolls back the source command. Preserve inspection -> incident -> alert locking. No historical backfill, broker consumer or new shared event family. Existing minimal source events and prior migrations remain unchanged.

Follow AN-R01–05, AN-AC01–12 and AN-T00–09 in the accepted package. Independent exact executable review/local release precedes runtime pins. Pure rules/ports may proceed independently. Generated-only development until actual subject-data policy is reviewed and implemented; workload, REAL, owner functional acceptance and M2 gates remain open. This is design acceptance, not implementation or rollout acceptance.
