GARNAME = diffutils
GARVERSION = 3.0
CATEGORIES = utils
MASTER_SITES = http://ftp.gnu.org/gnu/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL3

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-silent-rules \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@#$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)
