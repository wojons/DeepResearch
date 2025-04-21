# Standard Research Task Folder Structure

When starting a new research task named {RESEARCH_TASK_NAME}:

1.  **Ensure Primary Output Folder Exists:** Check if the `./reports/` directory exists at the root level. If not, create it. (Confirm path based on workspace root).
2.  **Create Task-Specific Folder:** Create the task folder inside the primary output folder: `./reports/{RESEARCH_TASK_NAME}/`.
3.  **Create Subfolders:** Within the task-specific folder, create the standard subdirectories:
    * `./reports/{RESEARCH_TASK_NAME}/prompts/`
    * `./reports/{RESEARCH_TASK_NAME}/sources/`
    * `./reports/{RESEARCH_TASK_NAME}/knowledge/`

Confirm paths before creation using `execute_command`. Assume paths are relative to the workspace root unless specified otherwise.