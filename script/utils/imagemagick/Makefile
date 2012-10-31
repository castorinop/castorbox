GARNAME = ImageMagick
GARVERSION = 6.5.3-1
CATEGORIES = utils
MASTER_SITES = ftp://ftp.imagemagick.org/pub/ImageMagick/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/LICENSE

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/fontconfig lib/freetype lib/libjpeg lib/libpng

#WORKSRC = $(WORKDIR)/$(GARNAME)-$(word 1,$(subst -, ,$(GARVERSION)))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-pic \
	--without-perl \
	--enable-shared \
	--disable-static \
	--without-dps \
	--without-windows-font-dir \
	--without-modules \
	--with-threads \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libMagickCore.la
	@rm -f $(DESTDIR)$(libdir)/libMagick++.la
	@rm -f $(DESTDIR)$(libdir)/libMagickWand.la
	@rm -f $(DESTDIR)$(libdir)/ImageMagick-6.4.5/modules-Q16/coders/*.la
	@rm -f $(DESTDIR)$(libdir)/ImageMagick-6.4.5/modules-Q16/filters/*.la
	@$(MAKECOOKIE)

