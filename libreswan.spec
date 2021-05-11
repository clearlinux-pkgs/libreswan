#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libreswan
Version  : 4.4
Release  : 22
URL      : https://github.com/libreswan/libreswan/archive/v4.4/libreswan-4.4.tar.gz
Source0  : https://github.com/libreswan/libreswan/archive/v4.4/libreswan-4.4.tar.gz
Summary  : Libreswan IPSEC implementation
Group    : Development/Tools
License  : BSD-3-Clause BSD-4-Clause GPL-2.0 LGPL-2.0 MPL-2.0 OpenSSL
Requires: libreswan-bin = %{version}-%{release}
Requires: libreswan-config = %{version}-%{release}
Requires: libreswan-libexec = %{version}-%{release}
Requires: libreswan-license = %{version}-%{release}
Requires: libreswan-man = %{version}-%{release}
Requires: libreswan-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : flex
BuildRequires : libcap-ng-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : nspr-dev
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libevent)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(nss)
BuildRequires : xmlto
Patch1: 0001-Set-default-options-since-passing-them-later-doesn-t.patch
Patch2: 0002-Create-missing-var-lib-ipsec-nss-directory.patch

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
Requires: libreswan-libexec = %{version}-%{release}
Requires: libreswan-config = %{version}-%{release}
Requires: libreswan-license = %{version}-%{release}
Requires: libreswan-services = %{version}-%{release}

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
Requires: libreswan-man = %{version}-%{release}

%description doc
doc components for the libreswan package.


%package libexec
Summary: libexec components for the libreswan package.
Group: Default
Requires: libreswan-config = %{version}-%{release}
Requires: libreswan-license = %{version}-%{release}

%description libexec
libexec components for the libreswan package.


%package license
Summary: license components for the libreswan package.
Group: Default

%description license
license components for the libreswan package.


%package man
Summary: man components for the libreswan package.
Group: Default

%description man
man components for the libreswan package.


%package services
Summary: services components for the libreswan package.
Group: Systemd services

%description services
services components for the libreswan package.


%prep
%setup -q -n libreswan-4.4
cd %{_builddir}/libreswan-4.4
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620758662
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
## make_prepend content
CFLAGS="$CFLAGS -DNSS_PKCS11_2_0_COMPAT=1"
## make_prepend end
make  %{?_smp_mflags}  programs


%install
export SOURCE_DATE_EPOCH=1620758662
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libreswan
cp %{_builddir}/libreswan-4.4/COPYING %{buildroot}/usr/share/package-licenses/libreswan/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/libreswan-4.4/LICENSE %{buildroot}/usr/share/package-licenses/libreswan/1877c44246850c068da2ffbba94330c9463f6552
cp %{_builddir}/libreswan-4.4/lib/COPYING.LIB %{buildroot}/usr/share/package-licenses/libreswan/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/libreswan-4.4/testing/programs/getpeercon_server/LICENSE %{buildroot}/usr/share/package-licenses/libreswan/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install PREFIX=/usr DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipsec

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/libreswan.conf

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libreswan/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/ipsec/_import_crl
/usr/libexec/ipsec/_plutorun
/usr/libexec/ipsec/_secretcensor
/usr/libexec/ipsec/_stackmanager
/usr/libexec/ipsec/_unbound-hook
/usr/libexec/ipsec/_updown
/usr/libexec/ipsec/_updown.xfrm
/usr/libexec/ipsec/addconn
/usr/libexec/ipsec/algparse
/usr/libexec/ipsec/auto
/usr/libexec/ipsec/barf
/usr/libexec/ipsec/cavp
/usr/libexec/ipsec/dncheck
/usr/libexec/ipsec/ecdsasigkey
/usr/libexec/ipsec/enumcheck
/usr/libexec/ipsec/hunkcheck
/usr/libexec/ipsec/ipcheck
/usr/libexec/ipsec/jambufcheck
/usr/libexec/ipsec/keyidcheck
/usr/libexec/ipsec/letsencrypt
/usr/libexec/ipsec/look
/usr/libexec/ipsec/newhostkey
/usr/libexec/ipsec/pluto
/usr/libexec/ipsec/readwriteconf
/usr/libexec/ipsec/rsasigkey
/usr/libexec/ipsec/setup
/usr/libexec/ipsec/show
/usr/libexec/ipsec/showhostkey
/usr/libexec/ipsec/timecheck
/usr/libexec/ipsec/verify
/usr/libexec/ipsec/whack

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libreswan/1877c44246850c068da2ffbba94330c9463f6552
/usr/share/package-licenses/libreswan/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libreswan/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/ipsec.conf.5
/usr/share/man/man5/ipsec.secrets.5
/usr/share/man/man8/ipsec.8
/usr/share/man/man8/ipsec__import_crl.8
/usr/share/man/man8/ipsec__plutorun.8
/usr/share/man/man8/ipsec__secretcensor.8
/usr/share/man/man8/ipsec__stackmanager.8
/usr/share/man/man8/ipsec__unbound-hook.8
/usr/share/man/man8/ipsec__updown.8
/usr/share/man/man8/ipsec__updown.xfrm.8
/usr/share/man/man8/ipsec_addconn.8
/usr/share/man/man8/ipsec_auto.8
/usr/share/man/man8/ipsec_barf.8
/usr/share/man/man8/ipsec_checknss.8
/usr/share/man/man8/ipsec_ecdsasigkey.8
/usr/share/man/man8/ipsec_import.8
/usr/share/man/man8/ipsec_initnss.8
/usr/share/man/man8/ipsec_letsencrypt.8
/usr/share/man/man8/ipsec_look.8
/usr/share/man/man8/ipsec_newhostkey.8
/usr/share/man/man8/ipsec_pluto.8
/usr/share/man/man8/ipsec_readwriteconf.8
/usr/share/man/man8/ipsec_rsasigkey.8
/usr/share/man/man8/ipsec_setup.8
/usr/share/man/man8/ipsec_show.8
/usr/share/man/man8/ipsec_showhostkey.8
/usr/share/man/man8/ipsec_verify.8
/usr/share/man/man8/ipsec_whack.8
/usr/share/man/man8/pluto.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ipsec.service
