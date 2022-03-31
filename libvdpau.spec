Name:           libvdpau
Version:        1.5
Release:        10%{?dist}
Summary:        Wrapper library for the Video Decode and Presentation API
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/VDPAU/

Source0:        https://gitlab.freedesktop.org/vdpau/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libX11-devel
BuildRequires:  meson >= 0.41
BuildRequires:  tex(latex)
BuildRequires:  pkgconfig(dri2proto) >= 2.2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
VDPAU is the Video Decode and Presentation API for UNIX. It provides an
interface to video decode acceleration and presentation hardware present in
modern GPUs.

%package        trace
Summary:        Trace library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Supplements:    %{name}-debuginfo%{?_isa}
%endif

%description    trace
The %{name}-trace package contains trace library for %{name}.

%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    docs
The %{name}-docs package contains documentation for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Multilibs trace
Requires:       %{name}-trace%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(x11)
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
#find %{buildroot} -name '*.la' -delete
# Let RPM pick up the docs in the files section
rm -fr %{buildroot}%{_docdir}

%{?ldconfig_scriptlets}

%files
%license COPYING
%doc AUTHORS
%config(noreplace) %{_sysconfdir}/vdpau_wrapper.cfg
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.0.0
%dir %{_libdir}/vdpau/

%files trace
%{_libdir}/vdpau/%{name}_trace.so*

%files docs
%doc %{_vpath_builddir}/doc/html/*

%files devel
%{_includedir}/vdpau/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/vdpau.pc


%changelog
* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1.5-10
- Update to 1.5.

* Sun Feb 13 2022 Simone Caronni <negativo17@gmail.com> - 1.4-10
- Update SPEC file.
- Add upstream patches, enables AV1 decoding as shipped in the upstream Nvidia
  drivers.

* Wed Jun 24 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4-2
- Rebuilt
