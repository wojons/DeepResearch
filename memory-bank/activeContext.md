# Active Context: DeepResearch Workflow Automation for Cline

**Current work focus:**

- Stabilizing the project direction and workflow.
- Setting up and populating the core Memory Bank files to serve as a central source of truth.
- Preparing to test the core research workflow with the latest, demanding rules.
- **Reviewing and integrating relevant Fabric patterns to enhance research capabilities.**

**Recent changes:**

- Refined `.clinerules/research_process.md` to mandate per-section deep research (~5-7 sources/subsection) and specific professional writing styles (prose over bullets).
- Added automated Memory Bank querying at the start of tasks (`research_process.md`).
- Added an attempt at automated saving of the final report summary to Memory Bank (`memory_management.md`).
- Replaced the unreliable `update_research_index.md` rule with a dedicated Python script (`scripts/update_research_index.py`).
- Added `/reports/` to `.gitignore` to prevent research outputs from being committed to the main repository.
- Reorganized project files:
  - Moved script files (`convert_html_to_markdown.py`, `update_index.py`) to the `scripts/` directory.
  - Moved `research_index.json` to the `index/` directory alongside `source_index.json`.
  - Created a `test/` directory for test files.
  - Removed empty directories (`DeepResearch_reports/`, `user_knowlage/`, `viewer/`).
- Deleted the redundant `html_generation_rule.md` for task-specific HTML.
- Created the basic HTML viewer structure and moved its files (`index.html`, `style.css`, `script.js`) to the project root.
- Generated design documentation (PR/FAQ, Statedumps).
- Committed all changes to the git repository and pushed to the remote repository (GitHub).
- **Reviewed all patterns in `fabric-patterns/` and selected relevant ones for the DeepResearch workflow.**
- **Created the `.prompts/patterns/` directory.**
- **Copied selected patterns into `.prompts/patterns/`.**
- **Updated `.prompts/CDR-PAA.md` to guide users on leveraging available patterns.**

**Pattern Review and Selection:**

- Conducted a comprehensive review of all patterns in the `fabric-patterns/` directory based on their names, descriptions in `pattern_explanations.md`, and the content of their `system.md` and `user.md` files.
- Criteria for selection focused on patterns that directly support the core DeepResearch functions: research, information extraction, analysis, summarization, and report writing/improvement.
- The following patterns were selected and copied to `.prompts/patterns/`:
    - `summarize`: General summarization.
    - `extract_ideas`: Extracting core concepts.
    - `extract_wisdom`: Comprehensive insight and fact extraction.
    - `extract_recommendations`: Extracting actionable recommendations.
    - `analyze_paper`: Analyzing academic papers.
    - `analyze_prose`: Evaluating and improving writing quality.
    - `improve_prompt`: Refining research prompts.
    - `extract_references`: Extracting source references.
    - `find_logical_fallacies`: Analyzing arguments for fallacies.
    - `humanize`: Refining report language.
    - `summarize_lecture`: Summarizing lecture transcripts.
    - `summarize_paper`: Summarizing academic papers.
    - `summarize_prompt`: Summarizing prompts.
    - `md_callout`: Formatting reports with callouts.
- Patterns not selected were deemed less relevant to the core DeepResearch workflow.

**Next steps:**

- Complete the population of the core Memory Bank files (currently populating `activeContext.md`).
- Use the populated Memory Bank as the primary reference for project context.
- Test the core research workflow by running the demanding `v3` YouTube script prompt (with outline, keywords per section, high length targets) under the latest rules and leveraging the newly integrated patterns.
- Monitor the outcome of the test, particularly regarding report depth, writing style, token usage, and the reliability of automated Memory Bank interactions.
- Based on the test results, identify areas for further refinement in the rules or process.
- Potentially revisit the `research_index.json` update process or explore alternative indexing/cataloging methods if needed.
- **Create the automation rule for pattern management.**
- **Update the design documentation with the pattern review summary.**

**Active decisions and considerations:**

- Prioritizing the stabilization of the core research workflow and Memory Bank setup before addressing less critical features like the JSON index automation.
- Acknowledging the known unreliability of certain automation attempts and planning to monitor their performance during testing.
- Being mindful of potential high token usage with the demanding research requirements.
- Using the Memory Bank as the primary source of project context going forward.
- **Leveraging relevant Fabric patterns to enhance the quality and efficiency of the research process.**

**Learnings and project insights:**

- Iterative refinement of rules is necessary to achieve desired output quality.
- Automation within the current environment can be unreliable and requires careful testing and potential workarounds.
- Clear and detailed prompts, especially with outlines and section-specific guidance, are crucial for guiding LLM behavior in complex tasks.
- The importance of a central, reliable source of project context (the Memory Bank) has become evident through the iterative development process.
- **A wide range of existing patterns can be adapted and integrated to enhance specific aspects of a complex workflow like DeepResearch.**
