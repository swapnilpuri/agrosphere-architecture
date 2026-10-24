# 0007-license-security: License and security release gates

Status: Accepted for Milestone 0 foundation
Date: 2026-10-23

## Context
A new rubber-plantation POC needs a production-oriented foundation while keeping the first execution strictly limited to Milestone 0.

## Decision
No open-source license is chosen; reserve rights pending ownership approval. Keep secrets/env files and large assets out of Git. Gateway and services independently validate JWTs; require audience and estate authorization before domain endpoints.

## Consequences
M0 has no working business authorization or production runtime. Review third-party licenses and security status before redistribution/rollout.
