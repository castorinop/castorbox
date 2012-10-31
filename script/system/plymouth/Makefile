GARNAME = plymouth
GARVERSION = 0.8.3
CATEGORIES = system
MASTER_SITES = http://www.freedesktop.org/software/$(GARNAME)/releases/
DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES = $(DISTNAME)-autotools_fixes.patch $(DISTNAME)-remove_no_static.patch $(DISTNAME)-no_klibc.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libjpeg lib/libmng lib/libpng lib/zlib lib/freetype

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-shared \
	--enable-static \
	--disable-debug \
	--disable-pango \
	--with-gnu-ld \

BUILD_ENV = \
	QUIET=false

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC),configure)
	@$(MAKECOOKIE)

pre-install:
	@rm -f $(DESTDIR)$(esbindir)/fbcondecor_ctl.static
	@rm -f $(DESTDIR)$(esbindir)/fbsplashd.static
	@rm -f $(DESTDIR)$(esbindir)/splash_util.static
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libfbsplash.la
	@rm -f $(DESTDIR)$(libdir)/libfbsplashrender.la
	@$(MAKECOOKIE)
