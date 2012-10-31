GARNAME = dx2-xl
GARVERSION = 1.9.262
CATEGORIES = games
MASTER_SITES = http://www.descent2.de/downloads/
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/criticalmass/
DISTFILES = $(GARNAME)-src-$(GARVERSION).rar
PATCHFILES = $(DISTNAME).patch.gar
#DISTFILES += $(GARNAME).png  $(GARNAME).sh
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/SDL games/SDL_mixer games/SDL_image

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
	

include ../../gar.mk
include ../games.mk

pre-configure:
	@touch $(WORKSRC)/{NEWS,README,AUTHORS,ChangeLog}
	@cd $(WORKSRC) && autoreconf --force --install 
	sed s@sdl-config@$(DESTDIR)/$(bindir)/sdl-config@g < $(WORKSRC)/configure > $(WORKSRC)/configure.new
	cp -f $(WORKSRC)/configure.new $(WORKSRC)/configure
	@$(MAKECOOKIE)

install-launcher:
	@cp -rf $(WORKDIR)/Ri-li.* $(DESTDIR)$(games_launcher)/
	@$(MAKECOOKIE)
