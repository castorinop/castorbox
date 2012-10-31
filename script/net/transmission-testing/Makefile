GARNAME = transmission
GARVERSION = 2.33
CATEGORIES = net
MASTER_SITES = http://download.transmissionbt.com/files/
DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES += $(DISTNAME)-metainfo_title.002.patch
#PATCHFILES += $(DISTNAME)_changeset3827.patch
#PATCHFILES += $(DISTNAME)_changeset3837.patch
LICENSE = transmission
transmission_LICENSE_TEXT = $(WORKSRC)/LICENSE

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/openssl lib/libproxy

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-gtk \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@mv $(DESTDIR)$(bindir)/transmissioncli $(DESTDIR)$(bindir)/transmission-cli
	@$(MAKECOOKIE)
