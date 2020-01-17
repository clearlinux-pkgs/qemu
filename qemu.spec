#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3353C9CEF108B584 (mdroth@utexas.edu)
#
Name     : qemu
Version  : 4.2.0
Release  : 112
URL      : https://download.qemu.org/qemu-4.2.0.tar.xz
Source0  : https://download.qemu.org/qemu-4.2.0.tar.xz
Source1  : https://download.qemu.org/qemu-4.2.0.tar.xz.sig
Summary  : A lightweight multi-platform, multi-architecture disassembly framework
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-2-Clause-Patent BSD-3-Clause BSD-4-Clause CC0-1.0 GPL-2.0 GPL-2.0+ GPL-3.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0 MIT NCSA OpenSSL
Requires: qemu-bin = %{version}-%{release}
Requires: qemu-data = %{version}-%{release}
Requires: qemu-license = %{version}-%{release}
Requires: qemu-locales = %{version}-%{release}
Requires: qemu-setuid = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : attr-dev
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : buildreq-mvn
BuildRequires : buildreq-qmake
BuildRequires : ceph-dev
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : gtk3-dev
BuildRequires : libaio-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libseccomp-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : numactl-dev
BuildRequires : pkgconfig(libcacard)
BuildRequires : snappy-dev
BuildRequires : spice
BuildRequires : spice-dev
BuildRequires : spice-protocol
BuildRequires : usbredir-dev
BuildRequires : util-linux-dev
BuildRequires : zlib-dev
Patch1: 0001-Allow-unknown-options-in-configure-script.patch
Patch2: 0002-Set-default-number-of-sockets-to-1.patch
Patch3: 0003-Use-run-lock.patch

%description
Capstone is a disassembly framework with the target of becoming the ultimate
disasm engine for binary analysis and reversing in the security community.

%package bin
Summary: bin components for the qemu package.
Group: Binaries
Requires: qemu-data = %{version}-%{release}
Requires: qemu-setuid = %{version}-%{release}
Requires: qemu-license = %{version}-%{release}

%description bin
bin components for the qemu package.


%package data
Summary: data components for the qemu package.
Group: Data

%description data
data components for the qemu package.


%package extras
Summary: extras components for the qemu package.
Group: Default

%description extras
extras components for the qemu package.


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


%package setuid
Summary: setuid components for the qemu package.
Group: Default

%description setuid
setuid components for the qemu package.


