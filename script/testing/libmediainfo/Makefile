GARNAME = libmediainfo
GARVERSION = 0.7.37
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/mediainfo/
DISTFILES = $(GARNAME)_$(GARVERSION).tar.bz2
#PATCHFILES = $(DISTNAME)-shared.patch
LICENSE = GPL

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c testing/libzen 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--enable-visibility \
	--enable-libcurl \
	--disable-libmms 
LIBMDIR = $(WORKDIR)/MediaInfoLib
WORKSRC = $(LIBMDIR)/Project/GNU/Library

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)
				        
post-install:
	install -m755 $(WORKSRC)/$(GARNAME)-config $(DESTDIR)$(bindir)-config
	cp -a $(LIBMDIR)/Source/MediaInfo $(DESTDIR)$(includedir)

