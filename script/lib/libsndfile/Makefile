GARNAME = libsndfile
GARVERSION = 1.0.25
CATEGORIES = lib
MASTER_SITES = http://www.mega-nerd.com/libsndfile/files/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-configure.patch
LICENSE = LGPL2_1

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lang/cxx lib/alsa-lib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-silent-rules \
	--enable-shared \
	--disable-static \
	--disable-experimental \
	--disable-sqlite \
	--enable-alsa \
	--disable-external-libs \
	--disable-test-coverage \
	--enable-largefile \
	--disable-shave \
	--with-gnu-ld

include ../../gar.mk

# Fails to compile with GCC 4.5.2's link time optimization linker plugin enabled.
# See <http://gcc.gnu.org/bugzilla/show_bug.cgi?id=45007>
CFLAGS   := $(filter-out -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -fuse-linker-plugin, $(LDFLAGS))

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libsndfile.la
	@$(MAKECOOKIE)
