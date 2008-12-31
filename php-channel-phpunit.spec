Summary:	Adds phpunit channel to PEAR
Name:		php-channel-phpunit
Version:	1.0
Release:	%mkrel 5
Group:		Development/PHP
License:	BSD
URL:		http://pear.phpunit.de
Source0:	http://pear.phpunit.de/channel.xml
BuildRequires:	php-pear
Requires:	php-pear
Requires(post): php-pear
Requires(postun): php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package adds the phpunit channel which allows PEAR packages from this
channel to be installed.

%prep

%setup -q -c -T

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/packages

install -m0644 %{SOURCE0} %{buildroot}%{_datadir}/pear/packages/pear.phpunit.de.xml

%post
if [ $1 -eq  1 ] ; then
    %{_bindir}/pear channel-add %{_datadir}/pear/packages/pear.phpunit.de.xml > /dev/null || :
else
    %{_bindir}/pear channel-update %{_datadir}/pear/packages/pear.phpunit.de.xml > /dev/null ||:
fi

%postun
if [ $1 -eq 0 ] ; then
    %{_bindir}/pear channel-delete pear.phpunit.de > /dev/null || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/pear/packages/pear.phpunit.de.xml

