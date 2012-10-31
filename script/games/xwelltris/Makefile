GARNAME = xwelltris
GARVERSION = 1.0.1
CATEGORIES = games
MASTER_SITES = http://xnc.dubna.su/xwelltris/src/
DISTFILES = $(DISTNAME).src.tar.gz
DISTFILES += Xwelltris.png Xwelltris.sh 
PATCHFILES = $(DISTNAME).patch.gar
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/SDL
LIBDEPS   = games/SDL_image

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile launcher

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--cache-file=config.cache \
	--with-x \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk

pre-configure:
	@# Create config.cache
	@rm -f $(WORKSRC)/config.cache
	@echo "ac_cv_file__proc_self_maps=yes" >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

install-launcher:
	@cp -rf $(WORKDIR)/Xwelltris.* $(DESTDIR)$(games_launcher)/
	@$(MAKECOOKIE)
	
