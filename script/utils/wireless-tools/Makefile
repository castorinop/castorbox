GARNAME = wireless_tools
GARVERSION = 29
CATEGORIES = utils
MASTER_SITES = http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/
DISTFILES = $(GARNAME).$(GARVERSION).tar.gz
LICENSE = LGPL2

DESCRIPTION = 
define BLURB
endef

LIBDEPS = lang/c

WORKSRC = $(WORKDIR)/$(GARNAME).$(GARVERSION)

BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile


BUILD_ARGS   = \
	CC="$(CC)" \
	AR="$(AR)" \
	RANLIB="$(RANLIB)" \
	CFLAGS="$(CFLAGS)" \
	LDFLAGS="$(LDFLAGS)" \
	DESTDIR="$(DESTDIR)" \
	prefix="$(prefix)" \
	bindir="$(bindir)" \
	libdir="$(libdir)" \
	includedir="$(includedir)" \
	mandir="$(mandir)"

INSTALL_ARGS = \
	CC="$(CC)" \
	AR="$(AR)" \
	RANLIB="$(RANLIB)" \
	CFLAGS="$(CFLAGS)" \
	LDFLAGS="$(LDFLAGS)" \
	DESTDIR="$(DESTDIR)" \
	prefix="$(prefix)" \
	bindir="$(bindir)" \
	libdir="$(libdir)" \
	includedir="$(includedir)" \
	mandir="$(mandir)" \
	PREFIX="$(DESTDIR)$(prefix)"

include ../../gar.mk

