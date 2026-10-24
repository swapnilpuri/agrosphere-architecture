# 0005-toolchains: Independent supported toolchain baselines

Status: Accepted for Milestone 0 foundation
Date: 2026-10-23

## Context
A new rubber-plantation POC needs a production-oriented foundation while keeping the first execution strictly limited to Milestone 0.

## Decision
Use Java 25 LTS with Spring Boot 4.0.9 and Cloud 2025.1.4 at gateway. Override JUnit Jupiter to 5.14.4 to honor requested JUnit 5; verify independently. AI uses Python 3.12+, FastAPI/Pydantic; ML is optional. Web uses Angular 21 LTS/TypeScript 5.9 for local Node 24.13 compatibility. Unreal is descriptor-only UE5.8/Cesium2.30.0.

## Consequences
Pin direct dependencies; Maven BOM and npm lock constrain transitives. Python full transitive locking and image digest pinning remain follow-up hardening. Validate local builds and tests on JDK25 as well as the configured container and CI runtimes.

## Verified JUnit constraint
Spring 7 SpringExtension is incompatible with JUnit 5 (NoSuchMethodError for ExtensionContext.Store.computeIfAbsent). Foundation security tests therefore manage Spring web contexts explicitly with JUnit 5 lifecycle methods. Standard @SpringBootTest/SpringExtension integration is not supported by this override. Before M1 integration testing, choose a documented JUnit baseline exception/upgrade or maintain and verify explicit-context JUnit 5 tests. No silent upgrade to JUnit 6 is made.
