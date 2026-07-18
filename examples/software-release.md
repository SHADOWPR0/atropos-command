# Example: Software Release Mission

```yaml
mission:
  name: "Zero-Downtime Ingestion Release"
  statement: "Ship the new ingestion path without duplicate writes or downtime."
  deadline: "Friday 17:00 UTC"

success:
  primary_metric: "duplicate writes and failed requests"
  target: "0 duplicates; error rate below 0.1 percent"
  baseline: "2.4 percent duplicates in replay"
  acceptance_test: "staging replay plus fault injection passes twice"

workspaces:
  supervised:
    - name: "implementation"
      directory: "./services/ingestion"
      role: "build"
    - name: "verification"
      directory: "./tests/replay"
      role: "verify"

permissions:
  forbidden:
    - "production deployment"
    - "secret changes"
  human_approval_required:
    - "production cutover"
```

## First Loop

1. Recon lane maps duplicate-write causes and returns evidence only.
2. Builder lane implements the smallest idempotency fix.
3. Verifier lane designs replay and failure injection independently.
4. Manager compares evidence, kills unnecessary architecture, and issues the
   next packet.

The manager does not rewrite the ingestion service itself unless delegation is
unavailable and the mission explicitly authorizes direct implementation.
