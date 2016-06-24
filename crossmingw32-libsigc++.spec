Summary:	The Typesafe Signal Framework for C++ - MinGW32 cross version
Summary(pl.UTF-8):	Środowisko sygnałów z kontrolą typów dla C++ - wersja skrośna dla MinGW32
%define		realname	libsigc++
Name:		crossmingw32-%{realname}
Version:	2.8.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.8/%{realname}-%{version}.tar.xz
# Source0-md5:	3d26acbc813fa54edd4401ce1a981677
URL:		http://libsigc.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	crossmingw32-gcc-c++ >= 1:4.6
BuildRequires:	libtool >= 2:2.0
BuildRequires:	m4
BuildRequires:	mm-common >= 0.9.8
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	crossmingw32-gcc-c++ >= 1:4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++
%define		__pkgconfig_provides	%{nil}
%define		__pkgconfig_requires	%{nil}

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
%endif
# -z options are invalid for mingw linker, most of -f options are Linux-specific
%define		filterout_ld	-Wl,-z,.*
%define		filterout_c	-f[-a-z0-9=]*
%define		filterout_cxx	-f[-a-z0-9=]*

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a seperate library to
provide for more general use. It is the most complete library of its
kind with the ablity to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

This package contains cross MinGW32 version.

%description -l pl.UTF-8
Ta biblioteka jest implementacją pełnego systemu callbacków do
używania w bibliotekach widgetów, interfejsach abstrakcyjnych i
ogólnym programowaniu. Oryginalnie była to część zestawu widgetów
Gtk--, ale jest teraz oddzielną biblioteką ogólniejszego
przeznaczenia. Jest to kompletna biblioteka tego typu z możliwością
łączenia abstrakcyjnych callbacków z metodami klas, funkcjami lub
obiektami funkcji. Zawiera klasy adapterów do łączenia różnych
callbacków.

Ten pakiet zawiera wersję skrośną MinGW32.

%package static
Summary:	Static libsigc++ library (cross MinGW32 version)
Summary(pl.UTF-8):	Statyczna biblioteka libsigc++ (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static libsigc++ library (cross MinGW32 version).

%description static -l pl.UTF-8
Statyczna biblioteka libsigc++ (wersja skrośna MinGW32).

%package dll
Summary:	DLL libsigc++ library for Windows
Summary(pl.UTF-8):	Biblioteka DLL libsigc++ dla Windows
Group:		Applications/Emulators
Requires:	wine

%description dll
DLL libsigc++ library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL libsigc++ dla Windows.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure \
	--target=%{target} \
	--host=%{target} \
	--enable-static

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/{devhelp,doc}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libsigc-2.0.dll.a
%{_libdir}/libsigc-2.0.la
%{_libdir}/sigc++-2.0
%{_includedir}/sigc++-2.0
%{_pkgconfigdir}/sigc++-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsigc-2.0.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libsigc-2.0-*.dll
