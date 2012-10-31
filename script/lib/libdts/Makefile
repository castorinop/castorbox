GARNAME = libdts
GARVERSION = 0.0.2
CATEGORIES = lib
MASTER_SITES = http://download.videolan.org/pub/videolan/libdca/$(GARVERSION)/
DISTFILES = libdca-$(GARVERSION).tar.gz
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-debug \
	--disable-fixed \
	--disable-double \
	--disable-oss \
	--disable-solaris-audio \
	--disable-al-audio \
	--disable-win \
	--disable-warnings \
	--disable-gprof

include ../../gar.mk

post-install:
	@sed -i 's%-L$${libdir}%-L$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/libdts.pc
	@sed -i 's%-I$${includedir}%-I$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/libdts.pc
	@if [ -e $(DESTDIR)$(libdir)/libdts_pic.a ] ; then \
		mv -f $(DESTDIR)$(libdir)/libdts_pic.a $(DESTDIR)$(libdir)/libdts.a ; \
	 fi
	@$(MAKECOOKIE)
