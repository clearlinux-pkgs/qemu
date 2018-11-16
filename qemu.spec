#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3353C9CEF108B584 (mdroth@utexas.edu)
#
Name     : qemu
Version  : 2.12.1
Release  : 91
URL      : http://wiki.qemu-project.org/download/qemu-2.12.1.tar.xz
Source0  : http://wiki.qemu-project.org/download/qemu-2.12.1.tar.xz
Source99 : http://wiki.qemu-project.org/download/qemu-2.12.1.tar.xz.sig
Summary  : A lightweight multi-platform, multi-architecture disassembly framework
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-2.0+ GPL-3.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0 MIT NCSA Python-2.0
Requires: qemu-bin = %{version}-%{release}
Requires: qemu-data = %{version}-%{release}
Requires: qemu-libexec = %{version}-%{release}
Requires: qemu-license = %{version}-%{release}
Requires: qemu-locales = %{version}-%{release}
Requires: qemu-setuid = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
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
BuildRequires : snappy-dev
BuildRequires : spice
BuildRequires : spice-dev
BuildRequires : spice-protocol
BuildRequires : usbredir-dev
BuildRequires : util-linux-dev
BuildRequires : zlib-dev
Patch1: configure.patch
Patch2: cores-default.patch
Patch3: 0001-Use-run-lock.patch

%description
Capstone is a disassembly framework with the target of becoming the ultimate
disasm engine for binary analysis and reversing in the security community.

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


%package setuid
Summary: setuid components for the qemu package.
Group: Default

%description setuid
setuid components for the qemu package.


