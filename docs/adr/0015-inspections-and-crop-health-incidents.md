# ADR 0015 — Block inspections and crop-health incidents

Status: ACCEPTED by project owner, 2026-10-31. See [approval](../milestones/INCIDENT_INSPECTION_APPROVAL.md) and exact reviewed package hash.

Operations owns completed one-block inspections and manually managed crop-health incidents. CLEAR is explicit evidence, never inferred from missing reports. FOLLOW_UP creates its first linked incident atomically; direct incidents have no fabricated inspection. Distinct UUID roots retain immutable estate/block/provenance/link identities, optimistic versions and append-only evidence. Manager triage/resolve/reopen/void/correction commands enforce link and chronology invariants; VOIDED is terminal.

New feature permissions use signed subjects and trusted estate scope independently of legacy role unions. Managers administer; supervisors create today's evidence and read current views; auditors read protected history. No anonymous reports, worker/account assignment or new realm roles. Estate owns canonical identity/timezone, Spatial owns geometry; no cross-service SQL or geometry prerequisite.

Commands atomically persist root(s), revision(s), durable original-success actor/key receipt and outbox event(s). Four new minimal crop-health v1 families omit text and actor identities, preserving the legacy CropHealthIncidentDetected placeholder and all existing contracts. Independent executable candidate review/local release precedes pinning. No two-root atomic delivery or exactly-once guarantee is claimed.

The [accepted package](../milestones/INCIDENT_INSPECTION_REVIEW.md) defines II-R01–07, II-D01–10, II-AC01–16 and II-T00–09. Development remains SIMULATED-only. Workload/language/connectivity/performance and actual privacy/retention/deletion are open gates; REAL data, notifications, attachments, offline queues, MQTT/Analytics/AI and existing-stack deployment are excluded. This ADR records design acceptance, not implementation acceptance.
