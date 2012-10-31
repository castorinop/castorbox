GARNAME = alsaplayer
GARVERSION = 0.99.80
CATEGORIES = mediaplayers
MASTER_SITES = http://www.alsaplayer.org/
#MASTER_SITES += ftp://ftp.alsa-project.org/pub/people/andy/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-climits.patch $(DISTNAME)-gcc4.4.1.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/alsa-lib lib/libmad lib/flac lib/libvorbis

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-alsa \
	--disable-oss \
	--enable-oggvorbis \
	--enable-audiofile \
	--enable-flac \
	--enable-oggflac \
	--enable-mad \
	--disable-gtk2 \
	--disable-gtk \
	--disable-opengl \
	--disable-xosd \
	--with-gnu-ld \
	--without-x 

include ../../gar.mk

post-install: 
	@rm -rf $(DESTDIR)$(libdir)/libalsaplayer.la
	@rm -rf $(DESTDIR)$(libdir)/alsaplayer/*/*.la
	@$(MAKECOOKIE)
