Summary:	SETI@home client statistics monitor for WindowMaker
Summary(pl.UTF-8):	Monitor statystyk klienta SETI@home dla WindowMakera
Name:		wmseti
Version:	1.0.3
Release:	1
Group:		X11/Window Managers/Tools
License:	GPL
Source0:	http://dl.sourceforge.net/wmseti/%{name}-%{version}.tar.gz
# Source0-md5:	080d234c9f0d1178da8ab7b5d934a77c
Patch0:		%{name}-rcpath.patch
URL:		http://wmseti.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmseti is a WindowMaker dockapp which monitors your SETI@home client
statistics.

%description -l pl.UTF-8
wmseti jest dokowalnym apletem dla WindowMakera, który monitoruje
statystyki klienta SETI@home.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install wmsetirc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/wmseti
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wmsetirc
