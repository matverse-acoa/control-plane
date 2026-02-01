---
# README — Atlas Deploy Control Plane

## Overview

Atlas Deploy is a deterministic execution circuit designed to ingest repository artifacts, validate admissibility, execute registered motors, and generate cryptographically signed evidence.

The system exists to guarantee that every deployment is

* deterministic
* replayable
* verifiable
* cryptographically sealed

No execution occurs without evidence.

No evidence exists without signature.

No signature exists without a reproducible state.

---

## Architectural Role

Atlas Deploy belongs to the **execution domain** of the MatVerse stack and operates strictly below constitutional authority layers.

Authority never flows upward.

```
Atlas → Papers → Core → PBSE → QEX → Runtime → Deploy Circuit
```

The deploy circuit executes.

It never governs.

It never defines truth.

It materializes approved state transitions.

---

## Execution Circuit

Every deployment follows a closed proof cycle:

```
INPUT → VALIDATION → MOTOR → VERIFICATION → SIGNATURE → EVIDENCE
```

### Stages

**IA-RECEIVE**
Validates payload structure and motor registration.

**IA-ADMIN**
Generates deterministic task hash and prepares execution.

**MOTOR**
Executes inside controlled boundaries.
Arbitrary code is never allowed.

**ADMIN-VERIFY**
Validates:

* exit status
* structural schema
* output presence
* deterministic constraints

**IA-CLOSE**
Produces:

* result hash
* merkle leaf
* NaCl signature
* evidence note

---

## Security Model

### Registered Motors Only

Execution is restricted to motors declared in the registry.

This prevents total system compromise via arbitrary subprocess calls.

### Evidence-First Order

The circuit enforces the following sequence:

```
Merkle → Signature → Storage → (Optional) Blockchain Anchor
```

Blockchain is temporal anchoring — never the primary source of truth.

### Artifact Sanitization (MANDATORY)

Deployments must exclude sensitive metadata:

```
.git
.gitignore
__pycache__
*.pyc
.env
*.key
```

Publishing repository history is considered a structural security failure.

---

## Deterministic Deploy Requirement

Deployments must originate from immutable commit states.

Never deploy from a live directory.

Correct model:

```
git archive --format=zip --output=repo.zip <commit-sha>
```

Evidence must always be traceable to a Git object.

Without this property, scientific auditability collapses.

---

## Evidence Schema

Each execution produces a signed Evidence Note:

```
timestamp
motor
task_hash
result_hash
merkle_leaf
signature
verify_key
exit_code
stdout
(optional) blockchain_anchor
```

Evidence is the primary operational memory of the system.

Logs are not proof.

Evidence is.

---

## Operational Guarantees

* Fail-closed execution
* Append-only evidence store
* Deterministic replay capability
* Cryptographic verification
* Separation between decision and execution

If two executions diverge under identical inputs, the system is considered invalid.

---

## Known Failure Class — “Ghost State”

Execution without public state materialization is treated as a critical fault.

Formal definition:

```
execution ≠ state_transition
```

Deploy success is recognized only when evidence **and** public artifacts agree.

---

## Hardening Checklist (Non-Optional)

Before production freeze:

* enforce commit-based deploys
* store ZIP checksum inside evidence
* pin cryptographic dependencies
* require absolute paths
* version motors constitutionally

Expansion before hardening is strongly discouraged.

Durable systems grow after becoming rigid.

---

## What This System Is

Atlas Deploy is not a CI helper.

It is not a documentation tool.

It is an execution protocol capable of producing verifiable computational history.

The system does not ask:

“Did it work?”

It asks:

“Can it be proven?”

Crossing this boundary transforms software into epistemic infrastructure.

---

## Status

Regime: Candidate
Execution Model: Deterministic
Evidence: Signed (NaCl)
Replay: Supported

System readiness is no longer constrained by technology — only by structural hardening.

---
