%include	/usr/lib/rpm/macros.php
%define		_class		DBA
%define		_status		stable

%define		_pearname	%{_class}
Summary:	%{_pearname} - Berkeley-style Database Class
Summary(pl):	%{_pearname} - klasa bazy danych w stylu Berkeley
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	55bf3ff111e3ceea9fd985e975ac4d09
URL:		http://pear.php.net/package/DBA/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implements a DBM-style database using either PHP's DBA functions or a
simple DBM class written in PHP. Also provides a relational database
system with support for selects, joins, sorts, projects, multiple
tables, type checking, autoincrements and more.

In PEAR status of this package is: %{_status}.

%description -l pl
Implementacja bazy danych w stylu DBM, u¿ywaj±cej PHP-owych funkcji
DBA lub prostych klas DBM napisanych w PHP. Dostarcza tak¿e relacyjny
system bazodanowy z obs³ug± funkcji select, join, sort, project, wielu
tabel, sprawdzania typów, autoinkrementacji itd.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Driver

install %{_class}-%{version}/%{_class}.php $RPM_BUILD_ROOT%{php_pear_dir}
install %{_class}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_class}-%{version}/%{_class}/Driver/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Driver

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_class}-%{version}/{tests,docs}/*
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Driver
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Driver/*
