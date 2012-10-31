GARNAME = libdrm
GARVERSION = 2.4.21
CATEGORIES = $(CATEGORY)
MASTER_SITES = http://dri.freedesktop.org/libdrm/
DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES = $(DISTNAME)-stdint_h.patch $(DISTNAME)-update_20100101.patch
LICENSE = MIT

DESCRIPTION = 
define BLURB
endef

DEPENDS  = lang/c \
	$(CATEGORY)/libpthread-stubs
ifneq ($(DESTIMG),build)
DEPENDS += system/udev
endif

CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS  = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-static \
	--enable-shared \
	--disable-silent-rules \
	--enable-libkms \
	--enable-intel \
	--enable-radeon \
	--disable-vmwgfx-experimental-api \
	--enable-nouveau-experimental-api \
	--with-gnu-ld
ifeq ($(DESTIMG),build)
CONFIGURE_ARGS += \
	--disable-udev
else
CONFIGURE_ARGS += \
	--enable-udev
endif

include ../../gar.mk

pre-configure:
	@#cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/$(GARNAME).la
	@rm -f $(DESTDIR)$(libdir)/$(GARNAME)_intel.la
	@rm -f $(DESTDIR)$(libdir)/$(GARNAME)_nouveau.la
	@rm -f $(DESTDIR)$(libdir)/$(GARNAME)_radeon.la
	@rm -f $(DESTDIR)$(libdir)/libkms.la
	@$(MAKECOOKIE)
