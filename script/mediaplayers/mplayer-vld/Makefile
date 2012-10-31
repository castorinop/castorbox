GARNAME = MPlayer
GARVERSION = 1.0rc2
CATEGORIES = mediaplayers
MASTER_SITES  = http://www1.mplayerhq.hu/MPlayer/releases/
MASTER_SITES += http://www2.mplayerhq.hu/MPlayer/releases/
MASTER_SITES += http://www4.mplayerhq.hu/MPlayer/releases/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = \
	$(DISTNAME)-demux_audio_fix_20080129.patch \
	$(DISTNAME)-demux_mov_fix_20080129.patch \
	$(DISTNAME)-url_fix_20080120.patch \
	$(DISTNAME)-stream_cddb_fix_20080120.patch
PATCHFILES += $(DISTNAME)-gcc_4.4.0_hack.patch
PATCHFILES += $(DISTNAME)-liba52_external.patch
PATCHFILES += $(DISTNAME)-libdvdread_udf.patch
PATCHFILES += $(DISTNAME)-dvdnav.patch
PATCHFILES += $(DISTNAME)-openchrome.patch $(DISTNAME)-x11_headers.patch $(DISTNAME)-cross-$(GARCH_FAMILY).patch
LICENSE = mplayer
mplayer_LICENSE_TEXT = $(WORKSRC)/Copyright

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/a52dec lib/alsa-lib lib/faad2 lib/fontconfig lib/freetype lib/libcdio lib/libdca lib/libdvdnav lib/libjpeg lib/libmad lib/libpng lib/zlib system/lirc xorg/xorg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

# Directories
CONFIGURE_ARGS_DIR = \
	--prefix="$(prefix)" \
	--bindir="$(bindir)" \
	--datadir="$(datadir)/mplayer" \
	--mandir="$(mandir)" \
	--confdir="$(sysconfdir)/mplayer" \
	--libdir="$(libdir)" \
	--codecsdir="$(libdir)/codecs"
# Optional features
# --enable-fontconfig must be auto or cflags and libs will not be determined correctly.
# Support for external dvdread appears to be broken.
CONFIGURE_ARGS_OPTIONAL = \
	--disable-mencoder \
	--enable-mplayer \
	--disable-gui \
	--disable-gtk1 \
	--enable-largefiles \
	--disable-linux-devfs \
	--disable-termcap \
	--disable-termios \
	--enable-iconv \
	--enable-langinfo \
	--enable-lirc \
	--disable-lircc \
	--disable-joystick \
	--disable-apple-remote \
	--enable-vm \
	--enable-xf86keysym \
	--disable-radio \
	--disable-radio-capture \
	--disable-radio-v4l2 \
	--disable-radio-bsdbt848 \
	--disable-tv \
	--disable-tv-v4l1 \
	--disable-tv-v4l2 \
	--disable-tv-bsdbt848 \
	--disable-tv-teletext \
	--disable-pvr \
	--enable-rtc \
	--enable-network \
	--disable-winsock2 \
	--disable-smb \
	--disable-live \
	--disable-nemesi \
	--enable-dvdnav \
	--enable-dvdread \
	--enable-dvdread-internal \
	--disable-libdvdcss-internal \
	--disable-cdparanoia \
	--disable-cddb \
	--disable-bitmap-font \
	--enable-freetype \
	--enable-unrarlib \
	--enable-menu \
	--enable-sortsub \
	--disable-fribidi \
	--disable-enca \
	--disable-macosx \
	--disable-maemo \
	--disable-macosx-finder-support \
	--disable-macosx-bundle \
	--disable-inet6 \
	--enable-gethostbyname2 \
	--enable-ftp \
	--disable-vstream \
	--enable-pthreads \
	--disable-w32threads \
	--enable-ass \
	--disable-rpath
# Codecs
# --enable-libcdio must be auto or cflags and libs will not be determined correctly.
CONFIGURE_ARGS_CODEC = \
	--disable-gif \
	--enable-png \
	--enable-jpeg \
	--disable-liblzo \
	$(if $(filter i386,$(GARCH_FAMILY)),--enable-win32dll,--disable-win32dll) \
	--disable-qtx \
	--enable-xanim \
	--enable-real \
	--disable-xvid \
	--disable-x264 \
	--disable-libnut \
	--disable-tremor-internal \
	--disable-tremor-low \
	--disable-tremor-external \
	--disable-libvorbis \
	--disable-speex \
	--disable-theora \
	--enable-faad-external \
	--disable-faad-internal \
	--disable-faad-fixed \
	--disable-faac \
	--disable-ladspa \
	--disable-libdv \
	--enable-mad \
	--disable-twolame \
	--disable-xmms \
	--enable-libdca \
	--enable-mp3lib \
	--enable-liba52 \
	--enable-libmpeg2 \
	--disable-musepack \
	--disable-libamr_nb \
	--disable-libamr_wb
