GARNAME = frozen-bubble
GARVERSION = 2.1.0
CATEGORIES = extras
MASTER_SITES = http://www.frozen-bubble.org/data/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)_fix.patch
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c xorg/xorg lib/SDL \
	games/SDL_image games/SDL_mixer \
	perl/perl games/SDL_perl testing/SDL_Pango


BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-gtk=no \
	--enable-sound=yes \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld

BUILD_ARGS = PREFIX="$(prefix)" PERL="$(DESTDIR)$(bindir)/perl -I$(PERL_sitearch) -I$(PERL_configdir)"
INSTALL_ARGS =  PREFIX="$(prefix)"

include ../../perl/perl/package-api.mk
include ../../gar.mk
include ../games.mk

