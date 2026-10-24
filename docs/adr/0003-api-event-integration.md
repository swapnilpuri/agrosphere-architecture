# 0003-api-event-integration: API-first REST plus durable events

Status: Accepted for Milestone 0 foundation
Date: 2026-10-23

## Context
A new rubber-plantation POC needs a production-oriented foundation while keeping the first execution strictly limited to Milestone 0.

## Decision
Use OpenAPI 3.1 for synchronous APIs, JSON Schema 2020-12 for event envelopes/payloads, RabbitMQ for domain events and MQTT only for ingestion. Reserve SSE/WebSocket for justified notifications.

## Consequences
Transactional outbox and idempotent consumers must be implemented and tested when use cases arrive; schema compatibility is coordinated across independent releases.
