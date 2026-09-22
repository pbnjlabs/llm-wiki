This is an LLM-Wiki for Performance Medical Supply. 
To implement install Obsidian and Claude Pro.

Obsidian Set UP:
- https://obsidian.md/
- Create new vault
- Vault name: LLM-Wiki
- Location: C:\Users\[NAME]\Documents

Claude Set Up: 
- Install Git for Windows if not already installed: https://git-scm.com/download/win
- https://claude.ai
- Tell Claude, "git clone https://github.com/pbnjlabs/llm-wiki.git into Documents\LLM-Wiki." It must be an actual `git clone`, not just files copied/downloaded — the automatic push-after-ingest and the sync task both need a real `.git` folder with the GitHub remote set up, or they'll have nothing to push to / pull from.
- Confirm it worked: open a terminal in Documents\LLM-Wiki and run `git remote -v` — it should show `origin  https://github.com/pbnjlabs/llm-wiki.git`.

Sync Set Up (do this once per device, after cloning the repo):

This keeps the `wiki/` folder current from GitHub automatically, so you
don't have to remember to `git pull` before asking Claude a question.


Windows (Task Scheduler), from an elevated PowerShell, path adjusted to
your clone location. Runs once a day at 8:30am:
```
schtasks /Create /SC DAILY /ST 08:30 /TN "LLM-Wiki Sync" ^
  /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\[NAME]\Documents\LLM-Wiki\scripts\sync-wiki.ps1"
```

If a device already has the task registered on the old every-15-minutes
schedule, replace it (schtasks can't change the schedule type in place):
```
schtasks /Delete /TN "LLM-Wiki Sync" /F
schtasks /Create /SC DAILY /ST 08:30 /TN "LLM-Wiki Sync" ^
  /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\[NAME]\Documents\LLM-Wiki\scripts\sync-wiki.ps1"
```



If the script finds local uncommitted changes it skips the pull rather
than risk clobbering in-progress work — check `.sync.log` in the repo
root if the wiki ever seems stale.



Obsidian's vault is where all of this information will live--locally on your device.  
Claude's default working directory is \Documents.  


Claude must be told to query/consult/check the Wiki at the beginning of each session in order to use the Wiki. Otherwise Claude will search the web for answers. 


To add Source Materials drag/drop, copy/paste, or copy/past the path to the new material and tell Claude to “ingest the [source material] to the Wiki.” And then tell Claude to perform a Lint. Please understand, Obsidian is a library for Claude to maintain, and the Obsidian vault should not need any human curation.

----------------------------------------------------------------------------------------------------------------------------------
Example prompt: "check the /path/to/source-material folder for new sources and ingesting them."

Example prompt: "I'm done ingesting for the day. Perform a lint."

Example Prompt: "Help me troubleshoot a Bruno VPL that won't move. Consult the llm-wiki."





-----------------------------------------------------------------------------------------------------------------------------------

Contact: Lucas@PerformanceMedicalSupply.com 
