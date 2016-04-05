Summary: Coremark
Name: coremark
Version: 1.0
Release: 1
Group: System Environment/Libraries
URL: http://www.eembc.org/coremark
Vendor: EEMBC
License: Proprietary
Packager: Builder <builder@thales-ktw.site>
Source: %{name}-%{version}.tar.gz

%description
Coremark

%prep
%setup -q -n %{name}-%{version}

%build
make compile

%install
mkdir -p %{buildroot}/%{_bindir}/
install -m755 coremark.exe %{buildroot}/%{_bindir}/coremark

%files
%attr(0755,root,root) %{_bindir}/coremark

%changelog
