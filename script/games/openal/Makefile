GARNAME = openal
GARVERSION = 0.0.8
CATEGORIES = games
MASTER_SITES = http://www.openal.org/openal_webstf/downloads/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-gcc4.2.patch
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/c 


CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk

PARALLELMFLAGS := -j1

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libopenal.la
	@$(MAKECOOKIE)
