%define upstream_name    IO-BufferedSelect
%define upstream_version 1.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Line-buffered select interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The 'select' system call (and the 'IO::Select' interface) allows us to
process multiple streams simultaneously, blocking until one or more of them
is ready for reading or writing. Unfortunately, this requires us to use
'sysread' and 'syswrite' rather than Perl's buffered I/O functions. In the
case of reading, there are two issues with combining 'select' with
'readline': (1) 'select' might block but the data we want is already in
Perl's input buffer, ready to be slurped in by 'readline'; and (2) 'select'
might indicate that data is available, but 'readline' will block because
there isn't a full '$/'-terminated line available.

The purpose of this module is to implement a buffered version of the
'select' interface that operates on _lines_, rather than characters. Given
a set of filehandles, it will block until a full line is available on one
or more of them.

Note that this module is currently limited, in that (1) it only does
'select' for readability, not writability or exceptions; and (2) it does
not support arbitrary line separators ('$/'): lines must be delimited by
newlines.

%prep
%setup -q -n %{upstream_name}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 655029
- rebuild for updated spec-helper

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 396281
- import perl-IO-BufferedSelect


* Wed Jul 15 2009 cpan2dist 1.0-1mdv
- initial mdv release, generated with cpan2dist
