GARNAME = lbreakout2
GARVERSION = 2.6beta-7
CATEGORIES = extras
MASTER_SITES =  http://easynews.dl.sourceforge.net/sourceforge/lgames/
DISTFILES = $(DISTNAME).tar.gz
#LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c xorg/xorg lib/SDL testing/SDL_mixer


CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld

include ../../gar.mk


