GARNAME = mpeg2dec
GARVERSION = 0.4.1
CATEGORIES = lib
MASTER_SITES = http://libmpeg2.sourceforge.net/files/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/SDL xorg/xorg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--enable-shared \
	--enable-static \
	--with-gnu-ld \
	--with-x \
	$(if $(filter i386,$(GARCH_FAMILY)),,--disable-accel-detect)

CONFIGURE_ENV = \
	SDLCONFIG="$(DESTDIR)$(bindir)/sdl-config"

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	rm -f $(DESTDIR)$(libdir)/libmpeg2.la
	rm -f $(DESTDIR)$(libdir)/libmpeg2convert.la
	@$(MAKECOOKIE)
