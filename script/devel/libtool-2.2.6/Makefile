GARNAME = libtool
GARVERSION = 2.2.6b
CATEGORIES = devel
MASTER_SITES = http://ftp.gnu.org/gnu/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--disable-static \
	--program-suffix="-$(GARVERSION)" \
	--with-gnu-ld

BUILD_ARGS     = \
	pkgdatadir=$(datadir)/$(GARNAME)-$(GARVERSION)
	pkglibdir=$(libdir)/$(GARNAME)-$(GARVERSION)
	pkgincludedir=$(includedir)/$(GARNAME)-$(GARVERSION)
INSTALL_ARGS   = \
	pkgdatadir=$(datadir)/$(GARNAME)-$(GARVERSION)
	pkglibdir=$(libdir)/$(GARNAME)-$(GARVERSION)
	pkgincludedir=$(includedir)/$(GARNAME)-$(GARVERSION)

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libltdl.la
	@$(MAKECOOKIE)
