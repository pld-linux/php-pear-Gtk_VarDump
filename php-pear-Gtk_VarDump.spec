%define		_status		stable
%define		_pearname	Gtk_VarDump
Summary:	%{_pearname} - a simple GUI to example PHP data trees
Summary(pl.UTF-8):	%{_pearname} - proste GUI pokazujące przykładowe drzewo danych
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1dd54b74bb5ddd1e994b5261b4aacd21
URL:		http://pear.php.net/package/Gtk_VarDump/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gtk)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Just a regedit type interface to examine PHP data trees.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Prosty interfejs w stylu regedit do badania drzew danych PHP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Gtk/VarDump.php
%{php_pear_dir}/data/%{_pearname}
