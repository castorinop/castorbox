GARNAME = gtk
GARVERSION = 1.2.10
CATEGORIES = lib
MASTER_SITES = ftp://ftp.gtk.org/pub/gtk/v1.2/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
PATCHFILES = $(DISTNAME).patch.gar
MAINTAINER = Ian Harding <iharding@att.net>
LICENSE = LGPL2

DESCRIPTION = gtk
define BLURB
 This is GTK+ version $(GARVERSION). GTK+, which stands for the Gimp ToolKit,
 is a library for creating graphical user interfaces for the X Window
 System. It is designed to be small, efficient, and flexible. GTK+ is
 written in C with a very object-oriented approach.
endef

LIBDEPS = devel/glibc devel/glib xorg/xorg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-xim \
	--with-xinput=no \
	--disable-glibtest \
	--with-glib-prefix=$(DESTDIR)$(prefix) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--with-gnu-ld

BUILD_SCRIPTS = $(WORKSRC)/Makefile

INSTALL_SCRIPTS = $(WORKSRC)/Makefile gtk-config

include ../../gar.mk

install-gtk-config:
	mkdir -p $(STAGINGDIR)/$(GARNAME)
	cp -f $(DESTDIR)$(bindir)/gtk-config $(STAGINGDIR)/$(GARNAME)/
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libgdk.la
	@rm -f $(DESTDIR)$(libdir)/libgtk.la
	sed -i 's%-L$${libdir}%-L$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/gdk.pc
	sed -i 's%-I$${includedir}%-I$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/gdk.pc
	sed -i 's%-L$${libdir}%-L$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/gtk.pc
	sed -i 's%-I$${includedir}%-I$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/gtk.pc
	sed -i 's%$${DESTDIR}%$(DESTDIR)%g'         $(DESTDIR)$(bindir)/gtk-config
	@$(MAKECOOKIE)
