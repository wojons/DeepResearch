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
- **Integration of Fabric Patterns:** Incorporating relevant patterns from `fabric-patterns/` into the workflow to enhance specific research and analysis tasks.

**Design Patterns in Use:**

- **Rule-Based System:** The core workflow is driven by `.clinerules`.
- **Pipeline/Workflow:** The research process is defined as a sequence of steps (Understand/Plan, Gather, Analyze/Synthesize, Generate Output).
- **Information Repository:** The `knowledge/` directory and potentially the Memory Bank act as repositories for gathered information.
- **Indexing:** The `research_index.json` serves as an index for completed reports.
- **Leveraging Specialized Tools:** Utilizing selected Fabric patterns as specialized tools within the research process.

**Selected Fabric Patterns for DeepResearch:**

The following patterns from `fabric-patterns/` have been identified and integrated into the DeepResearch workflow to provide specialized capabilities:

-   `summarize`: Used for generating general summaries of research sources or sections of the report.
-   `extract_ideas`: Utilized to extract core concepts and key ideas from source materials.
-   `extract_wisdom`: Employed for comprehensive extraction of detailed insights, facts, quotes, and recommendations from research sources.
-   `extract_recommendations`: Focused on extracting actionable recommendations from research content.
-   `analyze_paper`: Specifically used for analyzing the structure, methodology, and findings of academic papers.
-   `analyze_prose`: Applied to evaluate and improve the writing quality of the generated research reports, ensuring adherence to the professional prose standard.
-   `improve_prompt`: Used by the CDR-PAA to refine the prompts given to Cline for research tasks.
-   `extract_references`: Utilized to extract source references from gathered research materials.
-   `find_logical_fallacies`: Can be used to analyze arguments within sources for logical soundness.
-   `humanize`: Potentially used to refine the language of the final report for better readability.
-   `summarize_lecture`: Useful for processing and summarizing transcripts from video or audio research sources.
-   `summarize_paper`: Another pattern for summarizing academic papers, providing an alternative or supplementary approach to `analyze_paper`.
-   `summarize_prompt`: Used for creating concise summaries of the research prompts themselves.
-   `md_callout`: Can be used to format and highlight important information within the research reports.

**Component Relationships:**

-   **Cline AI Assistant:** The execution engine.
-   **`.clinerules`:** Guides Cline's actions and workflow.
-   **User Prompts:** Initiate tasks and provide specific instructions (outline, keywords), potentially including instructions for pattern usage.
-   **Standardized Task Folders:** Output location and organization for research artifacts.
-   **Sources (`sources/citations.md`):** Document consulted external information.
-   **Knowledge (`knowledge/`):** Stores converted source content.
-   **Selected Fabric Patterns (`.prompts/patterns/`):** Specialized tools used by Cline during the research process as instructed in the prompt.
-   **Report (`report.md`):** The primary synthesized output, potentially enhanced by pattern usage.
-   **`research_index.json`:** Catalogs reports for the Viewer.
-   **HTML Viewer:** Separate component that consumes `research_index.json`.
-   **Memory Bank:** Provides context and potentially stores summaries across tasks.
-   **Scripts (`scripts/`):** External tools potentially used by Cline via `execute_command`.
