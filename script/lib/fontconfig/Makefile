GARNAME = fontconfig
GARVERSION = 2.8.0
CATEGORIES = lib
MASTER_SITES = http://www.fontconfig.org/release/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-build.patch
LICENSE = fontconfig
fontconfig_LICENSE_TEXT = $(WORKSRC)/COPYING

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/libxml2 lib/freetype
BUILDDEPS = lib/freetype

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-silent-rules \
	--enable-shared \
	--disable-static \
	--enable-libxml2 \
	--disable-docs \
	--with-gnu-ld \
	--with-arch=$(GARCH) \
	--with-add-fonts=no

DEFAULT_ENV   = \
	CPP_FOR_BUILD="$(build_CPP)" \
	CC_FOR_BUILD="$(build_CC)" \
	CXX_FOR_BUILD="$(build_CXX)" \
	AR_FOR_BUILD="$(build_AR)" \
	AS_FOR_BUILD="$(build_AS)" \
	CPPFLAGS_FOR_BUILD="$(build_CPPFLAGS)" \
	CFLAGS_FOR_BUILD="$(build_CFLAGS)" \
	CXXFLAGS_FOR_BUILD="$(build_CXXFLAGS)" \
	LDFLAGS_FOR_BUILD="$(build_LDFLAGS)"
CONFIGURE_ENV = $(DEFAULT_ENV) ac_cv_prog_HASDOCBOOK='no'
BUILD_ENV     = $(DEFAULT_ENV)
INSTALL_ENV   = $(DEFAULT_ENV)

include ../../gar.mk

# Fails to compile (x86_64) with GCC's O3 optimization, so convert it to O2 optimization.
CFLAGS   := $(if $(filter -O3, $(CFLAGS)), $(filter-out -O3, $(CFLAGS)) -O2)
CXXFLAGS := $(if $(filter -O3, $(CXXFLAGS)), $(filter-out -O3, $(CXXFLAGS)) -O2)

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

pre-install:
	@rm -rf $(DESTDIR)$(sysconfdir)/fonts
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libfontconfig.la
	@sed -i 's%-L$(DESTDIR)$(libdir)%-L$${libdir}%g' $(DESTDIR)$(libdir)/pkgconfig/fontconfig.pc
	@$(MAKECOOKIE)
