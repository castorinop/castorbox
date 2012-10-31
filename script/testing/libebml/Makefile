GARNAME = libebml
GARVERSION = 0.7.8
CATEGORIES = lib
MASTER_SITES = http://dl.matroska.org/downloads/libebml/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx 

BUILD_SCRIPTS     = $(WORKSRC)/make/linux/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/make/linux/Makefile

BUILD_ARGS = CXX="$(CXX)" AR="$(AR) rcvu" 
INSTALL_ARGS = prefix="$(DESTDIR)$(prefix)" 


include ../../gar.mk

