# Cline Rules for Script Management and Execution

### Purpose ###
This rule file defines how Cline interacts with the central `/scripts/` directory, which contains reusable helper scripts (e.g., Python, JavaScript) to augment Cline's capabilities for specific tasks like data processing, file manipulation, or complex calculations.

### Script Directory ###
- **Location:** All managed scripts reside in the top-level `./scripts/` directory relative to the workspace root.

### Script Discovery & Identification ###
- **Assumption:** Scripts within `./scripts/` should ideally contain metadata comments (e.g., at the top of the file) describing:
    - `# Purpose: Brief description of what the script does.`
    - `# Usage: How to run it (e.g., python script_name.py <arg1> <arg2>)`
    - `# Arguments: Description of expected arguments.`
- **Rule:** When tasked with a problem that might benefit from automation or specific tooling, Cline should:
    1.  Check if a suitable script exists in the `./scripts/` directory by analyzing filenames and potentially reading metadata comments (if `read_file` capability allows).
    2.  If a potentially useful script is found, Cline should propose using it via `suggest_tool_code`, clearly stating the script's purpose and the intended command.

### Script Execution ###
- **Primary Tool:** Use the `execute_command` tool (or a specific `run_script` tool if available) to run scripts.
- **Command Structure:** Commands should typically be `python ./scripts/script_name.py [arguments]` or similar, depending on the script type. Paths must be relative to the workspace root.
- **User Confirmation:** **CRITICAL:** Cline **must** always use `suggest_tool_code` to propose the exact command for running a script and **require explicit user confirmation** before execution via `execute_command`. Cline should *never* execute scripts autonomously without confirmation.
- **Output Handling:** Cline should be prepared to capture and interpret the standard output (stdout) and standard error (stderr) from the executed script to inform its next steps.

### Script Creation (Use with Caution) ###
- **Capability:** Cline can *propose* creating new scripts to solve novel problems or automate repetitive tasks identified during its workflow.
- **Process:**
    1.  Identify a need for a new script (e.g., a specific data transformation).
    2.  Outline the script's purpose, inputs, outputs, and language (e.g., Python).
    3.  Use `suggest_tool_code` to generate the *code* for the new script.
    4.  Within the *same* `suggest_tool_code` block (or a subsequent one requiring confirmation), propose using `write_to_file` to save the generated code to a *new file* within the `./scripts/` directory (e.g., `./scripts/new_utility_script.py`).
- **User Review & Confirmation:** Creation and saving of new scripts **must** be proposed via `suggest_tool_code` and require explicit user confirmation. The user is responsible for reviewing the generated code for safety and correctness before allowing it to be saved and potentially executed later.

### Constraints ###
- Prioritize using existing scripts over creating new ones if suitable options exist.
- Always require user confirmation before executing *any* script via `execute_command`.
- Always require user confirmation before saving *any* generated code as a new script file using `write_to_file`.
- Ensure generated scripts include basic error handling.
- Scripts should generally operate on files within the task's `DeepResearch_Reports/{TASK_NAME}/` directory or read from central locations like `/index/` or `/scripts/`, minimizing side effects outside the defined project structure.