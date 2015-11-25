#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libreswan
Version  : 3.15
Release  : 4
URL      : https://download.libreswan.org/libreswan-3.15.tar.gz
Source0  : https://download.libreswan.org/libreswan-3.15.tar.gz
Summary  : Libreswan IPSEC implementation
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 OpenSSL
Requires: libreswan-bin
Requires: libreswan-doc
Requires: libreswan-config
BuildRequires : Linux-PAM-dev
BuildRequires : bison
BuildRequires : curl-dev
BuildRequires : docbook-xml
BuildRequires : flex
BuildRequires : gmp-dev
BuildRequires : libcap-ng-dev
BuildRequires : libevent-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : unbound-dev
BuildRequires : util-linux
BuildRequires : xmlto

%description
Libreswan is a free implementation of IPSEC & IKE for Linux.  IPSEC is
the Internet Protocol Security and uses strong cryptography to provide
both authentication and encryption services.  These services allow you
to build secure tunnels through untrusted networks.  Everything passing
through the untrusted net is encrypted by the ipsec gateway machine and
decrypted by the gateway at the other end of the tunnel.  The resulting
tunnel is a virtual private network or VPN.

This package contains the daemons and userland tools for setting up
Libreswan on a freeswan enabled kernel. It optionally also builds the
Libreswan KLIPS IPsec stack that is an alternative for the NETKEY/XFRM
IPsec stack that exists in the default Linux kernel.

%package bin
Summary: bin components for the libreswan package.
Group: Binaries
Requires: libreswan-config

%description bin
bin components for the libreswan package.


%package config
Summary: config components for the libreswan package.
Group: Default

%description config
config components for the libreswan package.


%package doc
Summary: doc components for the libreswan package.
Group: Documentation

%description doc
doc components for the libreswan package.


%prep
%setup -q -n libreswan-3.15

%build
make V=1  %{?_smp_mflags} INC_USRLOCAL=/usr INC_MANDIR=share/man

%install
rm -rf %{buildroot}
%make_install INC_USRLOCAL=/usr INC_MANDIR=share/man

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipsec
/usr/libexec/ipsec/_import_crl
/usr/libexec/ipsec/_keycensor
/usr/libexec/ipsec/_pluto_adns
/usr/libexec/ipsec/_plutorun
/usr/libexec/ipsec/_secretcensor
/usr/libexec/ipsec/_stackmanager
/usr/libexec/ipsec/_updown
/usr/libexec/ipsec/_updown.klips
/usr/libexec/ipsec/_updown.netkey
/usr/libexec/ipsec/addconn
/usr/libexec/ipsec/auto
/usr/libexec/ipsec/barf
/usr/libexec/ipsec/eroute
/usr/libexec/ipsec/ikeping
/usr/libexec/ipsec/klipsdebug
/usr/libexec/ipsec/look
/usr/libexec/ipsec/newhostkey
/usr/libexec/ipsec/pf_key
/usr/libexec/ipsec/pluto
/usr/libexec/ipsec/readwriteconf
/usr/libexec/ipsec/rsasigkey
/usr/libexec/ipsec/secrets
/usr/libexec/ipsec/setup
/usr/libexec/ipsec/showhostkey
/usr/libexec/ipsec/spi
/usr/libexec/ipsec/spigrp
/usr/libexec/ipsec/tncfg
/usr/libexec/ipsec/verify
/usr/libexec/ipsec/whack

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ipsec.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libreswan/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
