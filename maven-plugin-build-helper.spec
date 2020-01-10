Name:           maven-plugin-build-helper
Version:        1.5
Release:        13%{?dist}
Summary:        Build Helper Maven Plugin

Group:          Development/Libraries
License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/build-helper-maven-plugin/
# The source tarball has been generated from upstream VCS:
# svn export https://svn.codehaus.org/mojo/tags/build-helper-maven-plugin-%{version} 
#            %{name}-%{version}
# tar caf %{name}-%{version}.tar.xz %{name}-%{version}
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         add-junit-dependency.patch
Patch1:         %{name}-core.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: plexus-utils
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-doxia-sitetools
BuildRequires: mojo-parent
BuildRequires: junit4

%description
This plugin contains various small independent goals to assist with
Maven build lifecycle.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%patch0
%patch1 -p1
cp %{SOURCE1} LICENSE-2.0.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc header.txt LICENSE-2.0.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc header.txt LICENSE-2.0.txt

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.5-13
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 1.5-12
- Migrate away from mvn-rpmbuild (Resolves: #997496)

* Mon Jul 29 2013 Michal Srb <msrb@redhat.com> - 1.5-11
- Install MIT license text

* Fri Jul 26 2013 Tomas Radej <tradej@redhat.com> - 1.5-10
- Add missing ASL license text and installed all license files

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.5-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Tomas Radej <tradej@redhat.com> - 1.5-4
- Update to current guidelines
- Fix build

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Alexander Kurtakov <akurtako@redhat.com> 1.5-2
- Maven plugins should require parent poms because they are totally unusable without them.

* Thu Sep 16 2010 Alexander Kurtakov <akurtako@redhat.com> 1.5-1
- Update to 1.5.
- Use newer maven packages' names.

* Thu Sep 10 2009 Alexander Kurtakov <akurtako@gmail.com> 1.4-1
- Initial package.
