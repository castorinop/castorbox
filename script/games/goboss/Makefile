GARNAME = GoBoss
GARVERSION = 0.1a
CATEGORIES = games
MASTER_SITES = http://www.ios-software.com/goboss/
DISTFILES = $(DISTNAME).tar.bz2 
PATCHFILES = $(GARNAME).patch.gar
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c games/gnugo
LIBDEPS   = lib/SDL games/SDL_ttf

WORKSRC = $(WORKDIR)/$(GARNAME)

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-gtk=no \
	--enable-sound=yes \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk


post-install:
	mkdir -p $(DESTDIR)$(datadir)/$(GARNAME)/
	@cp -rf $(WORKDIR)/data/* $(DESTDIR)$(datadir)/$(GARNAME)/
	@$(MAKECOOKIE)
