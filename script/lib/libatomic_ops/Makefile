GARNAME = libatomic_ops
GARVERSION = 1.2
CATEGORIES = lib
MASTER_SITES = http://www.hpl.hp.com/research/linux/atomic_ops/download/
DISTFILES = $(DISTNAME).tar.gz
#LICENSE = LGPL2_1

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
	@echo "ac_cv_func_malloc_0_nonnull=yes" >  $(WORKSRC)/config.cache
	@echo "ac_cv_func_realloc_0_nonnull=yes" >>  $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

