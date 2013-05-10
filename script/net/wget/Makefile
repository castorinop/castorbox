GARNAME = wget
GARVERSION = 1.11.4
CATEGORIES = net
MASTER_SITES = ftp://ftp.gnu.org/gnu/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-libproxy.patch
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c 
LIBDEPS = lib/openssl

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile


CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-libssl-prefix=$(DESTDIR)$(prefix) \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@cd $(WORKSRC); autoreconf --force --install --verbose
	@$(MAKECOOKIE)

