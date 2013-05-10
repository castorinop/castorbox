GARNAME = libssh
GARVERSION = 0.5.3
CATEGORIES = lib
MASTER_SITES = http://www.libssh.org/files/0.5/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = LGPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

WORKBLD = $(WORKSRC)_build
CONFIGURE_SCRIPTS = $(WORKBLD)/cmake
BUILD_SCRIPTS     = $(WORKBLD)/Makefile
INSTALL_SCRIPTS   = $(WORKBLD)/Makefile

CONFIGURE_ARGS = \
	-DCMAKE_INSTALL_PREFIX="$(prefix)" \
	-DCMAKE_FIND_ROOT_PATH="$(DESTDIR)$(prefix)" \
	-DCMAKE_VERBOSE_MAKEFILE="1" 

include ../../gar.mk


# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))


configure-%/cmake: 
	@echo " ==> Running configure in $*"
	mkdir -p $(WORKBLD)
	cd $* && $(CONFIGURE_ENV) cmake ../$(DISTNAME) $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

