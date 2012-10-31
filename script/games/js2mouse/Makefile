GARNAME = js2mouse
GARVERSION = 040208
CATEGORIES = games
MASTER_SITES = http://cedric.vincent.perso.free.fr/Projets/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(GARNAME).patch.gar
#LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c xorg/xorg

WORKSRC = $(WORKDIR)/$(GARNAME)/$(GARNAME)/

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--with-gnu-ld

INSTALL_ARGS = bindir=$(games_bindir)

include ../../gar.mk
include ../games.mk

