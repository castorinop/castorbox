GARNAME = Mesa
GARVERSION = 7.11-rc2
CATEGORIES = $(CATEGORY)
MASTER_SITES  = http://www.mesa3d.org/beta/
MASTER_SITES += ftp://ftp.freedesktop.org/pub/mesa/$(word 1,$(subst -, ,$(GARVERSION)))/
DISTFILES = MesaLib-$(GARVERSION).tar.bz2
PATCHFILES  = $(DISTNAME)-llvm_so.patch $(DISTNAME)-pkg_config.patch $(DISTNAME).patch.gar
PATCHFILES += $(DISTNAME)-version.patch
ifneq ($(DESTIMG),build)
PATCHFILES += $(DISTNAME)-cross.patch
endif
LICENSE = LGPL2/MIT

DESCRIPTION = 
define BLURB
endef

DEPENDS    = lang/c lang/cxx devel/llvm lib/expat \
	$(CATEGORY)/dri2proto \
	$(CATEGORY)/xextproto \
	$(CATEGORY)/glproto \
	$(CATEGORY)/libdrm \
	$(CATEGORY)/libX11 \
	$(CATEGORY)/libxcb \
	$(CATEGORY)/libXdamage \
	$(CATEGORY)/libXext \
	$(CATEGORY)/libXfixes \
	$(CATEGORY)/libXi \
	$(CATEGORY)/libXmu \
	$(CATEGORY)/libXxf86vm \
	$(CATEGORY)/libXt
ifneq ($(DESTIMG),build)
DEPENDS   += system/udev
endif
BUILDDEPS  = lib/libxml2 python/python \
	$(CATEGORY)/makedepend
ifneq ($(DESTIMG),build)
BUILDDEPS += $(CATEGORY)/Mesa
endif

PWD := $(shell pwd)
CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

CONFIGURE_SCRIPTS  = $(WORKSRC)/configure
BUILD_SCRIPTS      = $(WORKSRC)/Makefile
INSTALL_SCRIPTS    = $(WORKSRC)/Makefile source
ifeq ($(DESTIMG),build)
INSTALL_SCRIPTS   += cross
endif

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(includedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--disable-static \
	--enable-shared \
	--disable-texture-float \
	--disable-selinux \
	--enable-opengl \
	--disable-gles1 \
	--disable-gles2 \
	--disable-openvg \
	--disable-xorg \
	--disable-d3d1x \
	--disable-egl \
	--disable-gbm \
	--disable-gallium-egl \
	--disable-gallium-gbm \
	--disable-shared-glapi \
	--enable-xcb \
	--enable-shared-dricore \
	--disable-egl \
	--enable-gallium-llvm \
	--with-gallium-drivers="i915,i965,nouveau,r300,r600,svga,swrast" \
	--with-driver="dri" \
	--with-x \
	--with-dri-driverdir="$(libdir)/xorg/modules/dri" \
	--with-dri-drivers="$(DRI_DIRS)" \
	--with-state-trackers="dri,glx"

BUILD_ARGS  = \
	HOST_CC="$(build_CC)" \
	HOST_CFLAGS="$(build_CFLAGS)"

include ../../gar.mk

# Mesa 7.10.2 fails to compile when compiling with GCC's link time optimization plugin.
CFLAGS   := $(filter-out -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -fuse-linker-plugin, $(LDFLAGS))

# Mesa 7.10.2 has incorrect symbol visibility when using the GCC's link time optimization.
# Could be <http://gcc.gnu.org/ml/gcc-patches/2010-07/msg00580.html>.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))

# Mesa 7.10.2 nouveau-dri fails when compiled with at least some of GCC 4.5.2's graphite support.
CFLAGS   := $(filter-out -ftree-loop-distribution -floop-interchange -floop-strip-mine -floop-block -fgraphite-identity, $(CFLAGS))
CXXFLAGS := $(filter-out -ftree-loop-distribution -floop-interchange -floop-strip-mine -floop-block -fgraphite-identity, $(CXXFLAGS))

DRI_DIRS := $(strip \
	$(if $(filter i386  ,$(GARCH_FAMILY)),i810 i915 i965 nouveau r200 r300 r600 radeon savage sis swrast unichrome) \
	$(if $(filter x86_64,$(GARCH_FAMILY)),     i915 i965 nouveau r200 r300 r600 radeon savage sis swrast unichrome))
DRI_DIRS := `echo "$(DRI_DIRS)" | sed -e 's% %,%g'`

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(MAKECOOKIE)

install-source:
	@mkdir -p $(DESTDIR)$(sourcedir)
	@rm -f $(DESTDIR)$(sourcedir)/Mesa
	@ln -sf $(PWD)/$(WORKSRC) $(DESTDIR)$(sourcedir)/Mesa
	@$(MAKECOOKIE)

install-cross:
	@mkdir -p $(DESTDIR)$(bindir)
	@cp -f $(WORKSRC)/src/glsl/builtin_compiler $(DESTDIR)$(bindir)/mesa-builtin_compiler
	@$(MAKECOOKIE)
