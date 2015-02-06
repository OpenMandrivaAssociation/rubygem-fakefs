%define oname fakefs

Summary:    A fake filesystem. Use it in your tests
Name:       rubygem-%{oname}
Version:    0.2.1
Release:    2
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/defunkt/fakefs
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A fake filesystem. Use it in your tests.

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
rm %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/test
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CONTRIBUTORS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.markdown
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 584332
- import rubygem-fakefs

