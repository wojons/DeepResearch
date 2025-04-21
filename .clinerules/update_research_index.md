# Rule to update the central research_index.json using suggest_tool_code
# Trigger after the main report.md is successfully written in its correct location
when tool_used("write_to_file") and tool_params_contain_path_segment("reports/{RESEARCH_TASK_NAME}/report.md"):
  # Step 1: Ask the user for the necessary metadata
  suggest_task """
  The main report file at `reports/{RESEARCH_TASK_NAME}/report.md` has been saved.

  To update the central `./index/research_index.json` file, I need the following details for the new entry:
  1.  **Research Task Title** (For display purposes, can be same as name '{RESEARCH_TASK_NAME}' or slightly different):
  2.  **Current Date** (e.g., 2025-04-20):
  3.  **Brief Goal Summary** (A short description of the research task's objective):

  Please provide these details. Once I have them, I will propose the necessary tool code using `suggest_tool_code` for you to review and execute to update the index file located at `./index/research_index.json`.
  """
  apply_temperature 0.3

# Step 2: (Implied next step after user provides info via chat)
# The LLM should now use the user-provided info (Title, Date, Summary)
# and the known task name ({RESEARCH_TASK_NAME}) and report path
# (which triggered this rule, e.g., 'reports/{TASK_NAME}/report.md')
# to construct and suggest the tool code.

# Instruction for the LLM on how to act *after* getting user input from the suggest_task above:
# "Now that the user has provided the Title, Date, and Summary, construct the `suggest_tool_code`
# block to update the central index file. The tool code should:
# 1. Define the path to the index file: `./index/research_index.json`.
# 2. Define the new entry data including: task_name ('{RESEARCH_TASK_NAME}'), title, date, summary (from user input), and report_path ('reports/{RESEARCH_TASK_NAME}/report.md').
# 3. Read the current content of `./index/research_index.json`. Handle cases where the file doesn't exist or isn't valid JSON (initialize as an empty list []).
# 4. Check if an entry with the same task_name already exists. If yes, update it; otherwise, append the new entry to the list.
# 5. Write the updated list back to `./index/research_index.json` using indentation for readability.
# 6. Use appropriate error handling (e.g., try-catch blocks in JavaScript).
# Base the structure on the logic potentially found in `update_research_index.py` or similar examples."

# Example of how the LLM might generate the suggest_tool_code (internal logic):
# suggest_tool_code """
# // Tool code to update research_index.json
# const indexFilePath = "./index/research_index.json";
# const taskName = "{RESEARCH_TASK_NAME}";
# const reportPath = `reports/${taskName}/report.md`;
# const taskTitle = "{USER_PROVIDED_TITLE}"; // Placeholder
# const taskDate = "{USER_PROVIDED_DATE}";   // Placeholder
# const taskSummary = "{USER_PROVIDED_SUMMARY}"; // Placeholder
#
# try {
#   let indexData = [];
#   try {
#     const content = await read_file({ file: indexFilePath });
#     indexData = JSON.parse(content);
#     if (!Array.isArray(indexData)) {
#       console.warn('Index file is not an array, initializing.');
#       indexData = [];
#     }
#   } catch (e) {
#     console.warn(`Could not read or parse ${indexFilePath}, initializing: ${e.message}`);
#     indexData = [];
#   }
#
#   const newEntry = {
#     task_name: taskName,
#     title: taskTitle,
#     date: taskDate,
#     summary: taskSummary,
#     report_path: reportPath
#   };
#
#   let updated = false;
#   for (let i = 0; i < indexData.length; i++) {
#     if (indexData[i]?.task_name === taskName) {
#       indexData[i] = newEntry;
#       updated = true;
#       break;
#     }
#   }
#   if (!updated) {
#     indexData.push(newEntry);
#   }
#
#   await write_to_file({ file: indexFilePath, content: JSON.stringify(indexData, null, 2) });
#   console.log(`Successfully updated ${indexFilePath} for task ${taskName}`);
#
# } catch (error) {
#   console.error(`Error updating ${indexFilePath}: ${error.message}`);
# }
# """