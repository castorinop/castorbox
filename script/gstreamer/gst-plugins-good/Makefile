GARNAME = gst-plugins-good
GARVERSION = 0.10.23
CATEGORIES = lib
MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-good/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/flac lib/taglib lib/libshout gstreamer/gst-plugins-base

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-examples \
	--enable-external \
	--enable-experimental \
	--disable-schemas-install \
	--disable-gconftool \
	--disable-videofilter \
	--disable-alpha \
	--enable-apetag \
	--disable-audiofx \
	--disable-auparse \
	--enable-autodetect \
	--disable-avi \
	--disable-cutter \
	--disable-debug \
	--disable-effectv \
	--enable-equalizer \
	--enable-id3demux \
	--enable-icydemux\
	--disable-flx \
	--disable-goom \
	--disable-goom2k1 \
	--disable-law \
	--enable-level \
	--disable-matroska \
	--disable-monoscope \
	--disable-multifile \
	--disable-multipart \
	--disable-qtdemux \
	--enable-replaygain \
	--enable-rtp \
	--enable-rtsp \
	--disable-smpte \
	--disable-spectrum \
	--enable-udp \
	--disable-videobox \
	--disable-videocrop \
	--disable-videomixer \
	--enable-wavenc \
	--enable-wavparse \
	--disable-directdraw \
	--disable-directsound \
	--disable-oss \
	--disable-sunaudio \
	--disable-osx_audio \
	--disable-osx_video \
	--disable-gst_v4l2 \
	--disable-x \
	--disable-xshm \
	--disable-xvideo \
	--disable-aalib \
	--disable-aalibtest \
	--disable-annodex \
	--disable-cairo \
	--disable-cdio \
	--disable-esd \
	--disable-esdtest \
	--enable-flac \
	--disable-gconf \
	--disable-gdk_pixbuf \
	--disable-hal \
	--disable-jpeg \
	--disable-libcaca \
	--disable-libdv \
	--disable-libpng \
	--enable-pulse \
	--disable-dv1394 \
	--enable-shout2 \
	--disable-shout2test \
	--disable-soup \
	--disable-speex \
	--enable-taglib \
	--enable-wavpack \
	--enable-zlib \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/*.la
	@$(MAKECOOKIE)
