GARNAME = hal-info
GARVERSION = 20080508
CATEGORIES = utils
MASTER_SITES = http://hal.freedesktop.org/releases/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/alsa-lib lib/bluez-libs lib/dbus lib/expat lib/libsndfile lib/libusb

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-video \
	--disable-killswitch-dell-wlan \
	--disable-killswitch-dell-bluetooth \
	--disable-killswitch-dell-wwan \
	--disable-killswitch-sony-bluetooth \
	--disable-killswitch-thinkpad-bluetooth \
	--disable-killswitch-ipw-wlan \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_ctl_bluetooth.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_pcm_bluetooth.la
	@rm -f $(DESTDIR)$(libdir)/bluetooth/plugins/audio.la
	@rm -f $(DESTDIR)$(libdir)/bluetooth/plugins/input.la
	@rm -f $(DESTDIR)$(libdir)/bluetooth/plugins/network.la
	@rm -f $(DESTDIR)$(libdir)/bluetooth/plugins/serial.la
	@$(MAKECOOKIE)
