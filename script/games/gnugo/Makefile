GARNAME = gnugo
GARVERSION = 3.6
CATEGORIES = games
MASTER_SITES = http://ftp.gnu.org/gnu/gnugo/
DISTFILES = $(DISTNAME).tar.gz 
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-gtk=no \
	--enable-sound=yes \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk
