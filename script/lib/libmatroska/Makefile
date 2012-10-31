GARNAME = libmatroska
GARVERSION = 0.8.1
CATEGORIES = lib
MASTER_SITES = http://dl.matroska.org/downloads/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/cxx lib/libebml

BUILD_SCRIPTS     = $(WORKSRC)/make/linux/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/make/linux/Makefile

BUILD_ARGS   = \
	CXX="$(CXX)" \
	LD="$(CXX)" \
	AR="$(AR) rcvu" \
	RANLIB="$(RANLIB)" \
	prefix="$(prefix)" \
	libdir="$(libdir)" \
	includedir="$(includedir)/matroska" \
	sharedlib
INSTALL_ARGS = \
	CXX="$(CXX)" \
	LD="$(CXX)" \
	AR="$(AR) rcvu" \
	RANLIB="$(RANLIB)" \
	prefix="$(DESTDIR)$(prefix)" \
	libdir="$(DESTDIR)$(libdir)" \
	includedir="$(DESTDIR)$(includedir)/matroska"

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/$(GARNAME).a
	@$(MAKECOOKIE)
