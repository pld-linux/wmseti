Summary:	SETI@home client statistics monitor for WindowMaker
Summary(pl):	Monitor statystyk klienta SETI@home dla WindowMakera
Name:		wmseti
Version:	0.3.0
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
License:	GPL
Source:		http://catv6054.extern.kun.nl/~paul/wmseti/%{name}-%{version}.tar.gz
Patch:		wmseti-rcpath.patch
URL:		http://catv6054.extern.kun.nl/~paul/wmseti/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/Apps

%description
wmseti is a WindowMaker dockapp which monitors your SETI@home client
statistics.

%description -l pl
wmseti jest dokowalnym apletem dla WindowMakera, który monitoruje
statystyki twojego klienta SETI@home.

%prep
%setup -q
%patch -p0

%build
LDFLAGS="-s"; export LDFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog TODO BUGS AUTHORS NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,TODO,BUGS,AUTHORS,NEWS}.gz
%attr(755,root,root) %{_bindir}/wmseti
%config %{_sysconfdir}/wmsetirc
