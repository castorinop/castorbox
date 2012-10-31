GARNAME = fuse
GARVERSION = 2.8.1
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
CATEGORIES = net

DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-fix_cross.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-lib \
	--enable-util \
	--disable-mtab \
	--with-gnu-ld 

include ../../gar.mk

pre-configure:
	@#cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)


