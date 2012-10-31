GARNAME = libtheora
GARVERSION = 1.1.1
CATEGORIES = lib
MASTER_SITES = http://downloads.xiph.org/releases/theora/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = xiph
xiph_LICENSE_TEXT = $(WORKSRC)/COPYING

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libogg lib/libvorbis lib/SDL

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--disable-static \
	--disable-spec \
	--disable-valgrind-testing \
	--enable-asm \
	--disable-oggtest \
	--disable-vorbistest \
	--disable-sdltest \
	--disable-telemetry \
	--enable-float \
	--enable-encode \
	--disable-examples \
	--with-gnu-ld

Optional Packages:

include ../../gar.mk

post-patch:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	rm -f $(DESTDIR)$(libdir)/libtheora.la
	rm -f $(DESTDIR)$(libdir)/libtheoradec.la
	rm -f $(DESTDIR)$(libdir)/libtheoraenc.la
	@$(MAKECOOKIE)
