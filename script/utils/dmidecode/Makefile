GARNAME = dmidecode
GARVERSION =  2.8
CATEGORIES = utils
MASTER_SITES = http://download.savannah.gnu.org/releases/dmidecode/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS = \
	CC="$(CC)" \
	CFLAGS="$(CFLAGS)" \
	DESTDIR="$(DESTDIR)" \
	prefix="$(prefix)" \
	sbindir="$(sbindir)" \
	mandir="$(mandir)" \
	docdir="$(docdir)/dmidecode"
INSTALL_ARGS = \
	CC="$(CC)" \
	CFLAGS="$(CFLAGS)" \
	DESTDIR="$(DESTDIR)" \
	prefix="$(prefix)" \
	sbindir="$(sbindir)" \
	mandir="$(mandir)" \
	docdir="$(docdir)/dmidecode"

include ../../gar.mk

