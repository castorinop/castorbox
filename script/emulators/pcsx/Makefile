GARNAME = Pcsx
GARVERSION = 1.6beta
CATEGORIES = emulators
MASTER_SITES = http://mupen64.emulation64.com/files/0.5/
DISTFILES = $(DISTNAME).tgz cdr-1.71.tgz cdriso-1.3.tgz PeopsSoftGpu117.tar.gz gpupetemesagl176.tar.gz
PATCHFILES = $(DISTNAME).patch.gar
PATCHFILES = $(DISTNAME)_gcc4.patch cdriso.diff
LICENSE = GPL

DESCRIPTION = 
define BLURB
endef

DISTNAME := $(GARNAME)Src-$(GARVERSION)

WORKPLUGS = $(WORKDIR)/plugins
#WORKSRC = $(WORKDIR)/$(DISTNAME)/Linux

DEPENDS   = lang/c lib/libpng lib/SDL utils/gzip lib/gtk xorg/xorg
BUILDDEPS = devel/nasm

CONFIGURE_SCRIPTS     = $(WORKSRC)/Linux/configure
BUILD_SCRIPTS     = $(WORKSRC)/Linux/Makefile
INSTALL_SCRIPTS   = custom

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-x

SDL_FLAGS = $(shell $(DESTDIR)$(bindir)/sdl-config --cflags)
SDL_LIBS = $(shell $(DESTDIR)$(bindir)/sdl-config --libs)
FREETYPE_FLAGS = $(shell $(DESTDIR)$(bindir)/freetype-config --cflags)
FREETYPE_LIBS = $(shell $(DESTDIR)$(bindir)/freetype-config --libs)
GTK_FLAGS	=$(shell $(DESTDIR)$(bindir)/gtk-config --cflags)
GTK_LIBS	=$(shell $(DESTDIR)$(bindir)/gtk-config --libs)
GTHREAD_LIBS	=$(shell $(DESTDIR)$(bindir)/gtk-config --libs gtk gthread)


BUILD_OVERRIDE_DIRS = CC CXX 

BUILD_ARGS = OPTIMIZE='$(CFLAGS)' \
	DESTDIR='$(DESTDIR)' \
	CC='$(CC)'

include ../../gar.mk

# CDRISO 
extract-cdriso-1.3.tgz:
	mkdir -p $(WORKPLUGS)/cdriso
	@gzip -dc $(DOWNLOADDIR)/cdriso-1.3.tgz | tar -xf - -C $(WORKPLUGS)/cdriso
	@$(MAKECOOKIE)

patch-cdriso.diff:
	patch -d $(WORKPLUGS)/cdriso -p0 -F$(PATCHDIRFUZZ) < $(DOWNLOADDIR)/cdriso.diff

build-cdriso-1.3: 
	$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) -C $(WORKPLUGS)/cdriso/src $(BUILD_ARGS)
	@$(MAKECOOKIE)	

install-cdriso-1.3:
	mkdir -p $(DESTDIR)$(libdir)/pcsx/Plugin
	mkdir -p $(DESTDIR)$(datadir)/pcsx/cfg
	cp $(WORKPLUGS)/cdriso/src/libcdriso-1.3.so $(DESTDIR)$(libdir)/pcsx/Plugin
	cp $(WORKPLUGS)/cdriso/src/cfgCdrIso $(DESTDIR)$(datadir)/pcsx/cfg/
	@$(MAKECOOKIE)

# GPU SOFT X 
extract-PeopsSoftGpu117.tar.gz:
	mkdir -p $(WORKPLUGS)/gpupeopssoftx117
	@gzip -dc $(DOWNLOADDIR)/PeopsSoftGpu117.tar.gz | tar -xf - -C $(WORKPLUGS)/gpupeopssoftx117
	@$(MAKECOOKIE)

patch-acdriso.diff:
	patch -d $(WORKPLUGS)/cdriso -p0 -F$(PATCHDIRFUZZ) < $(DOWNLOADDIR)/cdriso.diff

build-PeopsSoftGpu117: 
	$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) -C $(WORKPLUGS)/gpupeopssoftx117/src $(BUILD_ARGS)
	@$(MAKECOOKIE)	

install-acdriso-1.3:
	mkdir -p $(DESTDIR)$(libdir)/pcsx/Plugin
	mkdir -p $(DESTDIR)$(datadir)/pcsx/cfg
	cp $(WORKPLUGS)/cdriso/src/libcdriso-1.3.so $(DESTDIR)$(libdir)/pcsx/Plugin
	cp $(WORKPLUGS)/cdriso/src/cfgCdrIso $(DESTDIR)$(datadir)/pcsx/cfg/
	@$(MAKECOOKIE)

pre-configure:
	@rm -f $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

install-custom:
	cp $(WORKSRC)/Linux/pcsx $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)
	

