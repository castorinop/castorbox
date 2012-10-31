GARNAME = dbus-glib
GARVERSION = 0.80
CATEGORIES = lib
MASTER_SITES = http://dbus.freedesktop.org/releases/dbus-glib/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-disable_tools.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/dbus gtk/glib lib/expat

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-checks \
	--with-xml=expat \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@rm -f $(WORKSRC)/config.cache
	@echo "ac_cv_func_posix_getpwnam_r=yes" >> $(WORKSRC)/config.cache
	@echo "ac_cv_have_abstract_sockets=yes" >> $(WORKSRC)/config.cache
	@echo "dbus_cv_va_val_copy=no"          >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libdbus-glib-1.la
	@$(MAKECOOKIE)
