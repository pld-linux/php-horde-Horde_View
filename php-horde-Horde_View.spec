%define		status		stable
%define		pearname	Horde_View
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde View API
Name:		php-horde-Horde_View
Version:	1.0.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	ca2948aac29882d1a9a8ba0ca6ebde7a
URL:		https://github.com/horde/horde/tree/master/framework/View/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Controller
Suggests:	php-horde-Horde_Routes
Suggests:	php-json
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Controller.*) pear(Horde/Routes.*)

%description
The Horde_View library provides a simple View pattern implementation.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/Horde_View/examples .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/Horde_View/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/View.php
%{php_pear_dir}/Horde/View
%{_examplesdir}/%{name}-%{version}
