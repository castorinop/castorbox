GARNAME = transcode
GARVERSION = 1.1.5
CATEGORIES = utils
MASTER_SITES = http://download.berlios.de/tcforge/
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += config.cache.$(GARCH_FAMILY)
PATCHFILES = $(DISTNAME)-configure.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/a52dec lib/alsa-lib lib/libogg lib/libtheora lib/libvorbis lib/ffmpeg lib/freetype lib/lame lib/libmpeg2 lib/lzo lib/xvidcore xorg/xorg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--x-include=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--disable-static \
	--enable-static \
	--enable-mmx \
	--enable-3dnow \
	--enable-sse \
	--enable-sse2 \
	--disable-altivec \
	--enable-ffmpeg \
	--enable-libavcodec \
	--enable-libavformat \
	--enable-libmpeg2 \
	--disable-experimental \
	--disable-deprecated \
	--enable-statbuffer \
	--disable-v4l \
	--disable-bktr \
	--disable-sunau \
	--disable-oss \
	--enable-alsa \
	--disable-libpostproc \
	--disable-freetype2 \
	--enable-lame \
	--disable-xvid \
	--disable-x264 \
	--enable-ogg \
	--enable-vorbis \
	--enable-theora \
	--disable-libdvdread \
	--disable-pvm3 \
	--disable-libdv \
	--disable-libquicktime \
	--enable-lzo \
	--enable-a52 \
	--disable-faac \
	--disable-libxml2 \
	--disable-ibp \
	--disable-mjpegtools \
	--disable-sdl \
	--disable-imagemagick \
	--disable-libjpegmmx \
	--disable-libjpeg \
	--disable-bsdav \
	--disable-iconv \
	--disable-pv3 \
	--disable-nuv \
	--disable-warnings-as-errors \
	--with-x \
	--with-gnu-ld \
	--with-libmpeg2-prefix=$(DESTDIR)$(prefix) \
	--with-libmpeg2-includes=$(DESTDIR)$(includedir) \
	--with-libmpeg2-libs=$(DESTDIR)$(libdir) \
	--with-lame-prefix=$(DESTDIR)$(prefix) \
	--with-lame-includes=$(DESTDIR)$(includedir) \
	--with-lame-libs=$(DESTDIR)$(libdir) \
	--with-lzo-prefix=$(DESTDIR)$(prefix) \
	--with-lzo-includes=$(DESTDIR)$(includedir) \
	--with-lzo-libs=$(DESTDIR)$(libdir) \
	--with-a52-prefix=$(DESTDIR)$(prefix) \
	--with-a52-includes=$(DESTDIR)$(includedir) \
	--with-a52-libs=$(DESTDIR)$(libdir) \
	--with-mod-path=$(libdir)/transcode

include ../../gar.mk

#CFLAGS += `pkg-config --cflags libavcodec` `pkg-config --libs libavcodec`

extract-config.cache.$(GARCH_FAMILY):
	@cp $(DOWNLOADDIR)/config.cache.$(GARCH_FAMILY) $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

pre-install:
	@rm -rf $(DESTDIR)$(libdir)/transcode
	@$(MAKECOOKIE)

post-install:
	@rm -rf $(DESTDIR)$(libdir)/transcode/*.a
	@rm -rf $(DESTDIR)$(libdir)/transcode/*.la
	@$(MAKECOOKIE)
