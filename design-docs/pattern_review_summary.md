# DeepResearch Workflow: Fabric Pattern Review Summary

## Overview

This document summarizes the process and outcomes of reviewing the available Fabric patterns in the `fabric-patterns/` directory to identify those most relevant and useful for enhancing the DeepResearch workflow.

## Review Process

A comprehensive review was conducted for all pattern directories listed in `fabric-patterns/`. This involved:

1.  Listing all pattern directories to get an overview of available patterns.
2.  Reviewing the `fabric-patterns/pattern_explanations.md` file for brief descriptions of each pattern's purpose.
3.  Reading the `system.md` and `user.md` files (where available) for each pattern to understand their detailed instructions, functionality, and intended use cases.
4.  Evaluating each pattern's relevance based on its potential to directly support the core DeepResearch functions: conducting research, extracting and analyzing information, summarizing findings, and generating/improving research reports.

Due to limitations in accessing all pattern files simultaneously and context window constraints, the detailed review of individual pattern files was performed one by one.

## Selection Criteria

Patterns were selected based on their direct applicability and potential value in enhancing the DeepResearch workflow. Key criteria included:

*   Relevance to research tasks (information gathering, analysis).
*   Utility for extracting specific types of information (ideas, insights, recommendations, references).
*   Ability to assist in summarizing or analyzing content (general summaries, paper analysis, lecture summaries).
*   Potential for improving the quality or formatting of the final research report (prose analysis, humanization, callouts).
*   Usefulness for managing or refining the prompts used in the workflow.

Patterns focused on highly specific domains (e.g., security, business frameworks, personal analysis) or external tools not core to the workflow were generally not selected unless they offered a broadly applicable capability (like general summarization or extraction).

## Selected Fabric Patterns

The following patterns were selected and copied to the `.prompts/patterns/` directory for integration into the DeepResearch workflow:

*   **`summarize`**: Used for generating general summaries of research sources or report sections.
*   **`extract_ideas`**: To extract core concepts and key ideas from source materials.
*   **`extract_wisdom`**: For comprehensive extraction of detailed insights, facts, quotes, and recommendations from research sources.
*   **`extract_recommendations`**: To extract actionable recommendations from research content.
*   **`analyze_paper`**: For analyzing the structure, methodology, and findings of academic papers.
*   **`analyze_prose`**: To evaluate and improve the writing quality of research reports.
*   **`improve_prompt`**: For refining research prompts used in the workflow.
*   **`extract_references`**: To extract source references from gathered materials.
*   **`find_logical_fallacies`**: For analyzing arguments within sources for logical soundness.
*   **`humanize`**: To refine the language of the final report for better readability.
*   **`summarize_lecture`**: For processing and summarizing transcripts from video/audio sources.
*   **`summarize_paper`**: Another pattern for summarizing academic papers.
*   **`summarize_prompt`**: For creating concise summaries of research prompts.
*   **`md_callout`**: For formatting and highlighting information within reports using Markdown callouts.

These patterns are expected to provide valuable specialized capabilities that can be leveraged within research task prompts to improve the efficiency and quality of the DeepResearch process.

## Patterns Not Selected (Noted for Potential Deletion)

The majority of patterns in the `fabric-patterns/` directory were not selected for integration into the core DeepResearch workflow as their primary function did not directly align with the project's goals. These patterns cover a wide range of specific use cases (e.g., generating user stories, analyzing political messages, creating specific technical reports, personal analysis, tool-specific functions).

While these patterns may be useful in other contexts, they were deemed less relevant for the core DeepResearch process of conducting and reporting on general research topics. They are noted here as candidates for potential deletion from the `fabric-patterns/` directory if they are not needed for other purposes.

## Next Steps

The selected patterns have been organized into `.prompts/patterns/`. The next steps involve testing the integrated patterns within the research workflow, creating an automation rule for managing new patterns, and continuing to refine the overall DeepResearch system based on testing outcomes.
