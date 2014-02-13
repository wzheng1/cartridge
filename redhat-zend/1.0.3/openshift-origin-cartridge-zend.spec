%global cartridgedir %{_libexecdir}/openshift/cartridges/zend
%global frameworkdir %{_libexecdir}/openshift/cartridges/zend

Name:    openshift-origin-cartridge-zend
Version: 1.2.4
Release: 1%{?dist}
Summary: Zend Server cartridge
Group:   Development/Languages
License: ASL 2.0
URL:     https://openshift.redhat.com
Source0: %{name}-%{version}.tar.gz

Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

Requires: rubygem-builder
# Zend Server 5.6
Requires: zend-server-php-5.3 >= 5.6.0-11
Requires: php-5.3-mongo-zend-server
Requires: php-5.3-imagick-zend-server
Requires: php-5.3-uploadprogress-zend-server
Requires: php-5.3-java-bridge-zend-server
Requires: php-5.3-optimizer-plus-zend-server
Requires: php-5.3-zend-extensions
Requires: php-5.3-extra-extensions-zend-server
Requires: php-5.3-loader-zend-server
# Zend Server 6.x
Requires: zend-server-php-5.4 >= 5.6.0-11

Obsoletes: openshift-origin-cartridge-zend-5.6

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Zend Server cartridge for openshift.

%prep
%setup -q

%build
find versions/ -name .gitignore -delete
find versions/ -name .gitkeep -delete

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%clean
%__rm -rf %{buildroot}

%post
# Zend Server 5.6
%__cp -rf %{cartridgedir}/versions/5.6/configuration/shared-files/usr/local/zend/* /usr/local/zend/
#configure /sandbox/zend dir
sh %{cartridgedir}/versions/5.6/rpm/zend_configure_filesystem.sh
# Zend Server 6.x
cp -rf %{cartridgedir}/versions/6.1/configuration/shared-files/usr/local/zend-server-6-php-5.4/* /usr/local/zend-server-6-php-5.4/

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.adoc
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Wed Feb 12 2014 Adam Miller <admiller@redhat.com> 1.2.4-1
- Card origin_cartridge_111 - Update cartridge versions for stage cut
  (mfojtik@redhat.com)

* Tue Feb 11 2014 Adam Miller <admiller@redhat.com> 1.2.3-1
- Merge pull request #2362 from lnader/master
  (dmcphers+openshiftbot@redhat.com)
- Merge pull request #2360 from danmcp/master
  (dmcphers+openshiftbot@redhat.com)
- Merge pull request #2298 from fabianofranz/dev/441
  (dmcphers+openshiftbot@redhat.com)
- Obsolete zend-5.6 cartridge (lnader@redhat.com)
- Bug 888714 - Remove gitkeep files from rpms (dmcphers@redhat.com)
- Removed references to OpenShift forums in several places
  (contact@fabianofranz.com)

* Mon Feb 10 2014 Adam Miller <admiller@redhat.com> 1.2.2-1
- Cleaning specs (dmcphers@redhat.com)

* Thu Jan 30 2014 Adam Miller <admiller@redhat.com> 1.2.1-1
- bump_minor_versions for sprint 40 (admiller@redhat.com)

* Fri Jan 24 2014 Adam Miller <admiller@redhat.com> 1.1.8-1
- Removing Obsolete flag until bug 1054654 is fixed (lnader@redhat.com)

* Thu Jan 23 2014 Adam Miller <admiller@redhat.com> 1.1.7-1
- Bump up cartridge versions (bparees@redhat.com)

* Fri Jan 17 2014 Adam Miller <admiller@redhat.com> 1.1.6-1
- Merge pull request #2271 from bparees/cart_data_cleanup
  (dmcphers+openshiftbot@redhat.com)
- remove unnecessary cart-data variable descriptions (bparees@redhat.com)

* Thu Jan 16 2014 Adam Miller <admiller@redhat.com> 1.1.5-1
- obsolete zend-5.6 (vvitek@redhat.com)

* Thu Jan 09 2014 Troy Dawson <tdawson@redhat.com> 1.1.4-1
- Bug 1033581 - minor update and adding comment (bleanhar@redhat.com)
- Bug 1033581 - Zend's jenkins_shell_command.erb was effectively the same as
  the stock jenkins-client script (bleanhar@redhat.com)