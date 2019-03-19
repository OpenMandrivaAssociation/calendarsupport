%define major 5
%define libname %mklibname KF5CalendarSupport %{major}
%define devname %mklibname KF5CalendarSupport -d

Name: calendarsupport
Version:	 18.12.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	2
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for calendar handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5AkonadiMime)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5CalendarUtils)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(KF5Holidays)
BuildRequires: cmake(KF5AkonadiCalendar)
BuildRequires: cmake(KF5PimCommon)
BuildRequires: cmake(KF5KdepimDBusInterfaces)
BuildRequires: cmake(KF5IMAP)
BuildRequires: cmake(KF5Libkdepim)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: boost-devel
BuildRequires: sasl-devel

%description
KDE library for calendar handling.

%package -n %{libname}
Summary: KDE library for calendar handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for calendar handling.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang calendarsupport

%files -f calendarsupport.lang
%{_sysconfdir}/xdg/calendarsupport.categories
%{_sysconfdir}/xdg/calendarsupport.renamecategories
%{_datadir}/kservicetypes5/calendarplugin.desktop

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
