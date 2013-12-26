# TODO
# - fix kopete-tool-{avdeviceconfig,smpppdcs} summaries/descriptions (copy-pastos!)
# - BR phonon-devel
# - FILES update
#
# Conditional build:
#
%define		_state		stable
%define		orgname		kget
%define		qtver		4.8.3

Summary:	File downloand manager
Summary(pl.UTF-8):	Zarządca ściągania plików
Name:		kde4-%{orgname}
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	8b8221bcff46af60191abdb75c9c0135
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	alsa-lib-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	giflib-devel
BuildRequires:	gmp-devel
BuildRequires:	gpgme-devel
BuildRequires:	jasper-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdebase-workspace-devel >= 4.11.4
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libgadu-devel >= 1.8.0
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libktorrent-devel >= 1.0.2
BuildRequires:	libmms-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	qca-devel >= 2.0
BuildRequires:	qimageblitz-devel >= 0.0.6
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-desktop-ontologies-devel >= 0.5
BuildRequires:	soprano-devel >= 2.4.64
BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	kde4-kdebase >= %{version}
Requires:	kde4-kdebase-workspace >= 4.11.4
Requires:	kde4-dolphin >= %{version}
Obsoletes:	kde4-kdenetwork-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GetRight-like file download manager with resuming support and
Konqueror/Mozilla integration.

%description -l pl.UTF-8
Zarządca ściągania plików podobny do GetRighta z obsługą wznawiania
oraz integracją z Konquerorem/Mozillą.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DMOZPLUGIN_INSTALL_DIR=%{_browserpluginsdir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%find_lang	%{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kget
%attr(755,root,root) %{_libdir}/kde4/kget_bittorrentfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_checksumsearchfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_mmsfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_kiofactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_metalinkfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_mirrorsearchfactory.so
%attr(755,root,root) %{_libdir}/kde4/kget_multisegkiofactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_bittorrentfactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_checksumsearchfactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_mmsfactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_metalinkfactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_mirrorsearchfactory.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kget_multisegkiofactory.so
%attr(755,root,root) %{_libdir}/kde4/krunner_kget.so
%attr(755,root,root) %{_libdir}/kde4/kget_browser_integration.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_kget.so
%attr(755,root,root) %{_libdir}/kde4/plasma_kget_barapplet.so
%attr(755,root,root) %{_libdir}/kde4/plasma_kget_piechart.so
%attr(755,root,root) %{_libdir}/libkgetcore.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkgetcore.so.?
%attr(755,root,root) %{_libdir}/libkgetcore.so
%{_datadir}/apps/kconf_update/kget.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kget_limitdownloads.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kget_sensitive.pl
%{_datadir}/apps/kget
%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.desktop
%dir %{_datadir}/apps/kwebkitpart/kpartplugins
%{_datadir}/apps/kwebkitpart/kpartplugins/kget_plug_in.rc
%{_datadir}/apps/kwebkitpart/kpartplugins/kget_plug_in.desktop
%{_datadir}/apps/dolphinpart/kpartplugins/kget_plug_in.rc
%{_datadir}/apps/dolphinpart/kpartplugins/kget_plug_in.desktop
%{_datadir}/config.kcfg/kget.kcfg
%{_datadir}/config.kcfg/kget_multisegkiofactory.kcfg
%{_datadir}/config.kcfg/kget_mirrorsearchfactory.kcfg
%{_datadir}/config.kcfg/kget_checksumsearchfactory.kcfg
%{_datadir}/config.kcfg/kget_mmsfactory.kcfg
%{_datadir}/kde4/services/kget_bittorrentfactory_config.desktop
%{_datadir}/kde4/services/kget_checksumsearchfactory.desktop
%{_datadir}/kde4/services/kget_checksumsearchfactory_config.desktop
%{_datadir}/kde4/services/kget_mmsfactory.desktop
%{_datadir}/kde4/services/kget_mmsfactory_config.desktop
%{_datadir}/kde4/services/kget_metalinkfactory_config.desktop
%{_datadir}/kde4/services/kget_mirrorsearchfactory_config.desktop
%{_datadir}/kde4/services/kget_multisegkiofactory_config.desktop
%{_datadir}/kde4/services/ServiceMenus/kget_download.desktop
%{_datadir}/kde4/services/kget_bittorrentfactory.desktop
%{_datadir}/kde4/services/kget_kiofactory.desktop
%{_datadir}/kde4/services/kget_metalinkfactory.desktop
%{_datadir}/kde4/services/kget_multisegkiofactory.desktop
%{_datadir}/kde4/services/kget_mirrorsearchfactory.desktop
%{_datadir}/kde4/services/kgetbarapplet-default.desktop
#%{_datadir}/kde4/services/kgetpanelbarapplet-default.desktop
%{_datadir}/kde4/services/kgetpiechartapplet-default.desktop
%{_datadir}/kde4/services/plasma-engine-kget.desktop
%{_datadir}/kde4/servicetypes/kget_plugin.desktop
%{_datadir}/kde4/services/plasma-runner-kget.desktop
#%{_datadir}/kde4/services/plasma-runner-kget_config.desktop
%{_datadir}/ontology/kde/kget_history.ontology
%{_datadir}/ontology/kde/kget_history.trig
%{_desktopdir}/kde4/kget.desktop
%{_datadir}/dbus-1/services/org.kde.kget.service
%{_iconsdir}/*/*/*/*kget*
