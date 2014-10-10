%define upstream_name    Text-Context
%define upstream_version 3.7

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A paragraph in context
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(Text::Context::EitherSide)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
Given a piece of text and some search terms, produces an object which
locates the search terms in the message, extracts a reasonable-length
string containing all the search terms, and optionally dumps the string out
as HTML text with the search terms highlighted in bold.

new
    Creates a new snippet object for holding and formatting context for
    search terms.

keywords
    Accessor method to get/set keywords. As the context search is done
    case-insensitively, the keywords will be lower-cased.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 3.700.0-2mdv2011.0
+ Revision: 655231
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 3.700.0-1mdv2011.0
+ Revision: 471154
- import perl-Text-Context


* Sun Nov 29 2009 cpan2dist 3.7-1mdv
- initial mdv release, generated with cpan2dist
