Summary:	SETI@home client statistics monitor for WindowMaker
Summary(pl):	Monitor statystyk klienta SETI@home dla WindowMakera
Name:		wmseti
Version:	0.3.6
Release:	1
Group:		X11/Window Managers/Tools
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO BUGS AUTHORS NEWS
%attr(755,root,root) %{_bindir}/wmseti
%config %{_sysconfdir}/wmsetirc
