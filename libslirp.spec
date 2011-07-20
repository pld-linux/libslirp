Summary:	User network stack library
Summary(pl.UTF-8):	Biblioteka stosu sieciowego użytkownika
Name:		libslirp
%define	snap	20110720
Version:	0.0.1
Release:	0.%{snap}.1
License:	BSD
Group:		Libraries
# git clone git://git.freedesktop.org/git/spice/slirp slirp
Source0:	slirp-%{version}-%{snap}.tar.xz
# Source0-md5:	a6718999a17207a32b0febf154efe222
URL:		http://spice-space.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User network stack library.

%description -l pl.UTF-8
Biblioteka stosu sieciowego użytkownika.

%package devel
Summary:	Header files for SLIRP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SLIRP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SLIRP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SLIRP.

%package static
Summary:	Static SLIRP library
Summary(pl.UTF-8):	Statyczna biblioteka SLIRP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SLIRP library.

%description static -l pl.UTF-8
Statyczna biblioteka SLIRP.

%prep
%setup -q -n slirp

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libslirp.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_libdir}/libslirp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libslirp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libslirp.so
%{_includedir}/libslirp
%{_pkgconfigdir}/slirp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libslirp.a
