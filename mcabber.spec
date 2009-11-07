Summary: Console jabber client
Name: mcabber
Version: 0.9.10
Release: %mkrel 1
License: GPLv2+
Group: Networking/Instant messaging
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.lilotux.net/~mikael/mcabber/
Source: http://www.lilotux.net/~mikael/mcabber/files/mcabber-%{version}.tar.bz2
BuildRequires: gcc-c++ ncursesw-devel glib2-devel openssl-devel
BuildRequires: enchant-devel
BuildRequires: libotr-devel
BuildRequires: gpgme-devel
%description
Mcabber is a small jabber console client which supports SSL support, history
logging, external actions and more.

%prep
%setup -q

%build
%configure2_5x --disable-dependency-tracking --enable-enchant --enable-otr
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc mcabberrc.example contrib 
%{_mandir}/man1/mcabber.1*
%{_bindir}/mcabber
%{_datadir}/%{name}/


