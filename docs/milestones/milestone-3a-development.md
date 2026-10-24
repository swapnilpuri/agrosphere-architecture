# Milestone 3A development and API examples

Build each Java service independently; Operations commands and environment properties are in its README. Follow Infrastructure README to configure private local passwords and Keycloak Code/PKCE. Existing imported realms need the additive scripts/configure_identity.py step for the new audience and roles; importing a realm file does not overwrite a running realm. Never assign estate_ids from browser input.

For a completely isolated acceptance test, from Infrastructure run python scripts/verify_tapping.py with Docker and PyYAML installed. It builds independent images, starts its own random project/ports/credentials/volumes, logs in through real Keycloak PKCE, creates SIMULATED master data and tapping work, verifies routing/security/events and removes only that project. It never reads the developer .env or local-secrets. The normal Compose apps profile adds Operations with its own DB user and no exposed service port. Gateway forwards /api/v1/tapping/** to Operations.

Use a bearer token carrying the operations-service, estate-service and agrosphere-api audiences. Below bodies are JSON; every request uses Content-Type: application/json and Authorization: Bearer <private token>. Do not copy real tokens into docs/logs.

1. POST /api/v1/tapping/schedules returns 201:

~~~json
{"estateId":"00000000-0000-0000-0000-000000000001","blockId":"00000000-0000-0000-0000-000000000002","name":"North daily tapping","recurrenceRule":"EVERY_N_DAYS:2","plannedTreeCount":120,"effectiveFrom":"2026-10-24","effectiveTo":"2026-11-24"}
~~~

2. POST /schedules/{id}/activate with {"version":0}.
3. POST /schedules/{id}/generate-assignments with {"version":1,"from":"2026-10-24","to":"2026-10-30","workerId":"<Keycloak subject>"}. Returns October 24,26,28,30. Repeating returns the same assignment IDs.
4. POST /assignments/{id}/start with {"version":0} on the estate-local tapping date.
5. POST /assignments/{id}/complete with {"version":1,"actualTreeCount":115,"notes":"Completed north row"}. Repeating the same payload is safe.
6. Alternatively POST /assignments/{id}/mark-missed with {"version":0,"reasonCode":"RAIN","remarks":"Heavy rain"}. Future dates are rejected; completion after missed/cancelled is rejected.
7. GET /summary?estateId={estate}&from=2026-10-24&to=2026-10-30&groupBy=worker&page=0&size=20. GET /records and /assignments use the same scope/date filters. Paths in steps 2–7 are relative to /api/v1/tapping.

For ad hoc work, POST /assignments with estateId,blockId,workerId,tappingDate,plannedTreeCount. Only management roles may create/reassign/cancel. Reassignment uses PATCH /assignments/{id}/worker with version and workerId while PLANNED.

The security matrix, summary denominator, cancellation and idempotency policy are in ADR 0012 and Operations README. Event schema inventory lives in Contracts events/operations/v1 with six representative SIMULATED examples; old schemas are preserved. Event version changes require a new namespace/version and consumer coordination.

Failure drills: invalid/stale versions → reload on 409; Estate unavailable → 503 with no operational writes; unknown/inactive or non-rubber block → 422; role/scope mismatch → 403; broker down/unroutable → committed work + pending outbox, capped retries then retained FAILED row; relay crash after confirm → possible duplicate event, consumer dedup required. No automatic missed marking or terminal reopening exists. Suspend/close stops generation without cancelling existing work.
