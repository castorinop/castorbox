GARNAME = mupen64_src
GARVERSION = 0.5
CATEGORIES = emulators
MASTER_SITES = http://mupen64.emulation64.com/files/0.5/
DISTFILES = $(DISTNAME).tar.bz2 config.h
PATCHFILES = $(DISTNAME).patch.gar $(DISTNAME)-gcc4.2.patch
PATCHFILES += $(DISTNAME)-fixdeps.patch 
LICENSE = GPL

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/libpng lib/SDL utils/gzip lib/gtk xorg/xorg
BUILDDEPS = devel/nasm

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-sdl-prefix="$(DESTDIR)$(prefix)" \
	--with-sdl-exec-prefix="$(DESTDIR)$(prefix)" \
	--disable-sdltest \
	--without-star \
	--with-x

SDL_FLAGS = $(shell $(DESTDIR)$(bindir)/sdl-config --cflags)
SDL_LIBS = $(shell $(DESTDIR)$(bindir)/sdl-config --libs)
FREETYPE_FLAGS = $(shell $(DESTDIR)$(bindir)/freetype-config --cflags)
FREETYPE_LIBS = $(shell $(DESTDIR)$(bindir)/freetype-config --libs)
GTK_FLAGS	=$(shell $(DESTDIR)$(bindir)/gtk-config --cflags)
GTK_LIBS	=$(shell $(DESTDIR)$(bindir)/gtk-config --libs)
GTHREAD_LIBS	=$(shell $(DESTDIR)$(bindir)/gtk-config --libs gtk gthread)

BUILD_OVERRIDE_DIRS = CC CXX SDL_FLAGS SDL_LIBS \
	FREETYPE_FLAGS FREETYPE_LIBS GTK_FLAGS GTK_LIBS GTHREAD_LIBS 
BUILD_ARGS = \
	OPT_FLAGS='$(CFLAGS)' \
	GL_PATH="$(DESTDIR)$(includedir)" 

INSTALL_ARGS = PREFIX='$(DESTDIR)$(prefix)/' 

include ../../gar.mk

pre-build:
	cp -f $(DOWNLOADDIR)/config.h $(WORKSRC)
	@$(MAKECOOKIE)
	
	

