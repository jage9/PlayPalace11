[CmdletBinding()]
[CmdletBinding()]
param(
    [string]$CommonName = "playpalace.local",
    [string]$OutDir = "$env:ProgramData/PlayPalace/ssl",
    [int]$ValidDays = 365,
    [string]$PfxPassword = "playpalace"
)

$ErrorActionPreference = "Stop"

if (-not $OutDir) {
    throw "Output directory is required."
}

if (-not (Test-Path $OutDir)) {
    New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
}

$certPath = Join-Path $OutDir "playpalace_cert.cer"
$keyPath = Join-Path $OutDir "playpalace_key.pfx"

# Create in CurrentUser to avoid NTE_PERM (key creation permission/provider issues),
# but still export files to the requested output directory.
$certStoreLocation = "Cert:\CurrentUser\My"

$cert = New-SelfSignedCertificate `
    -DnsName $CommonName `
    -CertStoreLocation $certStoreLocation `
    -KeyAlgorithm RSA `
    -KeyLength 2048 `
    -KeyExportPolicy Exportable `
    -KeySpec Signature `
    -KeyUsageProperty All `
    -NotAfter (Get-Date).AddDays($ValidDays) `
    -TextExtension @(
        "2.5.29.37={text}1.3.6.1.5.5.7.3.1" # EKU: Server Authentication
        "2.5.29.15={hex}03 02 05 A0"        # KeyUsage: DigitalSignature(0x80) + KeyEncipherment(0x20)
    )

$password = ConvertTo-SecureString -String $PfxPassword -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath $keyPath -Password $password | Out-Null
Export-Certificate -Cert $cert -FilePath $certPath | Out-Null

Write-Host "Generated certificate at $certPath"
Write-Host "Generated private key at $keyPath (password: $PfxPassword)"
