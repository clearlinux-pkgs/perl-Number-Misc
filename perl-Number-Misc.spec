#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Number-Misc
Version  : 1.2
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIKO/Number-Misc-1.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIKO/Number-Misc-1.2.tar.gz
Summary  : 'Number::Misc - handy utilities for numbers'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Number-Misc-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Number::Misc - handy utilities for numbers
SYNOPSIS
use Number::Misc ':all';

is_numeric('x');        # false
to_number('3,000');     # 3000
commafie('3000');       # 3,000
zero_pad(2, 10);        # 0000000002
rand_in_range(3, 10);   # a random number from 3 to 10, inclusive
is_even(3)              # true
is_odd(4);              # true

%package dev
Summary: dev components for the perl-Number-Misc package.
Group: Development
Provides: perl-Number-Misc-devel = %{version}-%{release}
Requires: perl-Number-Misc = %{version}-%{release}

%description dev
dev components for the perl-Number-Misc package.


%package perl
Summary: perl components for the perl-Number-Misc package.
Group: Default
Requires: perl-Number-Misc = %{version}-%{release}

%description perl
perl components for the perl-Number-Misc package.


%prep
%setup -q -n Number-Misc-1.2
cd %{_builddir}/Number-Misc-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Number::Misc.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Number/Misc.pm
/usr/lib/perl5/vendor_perl/5.28.2/Number/Misc.pod
