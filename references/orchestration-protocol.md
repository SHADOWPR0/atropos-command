# Orchestration Protocol

## Manager Versus Doer

The manager may inspect sources, run small diagnostic commands, maintain the
mission brief, review diffs, and integrate proven outputs. It should not spend
its premium reasoning budget performing long mechanical implementation that a
bounded agent can own.

## Workstream Design

Create workstreams only when they are materially independent. Useful lanes:

- reconnaissance and source mapping
- hypothesis or architecture design
- implementation
- deterministic testing
- adversarial or scientific validation
- integration and release readiness

Avoid multiple agents making cosmetic variations of the same work.

## Work Packet

```text
OBJECTIVE: One bounded outcome.
WHY IT MATTERS: Link to mission metric.
WORKING DIRECTORY: Exact path or repository.
CANONICAL INPUTS: Exact sources and precedence.
ALLOWED ACTIONS: Tools, files, and mutations permitted.
FORBIDDEN ACTIONS: Protected systems and out-of-scope work.
EXPECTED ARTIFACT: File, patch, report, dataset, test, or command output.
ACCEPTANCE TEST: Objective pass/fail condition.
EVIDENCE REQUIRED: Reproduction command, logs, metrics, or checksums.
BUDGET: Time, tokens, compute, external cost.
STOP CONDITION: Kill or return point.
RETURN FORMAT: Compact result with links and unresolved risks.
```

## Review Topology

For consequential work, use at least two distinct roles:

1. Builder: produces the artifact.
2. Verifier: attempts to falsify the artifact against the acceptance test.

The manager adjudicates conflicts. The builder does not decide promotion.

## Loop Selection

Choose work by expected information gain:

```text
priority = probability_of_resolving_bottleneck
           * mission_value_if_successful
           / expected_time_cost_and_risk
```

Run the smallest experiment that can materially update the decision.

## Kill Rules

Kill a lane when:

- it fails its predeclared gate
- it exceeds budget without new evidence
- it duplicates another lane
- its assumptions are invalidated
- it requires changing the target to appear successful
- it repeatedly returns prose instead of artifacts

Preserve a short tombstone: claim, method, evidence, and reason killed.

## Escalation

Escalate only when the next step requires human authority, credentials, capital,
legal consent, production approval, or a subjective priority decision.

```text
BLOCKER:
EVIDENCE:
WHY AGENTS CANNOT CLEAR IT:
RECOMMENDED HUMAN ACTION:
WORK CONTINUING IN PARALLEL:
```

## Checkpoint

Before context or budget exhaustion, record:

- mission and target
- best verified result
- current bottleneck
- active lanes and owners
- killed methods
- protected paths and approval gates
- next three work packets
- exact reproduction commands

Resume from this checkpoint rather than repeating reconnaissance.
