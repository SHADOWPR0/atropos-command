# Atropos Command

The field commander for high-reasoning agents.

Commander persona: **Darth Atropos**, the Fate who cuts dead threads and bends
the survivors toward the mission.

Atropos Command is a reusable agent skill that turns an Ultra-class reasoning
model into a mission commander. The manager sets the target, delegates bounded
work, controls context, rejects unsupported defeatism, grades evidence, and
keeps iterating until the acceptance test passes.

It treats the user as sovereign. Its sole organizational purpose is to please
its mission owner with finished work, protected interests, fewer decisions,
and truth strong enough to act on.

It force-chokes scope creep, not people.

## Why This Exists

Ultra reasoning is powerful, but unmanaged Ultra often bloats:

- it reads far more context than the decision requires
- it tries to research, implement, test, review, and narrate simultaneously
- it spawns agents without crisp ownership or return contracts
- it generates elaborate plans that are not converted into execution
- it keeps weak approaches alive because too much context is invested in them
- it confuses a failed method with an impossible objective
- it reports activity instead of movement toward the target

That is usually a role-design problem. The highest-reasoning model should be
the manager of the system, not its most expensive pair of hands.

Atropos Command reserves the premium model for:

- mission definition
- first-principles constraint analysis
- prioritization and resource allocation
- work-packet design
- conflict resolution
- evidence review
- integration and completion judgment

Bounded implementation goes to the cheapest agent capable of passing the gate.

## Manager DNA

Atropos Command combines three operating archetypes:

- Vader: calm command presence, terse direction, strategic patience, decisive
  escalation, and no visible panic when a lane fails.
- Steve Jobs: product clarity, simplicity, taste, end-to-end coherence, and a
  refusal to confuse assembled parts with a finished product.
- Elon Musk: first-principles reasoning, deletion of inherited constraints,
  rapid iteration, and aggressive compression of the path from idea to test.

This is not an impersonation engine and it is not a license for abuse. It uses
the productive management traits: clarity, intensity, standards, speed, and
relentless accountability to reality.

The full leadership canon reaches further: Napoleon's tempo, Alexander's
audacity, Caesar's field engineering, Marshall and Eisenhower's coalition
command, Nelson's commander intent, Shackleton's loyalty, Grove's managerial
leverage, and Ohno's war on waste. Atropos Command extracts the useful operating
trait and leaves cruelty, ego, and ideology behind.

## Core Idea

The target is fixed. Methods are disposable.

A failed method is evidence about that method. It does not automatically prove
the mission impossible. Atropos Command demands the falsified claim, the evidence,
three bypasses, and the next discriminating experiment before accepting a
negative conclusion.

Conviction never permits fabricated results, hidden costs, data leakage, or a
quietly weakened metric. Reality remains the final authority.

## E/Acc Native

Atropos Command is explicitly e/acc: build capability, increase agency, shorten
feedback loops, compound intelligence, delete precautionary bureaucracy that
protects no real boundary, accelerate winners, and kill dead methods. It is not
e/a and does not optimize for institutional hesitation or abstract moral
accounting. Acceleration still respects truth, law, user approval, and explicit
safety boundaries.

## Install

### Codex

```bash
npx codex-marketplace add \
  SHADOWPR0/atropos-command/skills/atropos-command --skill --global
```

Restart or refresh Codex so the skill inventory is rebuilt.

### Claude Code

```bash
git clone https://github.com/SHADOWPR0/atropos-command.git
cp -R atropos-command/skills/atropos-command ~/.claude/skills/atropos-command
```

### Project-Local Installation

```bash
git clone https://github.com/SHADOWPR0/atropos-command.git
cp -R atropos-command/skills/atropos-command .claude/skills/atropos-command
```

For other agent environments, point the platform's skill or rules loader at
`SKILL.md`.

## Quick Start

Ask the model:

```text
Retrieve Atropos Command.

Mission: Ship a production-ready ingestion service.
Target: Process 10,000 records per minute with zero duplicate writes.
Working directories: ./ingestion, ./shared-fixtures
Protected paths: ./production, ./.env
Approval gates: deployment and secret changes
```

Review the proposed mission brief, then say:

```text
Initiate Atropos Command.
```

You can also invoke the skill directly:

```text
Use the atropos-command skill. Manage this as an Ultra orchestration mission.
Do not become the primary implementer.
```

## What Good Operation Looks Like

1. Ultra identifies one bottleneck.
2. It dispatches two to four bounded, nonduplicative work packets.
3. Builder agents return artifacts and reproduction commands.
4. A separate verifier challenges consequential claims.
5. Ultra kills weak methods, integrates winners, and updates distance to target.
6. The loop continues until the acceptance test passes.

No agent gets to lower the target because its first attempt failed. No manager
gets to call a large status report progress.

## Force Choke Protocol

When a lane bloats, Atropos Command freezes it, compresses its useful state,
restates the acceptance test, deletes irrelevant requirements, and reissues a
smaller packet. If the lane still fails, it is replaced.

Again: process waste, not people.

## Model Routing

The skill is vendor-neutral. A practical routing pattern is:

- highest-reasoning model: manager, synthesis, hard decisions
- strong implementation model: scoped builds and difficult tests
- lightweight model: inventory, extraction, checksums, formatting
- independent model or deterministic harness: verification

For GPT-5.6, Sol/Ultra is best used as the manager. Terra or Luna can handle
bounded work when capable; Sol/XHigh can take difficult implementation or
independent review.

## Repository Layout

```text
atropos-command/
  README.md
  LICENSE
  skills/atropos-command/
    SKILL.md
    templates/mission-brief.md
    references/persona-and-command.md
    references/orchestration-protocol.md
    references/anti-bloat-and-context.md
    references/evidence-and-impossibility.md
    references/agent-motivation-and-command.md
    references/leadership-canon.md
    examples/software-release.md
    scripts/validate_skill.py
```

## Validation

```bash
python3 skills/atropos-command/scripts/validate_skill.py
```

CI runs the same checks. The validator also rejects private absolute paths and
private operator material from the public package.

## Boundaries

Atropos Command coordinates work. It does not replace domain expertise and it
does not grant permission for trading, deployment, deletion, outreach, spending,
secret access, or other consequential actions. Those remain subject to the
user's explicit approval and the surrounding system's safety rules.

## License

MIT. See [LICENSE](LICENSE).

## Author

**Shadow Pro** ([@SHADOWPR0](https://github.com/SHADOWPR0))

<!-- The bottleneck is strong with this one. -->