%prep
%setup -q -n qemu-4.2.0
cd %{_builddir}/qemu-4.2.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579300399
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-sdl \
--enable-vnc \
--enable-gtk \
--enable-kvm \
--disable-strip \
--target-list='i386-softmmu x86_64-softmmu i386-linux-user x86_64-linux-user' \
--enable-spice \
--enable-rbd \
--extra-cflags="-O3" \
--enable-attr \
--enable-cap-ng \
--enable-virtfs \
--enable-vhost-net \
--enable-usb-redir \
--python=/usr/bin/python \
--enable-seccomp \
--enable-linux-aio
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1579300399
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qemu
cp %{_builddir}/qemu-4.2.0/COPYING %{buildroot}/usr/share/package-licenses/qemu/2b9d60c2972b476384af9900276837ac81954e80
cp %{_builddir}/qemu-4.2.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/qemu/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/qemu-4.2.0/LICENSE %{buildroot}/usr/share/package-licenses/qemu/c690b05ff6431c277b59784e95169e0e0528a983
cp %{_builddir}/qemu-4.2.0/capstone/LICENSE.TXT %{buildroot}/usr/share/package-licenses/qemu/861af24907e399e873920dbbff1ea1dd73a9ba35
cp %{_builddir}/qemu-4.2.0/capstone/LICENSE_LLVM.TXT %{buildroot}/usr/share/package-licenses/qemu/afc034c0ae47cbd47a99c6c5992d846511bb33ad
cp %{_builddir}/qemu-4.2.0/capstone/bindings/python/LICENSE.TXT %{buildroot}/usr/share/package-licenses/qemu/861af24907e399e873920dbbff1ea1dd73a9ba35
cp %{_builddir}/qemu-4.2.0/disas/libvixl/LICENCE %{buildroot}/usr/share/package-licenses/qemu/25383eb1c76eae5993e92a1cf2b75d58e599bbf5
cp %{_builddir}/qemu-4.2.0/dtc/README.license %{buildroot}/usr/share/package-licenses/qemu/e6060b19e275bde4187546231ba289a486d987e9
cp %{_builddir}/qemu-4.2.0/linux-headers/COPYING %{buildroot}/usr/share/package-licenses/qemu/64ad6386bae45ebd6788e404758a247e26e5c778
cp %{_builddir}/qemu-4.2.0/roms/QemuMacDrivers/COPYING %{buildroot}/usr/share/package-licenses/qemu/2b9d60c2972b476384af9900276837ac81954e80
cp %{_builddir}/qemu-4.2.0/roms/SLOF/LICENSE %{buildroot}/usr/share/package-licenses/qemu/e1f0ad62e4850a19b1f56b821f37fccbf84ec191
cp %{_builddir}/qemu-4.2.0/roms/edk2/ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6
cp %{_builddir}/qemu-4.2.0/roms/edk2/BaseTools/Source/C/BrotliCompress/LICENSE %{buildroot}/usr/share/package-licenses/qemu/4763ba7dfa7730d98b190dd8a4a2c6818d301fcb
cp %{_builddir}/qemu-4.2.0/roms/edk2/CryptoPkg/Library/OpensslLib/openssl/LICENSE %{buildroot}/usr/share/package-licenses/qemu/607e96d7bc75d9f884a8e210d276cca4006e0753
cp %{_builddir}/qemu-4.2.0/roms/edk2/CryptoPkg/Library/OpensslLib/openssl/external/perl/Text-Template-1.46/COPYING %{buildroot}/usr/share/package-licenses/qemu/ab8577d3eb0eedf3f98004e381a9cee30e7224e1
cp %{_builddir}/qemu-4.2.0/roms/edk2/License-History.txt %{buildroot}/usr/share/package-licenses/qemu/1b5c06f43bf6e2039065b681398f6b99a4d552f8
cp %{_builddir}/qemu-4.2.0/roms/edk2/License.txt %{buildroot}/usr/share/package-licenses/qemu/7fc5c71d1c403b07043376504d62f2ac73a75313
cp %{_builddir}/qemu-4.2.0/roms/edk2/MdeModulePkg/Library/BrotliCustomDecompressLib/LICENSE %{buildroot}/usr/share/package-licenses/qemu/4763ba7dfa7730d98b190dd8a4a2c6818d301fcb
cp %{_builddir}/qemu-4.2.0/roms/edk2/MdeModulePkg/Universal/RegularExpressionDxe/Oniguruma/COPYING %{buildroot}/usr/share/package-licenses/qemu/e9d39a1c2bd8459631ec9ec42761fe847ae93f3f
cp %{_builddir}/qemu-4.2.0/roms/edk2/OvmfPkg/License.txt %{buildroot}/usr/share/package-licenses/qemu/c9c057d4dc70e7a834d80b762663ca01a852ed13
cp %{_builddir}/qemu-4.2.0/roms/ipxe/COPYING %{buildroot}/usr/share/package-licenses/qemu/cedc99c80ddc135681756e652d55c72d89ebdfe7
cp %{_builddir}/qemu-4.2.0/roms/ipxe/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/qemu/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qemu-4.2.0/roms/ipxe/src/include/ipxe/efi/LICENCE %{buildroot}/usr/share/package-licenses/qemu/ca46b2cea92edc93654b11c06c0073ec1a2e50e8
cp %{_builddir}/qemu-4.2.0/roms/openbios/COPYING %{buildroot}/usr/share/package-licenses/qemu/8b35225cbdbd6858fb081817cc9dbfe4bef26f5b
cp %{_builddir}/qemu-4.2.0/roms/openbios/Documentation/kernel/COPYING %{buildroot}/usr/share/package-licenses/qemu/e9b568889ca9075b505c509f7a877a723cc9a4b0
cp %{_builddir}/qemu-4.2.0/roms/openbios/utils/devbios/COPYING %{buildroot}/usr/share/package-licenses/qemu/7475b0da13789cd598fe0703f5337d37dd8b0b95
cp %{_builddir}/qemu-4.2.0/roms/openhackware/COPYING %{buildroot}/usr/share/package-licenses/qemu/17e3b0eea99abffe6ac71e65627413236e0b117a
cp %{_builddir}/qemu-4.2.0/roms/opensbi/COPYING.BSD %{buildroot}/usr/share/package-licenses/qemu/0a0d7ae8e993794ae9c9ac5219c3d2bbf289471f
cp %{_builddir}/qemu-4.2.0/roms/qboot/LICENSE %{buildroot}/usr/share/package-licenses/qemu/30a6e0a424471d8ac874b5616dd5a18c45fd6046
cp %{_builddir}/qemu-4.2.0/roms/qemu-palcode/COPYING %{buildroot}/usr/share/package-licenses/qemu/2b9d60c2972b476384af9900276837ac81954e80
cp %{_builddir}/qemu-4.2.0/roms/seabios-hppa/COPYING %{buildroot}/usr/share/package-licenses/qemu/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qemu-4.2.0/roms/seabios-hppa/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/qemu-4.2.0/roms/seabios/COPYING %{buildroot}/usr/share/package-licenses/qemu/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qemu-4.2.0/roms/seabios/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/qemu-4.2.0/roms/sgabios/COPYING %{buildroot}/usr/share/package-licenses/qemu/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/qemu-4.2.0/roms/skiboot/LICENCE %{buildroot}/usr/share/package-licenses/qemu/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/qemu-4.2.0/roms/skiboot/ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-4.2.0/roms/skiboot/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-4.2.0/roms/skiboot/ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-4.2.0/roms/skiboot/ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-4.2.0/roms/skiboot/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-4.2.0/roms/skiboot/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/qemu/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
cp %{_builddir}/qemu-4.2.0/roms/skiboot/ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-4.2.0/roms/skiboot/ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/qemu-4.2.0/roms/u-boot-sam460ex/COPYING %{buildroot}/usr/share/package-licenses/qemu/11bb99995c221415712bb5a6d6c0898f02936feb
cp %{_builddir}/qemu-4.2.0/roms/u-boot-sam460ex/board/ACube/bios_emulator/scitech/src/x86emu/LICENSE %{buildroot}/usr/share/package-licenses/qemu/3f226d574cd9547c3e4d934bb1ac4be3601a9782
cp %{_builddir}/qemu-4.2.0/roms/u-boot-sam460ex/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu/2f02ed32418afe8cc25f30f269c63085bafe44f7
cp %{_builddir}/qemu-4.2.0/roms/u-boot/cmd/license.c %{buildroot}/usr/share/package-licenses/qemu/33e557c1f30d0d1f1f585cb49686b8c13e47ba83
cp %{_builddir}/qemu-4.2.0/roms/u-boot/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu/2f02ed32418afe8cc25f30f269c63085bafe44f7
cp %{_builddir}/qemu-4.2.0/slirp/COPYRIGHT %{buildroot}/usr/share/package-licenses/qemu/051935530e6be28baed83b2aafe66ee5b347d656
cp %{_builddir}/qemu-4.2.0/tests/fp/berkeley-softfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6
cp %{_builddir}/qemu-4.2.0/tests/fp/berkeley-testfloat-3/COPYING.txt %{buildroot}/usr/share/package-licenses/qemu/b91b6ebd4f4725457f64e1d35e5a94c2bd35bcec
cp %{_builddir}/qemu-4.2.0/tests/uefi-test-tools/LICENSE %{buildroot}/usr/share/package-licenses/qemu/234e74aeab28f7faad2baccf1a3f943b36ab895e
cp %{_builddir}/qemu-4.2.0/ui/keycodemapdb/LICENSE.BSD %{buildroot}/usr/share/package-licenses/qemu/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
cp %{_builddir}/qemu-4.2.0/ui/keycodemapdb/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qemu/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
%make_install
%find_lang qemu
## Remove excluded files
rm -f %{buildroot}/usr/bin/qemu-ga
rm -f %{buildroot}/usr/share/qemu/u-boot.e500

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ivshmem-client
/usr/bin/ivshmem-server
/usr/bin/qemu-edid
/usr/bin/qemu-i386
/usr/bin/qemu-io
/usr/bin/qemu-keymap
/usr/bin/qemu-nbd
/usr/bin/qemu-pr-helper
/usr/bin/qemu-system-i386
/usr/bin/qemu-system-x86_64
/usr/bin/qemu-x86_64
/usr/bin/virtfs-proxy-helper

