GARNAME = zsnes
GARVERSION = 1.51
CATEGORIES = emulators
MASTER_SITES = http://downloads.sourceforge.net/project/$(GARNAME)/$(GARNAME)/ZSNES%20v$(GARVERSION)/
DISTFILES = $(GARNAME)$(subst .,,$(GARVERSION))src.tar.bz2
PATCHFILES = $(DISTNAME)-gcc_4.3.patch $(DISTNAME).patch
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lang/cxx lib/libpng lib/SDL lib/zlib xorg/xorg
BUILDDEPS = devel/nasm

WORKSRC = $(WORKDIR)/$(GARNAME)_$(subst .,_,$(GARVERSION))/src

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--disable-sdltest \
	--enable-libpng  \
	--disable-debugger \
	--enable-opengl  \
	--enable-jma \
	--disable-cpucheck \
	$(if $(filter yes,$(mm_DEBUG)),--enable-debug,--disable-debug) \
	$(if $(filter no,$(mm_DEBUG)),--enable-release,--disable-release) \
	--with-x

CONFIGURE_ENV = \
	force_arch="$(GARCH)" \
	CC_FOR_BUILD="$(build_CC)" \
	CXX_FOR_BUILD="$(build_CXX)" \
	CPPFLAGS_FOR_BUILD="$(build_CPPFLAGS)" \
	CFLAGS_FOR_BUILD="$(build_CFLAGS)" \
	CXXFLAGS_FOR_BUILD="$(build_CXXFLAGS)" \
	LDFLAGS_FOR_BUILD="$(build_LDFLAGS)" \
	SDL_CONFIG=$(DESTDIR)$(prefix)/bin-config/sdl-config

include ../../gar.mk

# Fails to compile with GCC 4.5.2's link time optimization linker plugin enabled.
CFLAGS   := $(filter-out -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -fuse-linker-plugin, $(LDFLAGS))
build_CFLAGS   := $(filter-out -fuse-linker-plugin, $(build_CFLAGS))
build_CXXFLAGS := $(filter-out -fuse-linker-plugin, $(build_CXXFLAGS))
build_LDFLAGS  := $(filter-out -fuse-linker-plugin, $(build_LDFLAGS))

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(MAKECOOKIE)
