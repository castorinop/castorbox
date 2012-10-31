GARNAME = alsa-plugins
GARVERSION = 1.0.23
CATEGORIES = testing
MASTER_SITES = ftp://ftp.alsa-project.org/pub/plugins/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c system/pulse

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-static \
	--enable-shared \
  	--disable-jack \
	--enable-pulseaudio

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_conf_pulse.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_ctl_arcam_av.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_ctl_oss.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_ctl_pulse.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_pcm_oss.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_pcm_pulse.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_pcm_speex.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_pcm_upmix.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_pcm_usb_stream.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_pcm_vdownmix.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_rate_samplerate.la
	@rm -f $(DESTDIR)$(libdir)/alsa-lib/libasound_module_rate_speexrate.la
	@$(MAKECOOKIE)
