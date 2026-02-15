$ErrorActionPreference = "Stop"

# Ensure PyInstaller is available in this uv project
uv run --project . pyinstaller --version 2>$null
if ($LASTEXITCODE -ne 0) {
	Write-Host "PyInstaller not found in uv environment. Installing..."
	uv add --dev pyinstaller pyinstaller-hooks-contrib
}

Write-Host "Building PlayPalace..."

uv run --project . pyinstaller -y --clean --onedir --noconsole --name PlayPalace --add-data "sounds;sounds" client.py
if ($LASTEXITCODE -ne 0) {
	throw "PyInstaller failed."
}

$dist = "dist\PlayPalace"
$src  = Join-Path $dist "_internal\sounds"
$dst  = Join-Path $dist "sounds"

if (!(Test-Path $src)) {
	throw "Expected sounds folder not found at: $src"
}

if (Test-Path $dst) {
	Remove-Item -Recurse -Force $dst
}

Move-Item -Force $src $dst

Write-Host "Build complete. Output in $dist"
