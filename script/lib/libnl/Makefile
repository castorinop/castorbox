GARNAME = libnl
GARVERSION = 1.1
CATEGORIES = lib
MASTER_SITES = http://downloads.openwrt.org/sources/ http://people.suug.ch/~tgr/libnl/files/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES= $(DISTNAME)-include-limits-h.patch
LICENSE = MIT/MIT_Modified

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/zlib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

