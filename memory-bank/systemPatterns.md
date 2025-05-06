# System Patterns: DeepResearch Workflow Automation for Cline

**System Architecture:**

The system is primarily a configuration and workflow layer built on top of the Cline AI assistant. It leverages Cline's core capabilities (tool use, file access, memory) guided by custom rules.

**Key Technical Decisions:**

- **Use of `.clinerules`:** Central to defining the multi-step research process, writing style mandates, and automation attempts.
- **Standardized Folder Structure:** A consistent directory structure (`{TASK_NAME}/{prompts, sources, knowledge, report.md}`) for each research task to ensure organization.
- **Markdown as Primary Format:** Reports (`report.md`) and captured knowledge are stored in Markdown for readability and compatibility.
- **JSON Indexes:**
  - `index/source_index.json`: For cataloging and reusing captured knowledge across tasks.
  - `index/research_index.json`: For cataloging completed tasks for the HTML viewer.
- **Memory Bank Integration:** Attempting to use Cline's built-in Memory Bank for context retention and querying.
- **Script Usage:** Using helper scripts in `./scripts/` for specific tasks:
  - `scripts/convert_html_to_markdown.py`: For converting web content to Markdown.
  - `scripts/update_research_index.py`: For updating the research index after report generation.

**Design Patterns in Use:**

- **Rule-Based System:** The core workflow is driven by `.clinerules`.
- **Pipeline/Workflow:** The research process is defined as a sequence of steps (Understand/Plan, Gather, Analyze/Synthesize, Generate Output).
- **Information Repository:** The `knowledge/` directory and potentially the Memory Bank act as repositories for gathered information.
- **Indexing:** The `research_index.json` serves as an index for completed reports.

**Component Relationships:**

- **Cline AI Assistant:** The execution engine.
- **`.clinerules`:** Guides Cline's actions and workflow.
- **User Prompts:** Initiate tasks and provide specific instructions (outline, keywords).
- **Standardized Task Folders:** Output location and organization for research artifacts.
- **Sources (`sources/citations.md`):** Document consulted external information.
- **Knowledge (`knowledge/`):** Stores converted source content.
- **Report (`report.md`):** The primary synthesized output.
- **`research_index.json`:** Catalogs reports for the Viewer.
- **HTML Viewer:** Separate component that consumes `research_index.json`.
- **Memory Bank:** Provides context and potentially stores summaries across tasks.
- **Scripts (`scripts/`):** External tools potentially used by Cline via `execute_command`.
