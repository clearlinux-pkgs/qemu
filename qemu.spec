#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0x3353C9CEF108B584 (mdroth@utexas.edu)
#
Name     : qemu
Version  : 9.0.0
Release  : 175
URL      : https://download.qemu.org/qemu-9.0.0.tar.xz
Source0  : https://download.qemu.org/qemu-9.0.0.tar.xz
Source1  : https://download.qemu.org/qemu-9.0.0.tar.xz.sig
Source2  : 3353C9CEF108B584.pkey
Summary  : OPAL firmware
Group    : Development/Tools
License  : Apache-2.0 Artistic-1.0 Artistic-1.0-Perl BSD-2-Clause BSD-2-Clause-Patent BSD-3-Clause CC0-1.0 GPL-1.0 GPL-2.0 GPL-2.0+ GPL-3.0 HPND LGPL-2.1 LGPL-2.1+ LGPL-3.0 MIT
Requires: qemu-bin = %{version}-%{release}
Requires: qemu-data = %{version}-%{release}
Requires: qemu-libexec = %{version}-%{release}
Requires: qemu-license = %{version}-%{release}
Requires: qemu-locales = %{version}-%{release}
Requires: qemu-man = %{version}-%{release}
Requires: qemu-setuid = %{version}-%{release}
BuildRequires : SDL2_image-dev
BuildRequires : attr-dev
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : dtc-dev
BuildRequires : flex
BuildRequires : fuse-dev
BuildRequires : glib-dev
BuildRequires : gnupg
BuildRequires : gtk3-dev
BuildRequires : libaio-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libgcrypt-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libseccomp-dev
BuildRequires : libslirp-dev
BuildRequires : libssh-dev
BuildRequires : libssh2-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : liburing-dev
BuildRequires : m4
BuildRequires : nfs-utils-dev
BuildRequires : ninja
BuildRequires : numactl-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(capstone)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(glusterfs-api)
BuildRequires : pkgconfig(gmp)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gvnc-1.0)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libbpf)
BuildRequires : pkgconfig(libcacard)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libdaxctl)
BuildRequires : pkgconfig(libdw)
BuildRequires : pkgconfig(libiscsi)
BuildRequires : pkgconfig(libkeyutils)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libpmem)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(sysprof-capture-4)
BuildRequires : pkgconfig(virglrenderer)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : pypi(sphinx_rtd_theme)
BuildRequires : pypi-sphinx
BuildRequires : snappy-dev
BuildRequires : spice
BuildRequires : spice-dev
BuildRequires : spice-protocol
BuildRequires : usbredir-dev
BuildRequires : util-linux-dev
BuildRequires : vte-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Allow-unknown-options-in-configure-script.patch

%description
This package provides a daemon to load and run the OpenPower firmware's
Processor Recovery Diagnostics binary. This is responsible for run time
maintenance of OpenPower Systems hardware.

%package bin
Summary: bin components for the qemu package.
Group: Binaries
Requires: qemu-data = %{version}-%{release}
Requires: qemu-libexec = %{version}-%{release}
Requires: qemu-setuid = %{version}-%{release}
Requires: qemu-license = %{version}-%{release}

%description bin
bin components for the qemu package.


%package data
Summary: data components for the qemu package.
Group: Data

%description data
data components for the qemu package.


%package dev
Summary: dev components for the qemu package.
Group: Development
Requires: qemu-bin = %{version}-%{release}
Requires: qemu-data = %{version}-%{release}
Provides: qemu-devel = %{version}-%{release}
Requires: qemu = %{version}-%{release}

%description dev
dev components for the qemu package.


%package doc
Summary: doc components for the qemu package.
Group: Documentation
Requires: qemu-man = %{version}-%{release}

%description doc
doc components for the qemu package.


%package extras
Summary: extras components for the qemu package.
Group: Default

%description extras
extras components for the qemu package.


%package libexec
Summary: libexec components for the qemu package.
Group: Default
Requires: qemu-license = %{version}-%{release}

%description libexec
libexec components for the qemu package.


%package license
Summary: license components for the qemu package.
Group: Default

%description license
license components for the qemu package.


%package locales
Summary: locales components for the qemu package.
Group: Default

%description locales
locales components for the qemu package.


%package man
Summary: man components for the qemu package.
Group: Default

%description man
man components for the qemu package.


%package setuid
Summary: setuid components for the qemu package.
Group: Default

