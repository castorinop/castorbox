GARNAME = xorg-server
GARVERSION = 1.13.2
CATEGORIES = $(CATEGORY)
MASTER_SITES = $(XORG_MASTER_SITES)
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = \
	$(DISTNAME)-perl.patch.gar \
	$(DISTNAME)-pkg_config.patch \
	$(DISTNAME)-detect_radeon.patch
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/COPYING

DESCRIPTION = 
define BLURB
endef

DEPENDS  = lang/c lib/openssl \
	$(CATEGORY)/bigreqsproto \
	$(CATEGORY)/damageproto \
	$(CATEGORY)/dri2proto \
	$(CATEGORY)/fixesproto \
	$(CATEGORY)/font-util \
	$(CATEGORY)/fontsproto \
	$(CATEGORY)/glproto \
	$(CATEGORY)/inputproto \
	$(CATEGORY)/kbproto \
	$(CATEGORY)/libdrm \
	$(CATEGORY)/libpciaccess \
	$(CATEGORY)/libX11 \
	$(CATEGORY)/libXau \
	$(CATEGORY)/libXfont \
	$(CATEGORY)/libxkbfile \
	$(CATEGORY)/Mesa \
	$(CATEGORY)/pixman \
	$(CATEGORY)/randrproto \
	$(CATEGORY)/recordproto \
	$(CATEGORY)/renderproto \
	$(CATEGORY)/resourceproto \
	$(CATEGORY)/scrnsaverproto \
	$(CATEGORY)/util-macros \
	$(CATEGORY)/videoproto \
	$(CATEGORY)/xcmiscproto \
	$(CATEGORY)/xextproto \
	$(CATEGORY)/xf86bigfontproto \
	$(CATEGORY)/xf86dgaproto \
	$(CATEGORY)/xf86driproto \
	$(CATEGORY)/xf86vidmodeproto \
	$(CATEGORY)/xineramaproto \
	$(CATEGORY)/xproto \
	$(CATEGORY)/xtrans
ifneq ($(DESTIMG),build)
DEPENDS += system/udev
endif
BUILDDEPS = \
	$(CATEGORY)/xorg-sgml-doctools

CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-strict-compilation \
	--disable-silent-rules \
	--disable-static \
	--enable-shared \
	--enable-largefile \
	--disable-debug \
	--disable-unit-tests \
	--disable-sparkle \
	--disable-install-libxf86config \
	--enable-visibility \
	--enable-pc98=auto \
	--enable-aiglx \
	--enable-registry \
	--disable-composite \
	--enable-mitshm \
	--disable-xres \
	--enable-record \
	--enable-xv \
	--enable-xvmc \
	--enable-dga \
	--enable-screensaver \
	--disable-xdmcp \
	--disable-xdm-auth-1 \
	--enable-glx \
	--enable-dri \
	--enable-dri2 \
	--enable-xinerama \
	--enable-xf86vidmode \
	--disable-xace \
	--disable-xselinux \
	--disable-xcsecurity \
	--disable-xcalibrate \
	--disable-tslib \
	--enable-dbe \
	--enable-xf86bigfont \
	--enable-dpms \
	$(if $(filter build, $(DESTIMG)), --disable-config-udev, --enable-config-udev) \
	$(if $(filter build, $(DESTIMG)), --disable-config-udev-kms, --enable-config-udev-kms) \
	--disable-config-dbus \
	--disable-config-hal \
	--enable-xfree86-utils \
	--enable-vgahw \
	--enable-vbe \
	--enable-int10-module \
	--disable-windowswm \
	--enable-libdrm \
	--enable-xorg \
	--disable-dmx \
	--disable-xvfb \
	--disable-xnest \
	--disable-xquartz \
	--disable-standalone-xpbproxy \
	--disable-xwin \
	--disable-kdrive \
	--disable-xephyr \
	--disable-xfake \
	--disable-xfbdev \
	--disable-install-setuid \
	--enable-unix-transport \
	--disable-tcp-transport \
	--disable-ipv6 \
	--disable-local-transport \
	--disable-secure-rpc \
	--disable-devel-docs \
	--with-gnu-ld \
	--with-default-font-path="$(datadir)/fonts/X11/TTF,$(datadir)/fonts/X11/misc" \
	--with-xkb-path="$(datadir)/X11/xkb" \
	--with-xkb-output="$(datadir)/X11/xkb/compiled" \
	--with-serverconfig-path="$(libdir)/xserver" \
	--without-xmlto \
	--without-fop \
	--with-sha1=libcrypto

CONFIGURE_ENV = \
	XORG_SGML_PATH="$(DESTDIR)$(includedir)/xorg"

GAR_EXTRA_CONF += $(CATEGORY)/xorg/package-api.mk
include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

# Workaround to a problem in xorg-server 1.10.0.
pre-build:
	@rm -f $(WORKSRC)/hw/xfree86/loader/sdksyms.c

post-install:
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/extensions/libdbe.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/extensions/libdri.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/extensions/libdri2.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/extensions/libextmod.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/extensions/libglx.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/extensions/librecord.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libexa.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libfb.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libfbdevhw.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libint10.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libshadow.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libshadowfb.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libvbe.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libvgahw.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/libwfb.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/multimedia/bt829_drv.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/multimedia/fi1236_drv.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/multimedia/msp3430_drv.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/multimedia/tda8425_drv.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/multimedia/tda9850_drv.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/multimedia/tda9885_drv.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/multimedia/uda1380_drv.la
	@$(MAKECOOKIE)
