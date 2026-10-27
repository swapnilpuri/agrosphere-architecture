# Milestone 3B — Owner approval record

Date: 2026-10-27 (America/Chicago). Reviewer: project owner, through the explicit user message in this Codex conversation. Status: ACCEPTED DESIGN AND CONDITIONAL IMPLEMENTATION AUTHORIZATION. This records the owner's actual decision; it does not assert any additional external reviewer signature, contract release or functional acceptance.

## Exact owner instruction

> I approve the proposed Milestone 3B decisions D01–D12, ADR 0013, requirements, technical design, acceptance criteria, and REST/event contract design referenced in the consolidated review.
>
> I accept clarification R01: timestamps must be exactly representable at microsecond precision; extra trailing zeros are permitted.
>
> I accept clarification R02: lists may omit both date bounds but must reject a single bound; summaries require both bounds.
>
> I authorize implementation of T01–T09 in dependency order, subject to required validation and independent contract review/release gates. Production deployment, destructive migrations, secret-handling changes and AEO changes remain unauthorized.

## Reviewed content and binding clarifications

Immediately before recording this decision, all 14 package fingerprints matched the previously recorded reviewed baseline: four milestone documents, validation record, proposed ADR 0013, six diagram sources, owning REST/event specification and consolidated readiness review. Exact pre-approval SHA-256 values are preserved in [approval evidence](MILESTONE_3B_APPROVAL_EVIDENCE.json). Git HEAD alone does not identify the approved working-tree content; those fingerprints do. Local working-tree status remains unverified.

D01–D12, ADR 0013 and the referenced requirements/design/acceptance/wire design are accepted by the owner. R01 means an explicit-offset instant must be exactly representable at microsecond precision: fractional positions after the sixth must all be zero, regardless of how many nonzero digits occur earlier. Extra trailing zeros may be normalized without loss. R02 means lists may omit both dates, reject exactly one date bound, and summaries require both bounds; both retain ordered bounds and a maximum difference of 366 days. These clarifications are now reflected in the owning documents.

The six PlantUML sources retain their reviewed bytes, including historical 'proposed' titles; acceptance of their design is recorded here, not inferred from those titles. Syntax/render validation remains unavailable. The prior readiness review and design-validation report remain historical inspection records with a current-disposition notice.

## Authorization and gates retained

T01–T09 are authorized in dependency order, subject to required validation and independent contract review/release gates. Approval of the wire design is not publication or acceptance of executable OpenAPI/schema artifacts that do not yet exist. No VERSION bump, release, producer pin or consumer implementation follows from this record.

Production deployment, destructive migrations, secret-handling changes and all AEO changes remain unauthorized. No new credential wiring/provisioning has occurred. T03's runtime/migration-role design is accepted, but any task portion constituting a secret-handling change must remain deferred until separately authorized; do not assume permission merely from the technical design. No production retention policy or deployment readiness is claimed. Milestone 2 performance acceptance stays open independently.

T00's decision component is complete. Its Git/validation baseline is not: the current harmless shell probe failed before execution with CreateProcessAsUserW failed: 5 (Access is denied.). The original owner instructions permit safe documentation/code review in this state and prohibit a sandbox bypass. T01/T02 therefore remain not started while T00's baseline is unresolved. Required Git/Python/Maven/PlantUML/Docker/database/broker checks are not passed or waived.

ADR 0013's status is updated in its existing docs/adr/proposed location to preserve links and avoid silently breaking the validator's twelve-file accepted inventory. This location is transitional and does not negate the owner's acceptance. Canonical relocation to docs/adr, corresponding link/count/CI updates and verification must be one coherent follow-up once command execution is restored. No executable validator or CI configuration was changed during this execution-blocked documentation increment.

## Safe next action

Restore permitted command execution; capture per-repository Git status/revisions/diffs and recheck package/source changes, migrations and compatibility baselines. Complete T00, relocate ADR 0013 with validator/diagram inventory updates and run required checks, then start T01 contract authoring. Continue authorized increments without another per-task prompt; pause only at an actual required release/authorization/validation gate. See [checkpoint](DEVELOPMENT_CHECKPOINT.md).
