GARNAME = vdpau-video
GARVERSION = 0.7.3
CATEGORIES = X11
MASTER_SITES = http://www.splitted-desktop.com/~gbeauchesne/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-remove_sds_checks.patch $(DISTNAME)-utils_glx_h.patch $(DISTNAME)-install.patch
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c X11/libva X11/libvdpau xorg/xorg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-glx \
	--disable-debug \
	--disable-tracer \
	--disable-static \
	--enable-shared \
	--with-gnu-ld

include ../../gar.mk

CPPFLAGS += -DVA_SDS_VERSION=1

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/va/vdpau_drv_video.la
	@$(MAKECOOKIE)
