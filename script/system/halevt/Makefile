GARNAME = halevt
GARVERSION = 0.1.4
CATEGORIES = system
MASTER_SITES = http://savannah.nongnu.org/download/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-fix-umount.patch \
#		$(DISTNAME)-nonexisting_cdrom.diff \
#		$(DISTNAME)-drop_privs.diff \
#		$(DISTNAME)-fix_mountpoint_loop.diff

LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/dbus-glib system/hal lib/libxml2 lib/boolstuff

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld

include ../../gar.mk
