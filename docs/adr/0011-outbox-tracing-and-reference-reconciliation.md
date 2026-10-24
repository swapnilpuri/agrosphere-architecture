# 0011: Durable trace transport and delayed-reference reconciliation

Status: Accepted for Milestone 1C
Date: 2026-10-24 (America/Chicago)

Each service adds its own V3 migration with nullable trace_parent/trace_state columns beside the transactional outbox payload. The event envelope and all V1/V2 migration files remain unchanged. Mutation and trace metadata commit atomically; publication restores the stored W3C context before observed RabbitTemplate sends. The observed Spatial listener extracts transport headers and creates its own consumer span. Legacy rows with absent trace metadata remain valid and start a new trace. correlationId remains the stable event/application correlation and is also carried in message properties. No secret-bearing baggage is persisted.

Service-owned copies of a small transport helper preserve build/deployment independence; there is no shared Maven parent or persistence dependency. Live acceptance asserts HTTP, outbox publishing and consuming operations on one known Jaeger trace. Database operation spans are only claimed where instrumentation exists; this milestone adds no JDBC agent or production metrics/log retention backend.

Existing Spatial projection semantics deliberately retain valid block snapshots arriving before Estate. There is no local parent foreign key requiring event order. The block and inferred division retain canonical estate identity; missing authoritative Estate references prevent geometry mutation until a later Estate snapshot upserts that parent. This automatically reconciles the child without dropping it or querying Estate synchronously. A service-owned unresolved-parent query, queue/DLQ inspection and controlled authoritative snapshot replay are the operator recovery path if a parent never arrives. Newer revisions win; deduplication remains transactional; invalid messages use bounded retry/DLQ. No authoritative division lifecycle is invented.

The development acceptance suite uses actual human users authenticated through Authorization Code with PKCE S256. Existing PLATFORM_ADMIN-only estate creation is preserved; an assigned ESTATE_MANAGER executes subsequent commands. Gateway forwards signed user identity and both backends independently validate it. No client-credential account impersonates human manager/viewer roles and no synchronous Spatial-to-Estate authentication is required on reads.

A shared default 2 MiB bound protects JSON ingress at Gateway, Estate and Spatial for declared-length and streamed bodies. This is transport integration, not a domain API/schema change. Structured logs include service identity, correlation and active trace/span IDs; access logs omit query strings, tokens and request bodies. Data/volume resets are never automated, including CI shutdown.
