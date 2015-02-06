%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define pear_xmldir  /var/lib/pear

Name:		php-channel-phpunit
Version:		1.3
Release:		10
Summary:		Adds phpunit channel to PEAR
Group:		Development/PHP
License:		BSD
URL:		http://pear.phpunit.de
Source0:		http://pear.phpunit.de/channel.xml
BuildRequires:	php-pear
Requires(pre): php-cli
Requires(pre): php-pear
Requires(postun): php-pear
Requires:	php-pear
BuildArch:	noarch


%description
This package adds the phpunit channel which allows PEAR packages from this
channel to be installed.

%prep

%setup -q -c -T

%build
# Empty build section, nothing to build

%install

%{__mkdir_p} %{buildroot}%{_datadir}/pear/packages/
%{__install} -pm 644 %{SOURCE0} %{buildroot}%{_datadir}/pear/packages/pear.phpunit.de.xml


%post
if [ $1 -eq  1 ] ; then
    pear channel-add %{_datadir}/pear/packages/pear.phpunit.de.xml
else
    pear channel-update %{_datadir}/pear/packages/pear.phpunit.de.xml
fi

%preun
if [ $1 -eq 0 ] ; then
    pear channel-delete pear.phpunit.de
fi


%files
%{_datadir}/pear/packages/pear.phpunit.de.xml


%changelog
* Mon Apr 02 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.3-5mdv2012.0
+ Revision: 788601
+ rebuild (emptylog)

* Tue Mar 27 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.3-4
+ Revision: 787371
+ rebuild (emptylog)

* Tue Mar 27 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.3-3.1
+ Revision: 787365
+ rebuild (emptylog)

* Thu Mar 22 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.3-3
+ Revision: 785994
- fixed spec so it will update and install on BS

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3-2
+ Revision: 679254
- mass rebuild

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdv2011.0
+ Revision: 600418
- 1.3
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 1.0-7mdv2010.0
+ Revision: 397361
- rebuild
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2009.1
+ Revision: 321707
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 258994
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 246868
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Nov 06 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2008.1
+ Revision: 106411
- import php-channel-phpunit


* Tue Nov 06 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2008.1
- initial Mandriva package (fc8 import)

* Fri Dec 29 2006 Christopher Stone <chris.stone@gmail.com> 1.0-2
- Add virtual provides on channel name

* Wed Dec 27 2006 Christopher Stone <chris.stone@gmail.com> 1.0-1
- Initial Release
