This is an LLM-Wiki for Performance Medical Supply. 
To set it up, install Obsidian and Claude Pro.

Obsidian Set Up:
- https://obsidian.md/
- Create new vault
- Vault name: LLM-Wiki
- Location: C:\Users\[NAME]\Documents

Claude Set Up: 
- https://claude.ai
- Pick one of the two options below depending on whether you want this
  device to stay updated automatically or not.

Option A — one-time download, no auto-sync (simplest; fine for a device
that only needs a snapshot and won't be kept current):
- Tell Claude, "create a new project called LLM-Wiki. Here is the GitHub repo:
  https://github.com/pbnjlabs/llm-wiki. Save the project to
  Documents\LLM-Wiki."
- This device's copy is a one-time download. If the wiki changes later
  (new manuals ingested, pages updated), it will NOT pick those changes
  up on its own — you'd need to redo this step to refresh it.
- Don't set up the sync task (Sync Set Up below) on an Option A copy —
  it only works on a git clone. Use Option B if you want auto-sync.


Option B — git clone with auto-sync (recommended if this device should
always have the latest wiki):

First make sure `winget` works in a terminal. If it doesn't, do WinGet
Set Up below first.

Then install Git non-interactively (no manual download):
```
winget install --id Git.Git -e --source winget
```



- Tell Claude, "git clone https://github.com/pbnjlabs/llm-wiki.git into Documents\LLM-Wiki." It must be an actual `git clone`, not just files copied/downloaded — the automatic push-after-ingest and the sync task both need a real `.git` folder with the GitHub remote set up, or they'll have nothing to push to / pull from.
- Confirm it worked: open a terminal in Documents\LLM-Wiki and run `git remote -v` — it should show `origin  https://github.com/pbnjlabs/llm-wiki.git`.
- Then follow Sync Set Up below.

Sync Set Up (do this once per device, after cloning the repo):

This keeps the LLM-Wiki folder current from GitHub automatically, so you
don't have to remember to `git pull` before asking Claude a question.


Windows (Task Scheduler), from an elevated PowerShell, path adjusted to
your clone location (C:\Users\[NAME]\...). Runs once a day at 8:30am:
```
schtasks /Create /SC DAILY /ST 08:30 /TN "LLM-Wiki Sync" /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\[NAME]\Documents\LLM-Wiki\scripts\sync-wiki.ps1"
```



If the script finds local uncommitted changes it skips the pull rather
than risk clobbering in-progress work — check `.sync.log` in the repo
root if the wiki ever seems stale. The log will also show an error if the
folder isn't a git clone.


WinGet Set Up (once per device, only if `winget` doesn't already work in a
terminal), from an elevated PowerShell:
```
$progressPreference = 'silentlyContinue'
Write-Host "Installing WinGet PowerShell module from PSGallery..."
Install-PackageProvider -Name NuGet -Force | Out-Null
Install-Module -Name Microsoft.WinGet.Client -Force -Repository PSGallery | Out-Null
Write-Host "Using Repair-WinGetPackageManager cmdlet to bootstrap WinGet..."
Repair-WinGetPackageManager -AllUsers
Write-Host "Done."
```

-----------------------------------------------------------------------------------------------------------------------------------
Obsidian's vault is where all of this information will live--locally on your device.  
The wiki lives in Documents\LLM-Wiki.  


Claude must be told to query/consult/check the wiki at the beginning of each session in order to use the wiki. Otherwise Claude will search the web for answers. 


To add source material, drag and drop it, copy and paste it, or paste its path, and tell Claude to "ingest the [source material] to the wiki." Then tell Claude to run a lint. Please understand, Obsidian is a library for Claude to maintain, and the Obsidian vault should not need any human curation.

----------------------------------------------------------------------------------------------------------------------------------
Example prompt: "check the /path/to/source-material folder for new sources and ingest them."

Example prompt: "I'm done ingesting for the day. Perform a lint."

Example prompt: "Help me troubleshoot a Bruno VPL that won't move. Consult the LLM-Wiki."





-----------------------------------------------------------------------------------------------------------------------------------
Sources: https://git-scm.com/install/windows (Windows Git install), 
         https://learn.microsoft.com/en-us/windows/package-manager/winget/ (WinGet install), 
         https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (LLM-Wiki, Karpathy)


Contact: Lucas@PerformanceMedicalSupply.com 
