GARNAME = crack-attack
GARVERSION = 1.1.14
CATEGORIES = games
MASTER_SITES = http://savannah.nongnu.org/download/$(GARNAME)/
MASTER_SITES += http://www.miguev.net/misc/
DISTFILES = $(DISTNAME).tar.bz2 $(GARNAME)-sounds.tar.gz $(GARNAME)-music.tar.bz2
DISTFILES += Crack-Attack.png Crack-Attack.sh 
#LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c 
LIBDEPS   = games/SDL_mixer

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile launcher

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--cache-file=config.cache \
	--enable-gtk=no \
	--enable-sound=yes \
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

post-install:
	@mkdir -p $(DESTDIR)$(games_datadir)/$(GARNAME)/
	@cp -rf $(WORKDIR)/data/* $(DESTDIR)$(games_datadir)/$(GARNAME)/
	@$(MAKECOOKIE)

install-launcher:
	@cp -rf $(WORKDIR)/Crack-Attack.* $(DESTDIR)$(games_launcher)/
	@$(MAKECOOKIE)
	
