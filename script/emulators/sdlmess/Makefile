GARNAME = sdlmess
GARVERSION = 0.110
CATEGORIES = emulators
DISTFILES = $(GARNAME)$(subst .,,$(GARVERSION)).zip
PATCHFILES = $(DISTNAME).patch.gar
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/expat lib/SDL lib/zlib xorg/xorg

WORKSRC = $(WORKDIR)/$(GARNAME)$(subst .,,$(GARVERSION))

BUILD_SCRIPTS   = $(WORKSRC)/makefile
INSTALL_SCRIPTS = custom

BUILD_ENV = \
	CC_FOR_BUILD="$(build_CC)" \
	CFLAGS_FOR_BUILD="$(build_CFLAGS)" \
	CFLAGS_FOR_TARGET="$(CFLAGS)" \
	$(if $(filter x86_64,$(GARCH_FAMILY)),PTR64="1")

include ../../gar.mk

install-custom:
	@mkdir -p $(DESTDIR)$(bindir)
	@cp -f $(WORKSRC)/messcli $(DESTDIR)$(bindir)/mess
	@$(MAKECOOKIE)
