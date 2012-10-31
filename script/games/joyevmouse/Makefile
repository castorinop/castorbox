GARNAME = joyevmouse
GARVERSION = 0.3
CATEGORIES = games
MASTER_SITES = http://welz.org.za/projects/joyevmouse/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME).patch
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS   = \
	CC="$(CC)" \
	CFLAGS="$(CFLAGS)" \
	DESTINATION="$(DESTDIR)$(games_bindir)"
INSTALL_ARGS = $(BUILD_ARGS)

include ../../gar.mk
include ../games.mk
