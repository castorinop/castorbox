GARNAME = libebml
GARVERSION = 0.7.8
CATEGORIES = lib
MASTER_SITES = http://dl.matroska.org/downloads/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/cxx

BUILD_SCRIPTS     = $(WORKSRC)/make/linux/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/make/linux/Makefile

BUILD_ARGS   = \
	CXX="$(CXX)" \
	LD="$(CXX)" \
	AR="$(AR) rcvu" \
	RANLIB="$(RANLIB)" \
	prefix="$(prefix)" \
	libdir="$(libdir)" \
	includedir="$(includedir)/ebml"
INSTALL_ARGS = \
	CXX="$(CXX)" \
	LD="$(CXX)" \
	AR="$(AR) rcvu" \
	RANLIB="$(RANLIB)" \
	prefix="$(DESTDIR)$(prefix)" \
	libdir="$(DESTDIR)$(libdir)" \
	includedir="$(DESTDIR)$(includedir)/ebml"

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/$(GARNAME).a
	@$(MAKECOOKIE)