%description setuid
setuid components for the qemu package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 3353C9CEF108B584' gpg.status
%setup -q -n qemu-9.0.0
cd %{_builddir}/qemu-9.0.0
%patch -P 1 -p1
pushd ..
cp -a qemu-9.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1714005849
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-sdl \
--enable-vnc \
--enable-gtk \
--enable-kvm \
--disable-strip \
--target-list='i386-softmmu x86_64-softmmu i386-linux-user x86_64-linux-user' \
--enable-spice \
--disable-rbd \
--extra-cflags="-O3" \
--enable-attr \
--enable-cap-ng \
--enable-virtfs \
--enable-vhost-net \
--enable-usb-redir \
--python=/usr/bin/python \
--enable-seccomp \
--enable-linux-aio \
--audio-drv-list='pa,alsa,oss,sdl' \
--disable-curses \
--enable-lto \
--enable-linux-io-uring
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-sdl \
--enable-vnc \
--enable-gtk \
--enable-kvm \
--disable-strip \
--target-list='i386-softmmu x86_64-softmmu i386-linux-user x86_64-linux-user' \
--enable-spice \
--disable-rbd \
--extra-cflags="-O3" \
--enable-attr \
--enable-cap-ng \
--enable-virtfs \
--enable-vhost-net \
--enable-usb-redir \
--python=/usr/bin/python \
--enable-seccomp \
--enable-linux-aio \
--audio-drv-list='pa,alsa,oss,sdl' \
--disable-curses \
--enable-lto \
--enable-linux-io-uring
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1714005849
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qemu
cp %{_builddir}/qemu-%{version}/COPYING %{buildroot}/usr/share/package-licenses/qemu/2b9d60c2972b476384af9900276837ac81954e80 || :
cp %{_builddir}/qemu-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/qemu/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/qemu-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/qemu/c690b05ff6431c277b59784e95169e0e0528a983 || :
cp %{_builddir}/qemu-%{version}/roms/QemuMacDrivers/COPYING %{buildroot}/usr/share/package-licenses/qemu/2b9d60c2972b476384af9900276837ac81954e80 || :
cp %{_builddir}/qemu-%{version}/roms/SLOF/LICENSE %{buildroot}/usr/share/package-licenses/qemu/e1f0ad62e4850a19b1f56b821f37fccbf84ec191 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/.pytool/Plugin/LicenseCheck/LicenseCheck_plug_in.yaml %{buildroot}/usr/share/package-licenses/qemu/f1a6a8f321d20cb5fbec859a848bff49ad31de69 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/BaseTools/Source/C/BrotliCompress/brotli/LICENSE %{buildroot}/usr/share/package-licenses/qemu/c045813a6c514f2d30d60a07c6aaf3603850e608 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/CryptoPkg/Library/OpensslLib/openssl/LICENSE.txt %{buildroot}/usr/share/package-licenses/qemu/c5c8a68f4b80929b3e66f054f37bb9e16078847f || :
cp %{_builddir}/qemu-%{version}/roms/edk2/CryptoPkg/Library/OpensslLib/openssl/external/perl/Text-Template-1.56/LICENSE %{buildroot}/usr/share/package-licenses/qemu/f12894289cb0f379f24b8d63e2e761dbcba1b216 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/License-History.txt %{buildroot}/usr/share/package-licenses/qemu/1b5c06f43bf6e2039065b681398f6b99a4d552f8 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/License.txt %{buildroot}/usr/share/package-licenses/qemu/7fc5c71d1c403b07043376504d62f2ac73a75313 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/MdeModulePkg/Library/BrotliCustomDecompressLib/brotli/LICENSE %{buildroot}/usr/share/package-licenses/qemu/c045813a6c514f2d30d60a07c6aaf3603850e608 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/OvmfPkg/Bhyve/License.txt %{buildroot}/usr/share/package-licenses/qemu/6b5c7cbcd561ea8f6bba9dd24393f995c1a006e9 || :
cp %{_builddir}/qemu-%{version}/roms/edk2/OvmfPkg/License.txt %{buildroot}/usr/share/package-licenses/qemu/c9c057d4dc70e7a834d80b762663ca01a852ed13 || :
cp %{_builddir}/qemu-%{version}/roms/ipxe/COPYING %{buildroot}/usr/share/package-licenses/qemu/cedc99c80ddc135681756e652d55c72d89ebdfe7 || :
cp %{_builddir}/qemu-%{version}/roms/ipxe/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/qemu/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qemu-%{version}/roms/ipxe/src/include/ipxe/efi/LICENCE %{buildroot}/usr/share/package-licenses/qemu/ca46b2cea92edc93654b11c06c0073ec1a2e50e8 || :
cp %{_builddir}/qemu-%{version}/roms/openbios/COPYING %{buildroot}/usr/share/package-licenses/qemu/8b35225cbdbd6858fb081817cc9dbfe4bef26f5b || :
cp %{_builddir}/qemu-%{version}/roms/openbios/Documentation/kernel/COPYING %{buildroot}/usr/share/package-licenses/qemu/e9b568889ca9075b505c509f7a877a723cc9a4b0 || :
cp %{_builddir}/qemu-%{version}/roms/openbios/utils/devbios/COPYING %{buildroot}/usr/share/package-licenses/qemu/7475b0da13789cd598fe0703f5337d37dd8b0b95 || :
cp %{_builddir}/qemu-%{version}/roms/opensbi/COPYING.BSD %{buildroot}/usr/share/package-licenses/qemu/0a0d7ae8e993794ae9c9ac5219c3d2bbf289471f || :
cp %{_builddir}/qemu-%{version}/roms/opensbi/scripts/Kconfiglib/LICENSE.txt %{buildroot}/usr/share/package-licenses/qemu/864f15fbb4dcd073bbe20eb3c0b839a45b8902ab || :
cp %{_builddir}/qemu-%{version}/roms/qboot/LICENSE %{buildroot}/usr/share/package-licenses/qemu/30a6e0a424471d8ac874b5616dd5a18c45fd6046 || :
cp %{_builddir}/qemu-%{version}/roms/qemu-palcode/COPYING %{buildroot}/usr/share/package-licenses/qemu/2b9d60c2972b476384af9900276837ac81954e80 || :
cp %{_builddir}/qemu-%{version}/roms/seabios-hppa/COPYING %{buildroot}/usr/share/package-licenses/qemu/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qemu-%{version}/roms/seabios-hppa/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9 || :
cp %{_builddir}/qemu-%{version}/roms/seabios/COPYING %{buildroot}/usr/share/package-licenses/qemu/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qemu-%{version}/roms/seabios/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/LICENCE %{buildroot}/usr/share/package-licenses/qemu/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/heap/LICENSE %{buildroot}/usr/share/package-licenses/qemu/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/qemu/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3 || :
cp %{_builddir}/qemu-%{version}/roms/skiboot/libstb/crypto/mbedtls/LICENSE %{buildroot}/usr/share/package-licenses/qemu/4d6c5af1a9cc4eaab3b93353fc166d8e29c150c6 || :
cp %{_builddir}/qemu-%{version}/roms/u-boot-sam460ex/COPYING %{buildroot}/usr/share/package-licenses/qemu/11bb99995c221415712bb5a6d6c0898f02936feb || :
cp %{_builddir}/qemu-%{version}/roms/u-boot-sam460ex/board/ACube/bios_emulator/scitech/src/x86emu/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3f226d574cd9547c3e4d934bb1ac4be3601a9782 || :
cp %{_builddir}/qemu-%{version}/roms/u-boot-sam460ex/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu/2f02ed32418afe8cc25f30f269c63085bafe44f7 || :
cp %{_builddir}/qemu-%{version}/roms/u-boot/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu/2f02ed32418afe8cc25f30f269c63085bafe44f7 || :
cp %{_builddir}/qemu-%{version}/roms/vbootrom/LICENSE %{buildroot}/usr/share/package-licenses/qemu/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qemu-%{version}/subprojects/berkeley-softfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6 || :
cp %{_builddir}/qemu-%{version}/subprojects/berkeley-testfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu/b91b6ebd4f4725457f64e1d35e5a94c2bd35bcec || :
cp %{_builddir}/qemu-%{version}/subprojects/dtc/README.license %{buildroot}/usr/share/package-licenses/qemu/a6759c569917866b44961c88629ae4f3f07ea686 || :
cp %{_builddir}/qemu-%{version}/subprojects/keycodemapdb/LICENSE.BSD %{buildroot}/usr/share/package-licenses/qemu/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8 || :
cp %{_builddir}/qemu-%{version}/subprojects/keycodemapdb/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qemu/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/qemu-%{version}/subprojects/libvfio-user/LICENSE %{buildroot}/usr/share/package-licenses/qemu/36fb901125ffda91bbec1cab3efc5c9f8f2d15a7 || :
cp %{_builddir}/qemu-%{version}/tests/lcitool/libvirt-ci/COPYING %{buildroot}/usr/share/package-licenses/qemu/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qemu-%{version}/tests/uefi-test-tools/LICENSE %{buildroot}/usr/share/package-licenses/qemu/234e74aeab28f7faad2baccf1a3f943b36ab895e || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang qemu
## Remove excluded files
rm -f %{buildroot}*/usr/bin/qemu-ga
rm -f %{buildroot}*/usr/share/qemu/u-boot.e500
rm -f %{buildroot}*/usr/share/man/man7/qemu-ga-ref.7
rm -f %{buildroot}*/usr/share/man/man8/qemu-ga.8
rm -f %{buildroot}*/usr/share/doc/qemu/.buildinfo
rm -f %{buildroot}*/usr/include/fdt.h
rm -f %{buildroot}*/usr/include/libfdt.h
rm -f %{buildroot}*/usr/include/libfdt_env.h
rm -f %{buildroot}*/usr/lib64/pkgconfig/libfdt.pc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name} --skip-path /usr/libexec/qemu-bridge-helper

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/elf2dmp
/V3/usr/bin/qemu-edid
/V3/usr/bin/qemu-i386
/V3/usr/bin/qemu-io
/V3/usr/bin/qemu-keymap
/V3/usr/bin/qemu-nbd
/V3/usr/bin/qemu-pr-helper
/V3/usr/bin/qemu-storage-daemon
/V3/usr/bin/qemu-system-i386
/V3/usr/bin/qemu-system-x86_64
/V3/usr/bin/qemu-x86_64
/usr/bin/elf2dmp
/usr/bin/qemu-edid
/usr/bin/qemu-i386
/usr/bin/qemu-io
/usr/bin/qemu-keymap
/usr/bin/qemu-nbd
/usr/bin/qemu-pr-helper
/usr/bin/qemu-storage-daemon
/usr/bin/qemu-system-i386
/usr/bin/qemu-system-x86_64
/usr/bin/qemu-x86_64

