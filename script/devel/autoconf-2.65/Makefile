GARNAME = autoconf
GARVERSION = 2.65
CATEGORIES = devel
MASTER_SITES = http://ftp.gnu.org/gnu/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-dash.patch $(DISTNAME)-bash.patch.gar
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c perl/perl utils/bash

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--program-suffix="-$(GARVERSION)"
BUILD_ARGS     = \
	pkgdatadir=$(datadir)/autoconf-$(GARVERSION)
	pkglibdir=$(libdir)/autoconf-$(GARVERSION)
	pkgincludedir=$(includedir)/autoconf-$(GARVERSION)
INSTALL_ARGS   = \
	pkgdatadir=$(datadir)/autoconf-$(GARVERSION)
	pkglibdir=$(libdir)/autoconf-$(GARVERSION)
	pkgincludedir=$(includedir)/autoconf-$(GARVERSION)

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(MAKECOOKIE)
