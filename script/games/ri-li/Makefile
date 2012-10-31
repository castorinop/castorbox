GARNAME = Ri-li
GARVERSION = 2.0.0
CATEGORIES = games
MASTER_SITES = http://download.sourceforge.net/ri-li/
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/ri-li/
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += $(GARNAME).png  $(GARNAME).sh
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/SDL games/SDL_mixer

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile launcher

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld \
	CXXFLAGS="$(CXXFLAGS) -I$(DESTDIR)$(includedir)/SDL"
	

include ../../gar.mk
include ../games.mk

install-launcher:
	@cp -rf $(WORKDIR)/Ri-li.* $(DESTDIR)$(games_launcher)/
	@$(MAKECOOKIE)
