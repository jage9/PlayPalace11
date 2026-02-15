param(
    [string]$ProgramDataPath,
    [string]$HostName,
    [int]$Port,
    [string]$AllowInsecure = "0",
    [string]$EnableSsl = "0",
    [string]$CertificatePath = "",
    [string]$PrivateKeyPath = ""
)

$ErrorActionPreference = "Stop"

function Convert-ToBool([string]$value) {
    if ([string]::IsNullOrWhiteSpace($value)) { return $false }
    switch ($value.Trim().ToLowerInvariant()) {
        "1" { return $true }
        "true" { return $true }
        "yes" { return $true }
        "on" { return $true }
        default { return $false }
    }
}

$AllowInsecureFlag = Convert-ToBool $AllowInsecure
$EnableSslFlag = Convert-ToBool $EnableSsl

if (-not $ProgramDataPath) {
    throw "ProgramData path is required."
}

$targetDir = Join-Path $ProgramDataPath "PlayPalace"
if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir | Out-Null
}

$configFile = Join-Path $targetDir "config.toml"
$example = Join-Path $PSScriptRoot "..\server\config.example.toml"

if (-not (Test-Path $configFile) -and (Test-Path $example)) {
    Copy-Item $example $configFile -Force
}

$toml = Get-Content $configFile -Raw

if ($HostName) {
    if ($toml -match "host = \".*\"") {
        $toml = [System.Text.RegularExpressions.Regex]::Replace($toml, "host = \".*\"", "host = \"$HostName\"")
    } else {
        $toml += "`n[server]`nhost = \"$HostName\"`n"
    }
}

if ($Port) {
    if ($toml -match "port = \d+") {
        $toml = [System.Text.RegularExpressions.Regex]::Replace($toml, "port = \d+", "port = $Port")
    } else {
        if ($toml -notmatch "\[server\]") { $toml += "`n[server]\n" }
        $toml += "port = $Port`n"
    }
}

function Set-NetworkFlag {
    param([string]$content, [bool]$allowInsecure)
    $sectionPattern = "(?ms)^\[network\](.*?)(?=^\[|\Z)"
    $entry = "allow_insecure_ws = {0}" -f ($allowInsecure ? "true" : "false")
    if ($content -match $sectionPattern) {
        $block = $Matches[0]
        if ($block -match "allow_insecure_ws\s*=") {
            $updatedBlock = [System.Text.RegularExpressions.Regex]::Replace($block, "allow_insecure_ws\s*=.*", $entry)
        } else {
            $updatedBlock = $block.TrimEnd() + "`n" + $entry + "`n"
        }
        return $content -replace [System.Text.RegularExpressions.Regex]::Escape($block), $updatedBlock
    }
    return $content + "`n[network]`n" + $entry + "`n"
}

if ($EnableSslFlag) {
    $toml = Set-NetworkFlag -content $toml -allowInsecure:$false
} elseif ($AllowInsecureFlag) {
    $toml = Set-NetworkFlag -content $toml -allowInsecure:$true
}

if ($EnableSslFlag -and $CertificatePath -and $PrivateKeyPath) {
    $installerBlock = "`n[installer.ssl]`ncertificate = `"$CertificatePath`"`nkey = `"$PrivateKeyPath`"`n"
    if ($toml -match "(?ms)^\[installer\.ssl\](.*?)(?=^\[|\Z)") {
        $toml = [System.Text.RegularExpressions.Regex]::Replace(
            $toml,
            "(?ms)^\[installer\.ssl\](.*?)(?=^\[|\Z)",
            $installerBlock.Trim()
        ) + "`n"
    } else {
        $toml += "`n# SSL paths configured via installer" + $installerBlock
    }
}

Set-Content -Path $configFile -Value $toml -Encoding UTF8
