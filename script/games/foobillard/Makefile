GARNAME = foobillard
GARVERSION = 3.0a
CATEGORIES = games
MASTER_SITES = http://foobillard.sunsite.dk/dnl/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c games/Xaw3d

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-glut \
	--enable-sound=yes \
	--enable-nvidia=no \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk

