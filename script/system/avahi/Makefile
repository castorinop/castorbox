GARNAME = avahi
GARVERSION = 0.6.30
CATEGORIES = system
MASTER_SITES =  http://www.avahi.org/download/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/expat lib/libdaemon lib/dbus

CONFIGURE_SCRIPTS   = $(WORKSRC)/configure
BUILD_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--with-distro=Debian \
	--disable-stack-protector \
	--disable-qt3 \
	--disable-qt4 \
	--disable-gtk \
	--disable-gtk3 \
	--disable-gdbm \
	--disable-python \
	--disable-mono \
	--disable-nls \
	--with-avahi-user=nobody \
	--with-avahi-group=nogroup \
	--with-avahi-priv-access-group=root \
	--with-autoipd-user=nobody \
	--with-autoipd-group=nogroup \
	--with-gnu-ld

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/libavahi-client.la
	@rm -f $(DESTDIR)$(libdir)/libavahi-common.la
	@rm -f $(DESTDIR)$(libdir)/libavahi-core.la
	@rm -f $(DESTDIR)$(libdir)/libavahi-glib.la
	@rm -f $(DESTDIR)$(libdir)/libavahi-gobject.la
	@$(MAKECOOKIE)