# Video output: enable xv (requires x11 and vm) and xvmc
CONFIGURE_ARGS_VIDEO = \
	--disable-vidix-internal \
	--disable-vidix-external \
	--enable-gl \
	--disable-dga2 \
	--disable-dga1 \
	--disable-vesa \
	--disable-svga \
	--disable-sdl \
	--disable-aa \
	--disable-caca \
	--disable-ggi \
	--disable-ggiwmh \
	--disable-directx \
	--disable-dxr2 \
	--disable-dxr3 \
	--disable-ivtv \
	--disable-v4l2 \
	--disable-dvb \
	--disable-dvbhead \
	--disable-mga \
	--disable-xmga \
	--enable-xv \
	--enable-xvmc \
	--enable-vm \
	--enable-xinerama \
	--enable-x11 \
	--disable-xshape \
	--disable-fbdev \
	--disable-mlib \
	--disable-3dfx \
	--disable-tdfxfb \
	--disable-s3fb \
	--disable-directfb \
	--disable-zr \
	--disable-bl \
	--disable-tdfxvid \
	--disable-xvr100 \
	--disable-tga \
	--disable-pnm \
	--disable-md5sum
# Audio output: enable alsa
CONFIGURE_ARGS_AUDIO = \
	--enable-alsa \
	--disable-ossaudio \
	--disable-arts \
	--disable-esd \
	--disable-polyp \
	--disable-jack \
	--disable-openal \
	--disable-nas \
	--disable-sgiaudio \
	--disable-sunaudio \
	--disable-win32waveout \
	--disable-select
CONFIGURE_ARGS_MISC = \
	--enable-runtime-cpudetection \
	--enable-cross-compile \
	--cc="$(CC)" \
	--host-cc="$(build_CC)" \
	--as="$(AS)" \
	--ar="$(AR)" \
	--ranlib="$(RANLIB)" \
	--target="$(GARCH_FAMILY)-linux" \
	--disable-static \
	--charset="UTF-8" \
	--language="all"
CONFIGURE_ARGS_ADVANCED = \
	--enable-mmx \
	--enable-mmxext \
	--enable-3dnow \
	--enable-3dnowext \
	--enable-sse \
	--enable-sse2 \
	--enable-ssse3 \
	--enable-shm \
	--disable-altivec \
	--disable-armv5te \
	--disable-armv6 \
	--disable-iwmmxt \
	--enable-fastmemcpy \
	--disable-big-endian \
	--disable-debug \
	--disable-profile \
	--enable-sighandler \
	--disable-crash-debug \
	--disable-dynamic-plugins
CONFIGURE_ARGS_WITH = \
	--extra-libs="-lXext -lX11" \
	--with-xvmclib=XvMCW
CONFIGURE_ARGS = \
	$(CONFIGURE_ARGS_DIR) \
	$(CONFIGURE_ARGS_OPTIONAL) \
	$(CONFIGURE_ARGS_CODEC) \
	$(CONFIGURE_ARGS_VIDEO) \
	$(CONFIGURE_ARGS_AUDIO) \
	$(CONFIGURE_ARGS_MISC) \
	$(CONFIGURE_ARGS_ADVANCED) \
	$(CONFIGURE_ARGS_WITH)
INSTALL_ARGS   = \
	INSTALLSTRIP=

CONFIGURE_ENV  = \
	DESTDIR="$(DESTDIR)"
BUILD_ENV  = \
	DESTDIR="$(DESTDIR)"

include ../../gar.mk

CFLAGS :=

# When using the SVN version, GARVERSION must have the form <mplayer-svn-version>.<ffmpeg-svn-version>.
# This is done to ensure that the correct version of FFmpeg is used.
svn//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_SVN, svn://$*/mplayer/trunk           , $(word 1,$(subst ., ,$(GARVERSION))), $(DISTNAME))
	@$(call FETCH_SVN, svn://$*/ffmpeg/trunk/libavutil  , $(word 2,$(subst ., ,$(GARVERSION))), libavutil  )
	@$(call FETCH_SVN, svn://$*/ffmpeg/trunk/libavcodec , $(word 2,$(subst ., ,$(GARVERSION))), libavcodec )
	@$(call FETCH_SVN, svn://$*/ffmpeg/trunk/libavformat, $(word 2,$(subst ., ,$(GARVERSION))), libavformat)
	@$(call FETCH_SVN, svn://$*/ffmpeg/trunk/libpostproc, $(word 2,$(subst ., ,$(GARVERSION))), libpostproc)
	@cd $(PARTIALDIR) ; tar -jxf $(DISTNAME).tar.bz2 ; rm -r $(DISTNAME).tar.bz2
	@cd $(PARTIALDIR) ; tar -jxf libavutil.tar.bz2   ; rm -r libavutil.tar.bz2   ; rm -rf $(DISTNAME)/libavutil   ; mv libavutil   $(DISTNAME)/
	@cd $(PARTIALDIR) ; tar -jxf libavcodec.tar.bz2  ; rm -r libavcodec.tar.bz2  ; rm -rf $(DISTNAME)/libavcodec  ; mv libavcodec  $(DISTNAME)/
	@cd $(PARTIALDIR) ; tar -jxf libavformat.tar.bz2 ; rm -r libavformat.tar.bz2 ; rm -rf $(DISTNAME)/libavformat ; mv libavformat $(DISTNAME)/
	@cd $(PARTIALDIR) ; tar -jxf libpostproc.tar.bz2 ; rm -r libpostproc.tar.bz2 ; rm -rf $(DISTNAME)/libpostproc ; mv libpostproc $(DISTNAME)/
	@cd $(PARTIALDIR) ; tar -jcf $(DISTNAME).tar.bz2 $(DISTNAME)
	@cd $(PARTIALDIR) ; rm -rf $(DISTNAME)
	@$(MAKECOOKIE)

install-custom:
	@mkdir -p $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/mplayer $(DESTDIR)$(bindir)/mplayer-vld
	@$(MAKECOOKIE)
