GARNAME = gst-ffmpeg
GARVERSION = 0.10.4
CATEGORIES = lib
MASTER_SITES = http://gstreamer.freedesktop.org/src/gst-ffmpeg/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/ffmpeg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-cross-compile \
	--with-system-ffmpeg \
	--with-gnu-ld 

include ../../gar.mk

old-post-install:
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
	@sed -i 's%-L$${libdir}%-L$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/gstreamer-plugins-base-0.10.pc
	@sed -i 's%-I$${includedir}%-I$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/gstreamer-plugins-base-0.10.pc
	@sed -i 's%-L$${libdir}%-L$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/gstreamer-{audio,base,cdda,fft,floatcast,netbuffer,pbutils,riff,rtp,rtsp,sdp,tag,video}-0.10.pc
	@sed -i 's%-I$${includedir}%-I$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/gstreamer-{audio,base,cdda,fft,floatcast,netbuffer,pbutils,riff,rtp,rtsp,sdp,tag,video}-0.10.pc
