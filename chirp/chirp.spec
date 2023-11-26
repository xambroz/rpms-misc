%global src_name chirp
%global debug_package %{nil}

Name:           chirp
Version:        20231125
Release:        1%{?dist}
Summary:        A tool for programming two-way radio equipment

License:        GPLv3+
URL:            http://chirp.danplanet.com/
# Source0:        http://trac.chirp.danplanet.com/chirp_daily/daily-%{version}/%{src_name}-%{version}.tar.gz
Source0:        https://trac.chirp.danplanet.com/chirp_next/next-%{version}/chirp-%{version}.tar.gz
Source1:        %{name}.desktop

# Patch0:         chirp-0.2.2-install.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils

BuildRequires:  python3-devel
BuildRequires:  python3-libxml2
BuildRequires:  python3-pyserial


Requires:       pygtk2
Requires:       %{py3_dist pyserial suds-jurko}
Requires:       python3-libxml2

%description
Chirp is a tool for programming two-way radio equipment It provides a generic
user interface to the programming data and process that can drive many radio
models under the hood.


%prep
%autosetup -p1 -n %{src_name}-%{version}


%build
%{py3_build}


%install
%{py3_install}

# Remove the tk8180 driver as it depends on python2-future which is no longer
# available in Fedora 31 and up.
rm -f %{buildroot}%{python3_sitelib}/%{name}/drivers/tk8180.py*

# Wrong .desktop config lets install the correct .desktop
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# %find_lang CHIRP


#%files -f CHIRP.lang
%files
%license COPYING
%{_bindir}/chirp
%{_bindir}/chirpc
# %{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
# %{_datadir}/pixmaps/%{name}.png
%{python3_sitelib}/%{src_name}-%{version}-*.egg-info
%{python3_sitelib}/%{name}/
%exclude %{_datadir}/%{name}/locale


%changelog
* Wed Jun 03 2020 Richard Shaw <hobbes1069@gmail.com> - 20200603-1
- Update to 20200603.

* Thu Apr 30 2020 Richard Shaw <hobbes1069@gmail.com> - 20200430-1
- Update to 20200430.

* Mon Apr 13 2020 Richard Shaw <hobbes1069@gmail.com> - 20200409-1
- Update to 20200409.

* Thu Feb 27 2020 Richard Shaw <hobbes1069@gmail.com> - 20200227-1
- Update to 20200227.

* Tue Feb 18 2020 Richard Shaw <hobbes1069@gmail.com> - 20200213-1
- Update to 20200213.

* Fri Jan 03 2020 Richard Shaw <hobbes1069@gmail.com> - 20200103-1
- Update to 20200103.

* Mon Dec 23 2019 Richard Shaw <hobbes1069@gmail.com> - 20191221-1
- Update to 20191221.

* Fri Dec 06 2019 Richard Shaw <hobbes1069@gmail.com> - 20191206-1
- Update to 20191206.
- Unretire chirp on f31 only.
- Remove tk8180 driver as it relies on python2-future which is not available.

* Mon Aug 12 2019 Richard Shaw <hobbes1069@gmail.com> - 20190812-1
- Update to 20190812.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190718-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Richard Shaw <hobbes1069@gmail.com> - 20190718-1
- Update to 20190718.

* Sat Jul 13 2019 Richard Shaw <hobbes1069@gmail.com> - 20190713-1
- Update to 20190713.

* Fri Jul 05 2019 Richard Shaw <hobbes1069@gmail.com> - 20190703-1
- Update to 20190703.

* Thu May 30 2019 Richard Shaw <hobbes1069@gmail.com> - 20190524-1
- Update to 20190524.

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 20190410-1
- Update to 20190410.

* Tue Mar 19 2019 Richard Shaw <hobbes1069@gmail.com> - 20190319-1
- Update to 20190319.

* Mon Mar 04 2019 Richard Shaw <hobbes1069@gmail.com> - 20190304-1
- Update to 20190304.

* Sun Mar 03 2019 Richard Shaw <hobbes1069@gmail.com> - 20190303-1
- Update to 20190303.

* Thu Feb 28 2019 Richard Shaw <hobbes1069@gmail.com> - 20190227-1
- Update to 20190227.

* Sun Feb 24 2019 Richard Shaw <hobbes1069@gmail.com> - 20190222-1
- Update to 20190222.

* Wed Feb 20 2019 Richard Shaw <hobbes1069@gmail.com> - 20190220-1
- Update to 20190220.

* Tue Feb 19 2019 Richard Shaw <hobbes1069@gmail.com> - 20190219-1
- Update to 20190219.

* Mon Feb 18 2019 Richard Shaw <hobbes1069@gmail.com> - 20190218-1
- Update to 20190218.

* Sun Feb 17 2019 Richard Shaw <hobbes1069@gmail.com> - 20190217-1
- Update to 20190217.