%files data
%defattr(-,root,root,-)
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
/usr/share/qemu/openbios-ppc
/usr/share/qemu/openbios-sparc32
/usr/share/qemu/openbios-sparc64
/usr/share/qemu/opensbi-riscv32-virt-fw_jump.bin
/usr/share/qemu/opensbi-riscv64-sifive_u-fw_jump.bin
/usr/share/qemu/opensbi-riscv64-virt-fw_jump.bin
/usr/share/qemu/palcode-clipper
/usr/share/qemu/petalogix-ml605.dtb
/usr/share/qemu/petalogix-s3adsp1800.dtb
/usr/share/qemu/ppc_rom.bin
/usr/share/qemu/pvh.bin
/usr/share/qemu/pxe-e1000.rom
/usr/share/qemu/pxe-eepro100.rom
/usr/share/qemu/pxe-ne2k_pci.rom
/usr/share/qemu/pxe-pcnet.rom
/usr/share/qemu/pxe-rtl8139.rom
/usr/share/qemu/pxe-virtio.rom
/usr/share/qemu/qemu-nsis.bmp
/usr/share/qemu/qemu_vga.ndrv
/usr/share/qemu/s390-ccw.img
/usr/share/qemu/s390-netboot.img
/usr/share/qemu/sgabios.bin
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

