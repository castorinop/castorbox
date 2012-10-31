GARNAME = check
GARVERSION = 0.9.5
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

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

BUILD_ARGS = LDFLAGS='-L$(DESTDIR)$(libdir)' \
	CFLAGS='$(CFLAGS)'

BUILD_OVERRIDE_DIRS = libdir LIBS INCLUDE
include ../../gar.mk

pre-configure:
	@echo "ac_cv_func_malloc_0_nonnull=yes" >  $(WORKSRC)/config.cache
	@echo "ac_cv_func_realloc_0_nonnull=yes" >>  $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libcheck.la
	sed -i 's%-L$${libdir}%-L$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/check.pc
	sed -i 's%-I$${includedir}%-I$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/check.pc
	@$(MAKECOOKIE)
