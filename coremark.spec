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

cat << \EOF >> run-coremark.sh
#!/bin/sh
ITERATIONS=0

echo "running coremark run 1, logs: /tmp/run1.log"
coremark 0x0 0x0 0x66 $ITERATIONS 7 1 2000 > /tmp/run1.log

echo "running coremark run 2, logs: /tmp/run2.log"
coremark 0x3415 0x3415 0x66 $ITERATIONS 7 1 2000 > /tmp/run2.log

echo "running coremark run 3, logs: /tmp/run3.log"
coremark 8 8 8 $ITERATIONS 7 1 2000 > /tmp/run3.log
EOF


%install
mkdir -p %{buildroot}/%{_bindir}/
install -m755 coremark.exe %{buildroot}/%{_bindir}/coremark
install -m755 run-coremark.sh %{buildroot}/%{_bindir}/

%files
%attr(0755,root,root) %{_bindir}/coremark
%attr(0755,root,root) %{_bindir}/run-coremark.sh

%changelog
* Tue Apr 05 2016 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com> 1.0-1
- new package built with tito