%prep
%setup -q -n qemu-2.12.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539624016
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
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
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1539624016
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qemu
cp COPYING %{buildroot}/usr/share/package-licenses/qemu/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/qemu/COPYING.LIB
cp COPYING.PYTHON %{buildroot}/usr/share/package-licenses/qemu/COPYING.PYTHON
cp LICENSE %{buildroot}/usr/share/package-licenses/qemu/LICENSE
cp capstone/LICENSE.TXT %{buildroot}/usr/share/package-licenses/qemu/capstone_LICENSE.TXT
cp capstone/LICENSE_LLVM.TXT %{buildroot}/usr/share/package-licenses/qemu/capstone_LICENSE_LLVM.TXT
cp capstone/bindings/python/LICENSE.TXT %{buildroot}/usr/share/package-licenses/qemu/capstone_bindings_python_LICENSE.TXT
cp disas/libvixl/LICENCE %{buildroot}/usr/share/package-licenses/qemu/disas_libvixl_LICENCE
cp dtc/README.license %{buildroot}/usr/share/package-licenses/qemu/dtc_README.license
cp linux-headers/COPYING %{buildroot}/usr/share/package-licenses/qemu/linux-headers_COPYING
cp roms/QemuMacDrivers/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_QemuMacDrivers_COPYING
cp roms/SLOF/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_SLOF_LICENSE
cp roms/ipxe/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_ipxe_COPYING
cp roms/ipxe/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/qemu/roms_ipxe_COPYING.GPLv2
cp roms/ipxe/src/include/ipxe/efi/LICENCE %{buildroot}/usr/share/package-licenses/qemu/roms_ipxe_src_include_ipxe_efi_LICENCE
cp roms/openbios/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_openbios_COPYING
cp roms/openbios/Documentation/kernel/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_openbios_Documentation_kernel_COPYING
cp roms/openbios/utils/devbios/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_openbios_utils_devbios_COPYING
cp roms/openhackware/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_openhackware_COPYING
cp roms/qemu-palcode/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_qemu-palcode_COPYING
cp roms/seabios-hppa/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_seabios-hppa_COPYING
cp roms/seabios-hppa/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu/roms_seabios-hppa_COPYING.LESSER
cp roms/seabios/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_seabios_COPYING
cp roms/seabios/COPYING.LESSER %{buildroot}/usr/share/package-licenses/qemu/roms_seabios_COPYING.LESSER
cp roms/sgabios/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_sgabios_COPYING
cp roms/skiboot/LICENCE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_LICENCE
cp roms/skiboot/ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_ccan_array_size_LICENSE
cp roms/skiboot/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_ccan_build_assert_LICENSE
cp roms/skiboot/ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_ccan_check_type_LICENSE
cp roms/skiboot/ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_ccan_container_of_LICENSE
cp roms/skiboot/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_ccan_endian_LICENSE
cp roms/skiboot/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_ccan_list_LICENSE
cp roms/skiboot/ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_ccan_short_types_LICENSE
cp roms/skiboot/ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_skiboot_ccan_str_LICENSE
cp roms/u-boot-sam460ex/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_u-boot-sam460ex_COPYING
cp roms/u-boot-sam460ex/board/ACube/bios_emulator/scitech/src/x86emu/LICENSE %{buildroot}/usr/share/package-licenses/qemu/roms_u-boot-sam460ex_board_ACube_bios_emulator_scitech_src_x86emu_LICENSE
cp roms/u-boot-sam460ex/fs/jffs2/LICENCE %{buildroot}/usr/share/package-licenses/qemu/roms_u-boot-sam460ex_fs_jffs2_LICENCE
cp roms/vgabios/COPYING %{buildroot}/usr/share/package-licenses/qemu/roms_vgabios_COPYING
cp slirp/COPYRIGHT %{buildroot}/usr/share/package-licenses/qemu/slirp_COPYRIGHT
cp tests/qemu-iotests/COPYING %{buildroot}/usr/share/package-licenses/qemu/tests_qemu-iotests_COPYING
cp ui/keycodemapdb/LICENSE.BSD %{buildroot}/usr/share/package-licenses/qemu/ui_keycodemapdb_LICENSE.BSD
cp ui/keycodemapdb/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qemu/ui_keycodemapdb_LICENSE.GPL2
%make_install
%find_lang qemu

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/qemu-img
/usr/bin/ivshmem-client
/usr/bin/ivshmem-server
/usr/bin/qemu-ga
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
/usr/share/package-licenses/qemu/disas_libvixl_LICENCE
/usr/share/package-licenses/qemu/roms_ipxe_src_include_ipxe_efi_LICENCE
/usr/share/package-licenses/qemu/roms_skiboot_LICENCE
/usr/share/package-licenses/qemu/roms_u-boot-sam460ex_fs_jffs2_LICENCE
/usr/share/qemu/QEMU,cgthree.bin
/usr/share/qemu/QEMU,tcx.bin
/usr/share/qemu/bamboo.dtb
/usr/share/qemu/bios-256k.bin
/usr/share/qemu/bios.bin
/usr/share/qemu/canyonlands.dtb
/usr/share/qemu/efi-e1000.rom
/usr/share/qemu/efi-e1000e.rom
/usr/share/qemu/efi-eepro100.rom
/usr/share/qemu/efi-ne2k_pci.rom
/usr/share/qemu/efi-pcnet.rom
/usr/share/qemu/efi-rtl8139.rom
/usr/share/qemu/efi-virtio.rom
/usr/share/qemu/efi-vmxnet3.rom
/usr/share/qemu/hppa-firmware.img
/usr/share/qemu/keymaps/ar
/usr/share/qemu/keymaps/bepo
/usr/share/qemu/keymaps/common
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
/usr/share/qemu/keymaps/modifiers
/usr/share/qemu/keymaps/nl
/usr/share/qemu/keymaps/nl-be
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
/usr/share/qemu/palcode-clipper
/usr/share/qemu/petalogix-ml605.dtb
/usr/share/qemu/petalogix-s3adsp1800.dtb
/usr/share/qemu/ppc_rom.bin
/usr/share/qemu/pxe-e1000.rom
/usr/share/qemu/pxe-eepro100.rom
/usr/share/qemu/pxe-ne2k_pci.rom
/usr/share/qemu/pxe-pcnet.rom
/usr/share/qemu/pxe-rtl8139.rom
/usr/share/qemu/pxe-virtio.rom
/usr/share/qemu/qemu-icon.bmp
/usr/share/qemu/qemu_logo_no_text.svg
/usr/share/qemu/qemu_vga.ndrv
/usr/share/qemu/s390-ccw.img
/usr/share/qemu/s390-netboot.img
/usr/share/qemu/sgabios.bin
/usr/share/qemu/skiboot.lid
/usr/share/qemu/slof.bin
/usr/share/qemu/spapr-rtas.bin
/usr/share/qemu/trace-events-all
/usr/share/qemu/u-boot-sam460-20100605.bin
/usr/share/qemu/u-boot.e500
/usr/share/qemu/vgabios-cirrus.bin
/usr/share/qemu/vgabios-qxl.bin
/usr/share/qemu/vgabios-stdvga.bin
/usr/share/qemu/vgabios-virtio.bin
/usr/share/qemu/vgabios-vmware.bin
/usr/share/qemu/vgabios.bin

