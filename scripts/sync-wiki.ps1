# Pulls wiki updates from GitHub without clobbering in-progress local edits.
# Safe to run unattended on a schedule (Windows Task Scheduler).

$RepoDir = Split-Path -Parent $PSScriptRoot
Set-Location $RepoDir
$Log = Join-Path $RepoDir ".sync.log"

function Write-Log($msg) {
    "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') $msg" | Out-File -Append -FilePath $Log
}

if (-not (Test-Path (Join-Path $RepoDir ".git"))) {
    Write-Log "FAILED: $RepoDir is not a git clone -- see README (Option B: git clone)"
    exit 1
}

# Untracked files (e.g. Obsidian's Welcome.md) don't block the pull;
# git pull --ff-only still refuses if it would overwrite one.
$status = git status --porcelain --untracked-files=no
if ($status) {
    Write-Log "skip: local changes pending"
    exit 0
}

git pull --ff-only origin master 2>&1 | Out-File -Append -FilePath $Log
if ($LASTEXITCODE -eq 0) {
    Write-Log "pulled ok"
} else {
    Write-Log "FAILED to pull -- needs manual look"
    exit 1
}
