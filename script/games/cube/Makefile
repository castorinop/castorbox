GARNAME = cube
GARVERSION = 2005_08_29
CATEGORIES = games
#MASTER_SITES = http://download.sourceforge.net/tuxracer/
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
MASTER_SITES += http://www.quadropolis.us/files/
DISTFILES = $(DISTNAME)_unix.tar.gz sauerjoy.zip
#PATCHFILES = $(GARNAME).patch.gar
LICENSE = GPL2

DISTNAME := $(GARNAME)_$(GARVERSION)

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/SDL

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--x-includes="$(DESTDIR)$(includedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-gl-inc="$(DESTDIR)$(includedir)" \
	--with-gl-libs="$(DESTDIR)$(libdir)" \
	--with-tcl-libs=$(DESTDIR)$(games_libdir) \
	--with-tcl-lib-name=tcl8.4 \
	--with-tcl-inc=$(DESTDIR)$(games_includedir) \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk

pre-configure:
	@cd $(WORKSRC) && autoreconf --force --install 
	@$(MAKECOOKIE)

post-install:
	@cp -rf $(WORKDIR)/data/* $(DESTDIR)$(datadir)/$(GARNAME)/
	@$(MAKECOOKIE)
