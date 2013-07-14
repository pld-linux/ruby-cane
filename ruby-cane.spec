#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	cane
Summary:	Code quality threshold checking as part of your build
Name:		ruby-%{pkgname}
Version:	2.6.0
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	4f5428737cf48129476ad789ebec3a69
URL:		http://github.com/square/cane
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.0
BuildRequires:	ruby-rspec-fire
BuildRequires:	ruby-simplecov
%endif
Requires:	ruby-parallel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fails your build if code quality thresholds are not met. Provides
complexity and style checkers built-in, and allows integration with
with custom quality metrics.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cane
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
