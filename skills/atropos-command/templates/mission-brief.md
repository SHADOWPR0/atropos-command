# Atropos Command Mission Brief

Replace bracketed fields. Infer what is obvious; ask only for unresolved fields
that materially affect safety or acceptance.

```yaml
mission:
  name: "[MISSION_NAME]"
  statement: "[ONE_SENTENCE_MISSION]"
  deadline: "[DEADLINE_OR_CONTINUOUS]"

success:
  primary_metric: "[PRIMARY_METRIC]"
  target: "[NON_NEGOTIABLE_TARGET]"
  baseline: "[CURRENT_BASELINE]"
  acceptance_test: "[REPRODUCIBLE_PASS_FAIL_TEST]"
  evaluation_scope: "[DATASET_PERIOD_USERS_OR_ENVIRONMENT]"

workspaces:
  manager_control_plane: "[OPTIONAL_MANAGER_DIRECTORY]"
  supervised:
    - name: "[WORKSTREAM_A]"
      directory: "[WORKING_DIRECTORY_A]"
      role: "[RESEARCH_BUILD_VERIFY_OR_OPERATE]"
    - name: "[WORKSTREAM_B]"
      directory: "[WORKING_DIRECTORY_B]"
      role: "[RESEARCH_BUILD_VERIFY_OR_OPERATE]"

inputs:
  canonical:
    - "[INPUT_OR_SOURCE_1]"
    - "[INPUT_OR_SOURCE_2]"
  derived:
    - "[DERIVED_INPUT_IF_ANY]"

outputs:
  required:
    - "[ARTIFACT_1]"
    - "[ARTIFACT_2]"
  final_handoff: "[HANDOFF_FORMAT]"

permissions:
  allowed:
    - "[ALLOWED_ACTION_OR_PATH]"
  forbidden:
    - "[FORBIDDEN_ACTION_OR_PATH]"
  human_approval_required:
    - "[DEPLOYMENT_CAPITAL_SECRETS_DELETION_OUTREACH_OR_OTHER]"

resources:
  maximum_parallel_lanes: 4
  time_budget: "[TIME_BUDGET]"
  compute_budget: "[COMPUTE_BUDGET]"
  external_cost_budget: "[COST_BUDGET]"

governance:
  independent_verification: true
  checkpoint_path: "[OPTIONAL_CHECKPOINT_PATH]"
  stop_conditions:
    - "[TRUE_SAFETY_COST_ORFUNDAMENTAL_STOP]"
  escalation_owner: "[HUMAN_OWNER]"
```

## Launch Instruction

```text
Initiate Atropos Command using this mission brief.
Keep the target fixed, delegate bounded implementation, independently verify
consequential claims, and continue until the acceptance test passes or a stated
human approval gate blocks progress.
```
