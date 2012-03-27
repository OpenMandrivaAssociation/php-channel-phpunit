%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define pear_xmldir  /var/lib/pear

Name:		php-channel-phpunit
Version:		1.3
Release:		%mkrel 3.1
Summary:		Adds phpunit channel to PEAR
Group:		Development/PHP
License:		BSD
URL:		http://pear.phpunit.de
Source0:		http://pear.phpunit.de/channel.xml
BuildRequires:	php-pear
Requires(post): php-pear
Requires(postun): php-pear
Requires:	php-pear
Requires(post): php-cli
BuildArch:	noarch


%description
This package adds the phpunit channel which allows PEAR packages from this
channel to be installed.

%prep

%setup -q -c -T

%build
# Empty build section, nothing to build

%install

%{__mkdir_p} %{buildroot}%{pear_xmldir}
%{__install} -pm 644 %{SOURCE0} %{buildroot}%{pear_xmldir}/pear.phpunit.de.xml


%clean

%{__rm} -rf %{buildroot

%post
if [ $1 -qt  1 ] ; then
    pear channel-update pear.phpunit.de
else
    pear channel-add %{pear_xmldir}/pear.phpunit.de.xml
fi

%preun

if [ $1 -eq 0 ] ; then
    pear channel-delete pear.phpunit.de
fi


%files
%defattr(-,root,root,-)
%{pear_xmldir}/pear.phpunit.de.xml
