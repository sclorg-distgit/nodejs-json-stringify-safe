%{?scl:%scl_package nodejs-json-stringify-safe}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-json-stringify-safe
Version:    5.0.0
Release:    3%{?dist}
Summary:    JSON.stringify that handles circular references
License:    BSD
Group:      Development/Libraries
URL:        https://github.com/isaacs/json-stringify-safe
Source0:    http://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This module provides functionality similar to JavaScript's JSON.stringify, but
it doesn't blow up when it encounters circular references.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/json-stringify-safe
cp -pr stringify.js package.json %{buildroot}%{nodejs_sitelib}/json-stringify-safe

%nodejs_symlink_deps

%check
%{?scl:scl enable %{scl} "}
%__nodejs test.js
%{?scl:"}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/json-stringify-safe
%doc README.md LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 5.0.0-3
- rebuilt

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 5.0.0-2
- replace provides and requires with macro


* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 5.0.0-1
- new upstream release 5.0.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 4.0.0-4
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 4.0.0-3
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.0-3
- Add support for software collections

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 4.0.0-2
- fix rpmlint warnings

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 4.0.0-1
- initial package
