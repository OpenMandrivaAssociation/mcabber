Summary: Console jabber client
Name: mcabber
Version: 0.9.1
Release: %mkrel 1
License: GPL
Group: Networking/Instant messaging
URL: http://www.lilotux.net/~mikael/mcabber/
Source: http://www.lilotux.net/~mikael/mcabber/files/mcabber-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++ ncurses-devel glib2-devel openssl-devel

%description
Mcabber is a small jabber console client which supports SSL support, history
logging, external actions and more.

%prep
%setup -q

%build
%configure
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc mcabberrc.example contrib 
%{_mandir}/man1/mcabber.1*
%{_bindir}/mcabber
%{_datadir}/%{name}/


