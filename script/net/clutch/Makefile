GARNAME = Clutch
GARVERSION = 0.4
CATEGORIES = net
MASTER_SITES = http://clutchbt.com/Files/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES += $(DISTNAME)_configfix.patch
#PATCHFILES += $(DISTNAME)_changeset3827.patch
#PATCHFILES += $(DISTNAME)_changeset3837.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/php

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--without-gtk \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@mv $(DESTDIR)$(bindir)/transmissioncli $(DESTDIR)$(bindir)/transmission-cli
	@$(MAKECOOKIE)
