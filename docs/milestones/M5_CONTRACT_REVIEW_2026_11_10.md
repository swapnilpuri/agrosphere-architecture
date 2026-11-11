# M5 independent contract-consumption review — 2026-11-10

Result: **ACCEPT existing exact Estate/Spatial artifacts for independent Immersive pinning**, subject to the consumer obligations below. No new public contract, event, release or migration is required for the six approved read operations. This is delegated engineering acceptance under approved M5 D05/D10, not owner functional acceptance, live integration verification or a new Contracts release. The owner approved D01–D10 with physical VR deferred. The original package bytes remain unchanged.

Reviewer: delegated contract_review agent, independent of the client implementation. Read applicable Architecture/Contracts AGENTS, M5 package, release/compatibility documentation, actual schemas, Web API/pins, Estate/Spatial controller/service/security source and Gateway rate-limit source. No private config, existing stack, Git index, contract bytes or consumer pins changed.

## Exact identities and release provenance

Observed Contracts HEAD `c7846584ac938c4f7344f5ed60244fcc888df729`, current repository VERSION `0.13.0`; Web HEAD `c3dc6a65f01b348a3d52c8222219bce76752e8e2`. Contracts had pre-existing staged AGENTS/CHANGELOG/README edits; these were untouched. Repository VERSION must not be confused with each artifact's original release or OpenAPI info.version.

Contracts README and docs/COMPATIBILITY.md identify Estate as the 0.2.0 contract set and Spatial as the 0.3.0 addition; documentation-only 0.3.1 preserved those bytes. The current 0.13.0 repository still carries these unchanged artifacts. Current source, existing Web pin and service-owned snapshot are byte-identical:

| Artifact | Original contract set / info.version | SHA-256 |
|---|---|---|
| openapi/estate-service.yaml | 0.2.0 / 0.2.0 | `2e7a0b028d91f9f2996289955d52d84e14d65e813582ade46772e59cd504a060` |
| openapi/spatial-service.yaml | 0.3.0 / 0.3.0 | `ca853e9ff9e8f8b752854ceaaf001622490b2a089478757320c356d15b301f74` |

Compared copies: Web contracts/estate.openapi.json and contracts/spatial.openapi.json; Estate src/test/resources/contracts/estate-service.openapi.json; Spatial src/main/resources/contracts/spatial-service.openapi.json. Both JSON semantic comparison and raw SHA-256 equality PASS across all three copies per service. Immersive should record source path, original contract-set version, observed Contracts HEAD and exact SHA-256 in its own manifest. Copy bytes into its own repository; do not use sibling paths at build/runtime. No VERSION bump or re-release is necessary just to consume unchanged artifacts.

## Actual GET operation/envelope review

| Path | operationId | Success schema |
|---|---|---|
| /api/v1/estates | listEstates | EstatePage |
| /api/v1/estates/{id} | getEstate | Estate |
| /api/v1/estates/{estateId}/blocks | listBlocks | PlantationBlockPage |
| /api/v1/blocks/{id} | getBlock | PlantationBlock |
| /api/v1/spatial/estates/{estateId}/features | getestatesestateIdfeatures | FeaturePage |
| /api/v1/spatial/blocks/{blockId}/geometry | getblocksblockIdgeometry | Feature |

All are present in current OpenAPI and actual controller mappings. GET requests have no mutation payload/idempotency key; bounded retries remain side-effect free. List envelopes contain content/page/size/totalElements, not a bare array or GeoJSON FeatureCollection. Page is zero-based, default 0; size defaults to 20 and permits 1–100. Spatial page additionally has maximum 100000. Estate lists support optional ACTIVE/INACTIVE status; the Spatial feature list does not expose a status filter. Do not invent pagination tokens or filters.

Web ApiClient.all explicitly fetches `?page=<index>&size=100` until `(page+1)*size >= totalElements`. Immersive should enforce approved finite ceilings and detect unexpected/nonprogressing page metadata, rather than silently truncate. The approved 100-feature/10000-vertex scene ceiling is narrower than general API capability and must yield a visible unsupported state for excess data.

