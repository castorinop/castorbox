GARNAME = nss-mdns
GARVERSION = 0.10
CATEGORIES = lib
MASTER_SITES = http://0pointer.de/lennart/projects/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c system/avahi

CONFIGURE_SCRIPTS   = $(WORKSRC)/configure
BUILD_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-avahi \
	--libdir=$(elibdir) \
	--with-gnu-ld

include ../../gar.mk

