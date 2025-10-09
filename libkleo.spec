#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6Libkleo
%define devname %mklibname KPim6Libkleo -d

Name: libkleo
Version:	25.08.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/libkleo/-/archive/%{gitbranch}/libkleo-%{gitbranchd}.tar.bz2#/libkleo-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/libkleo-%{version}.tar.xz
%endif
Summary: KDE library for PIM handling
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: sasl-devel
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6TextEdit)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(QGpgmeQt6)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

# Renamed after 6.0 2025-05-09
%rename plasma6-libkleo

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

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

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/libkleo.categories
%{_datadir}/qlogging-categories6/libkleo.renamecategories
%{_sysconfdir}/xdg/libkleopatrarc
%{_datadir}/libkleopatra

%files -n %{libname}
%{_libdir}/*.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
%{_datadir}/KPim6Libkleo
