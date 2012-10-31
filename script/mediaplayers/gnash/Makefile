GARNAME = gnash
GARVERSION = 0.8.6
CATEGORIES = mediaplayers
MASTER_SITES = ftp://ftp.gnu.org/gnu/$(GARNAME)/$(GARVERSION)/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-cross.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx gtk/atk gtk/glib gtk/gtk gtk/pango lib/agg lib/boost lib/expat lib/ffmpeg lib/fontconfig lib/freetype lib/giflib lib/libjpeg lib/libpng lib/libxml2 lib/zlib net/curl system/lirc xorg/xorg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-nls \
	--disable-rpath \
	--disable-avm2 \
	--disable-python \
	--disable-jemalloc \
	--disable-debugger \
	--disable-fps-debug \
	--disable-allstatic \
	--disable-menus \
	--disable-swftree \
	--disable-testsuite \
	--disable-write \
	--enable-sa-launcher \
	--disable-cygnal \
	--disable-cgibins \
	--disable-i810-lod-bias \
	--disable-sdkinstall \
	--enable-gui=gtk \
	--enable-renderer=agg \
	--enable-sound=sdl \
	--enable-media=ffmpeg \
	--enable-lirc \
	--disable-static \
	--enable-shared \
	--disable-ssh \
	--disable-ssl \
	--disable-glext \
	--disable-kparts3 \
	--disable-kparts4 \
	--enable-npapi \
	--enable-plugins \
	--disable-xpcom \
	--disable-ghelp \
	--disable-docbook \
	--enable-visibility \
	--disable-strict \
	--enable-cassert \
	--with-gnu-ld \
	--with-plugins-install=system \
	--with-npapi-install=system \
	--with-npapi-plugindir="$(libdir)/browser/plugins" \
	--with-z-incl="$(DESTDIR)$(includedir)" \
	--with-z-lib="$(DESTDIR)$(libdir)" \
	--with-jpeg-incl="$(DESTDIR)$(includedir)" \
	--with-jpeg-lib="$(DESTDIR)$(libdir)" \
	--with-boost-incl="$(DESTDIR)$(includedir)" \
	--with-boost-lib="$(DESTDIR)$(libdir)"

INSTALL_ARGS = \
	install-plugin

include ../../gar.mk

pre-configure:
	@rm -f $(WORKSRC)/macros/libltdl.m4
	@rm -f $(WORKSRC)/macros/pkg.m4
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)/$(libdir)/gnash/libgnashamf.la
	@rm -f $(DESTDIR)/$(libdir)/gnash/libgnashbase.la
	@rm -f $(DESTDIR)/$(libdir)/gnash/libgnashcore.la
	@rm -f $(DESTDIR)/$(libdir)/gnash/libgnashmedia.la
	@rm -f $(DESTDIR)/$(libdir)/gnash/libgnashnet.la
	@rm -f $(DESTDIR)/$(libdir)/gnash/libgnashsound.la
	@rm -f $(DESTDIR)/$(libdir)/gnash/libmozsdk.la
	@$(MAKECOOKIE)
