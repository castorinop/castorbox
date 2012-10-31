GARNAME = yajl
GARVERSION = 2.0.2
CATEGORIES = lib
MASTER_SITES = http://github.com/downloads/lloyd/yajl/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = LGPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = $(WORKSRC)/build/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/build/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 

BUILD_ARGS = VERBOSE=1

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
