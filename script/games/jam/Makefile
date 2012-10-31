GARNAME = jam
GARVERSION = 2.5
CATEGORIES = games
MASTER_SITES = ftp://ftp.perforce.com/pub/jam/
DISTFILES = $(DISTNAME).tar
PATCHFILES = $(GARNAME)-debian-fixes.patch $(GARNAME)-optflags.patch 
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/c 

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

BUILD_ARGS   = \
	CC="$(CC)" \
	AR="$(AR)" \
	RANLIB="$(RANLIB)" \
	CFLAGS="" \
	LDFLAGS="$(LDFLAGS)" \
	DESTDIR="$(DESTDIR)" \
	prefix="$(prefix)" \
	bindir="$(bindir)" \
	libdir="$(libdir)" \
	includedir="$(includedir)" \
	mandir="$(mandir)"

include ../../gar.mk

install-custom:
	@cp -f $(WORKSRC)/bin.linux*/jam $(DESTDIR)$(bindir)/
	@$(MAKECOOKIE)
