Summary:	Console jabber client
Name:		mcabber
Version:	0.10.1
Release:	2
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://www.lilotux.net/~mikael/mcabber/
Source:		http://www.lilotux.net/~mikael/mcabber/files/mcabber-%{version}.tar.bz2
BuildRequires:	gcc-c++ ncursesw-devel glib2-devel openssl-devel
BuildRequires:	enchant-devel
BuildRequires:	libotr-devel
BuildRequires:	gpgme-devel
BuildRequires:	loudmouth-devel >= 1.4.2
%description
Mcabber is a small jabber console client which supports SSL support, history
logging, external actions and more.

%prep
%setup -q

%build
%configure2_5x --disable-dependency-tracking --enable-enchant --enable-otr
%make

%install
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc mcabberrc.example contrib 
%{_mandir}/man1/mcabber.1*
%{_bindir}/mcabber
%{_datadir}/%{name}/
%_includedir/mcabber/*.c
%_includedir/mcabber/*.h
%{_libdir}/mcabber/libbeep.so
%{_libdir}/mcabber/libxttitle.so
%{_libdir}/pkgconfig/mcabber.pc



%changelog
* Fri Dec 10 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.10.1-1mdv2011.0
+ Revision: 620454
- update to 0.10.1

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2mdv2011.0
+ Revision: 612841
- the mass rebuild of 2010.1 packages

* Wed Apr 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 534886
- add a BR on loudmouth-devel
- new release 0.10.0
- fix file list

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.10-1mdv2010.1
+ Revision: 462311
- Update to new version 0.9.10
- Fix BuildRequires to enable UTF-8, spell check and encryption support

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.9.9-3mdv2010.0
+ Revision: 439790
- rebuild

* Thu Feb 05 2009 Michael Scherer <misc@mandriva.org> 0.9.9-2mdv2009.1
+ Revision: 337744
- rebuild as youri tell me the release part is wrong on x86_64

* Fri Oct 10 2008 Frederik Himpe <fhimpe@mandriva.org> 0.9.9-1mdv2009.1
+ Revision: 291496
- update to new version 0.9.9

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-2mdv2009.0
+ Revision: 268140
- rebuild early 2009.0 package (before pixel changes)

* Wed May 14 2008 Michael Scherer <misc@mandriva.org> 0.9.7-1mdv2009.0
+ Revision: 207256
- update to new version 0.9.7

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Thu Jan 17 2008 Michael Scherer <misc@mandriva.org> 0.9.6-1mdv2008.1
+ Revision: 154099
- new version 0.9.6

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Michael Scherer <misc@mandriva.org> 0.9.5-1mdv2008.1
+ Revision: 110930
- new version

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.9.4-2mdv2008.1
+ Revision: 109214
- rebuild for new lzma

* Wed Oct 31 2007 Michael Scherer <misc@mandriva.org> 0.9.4-1mdv2008.1
+ Revision: 104057
- new version

* Sat Jun 30 2007 Michael Scherer <misc@mandriva.org> 0.9.3-1mdv2008.0
+ Revision: 45966
- 0.9.3

* Wed Jun 13 2007 Michael Scherer <misc@mandriva.org> 0.9.2-1mdv2008.0
+ Revision: 38403
- version 0.9.2

* Sun Apr 22 2007 Michael Scherer <misc@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 16826
- update to 0.9.1


* Sun Dec 24 2006 Michael Scherer <misc@mandriva.org> 0.9.0-1mdv2007.0
+ Revision: 102027
- version 0.9.0

* Wed Dec 13 2006 Michael Scherer <misc@mandriva.org> 0.8.3-1mdv2007.1
+ Revision: 96049
- update to 0.8.3

* Tue Oct 03 2006 Michael Scherer <misc@mandriva.org> 0.8.2-1mdv2007.0
+ Revision: 62828
- update to 0.8.2
- Import mcabber

