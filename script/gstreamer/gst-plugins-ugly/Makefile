GARNAME = gst-plugins-ugly
GARVERSION = 0.10.15
CATEGORIES = lib
MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-ugly/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/alsa-lib lib/libogg lib/libvorbis lib/libtheora gstreamer/gstreamer-core lib/liboil

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-dependency-tracking \
	--disable-rpath \
	--disable-nls \
	--disable-examples \
	--enable-external \
	--enable-experimental \
	--enable-asfdemux \
	--disable-dvdlpcmdec \
	--disable-dvdsub \
	--disable-iec958 \
	--enable-mpegaudioparse \
	--enable-mpegstream \
	--enable-realmedia \
	--disable-synaesthesia \
	--enable-a52dec \
	--disable-amrnb \
	--disable-dvdread \
	--enable-dvdnav \
	--disable-lame \
	--enable-id3tag \
	--enable-mad \
	--disable-mpeg2dec \
	--disable-sidplay \
	--with-gnu-ld 

include ../../gar.mk

posta-install:
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/*.la
	@$(MAKECOOKIE)
	

