GARNAME = aMule
GARVERSION = 2.3.1
CATEGORIES = net
MASTER_SITES = http://download.sourceforge.net/sourceforge/amule/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-cross_compiling.patch \
	     $(DISTNAME)-handle_empty_statistics_file.patch \
	     $(DISTNAME)-gcc_4.7.patch

LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx lib/zlib lib/crypto++ lib/libupnp lib/wxWidgets

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-amule-daemon \
	--enable-amulecmd \
	--enable-webserver \
	--enable-upnp \
	--disable-monolithic \
	--with-libupnp-prefix=$(DESTDIR)$(prefix) \
	--with-zlib=$(DESTDIR)$(prefix) \
	--with-crypto-prefix=$(DESTDIR)$(prefix) \
	--with-wx-config=$(DESTDIR)$(bindir)/wx-config \
	--with-toolkit=base \
	--disable-debug \
	--with-gnu-ld 

include ../../gar.mk


# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))

