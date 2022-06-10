Summary:	TCP/IP emulator used by virtual machine hypervisors to provide virtual networking services
Summary(pl.UTF-8):	Emulator TCP/IP używany przez hipernadzorców maszyn wirtualnych do udostępniania wirtualnych usług sieciowych
Name:		libslirp
Version:	4.7.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://gitlab.freedesktop.org/slirp/libslirp/-/releases (JS required)
Source0:	https://gitlab.freedesktop.org/slirp/libslirp/uploads/60113f60cfd6abe2c16dde9f6c81b631/%{name}-%{version}.tar.xz
# Source0-md5:	05c144ca7863a5259d7e3ff25637f937
URL:		https://gitlab.freedesktop.org/slirp/libslirp
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	meson >= 0.50
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Conflicts:	spice-slirp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libslirp is a user-mode networking library used by virtual machines,
containers or various tools.

%description -l pl.UTF-8
libslirp to biblioteka sieciowa przestrzeni użytkownika, używana przez
maszyny wirtualne, kontenery lub różne narzędzia.

%package devel
Summary:	Header files for SLIRP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SLIRP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Conflicts:	spice-slirp-devel

%description devel
Header files for SLIRP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SLIRP.

%package static
Summary:	Static SLIRP library
Summary(pl.UTF-8):	Statyczna biblioteka SLIRP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	spice-slirp-static

%description static
Static SLIRP library.

%description static -l pl.UTF-8
Statyczna biblioteka SLIRP.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYRIGHT README.md
%attr(755,root,root) %{_libdir}/libslirp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libslirp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libslirp.so
%{_includedir}/slirp
%{_pkgconfigdir}/slirp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libslirp.a
