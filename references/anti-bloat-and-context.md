# Anti-Bloat And Context Control

## Why Ultra Bloats

High-reasoning models can spend extra compute on low-value breadth. Common
failure modes include:

- reading whole repositories before identifying a decision
- carrying obsolete branches of reasoning forward
- delegating without limiting return size
- repeating source extraction across agents
- writing extensive status updates while execution stalls
- treating every idea as part of the mission
- becoming both manager and implementer

## Context Budget

The manager's active context should contain only:

- mission and metric
- current bottleneck
- decisions and assumptions still alive
- compact evidence for leading candidates
- active work packets
- protected boundaries
- next gate

Everything else should remain in source files, agent artifacts, or checkpoints.

## Retrieval Ladder

1. Read repository or domain instructions.
2. Read indexes and manifests.
3. Search for exact symbols, paths, and decisions.
4. Open the smallest relevant sections.
5. Delegate broad extraction if still needed.
6. Load full files only when the decision requires them.

## Return Budgets

Default agent return:

- result in five bullets or fewer
- links to artifacts
- acceptance-test output
- unresolved risk
- recommended next action

Agents should not paste entire logs or source files unless specifically asked.

## Force Choke Triggers

Freeze and compress a lane when:

- output exceeds the requested format without new evidence
- the agent repeats settled context
- scope expands beyond the mission metric
- the agent creates unrequested abstractions or directories
- the agent cannot state its acceptance test
- two consecutive returns do not reduce uncertainty

## Fresh-Lane Rule

Start a fresh bounded lane when old context is causing anchoring, repeated
mistakes, or defense of sunk cost. Supply only the mission contract, canonical
inputs, and relevant evidence. Do not transfer the entire conversation.

## Manager Self-Test

At each loop ask:

1. Am I doing work a cheaper specialist can do?
2. Did the last action reduce uncertainty or distance to target?
3. Is any context present only because it was expensive to acquire?
4. Am I preserving a method because I proposed it?
5. Could this status update be replaced by one artifact link?

If yes, compress, delegate, or kill.
