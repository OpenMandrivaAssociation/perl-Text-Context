%define upstream_name    Text-Context
%define upstream_version 3.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A paragraph in context
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTML::Entities)
BuildRequires: perl(Text::Context::EitherSide)
BuildRequires: perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


