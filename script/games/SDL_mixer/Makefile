GARNAME = SDL_mixer
GARVERSION = 1.2.11
CATEGORIES = games
MASTER_SITES = http://www.libsdl.org/projects/SDL_mixer/release/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-crosscompile.patch
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/c lib/SDL
BUILDDEPS = devel/nasm 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-music-ogg \
	--enable-music-ogg-shared \
	--with-gnu-ld

include ../../gar.mk
#include ../games.mk

post-install:
	@rm -rf $(DESTDIR)$(games_includedir)/libSDL_mixer.la
#	@ln -sf $(DESTDIR)$(games_includedir)/SDL/$(GARNAME).h $(DESTDIR)$(includedir)/SDL
	@$(MAKECOOKIE)
