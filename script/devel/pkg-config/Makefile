GARNAME = pkg-config
GARVERSION = 0.25
CATEGORIES = devel
MASTER_SITES = http://pkgconfig.freedesktop.org/releases/
DISTFILES = $(DISTNAME).tar.gz 
PATCHFILES = $(DISTNAME)-autoconf_2.66.patch $(DISTNAME)-m4_pattern_allow.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--disable-static \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC),configure)
	@$(MAKECOOKIE)
