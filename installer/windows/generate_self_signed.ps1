param(
    [string]$CommonName = "playpalace.local",
    [string]$OutDir = "$env:ProgramData/PlayPalace/ssl",
    [int]$ValidDays = 365
)

$ErrorActionPreference = "Stop"

if (-not $OutDir) {
    throw "Output directory is required."
}

if (-not (Test-Path $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir | Out-Null
}

$certPath = Join-Path $OutDir "playpalace_cert.cer"
$keyPath = Join-Path $OutDir "playpalace_key.pfx"

$cert = New-SelfSignedCertificate -DnsName $CommonName -CertStoreLocation Cert:\LocalMachine\My -NotAfter (Get-Date).AddDays($ValidDays)

$password = ConvertTo-SecureString -String "playpalace" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath $keyPath -Password $password | Out-Null
Export-Certificate -Cert $cert -FilePath $certPath | Out-Null

Write-Host "Generated certificate at $certPath"
Write-Host "Generated private key at $keyPath (password: playpalace)"
