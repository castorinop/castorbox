GARNAME = vbetool
GARVERSION = 0.7
CATEGORIES = utils
MASTER_SITES = http://www.srcf.ucam.org/~mjg59/vbetool/
DISTFILES = $(GARNAME)_$(GARVERSION)-1.tar.gz
LICENSE = GPL2

define BLURB
endef

DEPENDS = lang/c utils/pciutils

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = CFLAGS="$(CFLAGS) -I $(DESTDIR)$(includedir)" DESTDIR="$(DESTDIR)" $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld

include ../../gar.mk
