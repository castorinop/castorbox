GARNAME = DeviceKit-disks
GARVERSION = 006
CATEGORIES = system
MASTER_SITES =  http://hal.freedesktop.org/releases/
DISTFILES = $(DISTNAME).tar.gz
NO_PATCHFILES = $(DISTNAME)-fix-hal-storage-mount-crash.patch \
	     $(DISTNAME)-fix-duplicate-udi.patch \
	     $(DISTNAME)-singleton_connection.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c system/udev lib/dbus-glib lib/expat utils/pciutils lib/libusb utils/usbutils disk/e2fsprogs/
BUILDDEPS = perl/perl /perl/perl-XML-Parser

CONFIGURE_SCRIPTS   = $(WORKSRC)/configure
BUILD_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-hwdata=$(datadir) \
	--with-udev-prefix=$(sysconfdir) \
	--enable-docbook-docs=no \
	--disable-policy-kit \
	--disable-smbios \
	--enable-umount-helper \
	--with-gnu-ld

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/hal.la
	@rm -f $(DESTDIR)$(libdir)/hal-storage.la
	@$(MAKECOOKIE)

