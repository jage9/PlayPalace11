$ErrorActionPreference = "Stop"

# build.ps1 may be run from repo root; ensure uv uses the server/ pyproject.toml
$ServerDir = $PSScriptRoot

# Ensure PyInstaller is available
uv run --project $ServerDir pyinstaller --version 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "PyInstaller not found in uv environment. Installing..."
    uv add --project $ServerDir --dev pyinstaller pyinstaller-hooks-contrib
}

Write-Host "Building PlayPalace server executable..."

Push-Location $ServerDir
try {
	$entry = "main.py"
$commonArgs = @(
    "-y",
    "--clean",
    "--noconfirm",
    "--noconsole",
    "--name", "PlayPalaceServer",
    "--additional-hooks-dir", "pyinstaller-hooks",
    "--hidden-import", "babel",
    "--hidden-import", "fluent_compiler",
    "--hidden-import", "fluent_compiler.bundle",
    "--hidden-import", "fluent_compiler.resource",
    "--hidden-import", "fluent_compiler.runtime",
    "--collect-submodules", "server"
)

uv run --project . pyinstaller $commonArgs --onefile $entry
if ($LASTEXITCODE -ne 0) {
    throw "Server PyInstaller build failed."
}

	Write-Host "Server build complete. Output in dist\PlayPalaceServer.exe"
} finally {
	Pop-Location
}