Spatial Feature is a service DTO: id is the spatial feature UUID; referenceEntityId is the canonical Estate entity UUID, with referenceEntityType ESTATE/DIVISION/BLOCK. Canonical block selection therefore joins Feature.referenceEntityId to PlantationBlock.id, verifies estateId on both, and retains Feature.id separately. Fields include geometryVersion, sourceType, nullable sourceReference, dataProvenance, status, geometryType, boundingBox, centroid and nullable calculatedAreaHectares. Estate metadata has no geometry and no per-row provenance field; do not fabricate an authoritative provenance property on its DTO. Show the Spatial provenance explicitly and label fixture/decorative provenance separately.

**Coordinate finding:** the current Spatial Geometry schema allows exactly two numbers per position (longitude, latitude), including Polygon/MultiPolygon rings. Generic roadmap references to optional altitude do not override this exact executable contract. An ellipsoid height of zero is an explicit client rendering assumption for the generated fixture, not a third API coordinate or surveyed height. Do not send or accept three-number positions as schema-valid under these pins. Point/LineString are legal API geometry types; the viewer may explicitly reject unsupported rendering types, never silently misrepresent them as polygons. Polygon closure, range/topology, identity and finite numeric validation require consumer/service semantic checks beyond JSON structure.

## Errors and security

Every operation uses bearerAuth JWT. Estate declares 400/401/403/404/409/500; Spatial declares 400/401/403/404/409/413. Estate Problem requires type/title/status/detail/correlationId; Spatial requires type/title/status/correlationId while detail and instance are optional. Both use application/problem+json. The client must tolerate absent Spatial detail and generic/empty/non-JSON transport failure bodies. Do not infer an empty estate from 401/403/404/5xx.

Gateway independently returns 429 with Retry-After seconds in its current fixed-minute subject limiter. Treat 429, transport failure and undeclared upstream 5xx as availability/retry states without changing the public service schemas. Retain the approved bounded retry and cancellation policy; never continuously retry authentication denial.

Service JWT decoders verify signatures, configured issuer, standard time validity and service audience (estate-service/spatial-service); Spatial explicitly selects RS256. Gateway remains a separate authenticated boundary. Existing authorization is enforced by owning services: estate list filters readableEstates; estate-scoped block/features lists check estate access; getBlock and selected Spatial geometry resolve owning estate then check access before returning. A read-only native client cannot replace those checks with local role visibility.

Scoped VIEWER is accepted by both services. Role sets are intentionally different: Estate additionally recognizes workforce/auditor and PLANTATION_ADMIN privileges; Spatial has AGRONOMIST and only PLATFORM_ADMIN global bypass. Do not widen Spatial roles to make unrelated Estate roles succeed. Generated demonstration subjects should carry the existing common VIEWER role with explicit estate_ids; foreign-estate/object and missing/invalid scope tests remain required. This review does not change any role, audience or identity registration.

Native PKCE and callback security are separate implementation requirements in D04. Artifact acceptance does not certify a login library, JWT validation implementation, fixture realm or token handling.

## Executed checks and limits

- `agrosphere-contracts/.venv/Scripts/python.exe scripts/validate.py` from the Contracts root: exit 0. Existing OpenAPI, v1/v2/spatial examples/negatives, compatibility and retained release checks PASS. The script's historical labels remain scoped to their stated artifacts; this does not claim all current service tests were rerun.
- Python json.loads plus hashlib.sha256 over six exact source/Web/service files: PASS exact hashes and semantic equality as listed above.
- Read-only controller/service/security/rate-limit/Web consumer inspection: all six approved GETs and named envelopes/parameters corroborated in source.
- No live HTTP/JWT/database/browser/Unreal runtime test was executed by this review. No consumer implementation existed in the reviewed scope. Later negative authorization, expiry, recovery, geometry and Web/Unreal integration checks remain required.

No blocking contract change was found. Proceed with exact independent pins and consumer implementation under the approved package; preserve the two-component coordinate finding and other obligations above. No SQL engineering gate is applicable to this read-only client artifact consumption itself.
