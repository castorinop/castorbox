GARNAME = mediainfo
GARVERSION = 0.7.37
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(GARNAME)_$(GARVERSION).tar.bz2
#PATCHFILES = $(DISTNAME)-shared.patch
LICENSE = GPL

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c testing/libmediainfo 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) 

WORKSRC = $(WORKDIR)/MediaInfo/Project/GNU/CLI

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)
