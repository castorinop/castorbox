GARNAME = libXt
GARVERSION = 1.0.8
CATEGORIES = $(CATEGORY)
MASTER_SITES = $(XORG_MASTER_SITES)
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/COPYING

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c \
	$(CATEGORY)/kbproto \
	$(CATEGORY)/libICE \
	$(CATEGORY)/libSM \
	$(CATEGORY)/libX11 \
	$(CATEGORY)/xproto
BUILDDEPS = $(CATEGORY)/util-macros

CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--disable-static \
	--disable-silent-rules \
	--enable-xkb \
	--enable-malloc0returnsnull \
	--with-gnu-ld

CONFIGURE_ENV = \
	CC_FOR_BUILD="$(build_CC)" \
	CFLAGS_FOR_BUILD="$(build_CPPFLAGS) $(build_CFLAGS)" \
	LDFLAGS_FOR_BUILD="$(build_LDFLAGS)"

GAR_EXTRA_CONF += $(CATEGORY)/xorg/package-api.mk
include ../../gar.mk

CFLAGS   := $(CPPFLAGS) $(CFLAGS)
CPPFLAGS :=

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/$(GARNAME).la
	@$(MAKECOOKIE)
