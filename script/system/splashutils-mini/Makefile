GARNAME = splashutils
GARVERSION = 1.5.4.4
CATEGORIES = system
MASTER_SITES = http://download.berlios.de/fbsplash/
DISTFILES = $(GARNAME)-lite-$(GARVERSION).tar.bz2
##PATCHFILES += $(DISTNAME)-autotools_fixes.patch $(DISTNAME)-daemon_opts.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libjpeg-static

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-debug \
	--disable-shared \
	--enable-static \
	--disable-deprecated \
	--disable-fbcondecor \
	--disable-helper \
	--disable-misc \
	--without-gpm \
	--without-mng \
	--without-png \
	--without-ttf \
	--without-ttf-kernel \
	--with-essential-prefix="$(if $(rootdir),$(rootdir),/)" \
	--with-essential-bindir="$(ebindir)" \
	--with-essential-sbindir="$(esbindir)" \
	--with-essential-libdir="/fs/root" \
	--with-themedir="$(sysconfdir)/splash"

BUILD_ENV = \
	QUIET=false

CFLAGS := 

include ../../gar.mk

pre-configure:
	 @$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC),configure)
	@$(MAKECOOKIE)

install-custom:
	install -m 755 $(WORKSRC)/src/fbsplashctl $(DESTDIR)$(esbindir)/fbsplashctl-mini
	@$(MAKECOOKIE)
