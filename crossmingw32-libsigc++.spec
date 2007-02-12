#
%define		_realname	libsigc++
Summary:	The Typesafe Signal Framework for C++ - Mingw32 cross version
Summary(pl.UTF-8):   Środowisko sygnałów z kontrolą typów dla C++ - wersja skrośna dla Mingw32
Name:		crossmingw32-%{_realname}
Version:	2.0.17
Release:	2
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libsigc++/2.0/%{_realname}-%{version}.tar.bz2
# Source0-md5:	fde0ee69e3125e982746d9fe005763e1
URL:		http://libsigc.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.9
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	m4
BuildRequires:	perl-base
Obsoletes:	libsigc++-examples
Conflicts:	libsigc++ < 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a seperate library to
provide for more general use. It is the most complete library of its
kind with the ablity to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

%description -l pl.UTF-8
Ta biblioteka jest implementacją pełnego systemu callbacków do
używania w bibliotekach widgetów, interfejsach abstrakcyjnych i
ogólnym programowaniu. Oryginalnie była to część zestawu widgetów
Gtk--, ale jest teraz oddzielną biblioteką ogólniejszego
przeznaczenia. Jest to kompletna biblioteka tego typu z możliwością
łączenia abstrakcyjnych callbacków z metodami klas, funkcjami lub
obiektami funkcji. Zawiera klasy adapterów do łączenia różnych
callbacków.

%prep
%setup -q -n %{_realname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}

%configure \
	--host=%{target_platform} \
	%{!?with_static_libs:--disable-static}
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%dir %{_includedir}/sigc++-2.0
%{_includedir}/sigc++-2.0
%dir %{_libdir}/sigc++-2.0
%{_libdir}/sigc++*
%{_prefix}/lib/pkgconfig/*
