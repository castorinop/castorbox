GARNAME = libsigc++
GARVERSION = 2.2.3
CATEGORIES = lib
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(GARNAME)/2.2/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld

include ../../gar.mk

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libsigcxx-2.0.la
	@$(MAKECOOKIE)