%files data
%defattr(-,root,root,-)
/V3/usr/share/qemu/hppa-firmware.img
/V3/usr/share/qemu/hppa-firmware64.img
/V3/usr/share/qemu/openbios-ppc
/V3/usr/share/qemu/openbios-sparc32
/V3/usr/share/qemu/openbios-sparc64
/V3/usr/share/qemu/palcode-clipper
/V3/usr/share/qemu/s390-ccw.img
/V3/usr/share/qemu/s390-netboot.img
/usr/share/applications/qemu.desktop
/usr/share/icons/hicolor/128x128/apps/qemu.png
/usr/share/icons/hicolor/16x16/apps/qemu.png
/usr/share/icons/hicolor/24x24/apps/qemu.png
/usr/share/icons/hicolor/256x256/apps/qemu.png
/usr/share/icons/hicolor/32x32/apps/qemu.bmp
/usr/share/icons/hicolor/32x32/apps/qemu.png
/usr/share/icons/hicolor/48x48/apps/qemu.png
/usr/share/icons/hicolor/512x512/apps/qemu.png
/usr/share/icons/hicolor/64x64/apps/qemu.png
/usr/share/icons/hicolor/scalable/apps/qemu.svg
/usr/share/qemu/QEMU,cgthree.bin
/usr/share/qemu/QEMU,tcx.bin
/usr/share/qemu/bamboo.dtb
/usr/share/qemu/bios-256k.bin
/usr/share/qemu/bios-microvm.bin
/usr/share/qemu/bios.bin
/usr/share/qemu/canyonlands.dtb
/usr/share/qemu/edk2-aarch64-code.fd
/usr/share/qemu/edk2-arm-code.fd
/usr/share/qemu/edk2-arm-vars.fd
/usr/share/qemu/edk2-i386-code.fd
/usr/share/qemu/edk2-i386-secure-code.fd
/usr/share/qemu/edk2-i386-vars.fd
/usr/share/qemu/edk2-licenses.txt
/usr/share/qemu/edk2-x86_64-code.fd
/usr/share/qemu/edk2-x86_64-secure-code.fd
/usr/share/qemu/efi-e1000.rom
/usr/share/qemu/efi-e1000e.rom
/usr/share/qemu/efi-eepro100.rom
/usr/share/qemu/efi-ne2k_pci.rom
/usr/share/qemu/efi-pcnet.rom
/usr/share/qemu/efi-rtl8139.rom
/usr/share/qemu/efi-virtio.rom
/usr/share/qemu/efi-vmxnet3.rom
/usr/share/qemu/firmware/50-edk2-i386-secure.json
/usr/share/qemu/firmware/50-edk2-x86_64-secure.json
/usr/share/qemu/firmware/60-edk2-aarch64.json
/usr/share/qemu/firmware/60-edk2-arm.json
/usr/share/qemu/firmware/60-edk2-i386.json
/usr/share/qemu/firmware/60-edk2-x86_64.json
/usr/share/qemu/hppa-firmware.img
/usr/share/qemu/hppa-firmware64.img
/usr/share/qemu/keymaps/ar
/usr/share/qemu/keymaps/bepo
/usr/share/qemu/keymaps/cz
/usr/share/qemu/keymaps/da
/usr/share/qemu/keymaps/de
/usr/share/qemu/keymaps/de-ch
/usr/share/qemu/keymaps/en-gb
/usr/share/qemu/keymaps/en-us
/usr/share/qemu/keymaps/es
/usr/share/qemu/keymaps/et
/usr/share/qemu/keymaps/fi
/usr/share/qemu/keymaps/fo
/usr/share/qemu/keymaps/fr
/usr/share/qemu/keymaps/fr-be
/usr/share/qemu/keymaps/fr-ca
/usr/share/qemu/keymaps/fr-ch
/usr/share/qemu/keymaps/hr
/usr/share/qemu/keymaps/hu
/usr/share/qemu/keymaps/is
/usr/share/qemu/keymaps/it
/usr/share/qemu/keymaps/ja
/usr/share/qemu/keymaps/lt
/usr/share/qemu/keymaps/lv
/usr/share/qemu/keymaps/mk
/usr/share/qemu/keymaps/nl
/usr/share/qemu/keymaps/no
/usr/share/qemu/keymaps/pl
/usr/share/qemu/keymaps/pt
/usr/share/qemu/keymaps/pt-br
/usr/share/qemu/keymaps/ru
/usr/share/qemu/keymaps/sl
/usr/share/qemu/keymaps/sv
/usr/share/qemu/keymaps/th
/usr/share/qemu/keymaps/tr
/usr/share/qemu/kvmvapic.bin
/usr/share/qemu/linuxboot.bin
/usr/share/qemu/linuxboot_dma.bin
/usr/share/qemu/multiboot.bin
/usr/share/qemu/multiboot_dma.bin
/usr/share/qemu/npcm7xx_bootrom.bin
/usr/share/qemu/openbios-ppc
/usr/share/qemu/openbios-sparc32
/usr/share/qemu/openbios-sparc64
/usr/share/qemu/opensbi-riscv32-generic-fw_dynamic.bin
/usr/share/qemu/opensbi-riscv64-generic-fw_dynamic.bin
/usr/share/qemu/palcode-clipper
/usr/share/qemu/petalogix-ml605.dtb
/usr/share/qemu/petalogix-s3adsp1800.dtb
/usr/share/qemu/pvh.bin
/usr/share/qemu/pxe-e1000.rom
/usr/share/qemu/pxe-eepro100.rom
/usr/share/qemu/pxe-ne2k_pci.rom
/usr/share/qemu/pxe-pcnet.rom
/usr/share/qemu/pxe-rtl8139.rom
/usr/share/qemu/pxe-virtio.rom
/usr/share/qemu/qboot.rom
/usr/share/qemu/qemu-nsis.bmp
/usr/share/qemu/qemu_vga.ndrv
/usr/share/qemu/s390-ccw.img
/usr/share/qemu/s390-netboot.img
/usr/share/qemu/skiboot.lid
/usr/share/qemu/slof.bin
/usr/share/qemu/trace-events-all
/usr/share/qemu/u-boot-sam460-20100605.bin
/usr/share/qemu/vgabios-ati.bin
/usr/share/qemu/vgabios-bochs-display.bin
/usr/share/qemu/vgabios-cirrus.bin
/usr/share/qemu/vgabios-qxl.bin
/usr/share/qemu/vgabios-ramfb.bin
/usr/share/qemu/vgabios-stdvga.bin
/usr/share/qemu/vgabios-virtio.bin
/usr/share/qemu/vgabios-vmware.bin
/usr/share/qemu/vgabios.bin
/usr/share/qemu/vhost-user/50-qemu-gpu.json
/usr/share/qemu/vof-nvram.bin
/usr/share/qemu/vof.bin

