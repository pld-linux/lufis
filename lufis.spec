Summary:	Wrapper to use lufs modules with fuse kernel support
Summary(pl):	Wrapper do u�ywania modu��w lufs z j�drem obs�uguj�cym fuse
Name:		lufis
Version:	0.3
Release:	1
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fuse/%{name}-%{version}.tar.gz
# Source0-md5:	fd3e4eebf3967b75157bc42418326d03
Patch0:		%{name}-no_lufs.patch
URL:		http://fuse.sourceforge.net/
BuildRequires:	libfuse-devel
Requires:	fusermount
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper to use lufs modules with fuse kernel support.

%description -l pl
Wrapper do u�ywania modu��w lufs z j�drem obs�uguj�cym fuse.

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
