GARNAME = wxWidgets
GARVERSION = 2.9.3
CATEGORIES = lib
MASTER_SITES =  http://downloads.sourceforge.net/sourceforge/wxwindows/
DISTFILES = $(DISTNAME).tar.bz2
#LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c


CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=cache-config \
	--disable-gui \
	--disable-precomp-headers \
	--without-subdirs \
	--enable-unicode \
	--enable-largefile \
	--disable-optimize \
	--with-gnu-ld

include ../../gar.mk

#PARAMSMFLAGS := -j1
# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))

pre-configure:
	@echo "ac_cv_sys_largefile_source=yes" >> $(WORKSRC)/cache-config

post-install:
	@rm -f $(DESTDIR)$(bindir)/wx-config
	@cp -f $(WORKSRC)/lib/wx/config/$(mm_GARHOST)-base-unicode-2.9 $(DESTDIR)$(bindir)/wx-config
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(bindir)/wx-config
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(bindir)/wx-config
	@$(MAKECOOKIE)
