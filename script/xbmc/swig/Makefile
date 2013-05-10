GARNAME = swig
GARVERSION = 2.0.9
CATEGORIES = lib
MASTER_SITES = http://prdownloads.sourceforge.net/swig/
DISTFILES = $(DISTNAME).tar.gz
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

http//%: 
	@cd $(PARTIALDIR) ; wget --no-check-certificate -c https://$*

configure-custom:
	mkdir -p  $(WORKSRC)/build
	cd $(WORKSRC)/build; cmake \
		-DCMAKE_INSTALL_PREFIX='$(prefix)' \
		-DCMAKE_C_COMPILER='$(CC)' \
		-DCMAKE_C_FLAGS='$(CFLAGS)' \
		..
	$(MAKECOOKIE)
