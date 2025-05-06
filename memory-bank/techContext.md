# Tech Context: DeepResearch Workflow Automation for Cline

**Technologies Used:**

- **Markdown:** Primary format for reports and knowledge capture.
- **HTML, CSS, JavaScript:** Used for the separate web viewer component.
- **JSON:** Used for the `research_index.json` catalog file.
- **Python (potentially):** For helper scripts in `./scripts/` (e.g., `convert_html_to_markdown.py`).

**Development Setup:**

- **Cline AI Assistant Environment:** The core operating environment.
- **Custom `.clinerules`:** Configuration files that define the workflow and behavior.
- **VSCode:** The user's development environment.
- **Operating System:** Windows 11 (based on environment details).
- **Default Shell:** C:\Windows\System32\cmd.exe (based on environment details).
- **Current Working Directory:** c:/Users/machi/OneDrive/Documents/wojons/projects/DeepResearch (based on environment details).
- **Project Structure:**
  - `/.clinerules/`: Contains the rule files that define the workflow.
  - `/index/`: Contains the JSON index files (`source_index.json`, `research_index.json`).
  - `/memory-bank/`: Contains the Memory Bank files for project context.
  - `/reports/`: Contains the research task folders (excluded from Git).
  - `/scripts/`: Contains helper scripts for the workflow.
  - `/test/`: Contains test files.
  - Root: Contains the HTML viewer files and project configuration files.

**Technical Constraints:**

- **LLM Capabilities:** Final report quality and depth are dependent on the underlying LLM's ability to analyze and synthesize information.
- **Automation Reliability:** Specific automated rules (like the JSON index update and potentially memory saving) have proven unreliable.
- **Token Usage:** Complex research tasks with deep source analysis can lead to high token consumption.
- **File Access:** Limited to allowed directories (current working directory and potentially others configured for MCP servers).
- **Tool Availability:** Dependent on the tools exposed by the Cline environment and connected MCP servers.

**Dependencies:**

- **Cline AI Assistant:** The fundamental platform.
- **Underlying LLM:** Provides the core text generation and analysis capabilities.
- **MCP Servers:** Provide additional tools (e.g., filesystem access, web search, markdown conversion).

**Tool Usage Patterns:**

- **`execute_command`:** Used for system operations like creating directories and moving files. Requires user approval for impactful operations.
- **`write_to_file`:** Used for creating and overwriting files (reports, knowledge, rules, viewer files).
- **`read_file`:** Used for examining file contents (rules, prompts, knowledge, index).
- **`search_files`:** Can be used for finding files or patterns within the project.
- **`browser_action`:** Can be used for interacting with web pages (research sources, testing the viewer).
- **`use_mcp_tool`:** Used for accessing capabilities provided by connected MCP servers (e.g., brave search, filesystem operations, markdown conversion).
- **`ask_followup_question`:** Used to gather necessary information from the user.
- **`attempt_completion`:** Used to present the final result of a task.
- **`suggest_tool_code`:** Used by rules to propose tool executions for user review.
- **Memory Bank Tools (`add_memory`, `@memory`):** Attempted for context management and knowledge retention.
