# Operations migration/runtime credential wiring — scope decision

Prepared: 2026-10-27 (America/Chicago). Status: REVIEWABLE PROPOSAL ONLY. No runtime secret configuration or private environment file has been changed. This request is separate from the already accepted domain and contract decisions.

## Why this is the next boundary

The owner's implementation instruction explicitly leaves secret-handling changes unauthorized. The accepted design requires a restricted Operations runtime login distinct from its Flyway migration owner. Current Operations and Compose configuration still use one DB_USER/DB_PASSWORD pair for both. V3 deliberately requires an existing restricted role and fails before DDL if it is missing, elevated, inherited from another role, or owns migration objects. Do not launch this intermediate build against an existing environment without the operator provisioning/configuration step.

The allowed preparation is implemented: service-owned V3, immutable evidence/receipt guards, grants and scoped JDBC adapter. Disposable tests create a **NOLOGIN** role and exercise its privileges via SET ROLE; they do not provision a runtime password. Typed Estate validation and positive per-operation collection permissions are implemented. These checks do not prove separate runtime/migration login wiring, which is still incomplete.

## Concrete proposed public configuration changes

Operations src/main/resources/application.yaml would add these required owner credentials under the existing spring.flyway settings:

```yaml
spring:
  flyway:
    enabled: true
    user: ${FLYWAY_USER}
    password: ${FLYWAY_PASSWORD}
```

Its existing datasource remains DB_USER/DB_PASSWORD, now intended for agrosphere_operations_app. Operations .env.example would contain placeholder-only values for the two pairs. No credentials enter source control and no fallback would silently reuse owner credentials for runtime.

Infrastructure compose.yaml's Operations environment would become:

```yaml
DB_USER: agrosphere_operations_app
DB_PASSWORD: ${OPERATIONS_APP_DB_PASSWORD:?Set private runtime service password}
FLYWAY_USER: agrosphere_operations
FLYWAY_PASSWORD: ${OPERATIONS_DB_PASSWORD:?Set private migration-owner password}
```

The existing migration-owner variable remains distinct from a new OPERATIONS_APP_DB_PASSWORD placeholder in Infrastructure .env.example and fresh-volume Postgres bootstrap environment. No other service's identity, credential or datasource changes.

## Proposed provisioning and test work

| Area | Planned change and limit |
|---|---|
| Infrastructure postgres/init.sh | Fresh-volume-only creation of the restricted Operations runtime login before V3. Retain the existing migration owner and service-owned database. No existing-volume bootstrap rerun. |
| New operator provisioning script/runbook | Prepare an additive, idempotent Operations-only role/privilege step for existing environments. Validate role flags/ownership and fail closed on unsafe drift. Keep passwords out of arguments/logs/artifacts. **Do not execute it against a running or existing stack under this requested implementation scope.** |
| scripts/init_local.py | Its existing generic placeholder generation should cover the new example key; preserve no-overwrite behavior. Do not read/modify an existing private .env. |
| Disposable test support | Generate distinct test-only runtime/owner credentials for fresh containers, never developer credentials; test actual login grants, Flyway owner credentials, upgrade and previous-3A compatibility. Destroy only those test resources. |
| Isolated acceptance wiring | Extend the independent disposable project pattern to pass the two credentials privately and verify rejected cross-service/DDL/evidence access. No authoritative fixture or shared database. |

The requested authorization covers implementing these public/configuration/tooling changes and testing with **new disposable generated credentials only**. It does not authorize reading or changing existing private .env files, rotating real credentials, provisioning existing/running environments, production operations, destructive migrations, remote publication, or AEO changes. No credential values are required from the owner in chat.

## Specific requested decision

Accept the scope above, or state a requested adjustment. Suggested reply:

> I authorize the proposed Operations migration/runtime credential wiring and provisioning-tool implementation, using placeholders in tracked files and generated credentials only in disposable tests. Do not read or modify existing private environment files, provision existing/running stacks, or change production or AEO state.

After acceptance, complete T03's restricted-login/configuration proof, then T05 transaction/replay and subsequent HTTP/event/acceptance tasks in dependency order. T03 is not marked complete solely from NOLOGIN/SET ROLE tests. This authorization request does not repeat the already accepted Contracts 0.5.0 release/pinning or D01–D12 decisions.
