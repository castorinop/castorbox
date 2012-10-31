GARNAME = wavpack
GARVERSION = 4.60.1
CATEGORIES = lib
MASTER_SITES = http://www.wavpack.com/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx lib/lzo 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 


include ../../gar.mk

# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
#CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
#CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
#LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL_LIBPATH,$(WORKSRC),configure)
	@$(MAKECOOKIE)

