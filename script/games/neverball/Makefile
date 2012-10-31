GARNAME = neverball
GARVERSION = 1.4.0
CATEGORIES = games
MASTER_SITES = http://icculus.org/neverball/
DISTFILES = $(DISTNAME).tar.gz
DISTFILES += NeverBall.sh NeverBall.jpg
PATCHFILES = $(DISTNAME).patch.gar
PATCHFILES += $(DISTNAME)_gamepad-fix.patch
#LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c xorg/xorg lib/SDL lib/freetype \
	games/SDL_image games/SDL_mixer games/SDL_ttf 

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom launcher

BUILD_ARGS   = \
	CC="$(CC)" \
	AR="$(AR)" \
	RANLIB="$(RANLIB)" \
	CFLAGS="$(CFLAGS) -ansi" \
	DESTDIR="$(DESTDIR)" \
	PREFIX="$(DESTDIR)$(games_prefix)" \
	BINDIR="$(DESTDIR)$(bindir)" \
	LIBDIR="$(DESTDIR)$(libdir)" \
	games_libdir="$(games_libdir)" \
	INCLUDEDIR="$(DESTDIR)$(includedir)" \
	X11_PATH="-L$(LIBDIR)" \
	MANDIR="$(DESTDIR)$(mandir)"

include ../../gar.mk
include ../games.mk

install-custom:
	@mkdir -p $(DESTDIR)$(games_datadir)/$(GARNAME)/
	@install -m 755 $(WORKSRC)/neverball   $(DESTDIR)$(games_bindir)
	#@install -m 755 $(WORKSRC)/neverputt   $(DESTDIR)$(bindir)
	@cp -rf $(WORKSRC)/data/* $(DESTDIR)$(games_datadir)/$(GARNAME)/
	@$(MAKECOOKIE)

install-launcher:
	@cp -rf $(WORKDIR)/NeverBall.* $(DESTDIR)$(games_launcher)/
	@$(MAKECOOKIE)
