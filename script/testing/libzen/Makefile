GARNAME = libzen
GARVERSION = 0.4.15
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/zenlib/
DISTFILES = $(GARNAME)_$(GARVERSION).tar.bz2
#PATCHFILES = $(DISTNAME)-shared.patch
LICENSE = GPL

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
		--enable-shared  

ZENDIR = $(WORKDIR)/ZenLib
WORKSRC = $(ZENDIR)/Project/GNU/Library

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)
	
post-install:
	install -m755 $(WORKSRC)/libzen-config $(DESTDIR)$(bindir)-config
	cp -a $(ZENDIR)/Source/ZenLib $(DESTDIR)$(includedir)
	@$(MAKECOOKIE)
