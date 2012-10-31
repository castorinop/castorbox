GARNAME = imlib2
GARVERSION = 1.4.2
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/enlightenment/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-fix_cross.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libjpeg lib/libpng lib/giflib lib/freetype lib/libmad lib/libid3tag utils/bzip2 xorg/xorg 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL_LIBPATH,$(WORKSRC),configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libImlib2.la
	@rm -f $(DESTDIR)$(libdir)/imlib2/loaders/*.la
	@rm -f $(DESTDIR)$(libdir)/imlib2/filters/*.la
	@rm -f $(DESTDIR)$(bindir)-config/imlib2-config
	@rm -f $(DESTDIR)$(bindir)-config/$(compiler_prefix)imlib2-config
	@mkdir -p $(DESTDIR)$(bindir)-config
	@mv $(DESTDIR)$(bindir)/imlib2-config $(DESTDIR)$(bindir)-config/imlib2-config
	@$(if $(compiler_prefix), ln -s imlib2-config $(DESTDIR)$(bindir)-config/$(compiler_prefix)imlib2-config)
	@$(MAKECOOKIE)
