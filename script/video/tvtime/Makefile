GARNAME = tvtime
GARVERSION = 1.0.2-ax
CATEGORIES = video
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
MASTER_SITES = http://www.stapelspeicher.org/tvtime/
DISTFILES = $(DISTNAME).tgz
#PATCHFILES = $(DISTNAME).buildfix.patch $(DISTNAME).glibc-2.10.patch
PATCHFILES = $(DISTNAME)-fix_localetable.patch
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c xorg/xorg lib/libpng lib/freetype lib/SDL
BUILDDEPS = lib/libxml2


CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir)  \
	--with-gnu-ld \
	--with-x

include ../../gar.mk
