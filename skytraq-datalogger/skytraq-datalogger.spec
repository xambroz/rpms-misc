%global         upversion 0.5-1
Name:           skytraq-datalogger
Version:        0.5
Release:        1%{?dist}
Summary:        Skytraq GPS Datalogger management tool

License:        GPLv2+
URL:            https://code.google.com/p/skytraq-datalogger/downloads/
#Source0:       https://code.google.com/p/skytraq-datalogger/downloads/%%{name}_%%{upversion}.tar.gz
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/%{name}/%{name}_%{upversion}.tar.gz

Patch0:         %{name}-curl.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libcurl-devel


%description
Manipulate data on skytraq GPS data logger.

%prep
%autosetup -n %{name}-%{upversion} -p 1


%build
#configure
%make_build


%install
mkdir -p %{buildroot}/%{_bindir}
%make_install


%files
%doc
%{_bindir}/skytraq-datalogger



%changelog
* Fri Mar 9 2018 Michal Ambroz <rebus AT seznam.cz> - 0.5-1
- initial package for Fedora


