GARNAME = xml-HTB
GARVERSION = 1.3
CATEGORIES = utils
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/xml-htb/
DISTFILES = $(DISTNAME).tar.bz2 
PATCHFILES = $(DISTNAME)-fix_xml2_config.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libxml2

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache

BUILD_ARGS = CC="$(CC)" CFLAGS="$(CFLAGS)"

INSTALL_ARGS = INSTALLBIN="$(DESTDIR)$(ebindir)" INSTALLETC="$(DESTDIR)$(sysconfdir)/xml-HTB"

include ../../gar.mk

PARALLELMFLAGS := -j1
