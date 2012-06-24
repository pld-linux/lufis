Summary:	Wrapper to use lufs modules with fuse kernel support
Summary(pl.UTF-8):   Wrapper do używania modułów lufs z jądrem obsługującym fuse
Name:		lufis
Version:	0.3
Release:	3
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fuse/%{name}-%{version}.tar.gz
# Source0-md5:	fd3e4eebf3967b75157bc42418326d03
Patch0:		%{name}-allow-uid-and-gid-addon.patch 
URL:		http://fuse.sourceforge.net/
BuildRequires:	libfuse-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper to use lufs modules with fuse kernel support.

%description -l pl.UTF-8
Wrapper do używania modułów lufs z jądrem obsługującym fuse.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install lufis $RPM_BUILD_ROOT%{_bindir}/lufis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/lufis
