#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qemu
Version  : 2.4.0
Release  : 26
URL      : http://wiki.qemu-project.org/download/qemu-2.4.0.tar.bz2
Source0  : http://wiki.qemu-project.org/download/qemu-2.4.0.tar.bz2
Summary  : OpenBIOS development utilities
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-2.0 GPL-2.0+ GPL-3.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0 MIT
Requires: qemu-bin
Requires: qemu-data
BuildRequires : automake-dev
BuildRequires : curl-dev
BuildRequires : glib-dev
BuildRequires : gnutls-dev
BuildRequires : libaio-dev
BuildRequires : libcap-ng-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : lzo-dev
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : nettle-dev
BuildRequires : numactl-dev
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : python-dev
BuildRequires : usbredir-dev
BuildRequires : zlib-dev
Patch1: configure.patch
Patch2: cores-default.patch
Patch3: 0001-Use-run-lock.patch
Patch4: 0001-Use-widechar-ncurses.patch
Patch5: nodatasync.patch

%description
This package contains the OpenBIOS development utilities.

There are
* toke - an IEEE 1275-1994 compliant FCode tokenizer
* detok - an IEEE 1275-1994 compliant FCode detokenizer
* paflof - a forth kernel running in user space
* an fcode bytecode evaluator running in paflof

See /usr/share/doc/packages/openbios for details and examples.

Authors:
--------
    Stefan Reinauer <stepan@openbios.net>
    Segher Boessenkool <segher@openbios.net>

%package bin
Summary: bin components for the qemu package.
Group: Binaries
Requires: qemu-data

%description bin
bin components for the qemu package.


%package data
Summary: data components for the qemu package.
Group: Data

%description data
data components for the qemu package.


%prep
%setup -q -n qemu-2.4.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure --disable-static --disable-sdl  --enable-kvm --enable-usb-redir --enable-curses --enable-system  --disable-strip
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qemu-aarch64
/usr/bin/qemu-alpha
/usr/bin/qemu-arm
/usr/bin/qemu-armeb
/usr/bin/qemu-cris
/usr/bin/qemu-ga
/usr/bin/qemu-i386
/usr/bin/qemu-img
/usr/bin/qemu-io
/usr/bin/qemu-m68k
/usr/bin/qemu-microblaze
/usr/bin/qemu-microblazeel
/usr/bin/qemu-mips
/usr/bin/qemu-mips64
/usr/bin/qemu-mips64el
/usr/bin/qemu-mipsel
/usr/bin/qemu-mipsn32
/usr/bin/qemu-mipsn32el
/usr/bin/qemu-nbd
/usr/bin/qemu-or32
/usr/bin/qemu-ppc
/usr/bin/qemu-ppc64
/usr/bin/qemu-ppc64abi32
/usr/bin/qemu-ppc64le
/usr/bin/qemu-s390x
/usr/bin/qemu-sh4
/usr/bin/qemu-sh4eb
/usr/bin/qemu-sparc
/usr/bin/qemu-sparc32plus
/usr/bin/qemu-sparc64
/usr/bin/qemu-system-aarch64
/usr/bin/qemu-system-alpha
/usr/bin/qemu-system-arm
/usr/bin/qemu-system-cris
/usr/bin/qemu-system-i386
/usr/bin/qemu-system-lm32
/usr/bin/qemu-system-m68k
/usr/bin/qemu-system-microblaze
/usr/bin/qemu-system-microblazeel
/usr/bin/qemu-system-mips
/usr/bin/qemu-system-mips64
/usr/bin/qemu-system-mips64el
/usr/bin/qemu-system-mipsel
/usr/bin/qemu-system-moxie
/usr/bin/qemu-system-or32
/usr/bin/qemu-system-ppc
/usr/bin/qemu-system-ppc64
/usr/bin/qemu-system-ppcemb
/usr/bin/qemu-system-s390x
/usr/bin/qemu-system-sh4
/usr/bin/qemu-system-sh4eb
/usr/bin/qemu-system-sparc
/usr/bin/qemu-system-sparc64
/usr/bin/qemu-system-tricore
/usr/bin/qemu-system-unicore32
/usr/bin/qemu-system-x86_64
/usr/bin/qemu-system-xtensa
/usr/bin/qemu-system-xtensaeb
/usr/bin/qemu-unicore32
/usr/bin/qemu-x86_64
/usr/libexec/qemu-bridge-helper

%files data
%defattr(-,root,root,-)
/usr/share/qemu/QEMU,cgthree.bin
/usr/share/qemu/QEMU,tcx.bin
/usr/share/qemu/acpi-dsdt.aml
/usr/share/qemu/bamboo.dtb
/usr/share/qemu/bios-256k.bin
/usr/share/qemu/bios.bin
/usr/share/qemu/efi-e1000.rom
/usr/share/qemu/efi-eepro100.rom
/usr/share/qemu/efi-ne2k_pci.rom
/usr/share/qemu/efi-pcnet.rom
/usr/share/qemu/efi-rtl8139.rom
/usr/share/qemu/efi-virtio.rom
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
/usr/share/qemu/q35-acpi-dsdt.aml
/usr/share/qemu/qemu-icon.bmp
/usr/share/qemu/qemu_logo_no_text.svg
/usr/share/qemu/s390-ccw.img
/usr/share/qemu/s390-zipl.rom
/usr/share/qemu/sgabios.bin
/usr/share/qemu/slof.bin
/usr/share/qemu/spapr-rtas.bin
/usr/share/qemu/trace-events
/usr/share/qemu/u-boot.e500
/usr/share/qemu/vgabios-cirrus.bin
/usr/share/qemu/vgabios-qxl.bin
/usr/share/qemu/vgabios-stdvga.bin
/usr/share/qemu/vgabios-virtio.bin
/usr/share/qemu/vgabios-vmware.bin
/usr/share/qemu/vgabios.bin
