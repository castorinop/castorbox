GARNAME = goalbit
#GARVERSION = snapshot-20091015-2228
GARVERSION = 0.7.3
CATEGORIES = mediaplayers
PATCHFILES  =
ifeq ($(word 1,$(subst -, ,$(GARVERSION))),snapshot)
MASTER_SITES  = http://nightlies.videolan.org/build/source/$(subst snapshot,trunk,$(GARVERSION))/
DISTFILES = $(GARNAME)-snapshot-$(word 2,$(subst -, ,$(GARVERSION))).tar.bz2
WORKSRC = $(WORKDIR)/$(GARNAME)-1.1.0-git
else
MASTER_SITES  = http://downloads.sourceforge.net/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
endif
PATCHFILES = $(DISTNAME)-libgcrypt_m4.patch 
#$(DISTNAME)-vaapi.patch $(DISTNAME)-vdpau_20090814.patch $(DISTNAME).patch.gar
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c \
	lib/a52dec \
	lib/alsa-lib \
	lib/faad2 \
	lib/ffmpeg \
	lib/fontconfig \
	lib/freetype \
	lib/libcdio \
	lib/libdvdnav \
	lib/libdvbpsi \
	lib/libdca \
	lib/libmad \
	lib/libmatroska \
	lib/libmpeg2 \
	lib/libpng \
	lib/libtheora \
	lib/libvorbis \
	lib/libxml2 \
	lib/taglib \
	lib/zlib \
	system/lirc \
	testing/libgcrypt \
	xorg/xorg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--disable-silent-rules \
	--disable-python-bindings \
	--disable-java-bindings \
	--disable-macosx-defaults \
	--disable-static \
	--enable-shared \
	--enable-nls \
	--disable-rpath \
	--disable-hal \
	--disable-mtp \
	--disable-dbus \
	--disable-dbus-control \
	--disable-telepathy \
	--disable-gprof \
	--disable-cprof \
	--enable-mmx \
	--enable-sse \
	--disable-altivec \
	--disable-optimize-memory \
	--disable-optimizations \
	--disable-debug \
	--disable-run-as-root \
	--disable-coverage \
	--enable-release \
	--enable-sout \
	--disable-switcher \
	--disable-shout \
	--disable-lua \
	--disable-httpd \
	--disable-libproxy \
	--disable-vlm \
	--disable-growl \
	--disable-notify \
	--disable-audioscrobbler \
	--enable-taglib \
	--disable-live555 \
	--disable-dc1394 \
	--disable-dv \
	--disable-dvdread \
	--enable-dvdnav \
	--disable-dshow \
	--disable-bda \
	--disable-opencv \
	--disable-smb \
	--enable-dvbpsi \
	--disable-v4l \
	--disable-v4l2 \
	--disable-libv4l2 \
	--disable-pvr \
	--disable-gnomevfs \
	--enable-libcdio \
	--disable-vcdinfo \
	--disable-cddax \
	--disable-libcddb \
	--disable-vcdx \
	--enable-cdda \
	--enable-vcd \
	--disable-dvb \
	--disable-screen \
	--disable-ogg \
	--enable-mkv \
	--disable-mod \
	--disable-mpc \
	--disable-gme \
	--disable-wma-fixed \
	--disable-shine \
	--enable-mad \
	--disable-id3tag \
	--enable-avcodec \
	--enable-avformat \
	--enable-swscale \
	--enable-postproc \
	--enable-faad \
	--disable-twolame \
	--disable-quicktime \
	--disable-real \
	--disable-realrtsp \
	--disable-libsysfs \
	--disable-libtar \
	--enable-a52 \
	--enable-dca \
	--disable-flac \
	--enable-libmpeg2 \
	--enable-vorbis \
	--disable-tremor \
	--disable-speex \
	--disable-tarkin \
	--enable-theora \
	--disable-dirac \
	--disable-schroedinger \
	--enable-png \
	--enable-vdpau \
	--disable-x264 \
	--disable-fluidsynth \
	--disable-zvbi \
	--disable-telx \
	--disable-csri \
	--disable-libass \
	--disable-asademux \
	--disable-cmml \
	--disable-kate \
	--disable-tiger \
	--enable-x11 \
	--enable-xvideo \
	--enable-glx \
	--enable-xvmc \
	--enable-xinerama \
	--enable-xcb \
	--enable-opengl \
	--disable-sdl \
	--disable-sdl-image \
	--enable-freetype \
	--disable-fribidi \
	--enable-fontconfig \
	--enable-libxml2 \
	--disable-svg \
	--disable-snapshot \
	--disable-qte \
	--disable-hd1000v \
	--disable-directx \
	--disable-fb \
	--disable-mga \
	--disable-omapfb \
	--disable-svgalib \
	--disable-directfb \
	--disable-ggi \
	--disable-aa \
	--disable-caca \
	--disable-wingdi \
	--disable-oss \
	--disable-pulse \
	--disable-portaudio \
	--enable-alsa \
	--disable-waveout \
	--disable-macosx-audio \
	--disable-hd1000a \
	--disable-jack \
	--disable-cyberlink \
	--disable-upnp \
	--disable-skins2 \
	--disable-pda \
	--disable-maemo \
	--disable-wince \
	--disable-opie \
	--disable-macosx \
	--disable-qnx \
	--disable-ncurses \
	--disable-xosd \
	--disable-fbosd \
	--disable-visual \
	--disable-galaktos \
	--disable-goom \
	--disable-atmo \
	--disable-bonjour \
	--enable-lirc \
	--enable-libgcrypt \
	--disable-gnutls \
	--disable-remoteosd \
	--disable-update-check \
	--disable-loader \
	--enable-vlc \
	--disable-activex \
	--disable-mozilla \
	--disable-testsuite \
	--without-contrib \
	--with-gnu-ld \
	--with-tuning=$(mm_ARCH) \
	--with-dvdnav-config-path=$(DESTDIR)$(bindir) \
	--with-x

