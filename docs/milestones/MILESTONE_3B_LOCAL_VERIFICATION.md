# Milestone 3B local verification

Date: 2026-10-27, America/Chicago. Status: LOCAL VERIFICATION COMPLETE. All T00-T09 local implementation/validation work is complete; final owner product acceptance and production readiness are not asserted. Authority: owner-approved T01-T09 and locally accepted Contracts 0.5.0; [credential scope](MILESTONE_3B_CREDENTIAL_WIRING_APPROVAL.json) permits tracked placeholders and generated credentials in disposable tests only.

## Result and implementation

Operations implements nine collection REST operations, exact kg/DRC calculations, immutable evidence/history, scoped summaries, durable actor/key replay and atomic root/measurement/revision/adjustment/outbox/receipt transactions. V3 is additive; separate Flyway-owner/runtime credentials have no fallback. Existing tapping source and v1 schemas remain compatible. Four collection event families use v2 and a separate durable bounded development sink. Gateway forwards key/bearer/correlation/body/query and explicitly permits Idempotency-Key in browser preflight; it contains no collection business logic.

The credential provisioner is implemented and tested with generated values only. It defaults to no changes, refuses another database or unsafe role drift, and does not rotate an existing password. Existing private files and running stacks were neither read nor provisioned. Previous-image rollback retains V3 evidence with Flyway disabled; backup restore targets another disposable database. No automatic destructive down migration exists.

## Verification commands and results

Windows, MSI PowerShell 7, Java 25.0.2, Maven Wrapper, Docker Desktop Linux engine and PostgreSQL/RabbitMQ Testcontainers. Commands run from each owning independent repository. Use the repository's pinned Python requirements in an isolated interpreter; the existing Contracts venv supplied the OpenAPI validator for Operations/Estate tooling where the default Python lacked that module. This is a development-tool choice, not a sibling runtime/build dependency.

| Owner / command | Local result |
|---|---|
| Operations: ./mvnw.cmd verify -Pintegration | PASS: 75 unit/security + 52 integration tests, zero failures/errors/skips; exact XML/log hashes recorded in MILESTONE_3B_LOCAL_EVIDENCE.json |
| Operations: scripts/validate_contracts.py | 27 operations and 10 actual legacy event exports pass |
| Operations: scripts/validate_collection_pins.py --snapshots target/collection-snapshots --events target/collection-events --api-responses target/collection-api | Five exact accepted pins, four actual JDBC/domain snapshots, all four actual v2 families and five actual HTTP response shapes pass |
| Operations: unittest discover -s scripts -p test_contract_comparison.py | Three comparator tests pass; order-only required-name normalization, constraint/missing-field detection and ref-sibling preservation |
| Operations: scripts/test_collection_projection.py | Five actual-export reconciliation tests pass; isolated in-memory SQLite only |
| Contracts: scripts/validate.py; scripts/build_collection_contracts.py --check; unittest discover -s scripts -p test_collection_contracts.py | PASS; 12 boundary tests, all 47 legacy file hashes and all 26 owner-accepted candidate hashes unchanged |
| Infrastructure: scripts/validate.py; scripts/verify_operations_credentials.py | PASS; public configuration/topology and actual generated-only provisioning/idempotence/privilege checks |
| Infrastructure: python -u scripts/verify_collections.py | PASS on corrected disposable projects, including original verify_tapping assertions, real PKCE/JWT/Gateway/Estate, collection lifecycle/scope, durable v2 sink and broker outage/recovery; final post-CORS run/cleanup recorded in evidence |
| Gateway: ./mvnw.cmd verify | 13 tests pass, including actual HTTP forwarding and allowed/denied-origin preflight with Idempotency-Key |
| Estate: ./mvnw.cmd verify -Pintegration; scripts/validate_events.py; scripts/validate_api.py | 39 unit + 9 integration tests pass; 78 actual event exports and all 16 API operations pass |
| Independent Docker packaging | Operations review image and separate Operations/Estate/Gateway images in the final disposable workflow build successfully |
| Architecture: scripts/validate.py --workspace C:/Projects/agrosphere | PASS; 12 independent product Git roots, standards and workflow/YAML checks; AEO excluded |
| Pinned PlantUML: -checkonly main/3A/3B; six 3B PNG renders | PASS; all six inspected visually; jar SHA256 aa4a1d06f8911c4b842beff4828dd955be431692b631a312d04c0e9fab9581de |
| Affected Git roots: git diff --check | PASS; no index/commit/tag/remote mutation by this agent |

## AC01-AC28 traceability

