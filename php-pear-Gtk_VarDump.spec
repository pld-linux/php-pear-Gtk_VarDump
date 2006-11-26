%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	VarDump
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a simple GUI to example PHP data trees
Summary(pl):	%{_pearname} - proste GUI pokazuj±ce przyk³adowe drzewo danych
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5ce06e3b157a9c86c4e669ded2fd4315
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

%description -l pl
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
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.glade
