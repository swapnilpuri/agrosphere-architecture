# AgroSphere milestone and phase prompt library

Prepared 2026-11-10 from the owner's requested format in [InitialPrompts.pdf](../../InitialPrompts.pdf), especially the 3A prompt on pages 9-27 and the 3B prompt on pages 29-59. The PDF is reference material, not a new instruction to execute its historical plans. Its proposed endpoints, entities, roles, Java version and completion claims do not override current source or accepted decisions.

## How to use

1. Open the selected milestone file and copy its **Complete milestone prompt** into a new task in this workspace. This selects only that milestone. For completed work, the prompt preserves it and targets remaining evidence or an explicitly requested correction.
2. New material choices are consolidated into one delivery package. Once approved, the full prompt runs all authorized phases without another prompt for each phase.
3. If you prefer to control each phase yourself, copy that milestone's **Individual phase prompt** instead. These intentionally stop at the selected phase. They are optional session controls, not extra mandatory approval gates.
4. Review the working demonstration and results, then explicitly accept the stated scope or request corrections. Select the next milestone yourself.

The current request creates this library and records bounded M4 acceptance. It does not execute any prompt or approve M5 decisions. [The checkpoint](../../milestones/DEVELOPMENT_CHECKPOINT.md) owns active scope; [the existing checklist](../PROJECT_COMPLETION_CHECKLIST.md) remains the only completion tracker. Status below is a dated navigation aid, not a competing tracker.

## Milestone prompts

| Prompt | Scope | Current use |
|---|---|---|
| [M0](M0.md) | Foundations and reproducibility | Close remaining reproduction/license evidence |
| [M1](M1.md) | Estate/GIS/identity integration | Preserve 1A/1B/1C; reconcile original scope and performance |
| [M2](M2.md) | 3D Web | Verify existing functionality and physical reference-device budgets |
| [M3](M3.md) | Operations, workforce, inspections, alerts, IoT | Remaining connected demonstration/policy dispositions |
| [M4](M4.md) | Analytics, forecasting, anomalies, evidence assistant | Accepted bounded delivery; optional requested reproduction/correction |
| [M5](M5.md) | Unreal, VR and MR feasibility | Next original-roadmap implementation candidate; unstarted |

Each contains a complete milestone prompt and seven concrete phase prompts: discovery; domain/contracts/review; implementation; integration; quality; documentation; completion. The PDF used seven phases for 3A and nine for 3B. This library groups persistence/business services into implementation and API/security/messaging into integration without removing their verification obligations.

## PDF increment mapping

| PDF label | Current authoritative scope | How to use now |
|---|---|---|
| 1A / 1B / 1C | Estate / Spatial / Gateway-identity-broker integration | Select M1 and the required increment; preserve delivered scope |
| 3A tapping | Existing 3A implementation | Targeted verification/correction only |
| 3B latex/DRC | Accepted 3B collection design and implementation | Do not recreate the PDF's proposed batch model |
| 3C inspections | II-1 manual inspections/incidents | Treatment automation is not accepted by this mapping |
| 3D IoT | TLM-01/02 | Generated MQTT ingestion and selected-block freshness |
| 3E analytics | ANL-01/02 under the reconciled M4 roadmap | Existing implementation; separate connected ANL acceptance remains tracked |
| 3F spatial overlays | M2 Web plus TLM-02 and ANL Web integration | Reuse delivered overlays; new heatmaps/refresh targets require scope review |
| 3G alerts/hardening | AN/privacy and remaining M3 connected walkthrough | Retain policy and operating boundaries |

[Increment selection prompts](INCREMENTS.md) retain the PDF's smaller independently selectable units. WA is an additional implemented increment; it is not lost because the older PDF omitted it. M5's XR-01/02 are included there too.

## One approval and continuation prompt

Use only after reviewing the concrete package identified in the checkpoint:

```text
I approve the current milestone delivery package identified by path, revision and
artifact hash in the checkpoint, including its stated decisions and delegated
engineering gates. Continue exclusively on that milestone through all authorized
implementation, integration, verification and demonstration phases. Resolve routine
reversible engineering choices without asking. Stop only for a material decision
outside the approved scope or a genuine blocker. Preserve all existing exclusions.
Finish with working results, actual checks, limitations and an updated checkpoint;
then wait for my acceptance or next milestone prompt.
```

## Resume after an interruption

```text
Resume only the active milestone and phase recorded in DEVELOPMENT_CHECKPOINT.md.
Read its prompt in docs/roadmap/prompts and the applicable approvals. Inspect actual
source and Git state, preserve completed work, and continue the authorized remainder.
Do not repeat satisfied approvals or switch milestones. If no milestone is active,
report the available next prompt and wait for my selection.
```

## Separate future tracks

Android offline inspections/incidents, office sync, individually assigned devices,
one workday offline and English/French remain required in the existing checklist.
They are not renamed M6 or silently included in M5. Actual-data/production readiness
is also separate. Selecting either track requires its own concrete package; this
library grants no REAL, deployment or publication authority.
