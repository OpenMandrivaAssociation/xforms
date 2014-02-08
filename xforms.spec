%define major 2
%define	libname_orig libforms
%define libname %mklibname forms %{major}
%define	libname_devel %mklibname forms -d
%define libname_static_devel %mklibname forms -s -d

%define	name	xforms
%define	version	1.0

Name:		xforms
Summary:	A X11 toolkit library
Version:	1.0.93.sp1
Release:	5
License:	LGPL
Group:		System/Libraries
Url:		http://xforms-toolkit.org/
Source0:	http://download.savannah.gnu.org/releases/xforms/xforms-1.0.93sp1.tar.gz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	jpeg-devel
BuildRequires:	GL-devel

%description
xforms is a graphical toolkit library.

%package -n	%{libname}
Summary:	Libraries for the xforms toolkit
Group:		System/Libraries

%description -n %{libname}
This package contains the runtime libraries for the xforms toolkit.

%package -n	%{libname_devel}
Summary:	Development files for the xforms toolkit
Group:		Development/C
Provides:	%{libname_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%mklibname -d forms 1

%description -n	%{libname_devel}
This package contains development headers and libraries for xforms.

Install this if you intend to develop / compile programs with xforms.

%package -n	%{libname_static_devel}
Summary:	The static development files for the xforms toolkit
Group:		Development/C
Provides:	%{libname_orig}-static-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname_devel} = %{version}-%{release}
Obsoletes:	%mklibname -d -s forms 1

%description -n	%{libname_static_devel}
This package contains the static libraries for xforms.

%prep
%setup -qn xforms-1.0.93sp1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-, root,root)
%_bindir/*
%_mandir/man1/*

%files -n %{libname}
%defattr(-,root,root)
%_libdir/*.so.%{major}*

%files -n %{libname_devel}
%defattr(-,root,root)
%_includedir/*
%_mandir/man5/*
%_libdir/*.so

%files -n %{libname_static_devel}
%defattr(-,root,root)
%_libdir/*.a


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.93.sp1-2mdv2011.0
+ Revision: 671313
- mass rebuild

* Thu Dec 23 2010 Funda Wang <fwang@mandriva.org> 1.0.93.sp1-1mdv2011.0
+ Revision: 623970
- new version 1.0.93 sp1

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-11mdv2011.0
+ Revision: 608207
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2010.1
+ Revision: 488815
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-9mdv2010.0
+ Revision: 416700
- fix deps
- rebuilt against libjpeg v7

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0-8mdv2009.1
+ Revision: 366672
- fix str fmt

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2009.0
+ Revision: 239734
- rebuild
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2008.1
+ Revision: 179506
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Funda Wang <fwang@mandriva.org> 1.0-5mdv2008.0
+ Revision: 81000
- reintroduce static devel package
- new devel package policy

* Sat May 05 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-4mdv2008.0
+ Revision: 22668
- clean spec, rebuild for new era
- Import xforms



* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.0-3mdk
- Rebuild

* Sat Dec 25 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.0-2mdk
- fix buildrequires
- drop useless-explicit-provides
- fix summary-ended-with-dot
- cosmetics

* Mon Jul 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.0-1mdk
- 1.0
- updated url
- use %%mklibname
- macroize a little
- drop some stuff from P0, some merged upstream

* Thu Sep 26 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0-0.2RC4mdk
- Fix Patch1 (makefile) to get correct SystemUsrLibDir and totally
  nuke references to -I/usr/local/include. Aka, make it lib64-aware.

* Thu Aug 15 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-0.1RC4mdk
- rc4
- rebuild for new g++-3.2 ABI
- major is 1 now
- rediff patch 0
- fix build

* Sat Jun 15 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.9999-6mdk
- Link against -lxpm as well. (Crufty!!)

* Wed Jun 05 2002 Stefan van der Eijk <stefan@eijk.nu> 0.9999-5mdk
- BuildRequires

* Fri May 17 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.9999-4mdk
- Add ldconfig to post and postun.

* Fri May 17 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.9999-3mdk
- Link against -lGL and -ljpeg.

* Thu May 16 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.9999-2mdk
- Add a url (askwar).

* Tue May 14 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.9999-1mdk
- First Mandrake version.
