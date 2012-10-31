GARNAME = agg
GARVERSION = 2.5
CATEGORIES = lib
MASTER_SITES = http://www.antigrain.com/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/cxx lib/freetype lib/SDL
BUILDDEPS = lib/SDL

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(includedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--enable-shared \
	--disable-static \
	--disable-examples \
	--disable-ctrl \
	--disable-platform \
	--disable-win32tt \
	--enable-freetype \
	--enable-gpc \
	--disable-sdltest \
	--with-gnu-ld \
	--with-sdl-prefix="$(DESTDIR)$(prefix)" \
	--with-x
	
include ../../gar.mk

pre-configure:
	@cd $(WORKSRC) ; aclocal
	@cd $(WORKSRC) ; autoheader
	@cd $(WORKSRC) ; autoconf
	@cd $(WORKSRC) ; libtoolize --force
	@cd $(WORKSRC) ; automake --foreign --add-missing --ignore-deps
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libagg.la
	@rm -f $(DESTDIR)$(libdir)/libaggfontfreetype.la
	@rm -f $(DESTDIR)$(libdir)/libagggpc.la
	@$(MAKECOOKIE)
