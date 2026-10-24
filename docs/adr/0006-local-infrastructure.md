# 0006-local-infrastructure: Definition-only local infrastructure and future Azure

Status: Accepted for Milestone 0 foundation
Date: 2026-10-23

## Context
A new rubber-plantation POC needs a production-oriented foundation while keeping the first execution strictly limited to Milestone 0.

## Decision
Compose defines PostGIS, RabbitMQ and optional authenticated MQTT, Keycloak and OTLP collector. Do not launch or install infrastructure in M0. Azure Container Apps is a future deployment option, not a commitment.

## Consequences
Stateful hosting, budget, TLS, backups, identity realm, authorization and limiter store remain explicit future decisions.
