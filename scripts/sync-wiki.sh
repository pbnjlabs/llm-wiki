#!/usr/bin/env bash
# Pulls wiki updates from GitHub without clobbering in-progress local edits.
# Safe to run unattended on a schedule (cron / systemd timer).
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="$REPO_DIR/.sync.log"

cd "$REPO_DIR"
ts() { date '+%Y-%m-%d %H:%M:%S'; }

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "$(ts) skip: local changes pending" >> "$LOG"
  exit 0
fi

if git pull --ff-only origin master >> "$LOG" 2>&1; then
  echo "$(ts) pulled ok" >> "$LOG"
else
  echo "$(ts) FAILED to pull -- needs manual look" >> "$LOG"
  exit 1
fi