%files dev
%defattr(-,root,root,-)
/usr/include/qemu-plugin.h

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/qemu/*

%files extras
%defattr(-,root,root,-)
/V3/usr/bin/qemu-img
/usr/bin/qemu-img

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/vhost-user-gpu
/V3/usr/libexec/virtfs-proxy-helper
/usr/libexec/vhost-user-gpu
/usr/libexec/virtfs-proxy-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qemu/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/qemu/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/qemu/0a0d7ae8e993794ae9c9ac5219c3d2bbf289471f
/usr/share/package-licenses/qemu/11bb99995c221415712bb5a6d6c0898f02936feb
/usr/share/package-licenses/qemu/1b5c06f43bf6e2039065b681398f6b99a4d552f8
/usr/share/package-licenses/qemu/234e74aeab28f7faad2baccf1a3f943b36ab895e
/usr/share/package-licenses/qemu/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/qemu/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/qemu/2b9d60c2972b476384af9900276837ac81954e80
/usr/share/package-licenses/qemu/2f02ed32418afe8cc25f30f269c63085bafe44f7
/usr/share/package-licenses/qemu/30a6e0a424471d8ac874b5616dd5a18c45fd6046
/usr/share/package-licenses/qemu/36fb901125ffda91bbec1cab3efc5c9f8f2d15a7
/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
/usr/share/package-licenses/qemu/3f226d574cd9547c3e4d934bb1ac4be3601a9782
/usr/share/package-licenses/qemu/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qemu/4d6c5af1a9cc4eaab3b93353fc166d8e29c150c6
/usr/share/package-licenses/qemu/6b5c7cbcd561ea8f6bba9dd24393f995c1a006e9
/usr/share/package-licenses/qemu/7475b0da13789cd598fe0703f5337d37dd8b0b95
/usr/share/package-licenses/qemu/7fc5c71d1c403b07043376504d62f2ac73a75313
/usr/share/package-licenses/qemu/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qemu/864f15fbb4dcd073bbe20eb3c0b839a45b8902ab
/usr/share/package-licenses/qemu/8b35225cbdbd6858fb081817cc9dbfe4bef26f5b
/usr/share/package-licenses/qemu/a6759c569917866b44961c88629ae4f3f07ea686
/usr/share/package-licenses/qemu/b91b6ebd4f4725457f64e1d35e5a94c2bd35bcec
/usr/share/package-licenses/qemu/c045813a6c514f2d30d60a07c6aaf3603850e608
/usr/share/package-licenses/qemu/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6
/usr/share/package-licenses/qemu/c5c8a68f4b80929b3e66f054f37bb9e16078847f
/usr/share/package-licenses/qemu/c690b05ff6431c277b59784e95169e0e0528a983
/usr/share/package-licenses/qemu/c9c057d4dc70e7a834d80b762663ca01a852ed13
/usr/share/package-licenses/qemu/ca46b2cea92edc93654b11c06c0073ec1a2e50e8
/usr/share/package-licenses/qemu/cedc99c80ddc135681756e652d55c72d89ebdfe7
/usr/share/package-licenses/qemu/e1f0ad62e4850a19b1f56b821f37fccbf84ec191
/usr/share/package-licenses/qemu/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
/usr/share/package-licenses/qemu/e9b568889ca9075b505c509f7a877a723cc9a4b0
/usr/share/package-licenses/qemu/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
/usr/share/package-licenses/qemu/f12894289cb0f379f24b8d63e2e761dbcba1b216
/usr/share/package-licenses/qemu/f1a6a8f321d20cb5fbec859a848bff49ad31de69

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/qemu-img.1
/usr/share/man/man1/qemu-storage-daemon.1
/usr/share/man/man1/qemu.1
/usr/share/man/man1/virtfs-proxy-helper.1
/usr/share/man/man7/qemu-block-drivers.7
/usr/share/man/man7/qemu-cpu-models.7
/usr/share/man/man7/qemu-qmp-ref.7
/usr/share/man/man7/qemu-storage-daemon-qmp-ref.7
/usr/share/man/man8/qemu-nbd.8
/usr/share/man/man8/qemu-pr-helper.8

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/libexec/qemu-bridge-helper

%files locales -f qemu.lang
%defattr(-,root,root,-)

