GARNAME = mp3gain
GARVERSION = 1.4.6
CATEGORIES = utils
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(GARNAME)-$(subst .,_,$(GARVERSION))-src.zip
#PATCHFILES = $(DISTNAME).patch.gar $(DISTNAME)-cramfs.patch $(DISTNAME)-cramfs_maxentries.patch
LICENSE = BSD/GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c 

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

EXTRACTDIR = $(WORKSRC)

BUILD_ARGS = CFLAGS="$(CGLAGS) -DHAVE_MEMCPY" CC=$(CC)
INSTALL_ARGS = INSTALL_PATH=$(DESTDIR)$(bindir)

include ../../gar.mk


pre-extract:
	mkdir -p $(WORKSRC)


