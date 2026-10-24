# 0002-service-data-ownership: Service-owned databases and clean boundaries

Status: Accepted for Milestone 0 foundation
Date: 2026-10-23

## Context
A new rubber-plantation POC needs a production-oriented foundation while keeping the first execution strictly limited to Milestone 0.

## Decision
Estate owns identity, spatial owns geometry, operations owns work/production, telemetry owns normalized observations, analytics owns projections, AI owns models/recommendations. Local PostgreSQL may host separate databases with separate roles; PostGIS belongs to spatial.

## Consequences
No cross-database reads or distributed transactions; projections need reconciliation and eventual consistency.
