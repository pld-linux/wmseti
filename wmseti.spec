Summary:	SETI@home client statistics monitor for WindowMaker
Summary(pl):	Monitor statystyk klienta SETI@home dla WindowMakera
Name:		wmseti
Version:	0.3.0
Release:	3
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
License:	GPL
Source0:	http://prdownloads.sourceforge.net/wmseti/%{name}-%{version}.tar.gz
Patch0:		%{name}-rcpath.patch
URL:		http://wmseti.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
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
rm -f missing
aclocal
autoconf
automake -a -c
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
%doc *.gz
%attr(755,root,root) %{_bindir}/wmseti
%config %{_sysconfdir}/wmsetirc
