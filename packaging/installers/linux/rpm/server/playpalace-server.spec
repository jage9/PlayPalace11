%{!?_unitdir: %define _unitdir /usr/lib/systemd/system}

Name:           playpalace-server
Version:        0.0.0
Release:        1%{?dist}
Summary:        PlayPalace multiplayer server

License:        TBD
URL:            https://github.com/XGDevGroup/PlayPalace11
Source0:        PlayPalaceServer.tar.gz
Source1:        playpalace-server.service

BuildArch:      x86_64
Requires:       systemd

%description
Placeholder RPM spec for the PyInstaller-built PlayPalace server. Replace
Source0 with the packaged artifact and update metadata before shipping.

%prep
%setup -q -n PlayPalaceServer

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/playpalace/server
cp -a * %{buildroot}/opt/playpalace/server/
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/playpalace-server.service
mkdir -p %{buildroot}%{_licensedir}/playpalace-server
install -m 0644 LICENSE %{buildroot}%{_licensedir}/playpalace-server/LICENSE

%post
%systemd_post playpalace-server.service

%preun
%systemd_preun playpalace-server.service

%files
%license %{_licensedir}/playpalace-server/LICENSE
/opt/playpalace/server
%{_unitdir}/playpalace-server.service

%changelog
# Update during release.
