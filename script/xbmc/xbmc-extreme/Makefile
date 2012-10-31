GARNAME = xbmc
GARVERSION = extreme
CATEGORIES = gui
#MASTER_SITES = http://mirrors.xbmc.org/releases/source/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-crosscompiling.patch.gar
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx \
	  db/mysql \
	  lib/boost \
	  xbmc/enca \
	  xbmc/fribidi \
	  xbmc/jasper \
	  xbmc/libass \
	  lib/libcdio \
	  lib/faad2 \
	  lib/ffmpeg \
       	  xbmc/libmicrohttpd \
 	  xbmc/libmms \
	  xbmc/libmodplug \
	  lib/libmad \
	  lib/libmpeg2 \
	  lib/libsamplerate \
	  xbmc/libsmbclient \
	  lib/lzo \
	  lib/SDL \
	  games/SDL_image \
	  games/SDL_mixer \
	  lib/libtiff \
	  xbmc/wavpack \
	  xbmc/yajl \
	  python/python

BUILDDEPS = xbmc/cmake utils/zip

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

#~PYTHON_ARGS = PYTHON_LDFLAGS="-L$(DESTDIR)$(libdir) -lpython2.6" \
#	      PYTHON_CPPFLAGS="-I$(DESTDIR)$(includedir)/python2.6" 
PYTHON_ARGS = PYTHON=$(DESTDIR)$(bindir)/python \
	      LD_LIBRARY_PATH="$(DESTDIR)$(libdir):$(LD_LIBRARY_PATH)"

#	      PYTHON_SITE_PKG="$(DESTDIR)$(libdir)/python2.6/site-packages"

CONFIGURE_ARGS = $(PYTHON_ARGS) $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	-C \
	--enable-external-libraries \
	--enable-ffmpeg-libvorbis \
	--disable-optimizations \
	--disable-texturepacker \
	--disable-non-free
#no
#	--disable-debug \
#	--disable-ccache \
#	--disable-dvdcss \
#	--enable-goom 


include ../../gar.mk

# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS)) -L$(DESTDIR)$(libdir)
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS)) -L$(DESTDIR)$(libdir)
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS)) -L$(DESTDIR)$(libdir)



pre-configure:
	# remove prebuilt libraries
	find $(WORKSRC) -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -delete
	cd $(WORKSRC) && ./bootstrap
	echo "ac_cv_prog_HAVE_ZIP=true" > $(WORKSRC)/config.cache
	@$(call FIX_LIBTOOL_LIBPATH,$(WORKSRC),configure)
	@$(MAKECOOKIE)
