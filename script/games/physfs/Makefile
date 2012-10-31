GARNAME = physfs
GARVERSION = 1.1.0
CATEGORIES = games
MASTER_SITES = http://icculus.org/physfs/downloads/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME).patch.gar
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

post-install:
	@echo installing gamedir mkdir -p $(games_prefix)
	@rm -rf $(DESTDIR)$(libdir)/libphysfs.la
	@$(MAKECOOKIE)
