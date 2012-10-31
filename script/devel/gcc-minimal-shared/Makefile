GARNAME = gcc-minimal-shared
GARVERSION = $(GCC_VERSION)
CATEGORIES = devel
SOURCEPKG = devel/gcc
LICENSE = GPL2/LGPL2_1

DESCRIPTION = 
define BLURB
endef

CROSSIMG ?= $(DESTIMG)
GARTARGET = $($(CROSSIMG)_GARHOST)

IMGDEPS += $(CROSSIMG)
ifneq ("$(DESTIMG)+$(CROSSIMG)","build+build")
$(CROSSIMG)_DEPENDS = kernel-headers/linux-headers devel/glibc-crtobjs
DEPENDS  = lang/c devel/binutils
else
DEPENDS  =
endif
DEPENDS += devel/cloog-ppl devel/gmp devel/libelf devel/mpc devel/mpfr devel/ppl

WORKDIR   = $(WORKROOTDIR)/$(DESTIMG)_$(CROSSIMG).d
COOKIEDIR = $(COOKIEROOTDIR)/$(DESTIMG)_$(CROSSIMG).d

WORKSRC = $(WORKDIR)/gcc-$(GARVERSION)

WORKBLD = $(WORKSRC)_build

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = $(WORKBLD)/Makefile
INSTALL_SCRIPTS   = $(WORKBLD)/Makefile

CONFIGURE_ARGS  = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) --target=$(GARTARGET) \
	--with-gnu-as \
	--with-gnu-ld \
	--with-local-prefix=$(patsubst %/include,%,$($(CROSSIMG)_includedir)) \
	--enable-plugin \
	--enable-__cxa_atexit \
	--enable-clocale=gnu \
	--enable-languages=c \
	--disable-libgomp \
	--disable-libmudflap \
	--enable-gold=both/ld \
	--disable-libada \
	--disable-libssp \
	--disable-ppl-version-check \
	--enable-lto \
	--disable-multilib \
	--disable-nls \
	--disable-decimal-float \
	--enable-shared \
	--enable-threads=no \
	--enable-version-specific-runtime-libs \
	--with-mpc-include=$(DESTDIR)$(includedir) \
	--with-mpc-lib=$(DESTDIR)$(libdir) \
	--with-mpfr-include=$(DESTDIR)$(includedir) \
	--with-mpfr-lib=$(DESTDIR)$(libdir) \
	--with-gmp-include=$(DESTDIR)$(includedir) \
	--with-gmp-lib=$(DESTDIR)$(libdir) \
	--with-ppl-include=$(DESTDIR)$(includedir) \
	--with-ppl-lib=$(DESTDIR)$(libdir) \
	--with-cloog-include=$(DESTDIR)$(includedir) \
	--with-cloog-lib=$(DESTDIR)$(libdir) \
	--with-libelf-include=$(DESTDIR)$(includedir) \
	--with-libelf-lib=$(DESTDIR)$(libdir) \
	--with-sysroot=$($(CROSSIMG)_DESTDIR)

GAR_EXTRA_CONF += devel/gcc/package-api.mk
include ../../gar.mk

CPPFLAGS :=
CFLAGS   :=
CXXFLAGS :=
LDFLAGS  :=

# Do not link to libc.so, because it is not available yet.
pre-configure:
	@sed -i '/^SHLIB_LC = /s%-lc%%' $(WORKSRC)/gcc/config/t-slibgcc-elf-ver
	@$(MAKECOOKIE)

configure-custom:
	@mkdir -p $(WORKBLD)
	@cd $(WORKBLD) && $(CONFIGURE_ENV) ./$(call DIRSTODOTS,$(WORKBLD))/$(WORKSRC)/configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)