CONFIGURE_ENV =

# Build VLC with the Qt4 GUI.
ifdef VLC_GUI_QT4
DEPENDS += \
	qt/qt4
CONFIGURE_ARGS += \
	--enable-qt4
CONFIGURE_ENV += \
	ac_cv_path_MOC=$(DESTDIR)$(qt4bindir)/moc \
	ac_cv_path_RCC=$(DESTDIR)$(qt4bindir)/rcc \
	ac_cv_path_UIC=$(DESTDIR)$(qt4bindir)/uic
else
CONFIGURE_ARGS += \
	--disable-qt4
endif

include ../../gar.mk

# Ignored when the vaapi patch is not applied.
CPPFLAGS += -DHAVE_AVCODEC_VAAPI
CFLAGS   += -DHAVE_AVCODEC_VAAPI
CXXFLAGS += -DHAVE_AVCODEC_VAAPI

pre-configure:
	@cd $(WORKSRC) ; ./bootstrap
	@$(MAKECOOKIE)

no-pre-configure:
	@$(if $(wildcard $(WORKSRC)/modules/codec/vdpau/*),cd $(WORKSRC) ; ./modules/genmf codec/vdpau)
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC),configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libvlc.la
	@rm -f $(DESTDIR)$(libdir)/libvlccore.la
	@rm -f `find $(DESTDIR)$(libdir)/vlc -name *.la`
	@$(MAKECOOKIE)

clean-all:
	@$(MAKE) -C ../vlc clean
	@rm -rf $(DESTDIR)$(bindir)/vlc
	@rm -rf $(DESTDIR)$(bindir)/cvlc
	@rm -rf $(DESTDIR)$(bindir)/qvlc
	@rm -rf $(DESTDIR)$(bindir)/rvlc
	@rm -rf $(DESTDIR)$(bindir)/vlc-wrapper
	@rm -rf $(DESTDIR)$(includedir)/vlc
	@rm -rf $(DESTDIR)$(libdir)/vlc
	@rm -rf $(DESTDIR)$(libdir)/libvlc.*
	@rm -rf $(DESTDIR)$(libdir)/libvlccore.*
	@rm -rf $(DESTDIR)$(datadir)/vlc
	@rm -rf $(DESTDIR)$(docdir)/vlc
