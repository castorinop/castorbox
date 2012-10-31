GARNAME = supertux
GARVERSION = 0.3.0
CATEGORIES = games
MASTER_SITES = http://download.berlios.de/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += SuperTux.png SuperTux.sh
PATCHFILES = $(GARNAME).patch.gar
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c lib/SDL lib/libogg lib/libvorbis xorg/xorg \
	games/SDL_image games/physfs games/openal
BUILDDEPS = games/jam

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = custom
INSTALL_SCRIPTS   = custom launcher

CONFIGURE_ARGS = $(DIRPATHS) DESTDIR=$(DESTDIR) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/$(prefix) \
  	--with-vorbis=$(DESTDIR) \
	--with-ogg=$(DESTDIR) \
	--with-libphysfs=$(DESTDIR)$(games_prefix) \
	--with-libOpenAL=$(DESTDIR)$(games_prefix) \
	--disable-debug \
	--with-x \
	--with-gnu-ld \
	CFLAGS="-I$(DESTDIR)/$(games_includedir)/SDL $(CFLAGS)" \
	CPPFLAGS="-I$(DESTDIR)/$(games_includedir)/SDL $(CPPFLAGS)" \
	CXXFLAGS="-I$(DESTDIR)/$(games_includedir)/SDL $(CXXFLAGS)"

include ../../gar.mk
include ../games.mk

PARALLELMFLAGS := -j1

build-custom:
	@cd $(WORKSRC) && $(BUILD_ENV) jam -dx
	@$(MAKECOOKIE)

install-custom:
	@cd $(WORKSRC) && $(BUILD_ENV) jam install
	@$(MAKECOOKIE)

install-launcher:
	@cp -rf $(WORKDIR)/SuperTux.* $(DESTDIR)$(games_launcher)/
	@$(MAKECOOKIE)
