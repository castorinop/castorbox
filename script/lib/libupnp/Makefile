GARNAME = libupnp
GARVERSION = 1.6.6
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/pupnp/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL

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

# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))


post-install:
	@rm -rf $(DESTDIR)$(libdir)/libupnp.la
	@$(MAKECOOKIE)

