GARNAME = libart_lgpl
GARVERSION = 2.3.20
CATEGORIES = lib
MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/$(GARNAME)/2.3/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES  = $(DISTNAME).patch.gar
ifneq ($(DESTIMG),build)
PATCHFILES += $(DISTNAME)-cross.patch
endif
LICENSE = LGPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c
ifneq ($(DESTIMG),build)
BUILDDEPS = lib/libart
endif

CONFIGURE_SCRIPTS  = $(WORKSRC)/configure
BUILD_SCRIPTS      = $(WORKSRC)/Makefile
INSTALL_SCRIPTS    = $(WORKSRC)/Makefile
ifeq ($(DESTIMG),build)
INSTALL_SCRIPTS   += cross
endif

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--disable-static \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

install-cross:
	@if test -e $(WORKSRC)/gen_art_config ; then cp -f $(WORKSRC)/gen_art_config $(DESTDIR)$(bindir)/libart-gen_art_config ; fi
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libart_lgpl_2.la
	@rm -f $(DESTDIR)$(bindir)-config/libart2-config
	@rm -f $(DESTDIR)$(bindir)-config/$(compiler_prefix)libart2-config
	@mkdir -p $(DESTDIR)$(bindir)-config
	@mv $(DESTDIR)$(bindir)/libart2-config $(DESTDIR)$(bindir)-config/libart2-config
	@$(if $(compiler_prefix), ln -s libart2-config $(DESTDIR)$(bindir)-config/$(compiler_prefix)libart2-config)
	@$(MAKECOOKIE)
