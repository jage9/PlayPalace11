# Trust Setup (Signing Keys & Certificates)

PlayPalace packages are currently signed with project-owned keys so developers and testers can verify downloads even before we obtain CA-issued certificates. This document explains how to import those keys on each platform.

> **Note:** Final public releases will use organization-issued keys/certificates. For now these instructions cover the self-managed keys described in the installer docs.

## Linux (GPG)

We publish a GPG public key alongside each release artifact (`playpalace-signing.asc`). Import it once on the systems you use for package installation:

```bash
curl -fsSL https://github.com/XGDevGroup/PlayPalace11/releases/latest/download/playpalace-signing.asc | gpg --import
```

Verify the fingerprint matches the value listed in the release notes (example):

```bash
gpg --fingerprint "PlayPalace Signing"
```

### Debian/Ubuntu (APT)
1. Copy the key into `/etc/apt/keyrings/` or `/usr/share/keyrings/`:
   ```bash
   sudo install -m 0644 playpalace-signing.asc /etc/apt/keyrings/playpalace.gpg
   ```
2. When adding our repository (future work) or installing local `.deb`s with `dpkg -i`, GPG validation will use that key.
3. Manual installs (`dpkg -i playpalace-server_*.deb`) will show the dpkg-sig trust output. Reject the package if the signature is invalid.

### RPM (Fedora/RHEL/CentOS/Oracle)
1. Import the key into the RPM database:
   ```bash
   sudo rpm --import playpalace-signing.asc
   ```
2. `rpm -K playpalace-server-*.rpm` should now report `pgp` signatures.
3. `dnf install playpalace-server-*.rpm` will automatically verify the signature before installing.

### Arch Linux / pacman
1. Import the key into your pacman keyring:
   ```bash
   gpg --homedir ~/.gnupg --import playpalace-signing.asc
   sudo pacman-key --add playpalace-signing.asc
   sudo pacman-key --lsign-key "PlayPalace Signing"
   ```
2. Install with `pacman -U playpalace-client-*.pkg.tar.zst`. Pacman refuses unsigned packages unless you override `SigLevel`, so keep signatures enabled.

## Windows (Authenticode)

Until we acquire a commercial Authenticode certificate, internal builds are signed with a self-issued certificate (`PlayPalaceTest.pfx`). To trust the MSI on your test machine:

1. Double-click the `.pfx` (or use PowerShell `Import-PfxCertificate`) to import it into **Current User → Trusted Root Certification Authorities** *and* **Trusted Publishers**. When prompted, mark the private key as non-exportable and provide the password from the build notes.
2. Alternatively, run:
   ```powershell
   $pwd = ConvertTo-SecureString -String 'playpalace' -AsPlainText -Force
   Import-PfxCertificate -FilePath .\PlayPalaceTest.pfx -Password $pwd -CertStoreLocation Cert:\CurrentUser\TrustedPeople
   Import-PfxCertificate -FilePath .\PlayPalaceTest.pfx -Password $pwd -CertStoreLocation Cert:\CurrentUser\Root
   ```
3. Re-run the MSI; Windows should now list the publisher as "XGDevGroup" without warning prompts.

> **Security reminder:** only import certificates directly from the PlayPalace release channels. Remove (`certmgr.msc`) the test cert once we migrate to a CA-issued cert.

## Publishing Keys
- Store the private keys securely (1Password/Hashicorp Vault) and restrict access to release engineers.
- Publish the public GPG key and the test Authenticode certificate on every release page so users can verify them.
- Update this document whenever fingerprints or passwords change.
