GARNAME = sdlmame
GARVERSION = 0.125
CATEGORIES = emulators
DISTFILES = $(GARNAME)$(subst .,,$(GARVERSION)).zip
PATCHFILES  = $(DISTNAME).patch.gar
ifneq ($(DESTIMG),build)
PATCHFILES += $(DISTNAME)-cross.patch
endif
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/docs/license.txt

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/expat lib/SDL lib/zlib xorg/xorg
ifneq ($(DESTIMG),build)
BUILDDEPS += emulators/sdlmame
endif

WORKSRC = $(WORKDIR)/$(GARNAME)$(subst .,,$(GARVERSION))

BUILD_SCRIPTS    = $(WORKSRC)/makefile
INSTALL_SCRIPTS  = custom
ifeq ($(DESTIMG),build)
INSTALL_SCRIPTS += cross
endif

BUILD_ARGS = \
	OPTIMIZE="$(OPTIMIZE)" \
	OPT_FLAGS="$(CFLAGS)" \
	$(if $(filter x86_64,$(GARCH_FAMILY)),PTR64="1")

include ../../gar.mk

OPTIMIZE := $(subst -O,,$(filter -O%,$(CFLAGS)))

install-custom:
	@mkdir -p $(DESTDIR)$(bindir)
	@cp -f $(WORKSRC)/mame $(DESTDIR)$(bindir)/mame
	@$(MAKECOOKIE)

install-cross:
	@mkdir -p $(DESTDIR)$(bindir)
	@cp -f $(WORKSRC)/obj/sdl/mame/build/file2str $(DESTDIR)$(bindir)/sdlmame-file2str
	@cp -f $(WORKSRC)/obj/sdl/mame/build/png2bdc  $(DESTDIR)$(bindir)/sdlmame-png2bdc
	@cp -f $(WORKSRC)/obj/sdl/mame/build/m68kmake $(DESTDIR)$(bindir)/sdlmame-m68kmake
	@$(MAKECOOKIE)
