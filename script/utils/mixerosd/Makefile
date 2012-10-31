GARNAME = mixerosd
GARVERSION = 0.02
CATEGORIES = utils
MASTER_SITES = http://www.csps.com.ar/castorbox/garchive/$(DISTNAME)/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c X11/xosd lib/alsa-lib system/lirc

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS   = \
	CC="$(CC)" \
	AR="$(AR)" \
	RANLIB="$(RANLIB)" \
	CFLAGS="$(CFLAGS)" \
	DESTDIR="$(DESTDIR)" \
	PREFIX="$(DESTDIR)$(prefix)" \
	BINDIR="$(DESTDIR)$(bindir)" \
	LIBDIR="$(DESTDIR)$(libdir)" \
	INCLUDEDIR="$(DESTDIR)$(includedir)" \
	MANDIR="$(DESTDIR)$(mandir)"
INSTALL_ARGS = \
	CC="$(CC)" \
	AR="$(AR)" \
	RANLIB="$(RANLIB)" \
	CFLAGS="$(CFLAGS)" \
	DESTDIR="$(DESTDIR)" \
	ETCDIR="$(DESTDIR)$(sysconfdir)" \
	PREFIX="$(DESTDIR)$(prefix)" \
	BINDIR="$(DESTDIR)$(bindir)" \
	LIBDIR="$(DESTDIR)$(libdir)" \
	INCLUDEDIR="$(DESTDIR)$(includedir)" \
	MANDIR="$(DESTDIR)$(mandir)"

include ../../gar.mk

