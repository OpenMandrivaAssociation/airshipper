%global debug_package %{nil}

Name:       airshipper
Version:    0.15.0
Release:    1
Summary:    Cross-platform Veloren launcher
Group:      Games/Launcher
License:    GPLv3+
URL:        https://github.com/veloren/Airshipper
Source0:    https://gitlab.com/veloren/airshipper/-/archive/v%{version}/airshipper-v%{version}.tar.bz2
Source1:    veloren.png
Source2:    vendor.tar.xz
Source3:    cargo_config

BuildRequires: git-core
BuildRequires: python
BuildRequires: rust
BuildRequires: cargo
BuildRequires: curl
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xkbcommon-x11)

%description
A cross-platform Veloren launcher.

Features

  * Update/Download and start nightly.
  * Fancy UI with batteries included.


%prep
%autosetup -n %{name}-v%{version} -a2
install -D -m 644 %{SOURCE3} .cargo/config

#curl https://sh.rustup.rs -sSf | sh -s -- \
#    --profile minimal \
#    --default-toolchain nightly -y \
#    %{nil}


%build
export RUSTC_BOOTSTRAP=1
cargo build --release --bin %{name}


%install
install -Dpm0755 target/release/%{name} -t %{buildroot}/%{_bindir}

# .desktop
install -dm 0755 %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=airshipper
Comment=Veloren game launcher
Exec=%{name}
Icon=veloren.png
Terminal=false
Type=Application
Categories=Application;Game;Launcher;
X-Vendor=OpenMandriva
EOF

install -m644 -D %{SOURCE1} %{buildroot}%{_iconsdir}/veloren.png

%files
%license LICENSE
%doc CHANGELOG.md
%{_bindir}/%{name}
%{_iconsdir}/veloren.png
%{_datadir}/applications/%{name}.desktop