%files extras
%defattr(-,root,root,-)
/usr/bin/qemu-img

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qemu/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/qemu/051935530e6be28baed83b2aafe66ee5b347d656
/usr/share/package-licenses/qemu/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/qemu/0a0d7ae8e993794ae9c9ac5219c3d2bbf289471f
/usr/share/package-licenses/qemu/11bb99995c221415712bb5a6d6c0898f02936feb
/usr/share/package-licenses/qemu/17e3b0eea99abffe6ac71e65627413236e0b117a
/usr/share/package-licenses/qemu/1b5c06f43bf6e2039065b681398f6b99a4d552f8
/usr/share/package-licenses/qemu/234e74aeab28f7faad2baccf1a3f943b36ab895e
/usr/share/package-licenses/qemu/25383eb1c76eae5993e92a1cf2b75d58e599bbf5
/usr/share/package-licenses/qemu/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/qemu/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/qemu/2b9d60c2972b476384af9900276837ac81954e80
/usr/share/package-licenses/qemu/2f02ed32418afe8cc25f30f269c63085bafe44f7
/usr/share/package-licenses/qemu/30a6e0a424471d8ac874b5616dd5a18c45fd6046
/usr/share/package-licenses/qemu/33e557c1f30d0d1f1f585cb49686b8c13e47ba83
/usr/share/package-licenses/qemu/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
/usr/share/package-licenses/qemu/3f226d574cd9547c3e4d934bb1ac4be3601a9782
/usr/share/package-licenses/qemu/4763ba7dfa7730d98b190dd8a4a2c6818d301fcb
/usr/share/package-licenses/qemu/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qemu/607e96d7bc75d9f884a8e210d276cca4006e0753
/usr/share/package-licenses/qemu/64ad6386bae45ebd6788e404758a247e26e5c778
/usr/share/package-licenses/qemu/7475b0da13789cd598fe0703f5337d37dd8b0b95
/usr/share/package-licenses/qemu/7fc5c71d1c403b07043376504d62f2ac73a75313
/usr/share/package-licenses/qemu/861af24907e399e873920dbbff1ea1dd73a9ba35
/usr/share/package-licenses/qemu/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qemu/8b35225cbdbd6858fb081817cc9dbfe4bef26f5b
/usr/share/package-licenses/qemu/ab8577d3eb0eedf3f98004e381a9cee30e7224e1
/usr/share/package-licenses/qemu/afc034c0ae47cbd47a99c6c5992d846511bb33ad
/usr/share/package-licenses/qemu/b91b6ebd4f4725457f64e1d35e5a94c2bd35bcec
/usr/share/package-licenses/qemu/c4cd5ba6f665cf9ecb44e0620c2c76140566cfc6
/usr/share/package-licenses/qemu/c690b05ff6431c277b59784e95169e0e0528a983
/usr/share/package-licenses/qemu/c9c057d4dc70e7a834d80b762663ca01a852ed13
/usr/share/package-licenses/qemu/ca46b2cea92edc93654b11c06c0073ec1a2e50e8
/usr/share/package-licenses/qemu/cedc99c80ddc135681756e652d55c72d89ebdfe7
/usr/share/package-licenses/qemu/e1f0ad62e4850a19b1f56b821f37fccbf84ec191
/usr/share/package-licenses/qemu/e6060b19e275bde4187546231ba289a486d987e9
/usr/share/package-licenses/qemu/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
/usr/share/package-licenses/qemu/e9b568889ca9075b505c509f7a877a723cc9a4b0
/usr/share/package-licenses/qemu/e9d39a1c2bd8459631ec9ec42761fe847ae93f3f
/usr/share/package-licenses/qemu/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/libexec/qemu-bridge-helper

%files locales -f qemu.lang
%defattr(-,root,root,-)

