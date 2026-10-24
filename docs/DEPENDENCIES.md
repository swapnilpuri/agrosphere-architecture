# Selected dependency baseline
Verified against upstream registries on 2026-10-23. Stable supported release lines are preferred; these pins are not a claim of vulnerability-free dependencies. Review patches and image digests before deployment.

| Area | Selected baseline | Source / notes |
|---|---|---|
| JVM | Java 25 LTS target; Maven 3.9.12; wrapper 3.3.4 | CI and service containers use Temurin25 |
| Spring | Boot 4.0.9; Cloud 2025.1.4 (gateway); springdoc 3.1.1 | Maven Central; Cloud train targets Boot4.0 |
| Tests | JUnit Jupiter 5.14.4 override | Boot4 normally uses JUnit6; see ADR-0005 and validation limitations |
| Persistence/security/OTel | Boot BOM-managed JPA, Security, Flyway, PostgreSQL, Testcontainers, OTLP | Each POM is independent |
| Python | Python >=3.12; FastAPI 0.161.1; Pydantic 2.14.1; Uvicorn 0.54.0 | PyPI release metadata; local Python3.14 |
| Python data | SQLAlchemy 2.1.6; psycopg 3.3.6; Alembic 1.20.1; optional sklearn 1.9.1 | ML not installed; no Ollama runtime started |
| Web | Angular 21.2.25; CLI/build 21.2.28; TS5.9.3; RxJS 7.8.2 | Angular21 LTS; Node24.13.1 local; npm lock included |
| Visualization | CesiumJS 1.146.0; ECharts 6.1.0 | Pinned only, integrations deferred |
| Immersive | UE5.8; Cesium for Unreal2.30.0; bundled OpenXR disabled | Matching upstream UE5.8 asset exists; no editor validation |
| Local infra | PostGIS17-3.6; RabbitMQ4.3.6-management; Mosquitto2.0.22; Keycloak26.5.7; OTel collector0.135.0 | Definitions only; version tags not immutable digests |
| Diagrams | C4-PlantUML2.12.0; PlantUML v1.2026.9 | Vendored C4 includes + license; jar in ignored target only |

Direct Python dependencies are pinned; full transitive lock is deferred. Java transitives are BOM managed, web transitives package-lock managed. Infrastructure tags must be refreshed and digest-pinned before runtime adoption. Independent repositories do not share an executable parent build or persistence library.

Sources: [Spring requirements](https://docs.spring.io/spring-boot/4.0/system-requirements.html), [Spring Cloud compatibility](https://spring.io/projects/spring-cloud), [Angular releases](https://angular.dev/reference/releases), [Angular compatibility](https://angular.dev/reference/versions), [RabbitMQ release/support](https://www.rabbitmq.com/release-information), [Cesium Unreal release](https://github.com/CesiumGS/cesium-unreal/releases/tag/v2.30.0), [Maven Central](https://repo.maven.apache.org/maven2/), [PyPI](https://pypi.org/), [npm registry](https://registry.npmjs.org/).
