GARNAME = unionfs-utils
GARVERSION = 0.2.1
CATEGORIES = utils
MASTER_SITES = http://download.filesystems.org/unionfs/unionfs-utils-0.x/
DISTFILES = $(subst -,_,$(GARNAME))-$(GARVERSION).tar.gz
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c

WORKSRC = $(WORKDIR)/$(subst -,_,$(GARNAME))-$(GARVERSION)

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)
