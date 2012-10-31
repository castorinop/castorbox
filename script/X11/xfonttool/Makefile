GARNAME = xfonttool
GARVERSION = 0.3
CATEGORIES = X11
MASTER_SITES = http://www.holoweb.net/~liam/fonts/
DISTFILES = $(DISTNAME).tgz
#PATCHFILES = $(DISTNAME)-defaults.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c xorg/xorg

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--enable-shared \
	--disable-static \
	--disable-gtktest \
	--enable-xinerama \
	--disable-gdk_pixbuftest \
	--disable-new-plugin \
	--disable-beep_media_player_plugin \
	--disable-old-plugin \
	--with-gnu-ld \
	--with-x

CONFIGURE_ENV = \
	GTK_CONFIG="no"

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/libxosd.la
	@rm -f $(DESTDIR)$(bindir)-config/xosd-config
	@rm -f $(DESTDIR)$(bindir)-config/$(compiler_prefix)xosd-config
	@mkdir -p $(DESTDIR)$(bindir)-config
	@mv $(DESTDIR)$(bindir)/xosd-config $(DESTDIR)$(bindir)-config/xosd-config
	@$(if $(compiler_prefix), ln -s xosd-config $(DESTDIR)$(bindir)-config/$(compiler_prefix)xosd-config)
	@$(MAKECOOKIE)
