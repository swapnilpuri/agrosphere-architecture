# 0001-independent-repositories: Independent service repositories

Status: Accepted for Milestone 0 foundation
Date: 2026-10-23

## Context
A new rubber-plantation POC needs a production-oriented foundation while keeping the first execution strictly limited to Milestone 0.

## Decision
Use twelve sibling independent repositories with no parent Git root, submodules, Maven aggregator or sibling source dependencies. Each project releases independently with SemVer and CI.

## Consequences
More coordination is needed; publish versioned contracts instead of sharing entities.
