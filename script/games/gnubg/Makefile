GARNAME = gnubg
GARVERSION = source-MAIN-20070202
CATEGORIES = games
MASTER_SITES = http://www.gnubg.org/media/sources/
DISTFILES = $(DISTNAME).tar.gz 
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c 

WORKSRC = $(WORKDIR)/$(GARNAME)

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--without-gtk \
	--with-board3d \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/$(prefix) \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk

pre-configure:
	@cd $(WORKSRC) && autoreconf --force --install 
	@$(MAKECOOKIE)

post-install:
	@cp -rf $(WORKDIR)/data/* $(DESTDIR)$(datadir)/$(GARNAME)/
	@$(MAKECOOKIE)