Names below refer to current named tests, not proposed future tests. Domain = CollectionDomainTest; service = CollectionServiceIT; schema/store/credentials = corresponding Collection*IT; access = config.CollectionAccessTest; reference = CollectionReferenceTest. XML report hashes and all test names are in the evidence JSON. The scenario clauses are covered by complementary domain, adapter, HTTP, SQL and full-stack checks; a unit check is not presented as proof of its broker or identity counterpart.

| AC | Passing evidence |
|---|---|
| AC01 | Domain completedNonzeroExecutionRequiredForEveryStatus; service invalidExecutionStatesRollbackReservationWithoutChangingTappingRows; schema completedOwnershipAndImmutableAttributionGuard |
| AC02 | Domain snapshotsAreDerivedAndMasterOwnershipMustAgree / recordAndAssignmentMustReferToSameExecution; reference invalidCanonicalOwnershipInactiveOrNonRubberIs422; service httpErrorsAreCorrelatedSanitizedAndRejectedCommandsLeaveNoRows; SQL root guard |
| AC03 | Domain replacementRequiresVoidedSameExecutionAndNewReference / referencesNormalizeAndRejectNonAsciiOrMalformedTokens; schema multipleLotsAndPermanentReferenceUniquenessSurviveVoid; service differentKeysSameReferenceAndCorrectionVersusVoidRace / sameAndDifferentKeysRaceWithoutDuplicateEffects |
| AC04 | Domain offsetAndExactMicrosecondsIncludingArbitrarilyManyTrailingZeros / estateTimezoneDateRolloverAndDstAreIndependentOfClockZone / collectionChronologyRejectsFutureAndPreCompletion / historicalEntryNeedsReasonAndSnapshotsDoNotChange; actual date-correction exports |
| AC05 | Domain decimalBoundariesDoNotRoundInvalidInputs; CollectionCommandTest strict lossless parser/precision cases; HTTP closed-shape/input assertions |
| AC06 | Domain calculationVectorsAndMissingVersusZero / correctionRecalculatesAndOldInputRemainsImmutable; actual-event exact formula validator; isolated Compose 40.662 ->32.400 correction |
| AC07 | Domain measurementEvidenceAndChronologyAreRequired / selectedMeasurementMustMatchOwnerProvenanceAndRevision / auditActorIsOpaqueSignedSubjectAndCannotBeForgedOnMeasurement |
| AC08 | Domain pendingAndInitialMeasurementKeepOriginalEvidence / timeCorrectionPastSelectedMeasurementRequiresAtomicReplacement / pendingCorrectionMayIntroduceFirstMeasurement / noopBlankReasonAndStaleWritesRejected / voidIsTerminalAndRetainsPendingOrCalculatedEvidence; service real lifecycle/history |
| AC09 | Access everyRoleAndOperationUsesPositiveWritePermissions / mixedReadRolesDoNotBroadenWorkerWrites; service everySignedRoleIsEnforcedAcrossAllNineHttpOperations, actualHttpRolesHistoryReceiptAndProblemDetails |
| AC10 | Access malformed/missing scopes and filter policies; service sqlScopePrecedesSecondPageCountsAndSummaryAggregation / boundedQueriesAndScopeAreEnforcedAtHttpBoundary; full-stack canonical foreign estate and other-worker denial |
| AC11 | Production decoder invalid signature/issuer/audience/expiry tests in Operations/Gateway; missing subject denied by access; Gateway collectionCommandsAndSummaryPreserveHeadersBodyAndQuery and CORS test; full-stack real Keycloak |
| AC12 | Service receiptReplaysOriginalBodyAfterLaterVersionsAndMasterOutage / existingCommandsNeedNoLiveMasterAndRevokedScopeCannotReplay / actualV2SnapshotsPublishWithStableIdentityAndNoReplayEvents; full-stack original raw body/Location retry |
| AC13 | Service sameAndDifferentKeysRaceWithoutDuplicateEffects / differentKeysSameReferenceAndCorrectionVersusVoidRace / concurrentMeasurementsRollbackLosingReservation / boundedReservationWaitReturnsConflictAndRolledBackKeyCanRetry; transaction barriers, no sleep-based races |
| AC14 | Service actualHttpRolesHistoryReceiptAndProblemDetails / httpErrorsAreCorrelatedSanitizedAndRejectedCommandsLeaveNoRows / boundedQueriesAndScopeAreEnforcedAtHttpBoundary / sqlScopePrecedesSecondPageCountsAndSummaryAggregation; literal summary, 366/367-day boundaries, paired bounds, second page and actual closed response schemas |
| AC15 | All seven reference HTTP adapter tests (bounded timeout, denied/missing/inactive/wrong/malformed/redirect cases), legacy port; service master-down existing writes/replay versus atomic failed creates |
| AC16 | Service summaryUsesRoundedLotsExactWeightedRatioPendingCoverageAndProvenance; actual HTTP summary schema/formula and full-stack correction/void/zero assertions |
| AC17 | Same summary test covers every grouping and provenance separation; service canonicalReparentAndTimezoneChangesCannotRewriteSnapshotGroups / dateCorrectionMovesCurrentContributionAndRetainsOldHistory; SQL-scoped second-page counts |
| AC18 | Domain revision/adjustment binding; real service history and all-write receipt replay; schema immutable/deferred guards; actual restricted credentials test denies evidence modification/DDL; stored prior revision kind/audit read from real history |
| AC19 | Service failureAfterRootRevisionOutboxOrReceiptRollsBackEverything / evidenceAndAdjustmentFailuresRollbackAndKeyCanBeRetried / responseSerializationFailureRollsBackAllStages; real stale-writer races; relay only reads committed rows |
| AC20 | Eight schema and seven store integration tests: permanent/local/composite/deferred FKs, immutable evidence/receipt, root guards, precision/range constraints and orphan reservation refusal; separate runtime foreign-DB denial |
| AC21 | Schema populatedV2UpgradeRetainsPublishedAndPendingOutbox / failedV3DdlRollsBackAtomically; tapping populated upgrade; credentials backupRestoresEvidenceIntoSeparateDisposableDatabase / previous3aImageRunsWithRestrictedLoginAgainstV3WithoutDeletingEvidence |
| AC22 | Service actualV2SnapshotsPublishWithStableIdentityAndNoReplayEvents exports all four real families, including atomic replacement measurement correction with Adjusted only; pinned schema/identity/version/provenance/formula checks; messageId=eventId |
| AC23 | Service actualBrokerNackAndConfirmTimeoutRetainCommittedEvent / unroutableV2IsRetainedAndOperatorReplayPreservesId; OutboxDispatcherTest capped retries/finite failure; full-stack actual outage/recovery with unchanged payload/eventId |
| AC24 | Service crashAfterBrokerAckRedeliversSameIdWithNoBusinessMutation and actual date exports; five transactional projection harness tests cover duplicate/stale/gap/conflict/void/date, rollback and bounded invalid/unsupported DLQ |
| AC25 | Contracts immutable 47 legacy /26 candidate hashes; five runtime pins; strict all-27-operation comparison, comparator negative tests; actual 10 legacy v1 exports and four v2 families; separate broker bindings, no dual publishing |
| AC26 | scripts/verify_collections.py builds independent images, runs actual disposable Compose/PKCE/Gateway completed tapping -> lots -> DRC -> correction -> summaries -> void, denies other worker/estate, checks sink and outage; generated-only resources removed in finally |
| AC27 | Existing 34 Operations unit/security baseline plus all ten TappingServiceIT regressions retained; verify_tapping original assertions execute inside full-stack run; independent Estate/Gateway suites and strict old contract/event checks pass |
| AC28 | This report/evidence, current checkpoint/runbooks, independent change inventory, Architecture/workspace checks and six rendered/visually reviewed diagrams; M2 remains open, AEO untouched |

