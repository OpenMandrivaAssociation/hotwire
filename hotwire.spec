%define name	hotwire
%define	version	0.721
%define	release	%mkrel 2

Name:		%{name}
Summary:	Hybrid text/graphical shell for developers and sysadmins
Version:	%{version} 
Release:	%{release} 
Epoch:		1
Source0:	http://hotwire-shell.googlecode.com/files/%{name}-%{version}.zip
URL:		http://hotwire-shell.org
Group:		Terminals
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	intltool
Requires:	python-vte 
Requires:	dbus-python 
Requires:	gnome-python-gnomevfs

%description
Hotwire is a shell replacement for gnome-terminal/xterm + sh + ssh for 
developers and system administrators. Hotwire is somewhat like Windows 
PowerShell, but graphical, and also a little like MacOS X Automator, 
but text based.

%prep
%setup -q

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/24x24/apps/*
%{py_puresitedir}/%{name}
%{py_puresitedir}/hotapps
%{py_puresitedir}/hotvte
%{py_puresitedir}/%{name}_ui
%{py_puresitedir}/%{name}-%{version}-py%pyver.egg-info
