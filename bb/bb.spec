Name:           bb
Version:        1.3
Release:        rc1.1%{?dist}
Summary:        Demo for the AAlib

License:        GPLv2+
URL:            http://aa-project.sourceforge.net/bb/
Source0:        http://downloads.sourceforge.net/aa-project/%{name}-%{version}rc1.tar.gz
#Patch0:         bb-gcc.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  aalib-devel
BuildRequires:  gpm-devel
BuildRequires:  libmikmod-devel

%description
Demo for the AAlib.

%prep
%autosetup -n %{name}-%{version}.0

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -m 555 -D %{name} "%{buildroot}/%{_bindir}/%{name}"


%files
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/bb.1*

%changelog
* Sat Feb 16 2013 Michal Ambroz <rebus at, seznam.cz> 1.0-1
- initial build for Fedora
