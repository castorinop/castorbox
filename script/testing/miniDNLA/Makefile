GARNAME = minidlna
GARVERSION = 1.0.18
CATEGORIES = net
MASTER_SITES +=  http://ufpr.dl.sourceforge.net/sourceforge/$(GARNAME)/$(GARNAME)/$(GARVERSION)/
DISTFILES = $(GARNAME)_$(GARVERSION)_src.tar.gz
#PATCHFILES = $(DISTNAME)-cross_compiling.patch
# http://amule-dlp.googlecode.com/files/aMule-2.2.6-DLP4102.patch
# PATCHFILES += $(DISTNAME)-DLP4102.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libexif lib/libjpeg lib/libid3tag lib/flac lib/libvorbis db/sqlite lib/ffmpeg 


WORKSRC = $(WORKDIR)/$(GARNAME)

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS = CC="$(CC)"

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-amule-daemon \
	--enable-amulecmd \
	--enable-webserver \
	--enable-upnp \
	--disable-monolithic \
	--with-upnp-prefix=$(DESTDIR)$(prefix) \
	--with-zlib=$(DESTDIR)$(prefix) \
	--with-crypto-prefix=$(DESTDIR)$(prefix) \
	--with-wx-config=$(DESTDIR)$(bindir)/wx-config \
	--with-toolkit=base \
	--disable-debug \
	--with-gnu-ld 

include ../../gar.mk
