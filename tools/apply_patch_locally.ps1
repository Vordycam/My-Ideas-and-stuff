<#
PowerShell helper to create a git patch and commit locally.
Use this if your local environment has git installed.
#>
param(
  [string]$Branch = 'tidy/assets-extract',
  [string]$Message = 'refactor: extract assets, modularize JS, add checks'
)

Write-Host "Creating branch $Branch and committing changes..."
# create branch, add, commit
if (-not (git rev-parse --is-inside-work-tree 2>$null)) {
  Write-Error "This directory is not a git repository. Aborting."
  exit 1
}

# Checkout or create branch
if (git show-ref --verify --quiet refs/heads/$Branch) {
  git checkout $Branch
} else {
  git checkout -b $Branch
}

git add .
git add .

# Try to commit; if commit fails due to missing user config, use temporary local config
$commitExit = 0
try {
  git commit -m $Message 2>&1 | Write-Host
  $commitExit = $LASTEXITCODE
} catch {
  $commitExit = $LASTEXITCODE
}

if ($commitExit -ne 0) {
  Write-Host "Initial commit attempt failed. Attempting to commit with temporary user config..."
  git -c user.email="you@example.com" -c user.name="Repo Bot" commit -m $Message 2>&1 | Write-Host
  $commitExit = $LASTEXITCODE
}

if ($commitExit -ne 0) {
  Write-Error "Commit failed or there were no changes to commit."
} else {
  Write-Host "Created branch and committed. You can push with: git push -u origin $Branch"

  # write a patch file for easy review
  $patch = "$Branch-changes.patch"
  git format-patch -1 --stdout > $patch
  if (Test-Path $patch) { Write-Host "Patch written to $patch" } else { Write-Error "Failed to write patch file." }
}
Write-Host "Created branch and committed. You can push with: git push -u origin $Branch"

# write a patch file
$patch = "$Branch-changes.patch"
git format-patch -1 --stdout > $patch
Write-Host "Patch written to $patch"
