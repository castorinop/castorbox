GARNAME = libpng
GARVERSION = 1.4.7
CATEGORIES = lib
MASTER_SITES = http://downloads.sourceforge.net/project/$(GARNAME)/$(GARNAME)14/$(GARVERSION)/
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += config.cache.$(GARCH_FAMILY)
PATCHFILES = $(DISTNAME).patch.gar
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/LICENSE

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/zlib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-shared \
	--disable-static \
	--with-gnu-ld

include ../../gar.mk

extract-config.cache.$(GARCH_FAMILY):
	@cp $(DOWNLOADDIR)/config.cache.$(GARCH_FAMILY) $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

pre-configure:
	@#$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libpng14.la
	@rm -f $(DESTDIR)$(libdir)/libpng.la
	@rm -f $(DESTDIR)$(bindir)-config/libpng14-config
	@rm -f $(DESTDIR)$(bindir)-config/libpng-config
	@rm -f $(DESTDIR)$(bindir)-config/$(compiler_prefix)libpng14-config
	@rm -f $(DESTDIR)$(bindir)-config/$(compiler_prefix)libpng-config
	@mkdir -p $(DESTDIR)$(bindir)-config
	@mv $(DESTDIR)$(bindir)/libpng14-config $(DESTDIR)$(bindir)-config/libpng14-config
	@mv $(DESTDIR)$(bindir)/libpng-config $(DESTDIR)$(bindir)-config/libpng-config
	@$(if $(compiler_prefix), ln -s libpng14-config $(DESTDIR)$(bindir)-config/$(compiler_prefix)libpng14-config)
	@$(if $(compiler_prefix), ln -s libpng-config $(DESTDIR)$(bindir)-config/$(compiler_prefix)libpng-config)
	@$(MAKECOOKIE)
