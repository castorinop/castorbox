GARNAME = dosbox
GARVERSION = 0.70
CATEGORIES = emulators
MASTER_SITES = http://superb-east.dl.sourceforge.net/sourceforge/$(GARNAME)/
#MASTER_SITES = svn://svn.bountysource.com/zsnes/trunk/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/cxx lib/libpng lib/SDL lib/SDL_net lib/SDL_sound xorg/xorg

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--disable-sdltest \
	--enable-libpng  \
	--disable-debugger \
	--enable-opengl  \
	--enable-jma \
	--disable-cpucheck \
	$(if $(filter yes,$(mm_DEBUG)),--enable-debug,--disable-debug) \
	$(if $(filter no,$(mm_DEBUG)),--enable-release,--disable-release) \
	--with-sdl-prefix="$(DESTDIR)$(prefix)" \
	--with-sdl-exec-prefix="$(DESTDIR)$(prefix)" \
	--with-zlib-prefix="$(DESTDIR)$(prefix)" \
	--with-x

include ../../gar.mk

