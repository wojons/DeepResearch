# Cline Rules for Automated Memory Bank Management

# Rule 1: Attempt to Automatically Save Report Summary to Memory
# Trigger: After the main report.md is successfully written within its task folder.
# Goal: Automatically generate and store a concise summary of the task's findings in the central /index/ directory.
# WARNING: Automated summarization quality may vary. Ensure index directory exists.
when tool_used("write_to_file") and tool_params_contain_path_segment("./{RESEARCH_TASK_NAME}/report.md"):
  suggest_tool_code """
  // Report saved. Attempting to automatically summarize and save key findings to memory index.
  const taskName = "{RESEARCH_TASK_NAME}"; // Assumes available in context
  const reportPath = `./reports/${taskName}/report.md`;
  const memoryIndexPath = "./index/"; // Define the central index directory path

  try {
    // Step 1: Read the report content
    const reportContent = await read_file({ file: reportPath });

    // Step 2: Generate a concise summary (Requires LLM thought process)
    // This needs an internal LLM call/prompt to summarize reportContent effectively.
    // The exact implementation depends on Cline's capabilities.
    // Example prompt for internal summarization:
    // `Create a concise summary (max 2-3 sentences) of the key findings and conclusions presented in the following research report:\n\n${reportContent}`
    const summary = await generate_summary_llm(reportContent); // Placeholder for actual LLM call

    // Step 3: Prepare Memory/Index Entry (Structure TBD - example below)
    const memoryEntry = {
      task_name: taskName,
      summary: summary,
      report_path: reportPath, // Store relative path to report
      timestamp: new Date().toISOString()
    };

    // Step 4: Append/Update Memory Index File in /index/ directory
    // Assumes a function exists to handle reading, updating, and writing a JSON/other index file
    // located within the memoryIndexPath (e.g., './index/memory_bank.json').
    // This logic might resemble the update_research_index.py script but operate on the memory file.
    await update_memory_index({ index_dir: memoryIndexPath, entry: memoryEntry }); // Placeholder for actual function call

    console.log(`Successfully generated summary and updated memory index for task: ${taskName}`);

  } catch (error) {
    console.error(`Error during automated memory saving for task ${taskName}: ${error.message}`);
    // Optional: Notify user of failure?
  }
  """

# Helper function placeholders (assumed available via MCP server or built-in):
# async function generate_summary_llm(content) { /* internal LLM call */ }
# async function update_memory_index({ index_dir, entry }) { /* read/update/write index file in specified dir */ }
# async function read_file({ file }) { /* reads file content */ }