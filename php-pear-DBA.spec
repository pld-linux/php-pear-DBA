%include	/usr/lib/rpm/macros.php
%define		_class		DBA
%define		_pearname	%{_class}
Summary:	%{_class} - Berkely-style Database Class
Summary(pl):	%{_class} - klasa bazy danych w stylu Berkely
Name:		php-pear-%{_pearname}
Version:	0.17
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implements a DBM-style database using either PHP's DBA functions or a
simple DBM class written in PHP. Also provides a relational database
system with support for selects, joins, sorts, projects, multiple
tables, type checking, autoincrements and more.

%description -l pl
Implementacja bazy danych w stylu DBM, u¿ywaj±cej PHP-owych funkcji
DBA lub prostych klas DBM napisanych w PHP. Dostarcza tak¿e relacyjny
system bazo-danowy z supportem do funkcji select, join, sort, project,
wielu tablic, sprawdzania typów, autoinkrementacji itd.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/DB/%{_class}

install %{_class}-%{version}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/DB/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_class}-%{version}/{tests,docs}/*
%dir %{php_pear_dir}/DB/%{_class}
%{php_pear_dir}/DB/%{_class}/*.php
