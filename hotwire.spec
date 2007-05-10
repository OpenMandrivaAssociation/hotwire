%define name	hotwire
%define	version	0.333
%define	release	%mkrel 1

Name:		%{name}
Summary:	Hybrid text/graphical shell for developers and sysadmins
Version:	%{version} 
Release:	%{release} 
Source0:	http://www.verbum.org-a.googlepages.com/%{name}-%{version}.tar.bz2
URL:		http://www.verbum.org-a.googlepages.com/hotwire
Group:		Terminals
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	desktop-file-utils
# Due to a bug in the software, remove dependency when the bug is fixed: http://groups.google.com/group/hotwire-shell/browse_thread/thread/cde063a55d3fff50
Requires:	python-setuptools
Requires:	python-vte

%description
Hotwire is a shell replacement for gnome-terminal/xterm + sh + ssh for 
developers and system administrators. Hotwire is somewhat like Windows 
PowerShell, but graphical, and also a little like MacOS X Automator, 
but text based.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%py_puresitedir
mkdir -p %{buildroot}%{_datadir}/applications
PYTHONPATH=$PYTHONPATH:%{buildroot}%py_puresitedir python setup.py install --single-version-externally-managed --root=$RPM_BUILD_ROOT

# Install the .desktop file, since the crappy build system can't do it.

install -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Shells" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
$RPM_BUILD_ROOT%{_datadir}/applications/*

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{py_puresitedir}/%{name}
%{py_puresitedir}/%{name}_ui
%{py_puresitedir}/%{name}-%{version}-py%pyver.egg-info
