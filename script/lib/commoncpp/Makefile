GARNAME = commoncpp2
GARVERSION = 1.8.0
CATEGORIES = lib
MASTER_SITES = http://ftp.gnu.org/pub/gnu/commoncpp/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-missing_stat.patch
LICENSE = GPL2
DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libxml2

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST)

include ../../gar.mk

#PARALLELMFLAGS := -j1

post-install:
	@rm -f $(DESTDIR)$(libdir)/libccext2.la
	@rm -f $(DESTDIR)$(libdir)/libccgnu2.la
	@$(MAKECOOKIE)
