GARNAME = webkit
GARVERSION = 1.1.11
#GARVERSION = r46126
CATEGORIES =lib
MASTER_SITES = http://www.webkitgtk.org/
#MASTER_SITES = http://builds.nightly.webkit.org/files/trunk/src/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-patch.gar
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c
BUILDDEPS = testing/gperf

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-unicode-backend=glib \
	--with-gnu-ld 


include ../../gar.mk

no-pre-configure:
	@cd $(WORKSRC); autoreconf --force --install --verbose;
	@$(MAKECOOKIE)

no-pre-configure:
	@echo "ac_cv_func_malloc_0_nonnull=yes" >  $(WORKSRC)/config.cache
	@echo "ac_cv_func_realloc_0_nonnull=yes" >>  $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libproxy.la
	@$(MAKECOOKIE)
