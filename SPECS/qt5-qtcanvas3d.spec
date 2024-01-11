%global qt_module qtcanvas3d

%global build_tests 1

Summary: Qt5 - Canvas3d component
Name:    qt5-%{qt_module}
Version: 5.12.5
Release: 4%{?dist}

License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

BuildRequires: qt5-rpm-macros >= %{version}
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtbase-private-devel
# libQt5Qml.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel

%description
Qt5 Canvas3D component

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%if 0%{?build_tests}
%package tests
Summary: Unit tests for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
%{summary}.
%endif


%prep
%setup -q -n %{qt_module}-everywhere-src-%{version}


%build
%{qmake_qt5}

%make_build

%if 0%{?build_tests}
make sub-tests %{?_smp_mflags} -k ||:
%endif


%install
make install INSTALL_ROOT=%{buildroot}

%if 0%{?build_tests}
# Install tests for gating
mkdir -p %{buildroot}%{_qt5_libdir}/qt5
find ./tests -not -path '*/\.*' -type d | while read LINE
do
    mkdir -p "%{buildroot}%{_qt5_libdir}/qt5/$LINE"
done
find ./tests -not -path '*/\.*' -not -name '*.h' -not -name '*.cpp' -not -name '*.pro' -not -name 'uic_wrapper.sh' -not -name 'Makefile' -not -name 'target_wrapper.sh' -type f | while read LINE
do
    cp -r --parents "$LINE" %{buildroot}%{_qt5_libdir}/qt5/
done
%endif


%files
%license LICENSE.*
%{_qt5_qmldir}/QtCanvas3D/

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/canvas3d/
%endif

%if 0%{?build_tests}
%files tests
%{_qt5_libdir}/qt5/tests
%endif


%changelog
* Wed Apr 13 2022 Jan Grulich <jgrulich@redhat.com> - 5.12.5-4
- Rebuild for Qt 5.15.3
  Resolves: bz#2074795

* Wed Apr 28 2021 Jan Grulich <jgrulich@redhat.com> - 5.12.5-3
- Rebuild (binutils)
  Resolves: bz#1930041

* Sun Apr 04 2021 Jan Grulich <jgrulich@redhat.com> - 5.12.5-2
- Rebuild for Qt 5.15.2
  Resolves: bz#1930041

* Thu Nov 07 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-1
- 5.12.5
  Resolves: bz#1733136

* Mon Dec 10 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.1-2
- Rebuild to fix CET notes
  Resolves: bz#1657233

* Mon Jul 02 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.1-1
- 5.11.1

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 5.10.1-1
- 5.10.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Jan Grulich <jgrulich@redhat.com> - 5.10.0-1
- 5.10.0

* Thu Nov 23 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.3-1
- 5.9.3

* Tue Oct 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.2-2
- BR: qt5-qtbase-private-devel

* Mon Oct 09 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.2-1
- 5.9.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.1-1
- 5.9.1

* Fri Jun 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.0-2
- drop shadow/out-of-tree builds (#1456211,QTBUG-37417)

* Wed May 31 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-1
- Upstream official release

* Fri May 26 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.1.rc
- Upstream Release Candidate retagged

* Wed May 24 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.rc.1
- Upstream Release Candidate 1

* Mon May 08 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.3
- Upstream beta 3

* Sun Apr 16 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.0
- New upstream beta3 version

* Mon Jan 30 2017 Helio Chissini de Castro <helio@kde.org> - 5.8.0-1
- New upstream version

* Sat Dec 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-2
- 5.7.1 dec5 snapshot, drop cmake/pkgconfig style BR

* Thu Nov 10 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.1-1
- New upstream version

* Wed Jun 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-1
- Qt 5.7.0 release

* Thu Jun 09 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-1
- Update to 5.6.1

* Wed Jun 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-4
- restore -doc pkg (#1341457)

* Sun Mar 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-3
- rebuild

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-2
- rebuild

* Mon Mar 14 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-1
- 5.6.0 final release

* Tue Feb 23 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.6.rc
- Update to final RC

* Mon Feb 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.5
- Update RC release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-0.4.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.3.beta3
- respin sources, use %%license, update URLs, fix -doc BR's, drop unneeded scriptlets

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.2
- Official beta3 release

* Tue Nov 03 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.1
- Start to implement 5.6.0 beta3

* Tue Nov 03 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.1
- Start to implement 5.6.0 beta3

* Thu Oct 15 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-2
- Update to final release 5.5.1

* Tue Sep 29 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-1
- Update to Qt 5.5.1 RC1

* Wed Jul 1 2015 Helio Chissini de Castro <helio@kde.org> 5.5.0-1
- New final upstream release Qt 5.5.0

* Thu Jun 25 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.0-0.2.rc
- Update for official RC1 released packages

* Thu Jun 25 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.0-0.1.rc
- Initial release