## Findings resolved and verification limits

A real reservation-lock contention test exposed PostgreSQL 55P03 being left uncategorized by Spring's fallback SQL translator. The adapter now translates it to CannotAcquireLockException, producing the required bounded retryable 409. A separate final review added the required browser CORS header without changing routing or business authorization.

Earlier isolated full-stack attempts failed on expired disposable management-token setup and an incorrectly missing foreign estate claim. The harness refreshes management tokens and uses a real second estate; corrected runs pass. Each failed attempt removed only its own project. A missing default-interpreter OpenAPI package was resolved by using the existing pinned development venv; it was not reported as a passed check before rerun. A repeated Maven invocation was refused by a log-file lock while the earlier run was finishing; no overlapping Maven run executed, and verification was rerun sequentially.

Collection OpenAPI uses contract-first documentation: it verifies registered paths/methods, then applies the exact accepted schemas/operations. Runtime enforcement is supported separately by actual signed HTTP/SQL/response tests. Schema equality alone does not prove enforcement. The reconciliation harness is test-only, not an Analytics service. No hosted CI, cloud, production rollout, real credential rotation, active environment upgrade, remote release, M2 device performance or final owner product sign-off is claimed. Application source changes remain Unreleased in independent changelogs; Contracts 0.5.0 alone has the explicitly authorized local release metadata. No private environment, production or AEO state was read/modified.

Generated logs/XML/event/API/diagram/image exports are ignored local artifacts, with hashes recorded for reproducibility; they can change on a future rerun. Source/document inventory in the evidence records current working-tree limits and independently observed HEADs. The agent did not create the externally observed commits. Preserve all staged and unrelated work.
