GARNAME = SDL_Pango
GARVERSION = 0.1.2
CATEGORIES = net
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/sdlpango/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/SDL

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-sdl-prefix=$(DESTDIR)$(prefix) \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/libSDL_Pango.la
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/SDL_Pango.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/SDL_Pango.pc
	@$(MAKECOOKIE)

