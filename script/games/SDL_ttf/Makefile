GARNAME = SDL_ttf
GARVERSION = 2.0.8
CATEGORIES = games
MASTER_SITES = http://www.libsdl.org/projects/$(GARNAME)/release/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-noftinternals.patch
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
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)$(prefix) \
	--with-freetype-prefix=$(DESTDIR) \
	--with-freetype-exec-prefix=$(DESTDIR)$(prefix) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--with-x \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk

post-install:
	@rm -rf $(DESTDIR)$(games_libdir)/libSDL_ttf.la
	@ln -sf $(DESTDIR)$(games_includedir)/SDL/$(GARNAME).h $(DESTDIR)$(includedir)/SDL
	@$(MAKECOOKIE)
