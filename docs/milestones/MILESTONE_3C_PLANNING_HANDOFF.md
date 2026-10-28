# Next application planning handoff

Status: PROPOSAL ONLY, following locally verified 3B. No next-milestone implementation is authorized or started. Existing roadmap M3-01 includes crop incident use cases alongside tapping/latex/DRC; M3-02 covers authenticated MQTT, and M4-01 covers projections. Those are separate ownership/security/contract decisions. M2 device performance remains open independently.

Recommended next review package: Operations incident/inspection backend (provisional 3C), preserving the delivered collection API/event family. Keep IoT normalization and Analytics consumers in separate subsequent increments. Prepare requirements, domain rules, exact REST/events, security matrix, acceptance criteria, ADR and independent repository/task map before implementation.

Proposed review scope: canonical estate/block identity; explicit observedAt/recordedAt and provenance; append-only observation/evidence and reasoned manager corrections; scoped list/object/history access; transactional versioned events and idempotent commands; independently pinned Contracts additions. No image uploads, health diagnosis or agronomic severity defaults should be inferred from collection work. No changes to AEO, production, private environment files or running-stack provisioning.

Decisions still needed in that concrete review package: inspection versus incident identity, supported observation categories and severity meanings, whether reports can be anonymous or assigned, lifecycle/closure/reopening rules, attachment policy, correction/void authority, observation precision/backdating policy, event version and consumer/reconciliation expectations. Recommend the existing canonical signed subject and trusted estate scope as the baseline, reviewed explicitly for each new operation.

Read PRODUCT_VISION/POC_SCOPE/FUNCTIONAL_REQUIREMENTS/NONFUNCTIONAL_REQUIREMENTS and current source evidence when drafting the package; the broad roadmap contains historical scope statements. This handoff is not a replacement for requirements/design review or permission to implement 3C. The completed 3B authorization and credential scope persist unchanged; do not ask the owner to reapprove them.
