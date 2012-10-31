GARNAME = libevent
GARVERSION = 1.4.13-stable
CATEGORIES = lib
MASTER_SITES = http://monkey.org/~provos/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = BSD

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
	@rm -rf $(DESTDIR)$(libdir)/libevent.la
	@$(MAKECOOKIE)
