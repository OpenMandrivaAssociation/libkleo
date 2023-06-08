# CMake files check for Qt 6.x already, but it's not used yet,
# so let's not make it a hard dependency
%global __requires_exclude ^.*qt6.*$

%define major 5
%define libname %mklibname KF5Libkleo %{major}
%define devname %mklibname KF5Libkleo -d

Name: libkleo
# This was in kdepim before
Epoch: 3
Version:	23.04.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for PIM handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: sasl-devel
BuildRequires: cmake(KPim5AkonadiSearch)
BuildRequires: cmake(KPim5Mime)
BuildRequires: cmake(KPim5TextEdit)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(QGpgme)
BuildConflicts: kdepimlibs4-devel >= 3:4.14.10
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

%description
KDE library for PIM handling.

%package -n %{libname}
Summary: KDE library for PIM handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for PIM handling.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkleopatra

%files -f libkleopatra.lang
%{_datadir}/qlogging-categories5/libkleo.categories
%{_datadir}/qlogging-categories5/libkleo.renamecategories
%{_sysconfdir}/xdg/libkleopatrarc
%{_datadir}/libkleopatra

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{qch,tags}
