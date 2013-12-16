%define		pkgname	files_epubviewer
Summary:	let you read your ebooks online!
Name:		owncloud-%{pkgname}
Version:	0.6.1
Release:	0.1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://www.les-charles.net/files/files_epubviewer_oc5.tar.gz
# Source0-md5:	8376b5ee02d6c21794539f9a00346651
URL:		http://apps.owncloud.com/content/show.php/EPub+online+reader+%28oc5%29?content=157609
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	owncloud >= 5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/owncloud/apps/%{pkgname}

%description
let you read your ebooks online!

%prep
%setup -q -n %{pkgname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -a * $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
