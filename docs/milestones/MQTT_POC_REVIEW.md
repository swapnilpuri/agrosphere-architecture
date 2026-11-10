# TLM-01: bounded MQTT POC review

Date: 2026-11-01 (America/Chicago). Status: **PROPOSED DOMAIN/SECURITY SCOPE; NOT IMPLEMENTED**. Prepared under the owner's re-anchoring request. This is a review package, not a new progress tracker. Roadmap/checklist own sequencing/completion; checkpoint owns authority.

## One next decision

Accept or revise this TLM-01 package for SIMULATED-only Contracts candidate authoring and Telemetry pure domain/ports/tests, followed by separately reviewed exact executable artifacts before release/pinning and adapters. No existing broker/database/account/private configuration change, real device provisioning, installation, spending or deployment. Existing service guidance permits foundation only; this new domain/security policy must be accepted before implementing business behavior. Record actual reviewer/date/package SHA-256 and conditions; do not infer acceptance from this file or the roadmap. No additional approval of 3B/WA/II/AN/privacy is requested.

## Recommended scope and policies to accept together

| Decision | Proposed rule and consequence |
|---|---|
| Ownership/identity | Telemetry owns a persistent device registry and observations; generated bootstrap registers one device per selected canonical block with immutable estateId/blockId/deviceId mapping. Verify references through authorized Estate API, not SQL. Reject unresolved/inactive mapping; no arbitrary caller remapping. No device-management UI, transfers or real hardware onboarding in TLM-01 |
| Measurement semantics | Three explicit kinds: air temperature in degrees Celsius, soil moisture in percent (0–100), interval rainfall in millimetres (nonnegative, with UTC interval start/end). Finite numeric values; no unit conversion, yield inference or agronomic threshold. Temperature gets no invented agronomic safe range; exact representable bounds/precision reviewed in candidate. Soil depth/calibration/accuracy are unknown for fixtures, not real sensor facts |
| Payload/provenance | Version, stable observation UUID, registered device UUID, canonical estate/block UUIDs, kind/value/unit, observedAt UTC and SIMULATED required; rainfall also interval. Server adds receivedAt UTC. No workforce identity/location payload. Invalid kind/unit/provenance/identity/timestamp fails validation; canonical encoding and field bounds defined in candidate |
| Authentication/ACL | Generated publisher principal tied to one device; only its estate/device topic may publish. No anonymous/wildcard publisher or retained-command channel. Topic proposal: agrosphere/v1/estates/{estateId}/devices/{deviceId}/observations. Compare trusted principal/topic/registry/payload identities. TLS outside loopback; exact broker auth/ACL and secret delivery reviewed before disposable integration. Do not add credentials/roles to an existing broker |
| Time/order | Both timestamps retained; observedAt must fit the explicit generated run's manifest window; propose at most five minutes future skew relative to server clock. Old in-window observations may enter history but cannot replace newer latest values. Equal observedAt ties use stable observation UUID ordering. Manifest admission is a demo boundary, not a production retention rule; stale/absent UI values are explicit, with display threshold specified in TLM-02 review |
| Dedup/durability | Same observation UUID + same canonical payload is a no-op; conflicting reuse is rejected/quarantined, never overwritten. Persist observation, dedup identity and versioned outbox event atomically in Telemetry DB. QoS 1 transport acknowledgement is not domain acceptance; expose accepted/rejected aggregate status in protected generated evidence, then prove accepted persistence through API/event. Bound input size/queue/retry in adapter review; no unbounded in-memory retries |
| Query/event boundary | Candidate proposes an estate/block-scoped latest-readings GET with source/observed/received/unit/provenance/coverage, and one immutable observation-recorded event. Gateway and Telemetry independently validate signed JWT issuer/audience/role/estate; reuse accepted estate-read role semantics, no new product role. No query before scope validation. Historical API and dashboard belong to Analytics/TLM-02 scope. Review exact paths, envelope/errors, authorization mapping and event schema independently in Contracts |
| Privacy/copies | Generated subjects/measurements only, no real accounts or private environment reads. Logs omit credentials/raw bodies. Disposable manifest identifies all owned storage/broker/log/export copies and verified teardown. No retained backup, external delivery, selected-environment privacy claim or change to accepted alert retention. Exact candidate includes message/field limits; no real workload/SLA inferred |

These are proposed domain/security decisions, not accepted defaults. Revising a row changes dependent contracts/tests. No new public schema is published by this document. Existing Telemetry OpenAPI has empty paths; use a new independently versioned release after exact executable review, preserving all old artifacts/pins. No version number is preassigned.

## Demonstration and acceptance

TLM-01 delivers one generated publisher → authenticated local broker → Telemetry transaction/outbox → scoped latest-readings query; TLM-02 adds deterministic simulator/overlay and full platform drill. Register a fixture device only inside a separately owned generated target. Use service-owned migrations/ports/adapters; no shared tables, parent build or sibling runtime imports.

| Gate | Required result before claiming delivery |
|---|---|
| TLM-AC01 registry/security | Correct principal/topic/mapping accepted; anonymous, wrong device/estate, altered payload mapping and unknown/inactive references denied; no cross-estate data leak |
| TLM-AC02 payload/time | All three kinds preserve units/observed/received/provenance; NaN/overflow/unit/range/missing rainfall interval/future-window cases rejected; out-of-order and tie behavior deterministic |
| TLM-AC03 durability | Duplicate delivery/restart changes no totals/latest; UUID conflict does not overwrite; rollback/outbox confirms, broker outage/reconnect and consumer replay preserve identities/effects |
| TLM-AC04 API/contracts | Independently accepted exact contract release pinned; real serialized events/responses validate; signed JWT issuer/audience/role/estate denial tested, not merely mock decoder tests |
| TLM-AC05 independent integration | Owning README Maven/checks pass; generated Postgres/broker tests and isolated Keycloak/Gateway/Estate flow demonstrate durable MQTT→query/event; no existing stack touched; exact resource cleanup verified |
| TLM-AC06 evidence | Commands/source/pin hashes, expected vs actual outcomes, failures/unavailable checks and limitations recorded; owner functional acceptance remains separate |

## Execution after decision

1. Record acceptance/revision and refresh affected independent baselines; update owning guidance only to the accepted scope.
2. Author isolated executable Contracts candidate plus pure Telemetry domain/ports/tests. Preserve existing releases. Exact candidate review/local release/pinning is a later gate, not covered by domain-package acceptance.
3. After exact acceptance, implement registry/ingestion/API/outbox and disposable broker/security adapters by dependency. Review exact broker ACL/provisioning/migrations before integration; use generated credentials only in owned tests.
4. Run required owning checks and TLM-AC01–06, then prepare TLM-02 simulator/overlay scope. M1/M2 performance, alerts walkthrough, field release and REAL/production gates remain open independently.

No claim of new service behavior, contract acceptance or test execution is made here. All approved alert/privacy bytes and AEO remain untouched.
