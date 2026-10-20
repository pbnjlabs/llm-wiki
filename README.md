# Performance Medical Supply — Equipment Wiki

A library of everything we know about the equipment we sell and fix:
stair lifts, porch lifts, vehicle lifts, power chairs, scooters, lift
chairs, ramps and more. Claude (an AI assistant) reads the
manufacturers' manuals, keeps this library organized, and answers your
questions from it.

You don't need to be good with computers to set this up. You do three
things yourself, then Claude does the rest and explains each step as it
goes.

---

## Setting it up on a new computer

### Step 1: Make a Claude account

1. Go to **https://claude.ai** and click **Sign up**.
2. Sign up with your email address.
3. Choose the **Pro** plan. (The free plan can't do this job.)

### Step 2: Install the Claude app

1. Go to **https://claude.ai/download**.
2. Download the app for your computer (Windows or Mac) and install it
   like any other program.
3. Open the app and sign in with the account from Step 1.

### Step 3: Ask Claude to do the rest

1. In the Claude app, switch to **Code** (Claude Code).
2. When it asks which folder to work in, choose your **Documents**
   folder.
3. Copy this whole sentence, paste it into the message box and press
   Enter:

   > Please set up the Performance Medical Supply wiki on this computer.
   > Read https://github.com/pbnjlabs/llm-wiki/blob/master/README.md and
   > follow the "Setup steps for Claude" section, explaining each step to
   > me in plain words.

4. Claude will ask your permission before it does things. When a box
   asks to allow something, click **Allow**. If Windows asks "Do you want
   to allow this app to make changes to your device?", click **Yes**.
5. Claude may ask you a question or two, such as whether this computer
   will be used to add new manuals. Just answer in your own words.

That's it. When Claude says it's finished, the wiki is ready.

---

## Using the wiki every day

1. Open the Claude app and switch to **Code**.
2. Choose the **LLM-Wiki** folder (inside Documents). Opening this folder
   is what tells Claude to use the wiki.
3. Ask your question the way you'd ask a coworker.

Things you can say:

- "A Bruno porch lift won't move. Help me troubleshoot it."
- "How do I reset the hand control on a Golden lift chair?"
- "What batteries does a Golden Companion GC440 take?"
- "Here is a new manual: [drag the file in]. Ingest it into the wiki."
- "I'm done adding manuals for today. Run a lint."

The wiki updates itself from the internet once a day, so you always
have the latest version.

### Good to know

- **The manuals themselves are not included.** A new computer gets every
  wiki page, but not the original PDF manuals (they're too big to share
  this way). Claude can still answer questions; it just can't open the
  original manual. If a computer needs the PDFs, ask Lucas for a copy of
  the `MANUALS` folder and put it inside the `LLM-Wiki` folder.
- **Adding manuals needs permission.** Looking things up works on any
  computer. To add manuals or change the wiki, this computer has to be
  signed in to GitHub with access to the wiki. Claude sets that up if
  you say you'll be adding manuals, but Lucas has to give your account
  access first.
- **Obsidian is optional.** Obsidian (https://obsidian.md) is a free
  program for browsing the wiki yourself, with clickable links between
  pages. Claude doesn't need it. Claude can install it for you if you
  want it.

Questions: Lucas@PerformanceMedicalSupply.com

---

## Setup steps for Claude

*Claude: the person you're helping may not be comfortable with
computers. Do these steps one at a time. Before each one, say in one or
two plain sentences what you're about to do and why. Don't ask them to
type commands; you run everything. If something fails, fix it yourself
if you can, and explain the problem simply if you can't. Never print
passwords or tokens.*

1. **Check the computer.** Find out the operating system (Windows, Mac or
   Linux). On Windows, find the real Documents folder with
   `[Environment]::GetFolderPath('MyDocuments')`; it is often inside
   OneDrive. The wiki goes in `<Documents>/LLM-Wiki`. If that folder
   already exists, check whether it's already a clone of this repo
   before changing anything, and ask before overwriting.

2. **Install Git if it's missing** (`git --version`).
   - Windows: `winget install --id Git.Git -e --source winget`. If
     `winget` doesn't work, bootstrap it from an elevated PowerShell:
     ```
     Install-PackageProvider -Name NuGet -Force | Out-Null
     Install-Module -Name Microsoft.WinGet.Client -Force -Repository PSGallery | Out-Null
     Repair-WinGetPackageManager -AllUsers
     ```
     Open a new shell afterwards so `git` is on the PATH.
   - Mac: `xcode-select --install` (or `brew install git` if Homebrew is
     present).
   - Linux: the package manager (e.g. `sudo apt install git`).

3. **Clone the wiki.** It must be a real `git clone`, not a download:
   ```
   git clone https://github.com/pbnjlabs/llm-wiki.git "<Documents>/LLM-Wiki"
   ```
   Check with `git -C "<Documents>/LLM-Wiki" remote -v`; it should show
   `origin https://github.com/pbnjlabs/llm-wiki.git`.

4. **Turn on the daily update.** It pulls from GitHub every morning and
   skips the pull if there are local changes (it logs to `.sync.log`).
   - Windows (current user, no admin needed):
     ```
     schtasks /Create /SC DAILY /ST 08:30 /TN "LLM-Wiki Sync" /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -File \"<Documents>\LLM-Wiki\scripts\sync-wiki.ps1\""
     ```
     Run the task once (`schtasks /Run /TN "LLM-Wiki Sync"`) and check
     `.sync.log` says `pulled ok`.
   - Mac/Linux: add a daily cron entry:
     `30 8 * * * "<Documents>/LLM-Wiki/scripts/sync-wiki.sh"`, then run
     the script once and check `.sync.log`.

5. **Ask: will this computer be used to add manuals or change the
   wiki?**
   - If **no**, skip to step 6. Looking things up needs nothing else.
   - If **yes**, sign this computer in to GitHub so it can save changes:
     install the GitHub CLI (`winget install --id GitHub.cli -e`,
     `brew install gh` or the Linux package), then run
     `gh auth login --web --git-protocol https`. Tell them the one-time
     code it shows, and that a browser page will open where they sign in
     to GitHub and enter that code. Then run `gh auth setup-git`. If they
     don't have a GitHub account, or `git push --dry-run` says
     permission denied, tell them to email Lucas to be added to the
     `pbnjlabs/llm-wiki` repo, then finish this step later.

6. **Manuals (optional).** Explain that the PDF manuals aren't included
   and the wiki works without them. If they have a copy of the `MANUALS`
   folder (from Lucas, a USB drive or a shared drive), copy it to
   `<Documents>/LLM-Wiki/MANUALS`. Never commit it; it's in
   `.gitignore`.

7. **Obsidian (optional).** Ask if they'd like Obsidian for browsing the
   wiki themselves. If yes: `winget install --id Obsidian.Obsidian -e`
   (Windows) or `brew install --cask obsidian` (Mac). Then walk them
   through opening it and choosing **"Open folder as vault"** →
   `<Documents>/LLM-Wiki`. Do **not** create a new vault; the repo
   already has its Obsidian settings.

8. **Test and finish.** From the `LLM-Wiki` folder, answer one sample
   question from the wiki (for example, how to reset a Golden lift chair
   hand control) to show it works. Then tell them, in plain words, how to
   use it every day: open Claude, switch to Code, choose the `LLM-Wiki`
   folder, and ask. Starting in that folder is what makes Claude read
   `CLAUDE.md` and use the wiki.

---

## For maintainers

- **How it works:** `CLAUDE.md` is the rulebook Claude follows (page
  formats, ingest, lint, git). `wiki/` holds the pages; start at
  `wiki/index.md`. `MANUALS/` (raw PDFs) and `assets/` (extracted images)
  stay local and are not in git.
- **Ingest, lint and pushes:** Claude commits and pushes after every
  ingest or lint. The device needs GitHub write access (setup step 5).
- **Optional tools:** `pdftoppm` (poppler-utils) for extracting diagrams
  from manuals; Python 3 for `scripts/techmate_pull.py`.
- **Sync scripts:** `scripts/sync-wiki.ps1` (Windows Task Scheduler) and
  `scripts/sync-wiki.sh` (cron or systemd timer).

Sources: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
(the LLM-Wiki idea, Andrej Karpathy), https://git-scm.com/install/windows,
https://learn.microsoft.com/en-us/windows/package-manager/winget/,
https://cli.github.com
