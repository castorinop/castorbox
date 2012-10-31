GARNAME = libshout
GARVERSION = 2.2.2
CATEGORIES = lib
MASTER_SITES = http://downloads.us.xiph.org/releases/libshout/
PATCHFILES = $(DISTNAME)-fix_linkage.patch
DISTFILES = $(DISTNAME).tar.gz
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/speex lib/libvorbis lib/libogg 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-speex=$(DESTDIR)$(prefix)  \
	--with-gnu-ld 

include ../../gar.mk

pre-configure:
	@ cd $(WORKSRC); autoreconf -fis
	@$(MAKECOOKIE)	

post-install:
	@rm -fv $(DESTDIR)$(libdir)/libshout.la
	@$(MAKECOOKIE)
