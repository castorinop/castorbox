GARNAME = joy2key
GARVERSION = 1.6
CATEGORIES = games
MASTER_SITES = http://interreality.org/~tetron/technology/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
#LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c xorg/xorg xorg-7.2/xwininfo

WORKSRC = $(WORKDIR)/$(DISTNAME).1

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk

