%global debug_package %{nil}

Name:       airshipper
Version:    0.7.0
Release:    1%{?dist}
Summary:    Cross-platform Veloren launcher

License:    GPLv3+
URL:        https://github.com/veloren/Airshipper
Source0:    https://gitlab.com/veloren/airshipper/-/archive/v%{version}/airshipper-v%{version}.tar.bz2

BuildRequires: git-core
BuildRequires: python
BuildRequires: rust
BuildRequires: cargo
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xkbcommon-x11)

%description
A cross-platform Veloren launcher.

Features

  * Update/Download and start nightly.
  * Fancy UI with batteries included.


%prep
%autosetup -p1

curl https://sh.rustup.rs -sSf | sh -s -- \
    --profile minimal \
    --default-toolchain nightly -y \
    %{nil}


%build
$HOME/.cargo/bin/cargo build --release --bin %{name}


%install
install -Dpm0755 target/release/%{name} -t %{buildroot}/%{_bindir}


%files
%license LICENSE
%doc CHANGELOG.md
%{_bindir}/%{name}
