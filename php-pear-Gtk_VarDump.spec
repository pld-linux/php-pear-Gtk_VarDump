%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	VarDump
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a simple GUI to example php data trees
Summary(pl):	%{_pearname} - proste GUI pokazujące przykładowe drzewo danych
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	91c0a92940bc614f0de5c16e7bb200bc
URL:		http://pear.php.net/package/Gtk_VarDump/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-gtk
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.glade $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.glade
