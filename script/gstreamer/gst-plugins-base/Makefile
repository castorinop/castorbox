GARNAME = gst-plugins-base
GARVERSION = 0.10.29
CATEGORIES = lib
MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-plugins-base/
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
	--cache-file=config.cache \
	--disable-dependency-tracking \
	--disable-nls \
	--disable-examples \
	--enable-experimental \
	--enable-adder \
	--enable-audioconvert \
	--enable-audiorate \
	--enable-audioresample \
	--enable-audiotestsrc \
	--disable-ffmpegcolorspace \
	--enable-gdp \
	--enable-playback \
	--enable-subparse \
	--enable-tcp \
	--enable-typefind \
	--disable-videotestsrc \
	--disable-videorate \
	--disable-videoscale \
	--disable-x \
	--disable-xvideo \
	--disable-xshm \
	--disable-gst_v4l \
	--enable-alsa \
	--enable-cdparanoia \
	--disable-gnome_vfs \
  	--disable-gio \
	--disable-libvisual \
	--enable-ogg \
	--disable-oggtest \
	--disable-pango \
	--enable-theora \
	--enable-vorbis \
	--disable-vorbistest \
	--disable-freetypetest \
	--with-gnu-ld 

INSTALL_ARGS = GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

include ../../gar.mk

pre-configure:
	@rm -f $(WORKSRC)/config.cache;
	@for i in lt_cv_dlopen_self=yes lt_cv_dlopen_self_static=yes; do \
		echo "$$i" >> $(WORKSRC)/config.cache; \
	done
	@$(MAKECOOKIE)

post-install:
	@rm -fv $(DESTDIR)$(libdir)/libgstaudio-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgstcdda-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgsttag-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgstriff-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgstvideo-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgstnetbuffer-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgstinterfaces-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstdecodebin2.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstffmpegcolorspace.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstalsa.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstcdparanoia.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstplaybin.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstgdp.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstsubparse.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstdecodebin.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstogg.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstximagesink.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgsttcp.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgsttypefindfunctions.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgsttheora.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstvideotestsrc.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstvorbis.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstaudiotestsrc.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstadder.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstvideo4linux.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstxvimagesink.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstvideorate.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstvideoscale.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstvolume.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstaudioresample.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstaudioconvert.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstaudiorate.la
	@rm -fv $(DESTDIR)$(libdir)/libgstrtp-0.10.la
	@$(MAKECOOKIE)
