GARNAME = mms
GARVERSION = 1.1.x-libmms
DISTNAME = $(GARVERSION)

CATEGORIES = mms
MASTER_SITES = bzr:///home/pablo/build/mms/castorbox/
MASTER_SITES += bzr-lp://lp:~castorinop/mms/cbx-mms-1.1.x/
MASTER_SITES += http://www.csps.com.ar/castorbox/garchive/$(DISTNAME)/
MASTER_SITES += bzr-http://www.csps.com.ar/mms/bzr/mms-cbx/
#http://www.csps.com.ar/gar-castorbox/mms/
DISTFILES = $(GARVERSION).tar.bz2 libtool config.h config.mak
#castorbox-theme.tar.bz2 eYe_Candy.tar.bz2
#PATCHFILES = fix-opengl.patch
PATCHFILES += window-video-left-bottom.patch
PATCHFILES += fix-mplayer-2files.patch
#PATCHFILES += fix-gstreamer_restore_device-001.patch
#PATCHFILES += new-lyrics.004.patch
PATCHFILES += external-program-transission.002.patch
PATCHFILES += fix-exclusive_access.patch
PATCHFILES += fix-startup-dbus.001.patch
#PATCHFILES += fix-series_startup.patch
PATCHFILES += sqlite-verbose_error.diff
#PATCHFILES += fix-mediarss.patch
PATCHFILES += mms-dpms.002.patch
PATCHFILES += media_rss-helper.001.patch
PATCHFILES += series-fix_cover.001.patch
PATCHFILES += mms-libmms.001.patch
PATCHFILES += cross-fix.diff
PATCHFILES = 
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/cxx \
	utils/findutils \
	utils/termcap \
	utils/inotify-tools \
	system/lirc \
	mediaplayers/alsaplayer \
	net/wget 

LIBDEPS = db/sqlite \
	lib/pcre \
	lib/ncurses \
	lib/taglib \
	lib/commoncpp \
	lib/SDL \
	lib/imlib2 \
	lib/ffmpeg \
	lib/dbus-cxx \
	lib/boost

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
BUILD_SCRIPTS     += $(WORKSRC)/plugins/feature/weather-com/Makefile
BUILD_SCRIPTS     += $(WORKSRC)/plugins/feature/dbus/Makefile
BUILD_SCRIPTS     += $(WORKSRC)/plugins/feature/media-rss/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   += $(WORKSRC)/plugins/feature/weather-com/Makefile
INSTALL_SCRIPTS   += $(WORKSRC)/plugins/feature/dbus/Makefile


CONFIGURE_ENV  = \
	DESTDIR="$(DESTDIR)"
BUILD_ENV  = \
	DESTDIR="$(DESTDIR)"

CONFIGURE_ARGS = \
	--host=$(GARHOST) \
	--prefix=$(prefix) \
	--config=$(sysconfdir) \
        --disable-epg \
	--disable-xine-audio \
	--enable-alsaplayer \
        --enable-opengl \
        --enable-notify-area \
        --enable-clock \
        --enable-game \
        --enable-lirc

BUILD_DIR="$(PWD)/../../$(CATEGORIES)/$(CATEGORIES)-$(word 1,$(subst -, ,$(GARVERSION)))/$(WORKSRC)"

BUILD_ARGS = BUILD_DIR="$(BUILD_DIR)" \
	AR="$(AR) mru" \
	C="$(CC)" \
	CC="$(CC)" \
	CXX="$(CXX)" \
	LDFLAGS="" \
	LD="$(LD)" \
	DESTDIR="$(DESTDIR)" \
	DEBUG=$(mm_DEBUG) \
	OPTIMIZATION="" \
	STDFLAGS="$(CXXFLAGS) -funroll-loops -fomit-frame-pointer -pthread -I. -I$(DESTDIR)$(includedir) -DSUPERUSER" \
	LIBTOOL="$(SHELL) $(BUILD_DIR)/libtool" \
	PKGCONFIG="pkg-config" \
	IMLIB2CONFIG="$(DESTDIR)$(bindir)-config/imlib2-config" \
	SDLCONFIG="$(DESTDIR)$(bindir)-config/sdl-config" 

INSTALL_ARGS = $(BUILD_ARGS)
# -L$(DESTDIR)$(libdir)"

include ../../gar.mk

PARALLELMFLAGS := -j1

cp-extract-%:
	@echo " ==> Copying $(DOWNLOADDIR)/$*"
	@cp $(DOWNLOADDIR)/$* $(WORKSRC)/
	@$(MAKECOOKIE)

bzr//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_BZR, file://$*/, $(word 2,$(subst -, ,$(GARVERSION))), $(DISTNAME))
	@$(MAKECOOKIE)

bzr-lp//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_BZR, $*/, $(word 2,$(subst -, ,$(GARVERSION))), $(DISTNAME))
	@$(MAKECOOKIE)

bzr-http//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_BZR, http://$*/, $(word 2,$(subst -, ,$(GARVERSION))), $(DISTNAME))
	@$(MAKECOOKIE)

checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

patch-Domestic_Manners.ttf:
	@cp $(DOWNLOADDIR)/Domestic_Manners.ttf $(WORKSRC)/fonts

extract-weather_com.tar.bz2:
	@bzip2 -dc $(DOWNLOADDIR)/weather_com.tar.bz2 | tar -xf - -C $(WORKSRC)
	@$(MAKECOOKIE)

#post-extract:
#	@cp -af $(WORKDIR)/castorbox $(WORKSRC)/themes
#	@cp -af $(WORKDIR)/eYe\ Candy $(WORKSRC)/themes/eYeCandy
#	@$(MAKECOOKIE)

#pre-configure:
#	@cd $(WORKSRC) && autoreconf --force --install 
#	@$(MAKECOOKIE)

pre-build:
	sed -i "s@^version=\"\(.*\)\"@version=\"\1 + castorbox revno: $(GARREVISION)\"@g" $(WORKSRC)/version.sh
	@$(MAKECOOKIE)

pre-install:
	@#Purge previous configuation
	@rm -rf $(DESTDIR)/etc/mms-1.1.0/ 
	@$(MAKECOOKIE)
