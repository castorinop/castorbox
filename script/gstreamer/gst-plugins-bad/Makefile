GARNAME = gst-plugins-bad
GARVERSION = 0.10.19
CATEGORIES = lib
MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-bad/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c gstreamer/gstreamer-core

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-check=no \
	--disable-app \
	--disable-bayer \
	--disable-cdxaparse \
	--disable-deinterlace \
	--disable-dvdspu \
	--disable-festival \
	--disable-filter \
	--disable-flv \
	--disable-freeze \
	--disable-h264parse \
	--disable-interleave \
	--disable-librfb \
	--disable-modplug \
	--disable-mpegtsparse \
	--disable-mpeg4videoparse \
	--disable-mpegvideoparse \
	--disable-mve \
	--disable-nsf \
	--disable-nuvdemux \
	--disable-rawparse \
	--disable-real \
	--enable-replaygain \
	--disable-rtpmanager \
	--disable-sdp \
	--disable-selector \
	--disable-speed \
	--disable-speexresample \
	--disable-subenc \
	--disable-stereo \
	--disable-tta \
	--disable-videosignal \
	--disable-vmnc \
	--disable-y4m \
	--disable-quicktime \
	--disable-vcd \
	--disable-alsa \
	--disable-amrwb \
	--disable-bz2 \
	--disable-cdaudio \
	--disable-dc1394 \
	--disable-directfb \
	--disable-dirac \
	--disable-dts \
	--disable-divx \
	--disable-metadata \
	--disable-faac \
	--disable-faad \
	--disable-fbdev \
	--disable-gsm \
	--disable-ivorbis \
	--disable-jack \
	--disable-ladspa \
	--disable-libmms \
	--disable-mpeg2enc \
	--disable-mplex \
	--disable-musepack \
	--disable-musicbrainz \
	--disable-mythtv \
	--disable-nas \
	--disable-neon \
	--disable-ofa \
	--disable-timidity \
	--disable-wildmidi \
	--disable-sdl \
	--disable-sdltest \
	--disable-sndfile \
	--disable-soundtouch \
	--disable-spc \
	--disable-swfdec \
	--disable-theoradec \
	--disable-x264 \
	--disable-xvid \
	--disable-dvb \
	--disable-oss4 \
	--disable-wininet \
	--with-gnu-ld 

include ../../gar.mk

posta-install:
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/*.la
	@$(MAKECOOKIE)
	

