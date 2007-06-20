%define name	hotwire
%define	version	0.567
%define	release	%mkrel 1

Name:		%{name}
Summary:	Hybrid text/graphical shell for developers and sysadmins
Version:	%{version} 
Release:	%{release} 
Epoch:		1
Source0:	http://hotwire-shell.org/download/%{name}-%{version}.zip
URL:		http://hotwire-shell.org
Group:		Terminals
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	desktop-file-utils
Requires:	python-vte dbus-python gnome-python-gnomevfs

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
PYTHONPATH=$PYTHONPATH:%{buildroot}%py_puresitedir python setup.py install --root=$RPM_BUILD_ROOT

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Shells" \
  --remove-category="Applications" \
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
