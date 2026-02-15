Name:           playpalace-client
Version:        0.0.0
Release:        1%{?dist}
Summary:        PlayPalace desktop client

License:        TBD
URL:            https://github.com/XGDevGroup/PlayPalace11
Source0:        PlayPalaceClient.tar.gz
Source1:        playpalace.desktop

BuildArch:      x86_64
Requires:       gtk3, glib2

%description
Placeholder spec for the wxPython client. Copy the PyInstaller onedir
into /opt/playpalace/client/ and install desktop resources.

%prep
%setup -q -n PlayPalaceClient

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/playpalace/client
cp -a * %{buildroot}/opt/playpalace/client/
mkdir -p %{buildroot}%{_bindir}
cat <<'LAUNCH' > %{buildroot}%{_bindir}/playpalace-client
#!/bin/sh
exec /opt/playpalace/client/PlayPalace
LAUNCH
chmod 755 %{buildroot}%{_bindir}/playpalace-client
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/playpalace.desktop
mkdir -p %{buildroot}%{_licensedir}/playpalace-client
install -m 0644 LICENSE %{buildroot}%{_licensedir}/playpalace-client/LICENSE

%files
%license %{_licensedir}/playpalace-client/LICENSE
%{_bindir}/playpalace-client
%{_datadir}/applications/playpalace.desktop
/opt/playpalace/client

%changelog
# Update during release.
