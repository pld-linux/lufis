Summary:	Wrapper to use lufs modules with fuse kernel support
Name:		lufis
Version:	0.2
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fuse/%{name}-%{version}.tar.gz
# Source0-md5:	3324523d2e9a10e24c0c5d7ddf76497b
Patch0:		%{name}-no_lufs.patch
URL:		http://fuse.sourceforge.net/
BuildRequires:	libfuse-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper to use lufs modules with fuse kernel support.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT/%{_bindir}
install lufis $RPM_BUILD_ROOT/%{_bindir}/lufis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/lufis