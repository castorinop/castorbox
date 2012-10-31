GARNAME = libIDL
GARVERSION = 0.8.14
CATEGORIES = lib
MASTER_SITES = ftp://ftp.gnome.org/pub/gnome/sources/libIDL/0.8/
DISTFILES = $(DISTNAME).tar.bz2
#LICENSE = MPL

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c 


CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile


CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@echo "libIDL_cv_long_long_format=ll" > $(WORKSRC)/config.cache
	@$(call FIX_LIBTOOL_LIBPATH,$(WORKSRC),configure)
	@$(MAKECOOKIE)
