# Cline Rules for Automated Pattern Management

# Rule 1: Analyze New Fabric Patterns
# Trigger: When a new directory is added to the `fabric-patterns/` directory.
# Goal: Automatically analyze the new pattern and suggest whether to integrate it into the DeepResearch workflow.
# WARNING: This rule requires user approval for any suggested actions (copying or deleting patterns).
when directory_created("fabric-patterns/*"):
  // A new pattern directory has been detected in `fabric-patterns/`.
  const newPatternPath = event.path; // Path to the newly created directory

  console.log(`Analyzing new pattern: ${newPatternPath}`);

  // Step 1: Read the pattern's system.md and user.md (if exists)
  const systemMdPath = `${newPatternPath}/system.md`;
  const userMdPath = `${newPatternPath}/user.md`;
  const filePathsToRead = [systemMdPath];

  // Use a try-catch around reading user.md in case it doesn't exist
  try {
    const userMdContent = await read_file({ path: userMdPath });
    filePathsToRead.push(userMdPath);
  } catch (e) {
    console.log(`No user.md found for pattern ${newPatternPath}`);
  }

  // Read the files using the filesystem MCP tool
  const fileContents = await use_mcp_tool({
    server_name: "github.com/modelcontextprotocol/servers/tree/main/src/filesystem",
    tool_name: "read_multiple_files",
    arguments: {
      paths: filePathsToRead
    }
  });

  // Analyze the pattern content (requires LLM analysis)
  // This is a placeholder for an internal LLM call to analyze the pattern's relevance.
  // The LLM would analyze fileContents and determine if the pattern is relevant to DeepResearch.
  // It should return a result object like { recommendation: "keep" | "discard", summary: "..." }
  // For now, we'll simulate a simple analysis based on keywords in the path.
  const patternName = newPatternPath.split('/').pop();
  let recommendation = "discard";
  let summary = `Pattern "${patternName}" does not appear directly relevant to DeepResearch based on its name.`;

  const relevantKeywords = ["summarize", "extract", "analyze", "report", "prose", "prompt", "fallacies", "humanize", "lecture", "paper", "callout"];
  if (relevantKeywords.some(keyword => patternName.includes(keyword))) {
      recommendation = "keep";
      summary = `Pattern "${patternName}" appears potentially relevant to DeepResearch based on its name.`;
  }


  console.log(`Analysis result for ${newPatternPath}: Recommendation - ${recommendation}, Summary - ${summary}`);

  // Step 2: Suggest action based on analysis
  if (recommendation === "keep") {
    // Suggest copying the pattern to .prompts/patterns/
    const destinationPath = `.prompts/patterns/${patternName}`;
    console.log(`Pattern "${patternName}" recommended to keep. Suggesting copy to ${destinationPath}`);

    // Placeholder for suggesting the copy command to the user for approval
    // suggest_tool_code """
    // // Suggestion: Copy pattern "${patternName}" to "${destinationPath}"
    // <execute_command>
    // <command>cp -r "${newPatternPath}" "${destinationPath}"</command>
    // <requires_approval>true</requires_approval>
    // </execute_command>
    // """

    // Suggest updating memory bank (This would require another complex LLM call or manual step)
    console.log(`Suggesting manual update of memory bank to document pattern integration.`);

  } else {
    // Suggest discarding/deleting the pattern
    console.log(`Pattern "${newPatternPath}" recommended to discard.`);
    // Placeholder for suggesting deletion to the user
    // suggest_tool_code """
    // // Suggestion: Consider deleting pattern "${newPatternPath}" from `fabric-patterns/` if not needed elsewhere.
    // // Note: Automatic deletion is not recommended without explicit user confirmation.
    // // User should manually review and delete if desired.
    // console.log("Pattern recommended for discard. Please review and manually delete if not needed from `fabric-patterns/`.");
    // """
  }
