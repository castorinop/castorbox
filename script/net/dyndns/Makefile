GARNAME = inadyn
GARVERSION = 1.96.2
CATEGORIES = net
MASTER_SITES = http://cdn.dyndns.com/
DISTNAME= $(GARNAME)
DISTFILES = $(DISTNAME).zip
PATCHFILES = $(DISTNAME).patch.gar
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

BUILD_SCRIPTS     = $(WORKSRC)/makefile
INSTALL_SCRIPTS   = custom

BUILD_ARGS = CC=$(CC)

include ../../gar.mk

install-custom:
	@cp $(WORKSRC)/bin/linux/inadyn $(DESTDIR)$(bindir)
	$(MAKECOOKIE)

