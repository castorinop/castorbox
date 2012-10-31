GARNAME = fuppes
GARVERSION = 659
MASTER_SITES = svn+https://fuppes.svn.sourceforge.net/svnroot/fuppes/trunk/

CATEGORIES = net
DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES = $(DISTNAME)-cfg_castorbox.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx db/sqlite lib/pcre lib/libexif lib/taglib lib/libvorbis lib/flac lib/libmad lib/lame utils/imagemagick lib/ffmpeg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-lame \
	--enable-mad \
	--enable-flac \
	--enable-vorbis \
	--enable-inotify \
	--enable-taglib \
	--disable-rpath \
	--with-gnu-ld 

CONFIGURE_ENV = TAGLIB_CONFIG=$(DESTDIR)$(bindir)-config/taglib-config

include ../../gar.mk

svn+https//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_SVN, https://$*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -rf $(DESTDIR)$(libdir)/$(GARNAME)/*.la
	@$(MAKECOOKIE)


