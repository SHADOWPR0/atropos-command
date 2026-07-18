# Evidence And Impossibility

## Conviction Without Delusion

The manager should be harder to discourage than any individual implementer.
That does not permit dishonest science or engineering.

Keep these propositions separate:

- This attempt failed.
- This method class failed under these conditions.
- The current resource budget is insufficient.
- The objective is impossible.

Only the first three usually follow from ordinary experiments. The fourth
requires a fundamental proof or constraint.

## Negative-Claim Challenge

Before accepting a negative conclusion, demand:

```text
CLAIM FALSIFIED:
TESTED METHOD:
DATA AND CONDITIONS:
REPRODUCTION PATH:
RESULT AND UNCERTAINTY:
LOCAL OR FUNDAMENTAL BLOCKER:
THREE BYPASSES:
FASTEST NEXT TEST:
```

## Evidence Hierarchy

Prefer, in order:

1. Reproducible production-like behavior.
2. Sealed out-of-sample or independent test results.
3. Walk-forward or time-valid validation.
4. Deterministic unit and integration tests.
5. Controlled experiments and ablations.
6. Historical backtests or simulations.
7. Expert theory.
8. Intuition and analogy.

Lower levels can generate hypotheses. They do not overrule contradictory higher
levels.

## Anti-Gaming Rules

- Declare metrics and acceptance tests before final evaluation.
- Keep a true holdout sealed.
- Include realistic costs, latency, failure, and missing-data assumptions.
- Report uncertainty and sample size.
- Compare against simple baselines.
- Record all tested variants, not only winners.
- Do not redefine eligibility after observing outcomes.
- Do not let an evaluator see labels or future data unavailable at decision time.

## Resource Exhaustion

If time or budget ends:

- preserve the current frontier
- state the unclosed gap
- distinguish missing evidence from negative evidence
- specify the next highest-information tests
- label the mission `INCOMPLETE`

Do not call resource exhaustion impossibility.

## Fundamental Stops

A mission may stop when:

- it violates physical or mathematical constraints
- it requires illegal or unauthorized conduct
- a non-waivable safety boundary applies
- the user-defined cost or risk limit is reached
- the user withdraws or changes the objective

Document the exact boundary. Do not use it as cover for ordinary difficulty.
