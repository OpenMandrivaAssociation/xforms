%define major 1
%define	libname_orig libforms
%define libname %mklibname forms %{major}
%define	libname_devel %mklibname forms -d
%define libname_static_devel %mklibname forms -s -d

%define	name	xforms
%define	version	1.0

Name:		%{name}
Summary:	A X11 toolkit library
Version:	%{version}
Release:	%mkrel 6
License:	LGPL
Group:		System/Libraries
Url:		http://world.std.com/~xforms
Source0:	http://savannah.nongnu.org/download/xforms/stable.pkg/1.0/%{name}-%{version}.tar.bz2
Patch0:		xforms-1.0-makefile.patch
BuildRequires:	X11-devel libjpeg-devel xpm-devel xpm-static-devel imake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q 
%patch0 -p1 -b .makefile

%build
(unset RPM_OPT_FLAGS; xmkmf -a)
make CDEBUGFLAGS="$RPM_OPT_FLAGS" REQUIREDLIBS="-lGL -ljpeg -lXpm"

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

%files -n %{libname}
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %{libname_devel}
%defattr(-,root,root)
%_includedir/*
%_libdir/*.so

%files -n %{libname_static_devel}
%defattr(-,root,root)
%_libdir/*.a
