# ADR 0014 — Estate worker register and daily attendance

Status: ACCEPTED by project owner, 2026-10-29. See [approval](../milestones/WORKER_ATTENDANCE_APPROVAL.md) for exact reviewed hash, authorization and retained gates.

Operations owns a minimal estate-scoped worker register and daily attendance, separate from its existing tapping/collection aggregates. Estate remains the source of plantation/division identity and timezone; Keycloak owns authentication. A registration UUID (`workerRegistrationId`) is distinct from existing tapping `workerId` signed-sub text. Non-login people may be registered; account provisioning/linking, transfer/global matching and attendance gating of tapping are deferred. Existing attribution/history/contracts remain unchanged.

Registration has immutable estate/code/provenance, a Unicode display name, optional division and nonoverlapping dated active periods. Attendance is one identity per estate/registration/local date with PRESENT/ABSENT/EXCUSED, reasoned manager corrections/void/re-record and immutable revisions. Missing evidence is UNMARKED. No hours/payroll, biometrics, GPS or offline cache is included. Authorize with positive operation permissions and trusted estate scope; generic viewer/worker/plantation-admin roles do not grant personal-data access.

Commands use optimistic versions, durable actor/key receipts and atomic root/revision/outbox persistence. New minimal workforce events omit names/codes/free-text reasons; existing event namespaces and byte-pinned releases are preserved. Contracts are authored/reviewed/released independently before pinning. Pure domain/ports may precede release; no source-path dependency or cross-service SQL is introduced.

The [reviewed package](../milestones/WORKER_ATTENDANCE_REVIEW.md) specifies WA-R01–08, D01–D10, fifteen REST operations, four events, WA-AC01–18 and WA-T00–09. D08 measured-load inputs and D09 actual privacy/retention parameters remain acceptance gates. Development uses SIMULATED fixtures and must technically block REAL use until its separate gate is met. No implementation or functional acceptance is asserted by this ADR.
