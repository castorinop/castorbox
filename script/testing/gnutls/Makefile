GARNAME = gnutls
GARVERSION = 1.6.3
CATEGORIES = utils
MASTER_SITES = ftp://ftp.gnutls.org/pub/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c extras/libgcrypt extras/boost

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-rpath \
	--with-libgcrypt-prefix=$(DESTDIR)$(prefix) \
	--with-gnu-ld

# --with-libgcrypt-prefix

include ../../gar.mk

PARALLELMFLAGS := -j1
