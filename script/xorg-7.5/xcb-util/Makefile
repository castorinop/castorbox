GARNAME = xcb-util
GARVERSION = 0.3.6
CATEGORIES = $(CATEGORY)
MASTER_SITES = http://xcb.freedesktop.org/dist/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = MIT

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c \
	$(CATEGORY)/libxcb \
	$(CATEGORY)/xproto
BUILDDEPS = utils/gperf

CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--disable-static \
	--with-gnu-ld

GAR_EXTRA_CONF += $(CATEGORY)/xorg/package-api.mk
include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libxcb-atom.la
	@rm -f $(DESTDIR)$(libdir)/libxcb-aux.la
	@rm -f $(DESTDIR)$(libdir)/libxcb-event.la
	@rm -f $(DESTDIR)$(libdir)/libxcb-icccm.la
	@rm -f $(DESTDIR)$(libdir)/libxcb-image.la
	@rm -f $(DESTDIR)$(libdir)/libxcb-keysyms.la
	@rm -f $(DESTDIR)$(libdir)/libxcb-property.la
	@rm -f $(DESTDIR)$(libdir)/libxcb-render-util.la
	@rm -f $(DESTDIR)$(libdir)/libxcb-reply.la
	@$(MAKECOOKIE)
