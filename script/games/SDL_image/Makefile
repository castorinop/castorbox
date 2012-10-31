GARNAME = SDL_image
GARVERSION = 1.2.5
CATEGORIES = games
MASTER_SITES = http://www.libsdl.org/projects/SDL_image/release/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME).patch.gar
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/c lib/SDL lib/zlib lib/libpng lib/libjpeg lib/libtiff


CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-png-shared \
	--disable-tif-shared \
	--disable-jpeg-shared \
	--disable-rpath \
	--with-gnu-ld

include ../../gar.mk
#include ../games.mk

post-install:
	@rm -rf $(DESTDIR)$(games_libdir)/libSDL_image.la
#	@ln -sfv $(DESTDIR)$(games_includedir)/SDL/$(GARNAME).h $(DESTDIR)$(includedir)/SDL
	@$(MAKECOOKIE)
