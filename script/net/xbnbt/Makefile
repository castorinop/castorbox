GARNAME = xbnbt
GARVERSION = 81b.3.5
CATEGORIES = net
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).zip
PATCHFILES = $(DISTNAME).patch.gar $(DISTNAME)-gcc_4.4.0.patch $(DISTNAME)-missing_stat.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx lib/zlib

WORKSRC = $(WORKDIR)/$(DISTNAME)/bnbt/src

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

BUILD_ARGS = bnbt

include ../../gar.mk

post-extract:
	mv $(WORKDIR)/Copy* $(WORKDIR)/$(DISTNAME)
	@$(MAKECOOKIE)

install-custom:
	cp $(WORKSRC)/bnbt $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)

