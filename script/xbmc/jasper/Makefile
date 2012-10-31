GARNAME = jasper
GARVERSION = 1.900.1
CATEGORIES = lib
MASTER_SITES = http://www.ece.uvic.ca/~mdadams/jasper/software/
DISTFILES = $(DISTNAME).zip
LICENSE = LGPL2

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
