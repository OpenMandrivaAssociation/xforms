%define major 1
%define	libname_orig libforms
%define libname %mklibname forms %{major}
%define	libname_devel %mklibname forms %{major} -d
%define libname_static_devel %mklibname forms %{major} -s -d
%define _xlibdir %{_prefix}/X11R6/%{_lib}

%define	name	xforms
%define	version	1.0
#%define beta RC4
#%if %beta
#%define rversion %version%beta
#%define release 0.3%{beta}mdk
#%else
%define release 3mdk
#%endif


Name:		%{name}
Summary:	A X11 toolkit library
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
Url:		http://world.std.com/~xforms
Source0:	http://savannah.nongnu.org/download/xforms/stable.pkg/1.0/%{name}-%{version}.tar.bz2
Patch0:		xforms-1.0-makefile.patch.bz2
BuildRequires:	XFree86-devel X11 libjpeg-devel xpm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
xforms is an X11 toolkit library.

It has now gone Open Source (LGPL).

%package -n	%{libname}
Summary:	Libraries for the xforms toolkit
Group:		System/Libraries

%description -n %{libname}
This package contains the runtime libraries for the xforms toolkit.

%package -n	%{libname_devel}
Summary:	Development files for the xforms toolkit
Group:		Development/C
Provides:	%{libname_orig}-devel
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname_devel}
This package contains development headers and libraries for xforms.

Install this if you intend to develop / compile programs with xforms.

%package -n	%{libname_static_devel}
Summary:	The static development files for the xforms toolkit
Group:		Development/C
Provides:	%{libname_orig}-static-devel
Requires:	%{libname_devel} = %{version}-%{release}

%description -n	%{libname_static_devel}
This package contains the static libraries for xforms.

%prep
#%if %beta
#%setup -q -n %name-%rversion
#%else
%setup -q 
#%endif
%patch0 -p1 -b .makefile

%build
(unset RPM_OPT_FLAGS; xmkmf -a)
make CDEBUGFLAGS="$RPM_OPT_FLAGS" REQUIREDLIBS="-L%_xlibdir -lGL -ljpeg -lXpm"

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-, root,root)
%{_prefix}/X11R6/bin/*

%files -n %{libname}
%defattr(-,root,root)
%_xlibdir/*.so.*

%files -n %{libname_devel}
%defattr(-,root,root)
%{_prefix}/X11R6/include/*
%_xlibdir/*.so

%files -n %{libname_static_devel}
%defattr(-,root,root)
%_xlibdir/*.a
