%define major 2
%define libname_orig libforms
%define libname %mklibname forms %{major}
%define libname_devel %mklibname forms -d

%define _empty_manifest_terminate_build 0

# Workaround duplicate symbols
%global optflags %{optflags} -fcommon

Name:		xforms
Summary:	A X11 toolkit library
Version:	1.2.4
Release:	2
License:	LGPL
Group:		System/Libraries
Url:		https://xforms-toolkit.org/
Source0:	http://download.savannah.gnu.org/releases/xforms/%{name}-%{version}.tar.gz
Patch0:   xforms-1.2.4-fno-common.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gl)

%description
xforms is a graphical toolkit library.

%package -n %{libname}
Summary:	Libraries for the xforms toolkit
Group:		System/Libraries

%description -n %{libname}
This package contains the runtime libraries for the xforms toolkit.

%package -n %{libname_devel}
Summary:	Development files for the xforms toolkit
Group:		Development/C
Provides:	%{libname_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname -d forms 1} < 1.2.4
Obsoletes:	%{mklibname -d -s forms 1} < 1.2.4
Obsoletes:	%{mklibname forms -s -d} < 1.2.4

%description -n	%{libname_devel}
This package contains development headers and libraries for xforms.
Install this if you intend to develop / compile programs with xforms.

%prep
%setup -q
%autopatch -p1

%build
#export CC=gcc
#export CXX=g++
%configure
%make_build

%install
%make_install

%files
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{libname_devel}
%{_includedir}/*
%{_mandir}/man5/*
%{_libdir}/*.so
