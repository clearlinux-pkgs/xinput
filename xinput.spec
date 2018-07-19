#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xinput
Version  : 1.6.2
Release  : 1
URL      : https://www.x.org/releases/individual/app/xinput-1.6.2.tar.bz2
Source0  : https://www.x.org/releases/individual/app/xinput-1.6.2.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xinput-bin
Requires: xinput-license
Requires: xinput-man
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xrandr)

%description
xinput
======
Overview
========
xinput is a utility to configure and test XInput devices. It wasn't
originally designed to be the primary tool for doing this but it's
still pretty much the only program out there for doing it. :-)

%package bin
Summary: bin components for the xinput package.
Group: Binaries
Requires: xinput-license
Requires: xinput-man

%description bin
bin components for the xinput package.


%package license
Summary: license components for the xinput package.
Group: Default

%description license
license components for the xinput package.


%package man
Summary: man components for the xinput package.
Group: Default

%description man
man components for the xinput package.


%prep
%setup -q -n xinput-1.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531977182
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1531977182
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xinput
cp COPYING %{buildroot}/usr/share/doc/xinput/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xinput

%files license
%defattr(-,root,root,-)
/usr/share/doc/xinput/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/xinput.1
