GARNAME = dgen-sdl
GARVERSION = 1.23
CATEGORIES = emulators
MASTER_SITES = http://pknet.com/~joe/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME).patch.gar
LICENSE = BSD

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/libpng lib/SDL utils/gzip xorg/xorg
BUILDDEPS = devel/nasm

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
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

include ../../gar.mk

