GARNAME = dxr3player
GARVERSION = 0.10
CATEGORIES = mediaplayers
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(GARNAME).patch.gar
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c xorg/xorg lib/freetype lib/libpng lirc/lirc

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-overlay \
	--without-em830 \
	--with-sdl=$(DESTDIR)$(prefix) \
	--with-mad=$(DESTDIR)$(prefix) \
 	--with-lirc=$(DESTDIR)$(prefix) \
	--cache-file=config.cache \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--with-gnu-ld \
	--with-x \

include ../../gar.mk

pre-configure:
	@echo "ac_cv_path_CURL_CONFIG=no"  >  $(WORKSRC)/config.cache
	@echo "ac_cv_path_AALIB_CONFIG=no" >> $(WORKSRC)/config.cache
	@echo "ac_cv_path_CACA_CONFIG=no"  >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)
