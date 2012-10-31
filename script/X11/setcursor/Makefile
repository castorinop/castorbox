GARNAME = unclutter
GARVERSION = 8
CATEGORIES = X11
MASTER_SITES = http://ftp.debian.org/debian/pool/main/u/unclutter/
MASTER_SITES += ftp://export.lcs.mit.edu/contrib/utilities/
DISTFILES = $(DISTNAME).tar.Z
#PATCHFILES = $(GARNAME)_$(GARVERSION)-5.diff.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c xorg/xorg

WORKSRC = $(WORKDIR)/$(GARNAME)
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

BUILD_ARGS = \
	QUIET="true" \
	KLCC="$(CC)" \
	CC="$(CC)" \
	CFLAGS="$(CFLAGS)" \
	LDFLAGS="$(LDFLAGS)" \
	STRIP="$(STRIP)" \
	LIBDIR="$(DESTDIR)$(libdir)" \
	prefix="$(prefix)" \
	sbindir="$(esbindir)" \
	usrbindir="$(bindir)" \
	mandir="$(mandir)"

include ../../gar.mk

install-custom:
	install -c -c -s $(WORKSRC)/unclutter $(DESTDIR)$(bindir)
