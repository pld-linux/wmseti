Summary:	SETI@home client statistics monitor for WindowMaker
Summary(pl):	Monitor statystyk klienta SETI@home dla WindowMakera
Name:		wmseti
Version:	0.2.0
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source:		http://catv6054.extern.kun.nl/~paul/wmseti/%{name}-%{version}.tar.gz
Patch:		wmseti-rcpath.patch
URL:		http://catv6054.extern.kun.nl/~paul/wmseti/
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

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

make CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

install -s wmseti $RPM_BUILD_ROOT%{_bindir}
install wmsetirc  $RPM_BUILD_ROOT%{_datadir}

gzip -9nf README Changelog TODO BUGS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changelog,TODO,BUGS,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/wmseti
%config %{_datadir}/wmsetirc
