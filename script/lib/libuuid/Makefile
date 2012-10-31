GARNAME = libuuid
GARVERSION = 1.41.7
CATEGORIES = lib
SOURCEPKG = disk/e2fsprogs
LICENSE = GPL2/LGPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

WORKSRC = $(WORKDIR)/e2fsprogs-$(GARVERSION)

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/lib/uuid/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/lib/uuid/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-rpath \
	--enable-elf-shlibs \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL_LIBPATH,$(WORKSRC),configure)
	@$(MAKECOOKIE)

install-custom:
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $(WORKSRC) $(INSTALL_ARGS) install install-libs
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libuuid.a
	@mv -f $(DESTDIR)$(libdir)/libuuid.*  $(DESTDIR)$(elibdir)/
	@$(MAKECOOKIE)
