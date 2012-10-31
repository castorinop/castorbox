GARNAME = ushare
GARVERSION = 1.1a
CATEGORIES = net
MASTER_SITES = http://ushare.geexbox.org/releases/
DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES = $(DISTNAME)-cross_compiling.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libupnp

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = --prefix=$(prefix) \
	--sysconfdir=$(sysconfdir) \
	--cross-compile \
	--disable-nls

include ../../gar.mk
