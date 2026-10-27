# ADR 0013 — Latex collection, DRC and immutable production evidence

Status: ACCEPTED by project owner, 2026-10-27; see [owner approval record](../milestones/MILESTONE_3B_APPROVAL.md). Design acceptance is recorded; implementation and functional acceptance are not claimed. Extends accepted ADR 0012 without changing its tapping contracts or terminal-state rules.

## Context

FR-04 requires mass, DRC and dry rubber. Completed 3A owns tapping execution, UUID references, JDBC/Flyway, scoped JWT and a confirmed outbox. A partial record may exist for aborted tapping and is not eligible production. A legacy foundation LatexCollectionRecorded.v1 requires DRC and has a different source/envelope; redefining that routing key would break compatibility.

## Accepted decision

Operations owns a new LatexCollection aggregate per separately weighed lot and references an immutable completed TappingRecord. DrcMeasurement and CollectionAdjustment are append-only children, not separately writable aggregates. A collection root serializes every first measurement, correction and void by optimistic version. Its current row is a rebuildable projection of immutable revision snapshots; before/after evidence and historical calculation inputs are preserved. All quantity arithmetic uses BigDecimal, HALF_UP at kg scale 3, policy DRC_KG_V1; missing DRC is null, never zero. Multiple lots are permitted with permanent execution/reference uniqueness.

Use existing /api/v1/tapping prefix plus /collections. New routes fit the existing Gateway predicate. Keep all 18 tapping operations, event schema bytes and 3A domain types unchanged. Put the collection event family in Contracts events/operations/v2 with eventVersion=2 and routing agrosphere.EventType.v2. The new LatexCollectionRecorded.v2 deliberately avoids the legacy v1 route; use v2 consistently for DrcMeasurementRecorded, LatexCollectionAdjusted and LatexCollectionVoided as well. Keep timestamp/source/correlation/provenance/aggregate metadata conventions from Operations; preserve every old namespace. Extend the emitter through a separate version-aware operation while preserving the old emit signature and v1 behavior. Relay already reads event_version and constructs the matching routing key.

One local transaction persists root, evidence, durable idempotency result and one outbox snapshot event per successful command. REST never publishes synchronously. Stable IDs survive confirmed publication retries. Downstream consumers are future independently owned work and must deduplicate and reject stale aggregate versions. Snapshots allow later versions to supersede older messages, including voids, without additive double counting.

Snapshot the canonical estate timezone and current block divisionId/master versions when the collection is created through authenticated Estate GET APIs. Do not copy geometry, claim authoritative division lifecycle, or introduce cross-service foreign keys. Current trusted estate access remains the authorization boundary even for historical reads. Correction operates on existing historical snapshots without requiring the master entity still be active; this allows repair after deactivation and creates no new production.

## Alternatives and consequences

Embedding quantities in TappingRecord would break terminal evidence and enforce one quantity per execution. A separate DRC aggregate would require cross-aggregate consistency for recalculation; sample pooling is deliberately deferred. An event-only production ledger would add replay complexity beyond the current JDBC architecture. In-place correction loses evidence; delete/recreate without a void can double count. Four-eyes approval would need pending/rejected states and additional actor constraints; this proposal instead gives explicit application approval to manager-authorized commands with an audit reason.

Indefinite historical/idempotency retention increases storage and preserves subject identifiers. Snapshot division grouping differs from current master hierarchy by design. Application/domain checks enforce cross-row temporal/ownership invariants; simple SQL constraints provide additional protection. Separate the Operations runtime login from its existing migration owner to enforce append-only evidence permissions; the same service database and ownership remain. No down migration may silently delete evidence. Real/simulated segregation is mandatory. Review business defaults D01–D12 in [requirements](../milestones/MILESTONE_3B_REQUIREMENTS.md) together with this ADR; its creation did not assert approval; owner acceptance is now explicitly recorded in the linked approval record.

## Verification

[Acceptance criteria](../milestones/MILESTONE_3B_ACCEPTANCE_CRITERIA.md) require exact decimal fixtures, race/rollback tests, 3A regression, upgrade and broker-failure drills in disposable environments. Design inspection is possible through filesystem access; Maven, Python, Docker, Git diff and PlantUML execution remain unverified in this design pass.