* Fri Feb 15 2019 Richard Shaw <hobbes1069@gmail.com> - 20190215-1
- Update to 20190215.

* Sat Feb 09 2019 Richard Shaw <hobbes1069@gmail.com> - 20190209-1
- Update to 20190209.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Richard Shaw <hobbes1069@gmail.com> - 20190120-1
- Update to 20190120.

* Sat Jan 19 2019 Richard Shaw <hobbes1069@gmail.com> - 20190112-1
- Update to 20190112.

* Fri Jan 04 2019 Richard Shaw <hobbes1069@gmail.com> - 20190104-1
- Update to 20190104.

* Wed Jan 02 2019 Richard Shaw <hobbes1069@gmail.com> - 20190102-1
- Update to 20190102.

* Mon Dec 17 2018 Richard Shaw <hobbes1069@gmail.com> - 20181214-1
- Update to 20181214.

* Thu Dec 06 2018 Richard Shaw <hobbes1069@gmail.com> - 20181205-1
- Update to 20181205.

* Fri Nov 30 2018 Richard Shaw <hobbes1069@gmail.com> - 20181128-1
- Update to 20181128.

* Mon Sep 10 2018 Richard Shaw <hobbes1069@gmail.com> - 20180906-2
- Fix install requirements.

* Sat Sep 08 2018 Richard Shaw <hobbes1069@gmail.com> - 20180906-1
- Update to 20180906.
- Initial build for epel7.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180614-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Richard Shaw <hobbes1069@gmail.com> - 20180614-1
- Update to 20180614.
- Add appdata file.

* Wed Jun 06 2018 Richard Shaw <hobbes1069@gmail.com> - 20180606-1
- Update to 20180606.

* Tue Mar 13 2018 Richard Shaw <hobbes1069@gmail.com> - 20180313-1
- Update to 20180313

* Sat Feb 10 2018 Richard Shaw <hobbes1069@gmail.com> - 20180210-1
- Update to 20180210.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171204-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Iryna Shcherbina <ishcherb@redhat.com> - 20171204-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Dec 06 2017 Richard Shaw <hobbes1069@gmail.com> - 20171204-1
- Update to latest upstream release.
- Fix ambiguous Python 2 dependency declarations
  https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170711-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Richard Shaw <hobbes1069@gmail.com> - 20170711-1
- Update to latest upstream release.

* Sat Mar  4 2017 Richard Shaw <hobbes1069@gmail.com> - 20170222-1
- Update to latest upstream release.
- Add pygtk2 as a runtime requirement, fixes RHBZ#1428979.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Richard Shaw <hobbes1069@gmail.com> - 20170115-1
- Update to latest upstream release.

* Tue Oct 18 2016 Richard Shaw <hobbes1069@gmail.com> - 20161018-1
- Update to latest upstream release.

* Tue Aug 23 2016 Richard Shaw <hobbes1069@gmail.com> - 20160819-1
- Update to latest upstream release.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20160706-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul  7 2016 Richard Shaw <hobbes1069@gmail.com> - 20160706-1
- Update to latest upstream release.

* Mon May 23 2016 Richard Shaw <hobbes1069@gmail.com> - 20160517-1
- Update to latest upstream release.

* Wed May  4 2016 Richard Shaw <hobbes1069@gmail.com> - 20160504-1
- Update to latest upstream release.

* Wed Apr  6 2016 Richard Shaw <hobbes1069@gmail.com> - 20160402-1
- Update to latest upstream release.

* Wed Mar  9 2016 Richard Shaw <hobbes1069@gmail.com> - 20160309-1
- Update to latest upstream release.

* Mon Feb 29 2016 Richard Shaw <hobbes1069@gmail.com> - 20160229-1
- Update to latest upstream release.

* Thu Feb 18 2016 Richard Shaw <hobbes1069@gmail.com> - 20160215-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Richard Shaw <hobbes1069@gmail.com> - 20151130-1
- Update to new rolling release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct  9 2014 Richard Shaw <hobbes1069@gmail.com> - 0.4.1-1
- Update to latest bugfix release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Richard Shaw <hobbes1069@gmail.com> - 0.4.0-1
- Update to latest upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.1-1
- Update to latest upstream release.

* Sat Feb 16 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-1
- Update to latest upstream release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Richard Shaw <hobbes1069@gmail.com> - 0.2.2-1
- Update to latest upstream release.

* Sun Mar 18 2012 Richard Shaw <hobbes1069@gmail.com> - 0.2.0-1
- Update to latest upstream release.

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-5
- Add source for .desktop, per review

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-4
- Add source for patches, per review

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-3
- Submit for review

* Sat Nov 19 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-2
- Own unowned directories
- Add correct .desktop file
- Apply patch to move COPYING file to proper directory
- Add shebang patch removes shebang from unnecessary files

* Sat Nov 19 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-1
- Initial Build and testing
