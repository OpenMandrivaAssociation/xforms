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
Release:	%mkrel 2
License:	LGPL
Group:		System/Libraries
Url:		http://xforms-toolkit.org/
Source0:	http://download.savannah.gnu.org/releases/xforms/xforms-1.0.93sp1.tar.gz
BuildRequires:	libx11-devel
BuildRequires:	libxpm-devel
BuildRequires:	jpeg-devel
BuildRequires:	GL-devel
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
%_libdir/*.la

%files -n %{libname_static_devel}
%defattr(-,root,root)
%_libdir/*.a
