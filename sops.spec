%global goipath go.mozilla.org/sops/v3
%global forgeurl https://github.com/mozilla/sops
Version: 3.7.3

%global gomodulesmode GO111MODULE=on

%gometa

%global commit0 e1edc059487ddd14236dfe47267b05052f6c20b4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: sops
Release: 1%{?dist}
Summary: Simple and flexible tool for managing secrets
License: MPL-2.0
URL: %{gourl}
Source0: %{gosource}

%description
%{summary}

%prep
%goprep -k

%build
%gobuild -o %{gobuilddir}/bin/sops %{goipath}/cmd/sops

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.rst CHANGELOG.rst CODE_OF_CONDUCT.md CONTRIBUTING.md
%{_bindir}/*

%changelog
* Mon Dec 26 2022 Karel Van Hecke <copr@karelvanhecke.com> - 3.7.3-1
- Initial build
