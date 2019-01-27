Name:           {{{ git_dir_name }}}
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        A cmdline tool to edit and retrieve information from /etc/kdump.conf
Group:          Applications/System
License:        GPL2+
URL:            https://github.com/kenneth-dsouza/kdump-config.git
VCS:            {{{ git_dir_vcs }}}
BuildRequires:  python3
Requires:       python3
Requires:       kexec-tools
Requires:       util-linux
Requires:       coreutils
BuildArch:      noarch

Source:         {{{ git_dir_pack }}}

%description
A cmdline tool to edit and retrieve information from /etc/kdump.conf
This tool will avoid typos and have basic sanity check for options.

%prep
{{{ git_dir_setup_macro }}}

# Change shebang in individual files
sed -i '1s=^#!\s*/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' kdump-config

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions

install -p -m 755 kdump-config %{buildroot}/%{_bindir}
install -p -m 644 kdump-config.1 %{buildroot}/%{_mandir}/man1
install -p -m 644 bash-completion/kdump-config %{buildroot}/%{_datadir}/bash-completion/completions

%files
%doc README
%license COPYING
%{_bindir}/kdump-config
%{_mandir}/man1/kdump-config.1*
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/kdump-config

%changelog
* Sun Nov 4  2018 Kenneth D'souza <kdsouza@redhat.com> - 0.1-1
- Release kdump-config package
~
