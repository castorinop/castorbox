GARNAME = hal
GARVERSION = 0.5.14
CATEGORIES = system
MASTER_SITES =  http://hal.freedesktop.org/releases/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-fix_consolekit.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c system/udev lib/dbus-glib lib/expat utils/pciutils lib/libusb utils/usbutils utils/util-linux-ng

BUILDDEPS = perl/perl /perl/perl-XML-Parser

CONFIGURE_SCRIPTS   = $(WORKSRC)/configure
BUILD_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-hwdata=$(datadir) \
	--with-udev-prefix=$(sysconfdir) \
	--enable-docbook-docs=no \
	--disable-policy-kit \
	--enable-console-kit=no \
	--enable-umount-helper \
	--with-gnu-ld

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/hal.la
	@rm -f $(DESTDIR)$(libdir)/hal-storage.la
	@$(MAKECOOKIE)