%files extras
%defattr(-,root,root,-)
/usr/bin/qemu-img

%files libexec
%defattr(-,root,root,-)
%exclude /usr/libexec/qemu-bridge-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qemu/COPYING
/usr/share/package-licenses/qemu/COPYING.LIB
/usr/share/package-licenses/qemu/COPYING.PYTHON
/usr/share/package-licenses/qemu/LICENSE
/usr/share/package-licenses/qemu/capstone_LICENSE.TXT
/usr/share/package-licenses/qemu/capstone_LICENSE_LLVM.TXT
/usr/share/package-licenses/qemu/capstone_bindings_python_LICENSE.TXT
/usr/share/package-licenses/qemu/dtc_README.license
/usr/share/package-licenses/qemu/linux-headers_COPYING
/usr/share/package-licenses/qemu/roms_QemuMacDrivers_COPYING
/usr/share/package-licenses/qemu/roms_SLOF_LICENSE
/usr/share/package-licenses/qemu/roms_ipxe_COPYING
/usr/share/package-licenses/qemu/roms_ipxe_COPYING.GPLv2
/usr/share/package-licenses/qemu/roms_openbios_COPYING
/usr/share/package-licenses/qemu/roms_openbios_Documentation_kernel_COPYING
/usr/share/package-licenses/qemu/roms_openbios_utils_devbios_COPYING
/usr/share/package-licenses/qemu/roms_openhackware_COPYING
/usr/share/package-licenses/qemu/roms_qemu-palcode_COPYING
/usr/share/package-licenses/qemu/roms_seabios-hppa_COPYING
/usr/share/package-licenses/qemu/roms_seabios-hppa_COPYING.LESSER
/usr/share/package-licenses/qemu/roms_seabios_COPYING
/usr/share/package-licenses/qemu/roms_seabios_COPYING.LESSER
/usr/share/package-licenses/qemu/roms_sgabios_COPYING
/usr/share/package-licenses/qemu/roms_skiboot_ccan_array_size_LICENSE
/usr/share/package-licenses/qemu/roms_skiboot_ccan_build_assert_LICENSE
/usr/share/package-licenses/qemu/roms_skiboot_ccan_check_type_LICENSE
/usr/share/package-licenses/qemu/roms_skiboot_ccan_container_of_LICENSE
/usr/share/package-licenses/qemu/roms_skiboot_ccan_endian_LICENSE
/usr/share/package-licenses/qemu/roms_skiboot_ccan_list_LICENSE
/usr/share/package-licenses/qemu/roms_skiboot_ccan_short_types_LICENSE
/usr/share/package-licenses/qemu/roms_skiboot_ccan_str_LICENSE
/usr/share/package-licenses/qemu/roms_u-boot-sam460ex_COPYING
/usr/share/package-licenses/qemu/roms_u-boot-sam460ex_board_ACube_bios_emulator_scitech_src_x86emu_LICENSE
/usr/share/package-licenses/qemu/roms_vgabios_COPYING
/usr/share/package-licenses/qemu/slirp_COPYRIGHT
/usr/share/package-licenses/qemu/tests_qemu-iotests_COPYING
/usr/share/package-licenses/qemu/ui_keycodemapdb_LICENSE.BSD
/usr/share/package-licenses/qemu/ui_keycodemapdb_LICENSE.GPL2

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/libexec/qemu-bridge-helper

%files locales -f qemu.lang
%defattr(-,root,root,-)

