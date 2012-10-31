GARNAME = miniupnpd
GARVERSION = 1.4.20100921
CATEGORIES = net
MASTER_SITES = http://miniupnp.free.fr/files/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = miniupnpc
miniupnpc_LICENSE_TEXT = $(WORKSRC)/LICENCE

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS = CC="$(CC)" CFLAGS="$(CFLAGS) -DNDEBUG" 
INSTALL_ARGS = PREFIX="$(DESTDIR)"

include ../../gar.mk

post-install:
	@cp $(WORKSRC)/upnpc-shared $(DESTDIR)$(bindir)/upnpc
	@$(MAKECOOKIE)

