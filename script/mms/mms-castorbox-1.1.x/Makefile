GARNAME = mms-castorbox
GARVERSION = 1.1.x-1792
GARREVISION = $(word 2,$(subst -, ,$(GARVERSION)))
CATEGORIES = mms
MASTER_SITES = bzr:///home/pablo/build/mms/castorbox/
MASTER_SITES += bzr-lp://lp:~castorinop/mms/cbx-mms-1.1.x/
MASTER_SITES += http://www.csps.com.ar/castorbox/garchive/$(DISTNAME)/
MASTER_SITES += bzr-http://www.csps.com.ar/mms/bzr/mms-cbx/
#http://www.csps.com.ar/gar-castorbox/mms/
DISTFILES = $(DISTNAME).tar.bz2 libtool config.h config.mak
#castorbox-theme.tar.bz2 eYe_Candy.tar.bz2
#PATCHFILES = fix-opengl.patch
PATCHFILES += window-video-left-bottom.patch
PATCHFILES += fix-mplayer-2files.patch
#PATCHFILES += fix-gstreamer_restore_device-001.patch
#PATCHFILES += new-lyrics.004.patch
PATCHFILES += external-program-transission.002.patch
PATCHFILES += fix-exclusive_access.patch
#PATCHFILES += fix-startup-dbus.001.patch
PATCHFILES += fix-compat_dbux_cxx_0.7.patch
#PATCHFILES += fix-series_startup.patch
PATCHFILES += sqlite-verbose_error.diff
#PATCHFILES += fix-mediarss.patch
PATCHFILES += mms-dpms.003.patch
PATCHFILES += media_rss-helper.001.patch
PATCHFILES += series-fix_cover.001.patch
#PATCHFILES += mms-libmms.002.patch
PATCHFILES += fix-mediarss_fetch_threads.002.patch
PATCHFILES += fix-mediarss_animations.001.patch
#PATCHFILES += fix-audio_exit_ssaver.001.patch
#PATCHFILES += fix-series_missing_info.004.patch
#PATCHFILES += fix-virtual_xml.001.patch
#PATCHFILES += mms-fix_series_db_concistency.001.patch
#PATCHFILES += mms-fix_series_download_without_name.001.patch
#PATCHFILES += mms-series_fix_multiple_items.001.patch
#PATCHFILES += mms-fix_build_movieplayers.001.patch
PATCHFILES += fix-disable_ffmpeg.001.patch
PATCHFILES += fix-mplayer_device.001.patch
PATCHFILES += mms-mediarss-fullregex_autodownload.002.patch
PATCHFILES += mms-series-bettertvdb_database.006.patch
PATCHFILES += mms-series-view_new_episodes.002.patch
PATCHFILES += mms-cmd_audio_plugin.001.patch
#PATCHFILES += fix-disable_cache_stat_fileSize.001.patch
PATCHFILES += fix-movie-play_fileSize.001.patch
PATCHFILES += fix-series-updateddb_segfault.patch
PATCHFILES += cross-fix.diff
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
	lib/boost \
	gstreamer/gstreamer \

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
BUILD_SCRIPTS     += $(WORKSRC)/plugins/feature/weather-com/Makefile
BUILD_SCRIPTS     += $(WORKSRC)/plugins/feature/dbus/Makefile
BUILD_SCRIPTS     += $(WORKSRC)/plugins/feature/media-rss/Makefile
BUILD_SCRIPTS     += $(WORKSRC)/plugins/feature/movie/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   += $(WORKSRC)/plugins/feature/weather-com/Makefile
INSTALL_SCRIPTS   += $(WORKSRC)/plugins/feature/dbus/Makefile

CONFIGURE_ARGS = $(DIRPATHS) \
	--prefix=$(prefix) \
	--config=$(sysconfdir) \
        --disable-epg \
        --enable-opengl \
        --enable-notify-area \
        --enable-clock \
        --enable-media-rss \
        --enable-ffmpeg-thumb \
        --enable-game \
        --enable-lirc

BUILD_DIR="$(PWD)/../../$(CATEGORIES)/$(GARNAME)-$(word 1,$(subst -, ,$(GARVERSION)))/$(WORKSRC)"

XTRA_FLAGS= -ffast-math -funroll-loops -fomit-frame-pointer -funit-at-a-time

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
	STDFLAGS="$(CXXFLAGS) $(XTRA_FLAGS) -pthread -pipe -D_GNU_SOURCE -I. -I$(DESTDIR)$(includedir) -DSUPERUSER" \
	LIBTOOL="$(SHELL) $(BUILD_DIR)/libtool" \
	PKGCONFIG="pkg-config" \
	IMLIB2CONFIG="$(DESTDIR)$(bindir)-config/imlib2-config" \
	SDLCONFIG="$(DESTDIR)$(bindir)-config/sdl-config" 

INSTALL_ARGS = $(BUILD_ARGS)
# -L$(DESTDIR)$(libdir)"

include ../../gar.mk

stats:
	echo $(BUILD_DIR)

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
	@sed -i "s@^version=\"\(.*\)\"@version=\"\1 + castorbox revno: $(GARREVISION)\"@g" $(WORKSRC)/version.sh
	@touch $(WORKSRC)/config.h
	@echo COMMONCPP2_CFLAGS	= `pkg-config --cflags	libccext2`	>> $(WORKSRC)/config.mak
	@echo COMMONCPP2_LIBS	= `pkg-config --libs	libccext2`	>> $(WORKSRC)/config.mak
	@echo glib_CFLAGS	= `pkg-config --cflags	glib-2.0`	>> $(WORKSRC)/config.mak
	@echo glib_LIBS		= `pkg-config --libs    glib-2.0`	>> $(WORKSRC)/config.mak
	@echo gstreamer_CFLAGS	= `pkg-config --cflags  gstreamer-0.10`	>> $(WORKSRC)/config.mak
	@echo gstreamer_LIBS	= `pkg-config --libs    gstreamer-0.10`	>> $(WORKSRC)/config.mak
	@echo imlib_CFLAGS	= `imlib2-config --cflags`		>> $(WORKSRC)/config.mak
	@echo imlib_LIBS	= `imlib2-config --libs`		>> $(WORKSRC)/config.mak
	@echo sdl_CFLAGS	= `sdl-config --cflags`			>> $(WORKSRC)/config.mak
	@echo sdl_LIBS		= `sdl-config --libs`			>> $(WORKSRC)/config.mak
	@echo taglib_CFLAGS	= `pkg-config --cflags  taglib`		>> $(WORKSRC)/config.mak
	@echo taglib_LIBS	= `pkg-config --libs    taglib`		>> $(WORKSRC)/config.mak
	@echo xine_CFLAGS	= `xine-config --cflags`		>> $(WORKSRC)/config.mak
	@echo xine_LIBS		= `xine-config --libs`			>> $(WORKSRC)/config.mak
	@echo ffmpeg_CFLAGS	= `pkg-config --cflags libavcodec libavutil libswscale libavformat` >> $(WORKSRC)/config.mak
	@echo ffmpeg_LIBS	= `pkg-config --libs libavcodec libavutil libswscale libavformat`   >> $(WORKSRC)/config.mak
	@$(MAKECOOKIE)

pre-install:
	@#Purge previous configuation
	@rm -rf $(DESTDIR)/etc/mms-1.1.0/ 
	@rm -rf $(DESTDIR)$(libdir)/mms 
	@$(MAKECOOKIE)
