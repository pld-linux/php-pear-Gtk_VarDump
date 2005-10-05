%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	VarDump
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a simple GUI to example PHP data trees
Summary(pl):	%{_pearname} - proste GUI pokazujące przykładowe drzewo danych
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8bd5e28c188d6cd139d9c8ce765a53f5
URL:		http://pear.php.net/package/Gtk_VarDump/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php4-gtk
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
