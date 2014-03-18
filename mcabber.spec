Summary:	Console jabber client
Name:		mcabber
Version:	0.10.2
Release:	2
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://www.lilotux.net/~mikael/mcabber/
Source0:	http://www.lilotux.net/~mikael/mcabber/files/mcabber-%{version}.tar.bz2
Patch0:		mcabber-0.10.2-libotr4.patch
BuildRequires:	gpgme-devel
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libotr)
BuildRequires:	pkgconfig(loudmouth-1.0)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(openssl)

%description
Mcabber is a small jabber console client which supports SSL support, history
logging, external actions and more.

%files
%doc AUTHORS ChangeLog NEWS README TODO
%doc mcabberrc.example contrib
%{_mandir}/man1/mcabber.1*
%{_bindir}/mcabber
%{_datadir}/%{name}/
%{_libdir}/mcabber/libbeep.so
%{_libdir}/mcabber/libxttitle.so
%{_libdir}/mcabber/libfifo.so
%{_libdir}/mcabber/liburlregex.so

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Conflicts:	%{name} < 0.10.2-2

%description devel
Development files for %{name}.

%files devel
%{_includedir}/mcabber/*.c
%{_includedir}/mcabber/*.h
%{_libdir}/pkgconfig/mcabber.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure2_5x \
	--disable-dependency-tracking \
	--enable-enchant \
	--enable-otr
%make

%install
%makeinstall_std

