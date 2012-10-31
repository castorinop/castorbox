GARNAME = oftpd
GARVERSION = 0.3.7
CATEGORIES = net
MASTER_SITES = http://www.time-travellers.org/oftpd/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES += $(DISTNAME)-metainfo_title.002.patch
#PATCHFILES += $(DISTNAME)_changeset3827.patch
#PATCHFILES += $(DISTNAME)_changeset3837.patch

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/openssl

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@mv $(DESTDIR)$(bindir)/transmissioncli $(DESTDIR)$(bindir)/transmission-cli
	@$(MAKECOOKIE)
