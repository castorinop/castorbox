GARNAME = sox
GARVERSION = 14.0.1
CATEGORIES = lib
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-taglib.patch $(DISTNAME)-destdir.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx lib/taglib lib/libmad

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libsox.la
	@$(MAKECOOKIE)
