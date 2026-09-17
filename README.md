This is an LLM-Wiki for Performance Medical Supply. 
To implement install Obsidian and Claude Pro.
Obsidian's working directory is all of this information will live--locally on your device. A good working directory is something like, ~./Documents/LLM-Wiki. 
When Claude is installed it may ask for a working directory. Have it use the same directory as Obsidian. This might need manually set in Claude's settings.  
Point Claude to this git (copy/past the URL), and tell Claude to “ingest the sources.”
Claude must be told to query/consult/check the Wiki at the beginning of each session in order to use the Wiki. Otherwise Claude will search the web for answers. 
To add Source Materials drag/drop, copy/paste, or copy/past the path to the new material and tell Claude to “ingest the [source material] to the Wiki.” And then tell Claude to perform a Lint.
Example prompt: "check the /path/to/source-material folder for new sources and ingesting them."
Example prompt: "I'm done ingesting for the day. Perform a lint."
Example Prompt: "Help me troubleshoot a Bruno VPL that won't move. Consult the llm-wiki."
