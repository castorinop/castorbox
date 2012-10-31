GARNAME = CriticalMass
GARVERSION = 1.0.0
CATEGORIES = games
MASTER_SITES = http://download.sourceforge.net/criticalmass/
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/criticalmass/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME).patch.gar $(DISTNAME)-disable-curl.patch
DISTFILES += $(GARNAME).png  $(GARNAME).sh
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/SDL games/SDL_mixer games/SDL_image net/curl

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile launcher

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-dyngl \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld \
	--disable-optimize \
	LDFLAGS="$(LDFLAGS)" \
	CXXFLAGS="$(CXXFLAGS) -I$(DESTDIR)$(includedir)/SDL"

BUILD_ARGS = LD_LIBPATH="$(DESTDIR)$(libdir):$(DESTDIR)$(games_libdir)" 

include ../../gar.mk
include ../games.mk

PARALLELMFLAGS := -j1

pre-configure:
	@touch $(WORKSRC)/{NEWS,README,AUTHORS,ChangeLog}
	@cd $(WORKSRC) && autoreconf --force --install 
	sed s@sdl-config@$(DESTDIR)/$(bindir)/sdl-config@g < $(WORKSRC)/configure > $(WORKSRC)/configure.new
	cp -f $(WORKSRC)/configure.new $(WORKSRC)/configure
	@$(MAKECOOKIE)

install-launcher:
	@cp -rf $(WORKDIR)/$(GARNAME).png $(DESTDIR)$(games_launcher)/Critical\ Mass.png
	@cp -rf $(WORKDIR)/$(GARNAME).sh  $(DESTDIR)$(games_launcher)/Critical\ Mass.sh
	@$(MAKECOOKIE)

