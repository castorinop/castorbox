GARNAME = SDL_sound
GARVERSION = 1.0.1
CATEGORIES = lib
MASTER_SITES = http://icculus.org/$(GARNAME)/downloads/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME).patch.gar
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/SDL

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-sdltest \
	--disable-gui \
	--with-gnu-ld \
	--with-sdl-prefix="$(DESTDIR)$(prefix)" \
	--with-sdl-exec-prefix="$(DESTDIR)$(prefix)"

include ../../gar.mk

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libSDL_sound.la
	@$(MAKECOOKIE)
