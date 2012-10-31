GARNAME = pango
GARVERSION = 1.28.4
CATEGORIES = gtk
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pango/1.28/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/c lang/cxx gtk/cairo gtk/glib lib/freetype xorg/xorg
BUILDDEPS = gtk/gtk-doc

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(includedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--disable-silent-rules \
	--disable-static \
	--enable-shared \
	--disable-debug \
	--enable-rebuilds \
	--disable-gtk-doc \
	--disable-man \
	--disable-doc-cross-references \
	--enable-explicit-deps=auto \
	--with-gnu-ld \
	--with-x

include ../../gar.mk

# Fails to compile with GCC 4.5.2's link time optimization linker plugin enabled.
CFLAGS   := $(filter-out -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -fuse-linker-plugin, $(LDFLAGS))

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC),configure)
	@$(MAKECOOKIE)

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libpango-1.0.la
	@rm -rf $(DESTDIR)$(libdir)/libpangocairo-1.0.la
	@rm -rf $(DESTDIR)$(libdir)/libpangoft2-1.0.la
	@rm -rf $(DESTDIR)$(libdir)/libpangox-1.0.la
	@rm -rf $(DESTDIR)$(libdir)/libpangoxft-1.0.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-arabic-fc.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-arabic-lang.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-basic-fc.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-basic-x.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-hangul-fc.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-hebrew-fc.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-indic-fc.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-indic-lang.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-khmer-fc.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-syriac-fc.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-thai-fc.la
	@rm -rf $(DESTDIR)$(libdir)/pango/1.6.0/modules/pango-tibetan-fc.la
	@$(MAKECOOKIE)
