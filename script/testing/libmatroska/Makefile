GARNAME = libmatroska
GARVERSION = 0.8.1
CATEGORIES = lib
MASTER_SITES = http://dl.matroska.org/downloads/libmatroska/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx testing/libebml

BUILD_SCRIPTS     = $(WORKSRC)/make/linux/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/make/linux/Makefile

BUILD_ARGS = CXX="$(CXX)" AR="$(AR) rcvu" 
INSTALL_ARGS = prefix="$(DESTDIR)$(prefix)" 

include ../../gar.mk


