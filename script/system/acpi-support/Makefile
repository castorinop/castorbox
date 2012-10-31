GARNAME = acpi_support
GARVERSION = 186
CATEGORIES = system
MASTER_SITES = bzr-lp://lp:acpi-support/
DISTFILES = $(DISTNAME).tar.bz2
#castorbox-theme.tar.bz2 eYe_Candy.tar.bz2
#PATCHFILES = fix-opengl.patch
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

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

include ../../gar.mk

bzr-lp//%/$(DISTNAME).tar.bz2:
	@echo $*/ $(GARVERSION), $(DISTNAME)
	$(call FETCH_BZR, $*, $(GARVERSION), $(DISTNAME))
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
	@echo glib_FLAGS	= `pkg-config --cflags	glib-2.0`	>> $(WORKSRC)/config.mak
	@echo glib_LIBS		= `pkg-config --libs    glib-2.0`	>> $(WORKSRC)/config.mak
	@echo gstreamer_FLAGS	= `pkg-config --cflags  gstreamer-0.10`	>> $(WORKSRC)/config.mak
	@echo gstreamer_LIBS	= `pkg-config --libs    gstreamer-0.10`	>> $(WORKSRC)/config.mak
	@echo imlib_FLAGS	= `imlib2-config --cflags`		>> $(WORKSRC)/config.mak
	@echo imlib_LIBS	= `imlib2-config --libs`		>> $(WORKSRC)/config.mak
	@echo sdl_FLAGS		= `sdl-config --cflags`			>> $(WORKSRC)/config.mak
	@echo sdl_LIBS		= `sdl-config --libs`			>> $(WORKSRC)/config.mak
	@echo taglib_FLAGS	= `pkg-config --cflags  taglib`		>> $(WORKSRC)/config.mak
	@echo taglib_LIBS	= `pkg-config --libs    taglib`		>> $(WORKSRC)/config.mak
	@echo xine_FLAGS	= `xine-config --cflags`		>> $(WORKSRC)/config.mak
	@echo xine_LIBS		= `xine-config --libs`			>> $(WORKSRC)/config.mak
	@echo ffmpeg_FLAGS	= `pkg-config --cflags libavcodec libavutil libswscale libavformat` >> $(WORKSRC)/config.mak
	@echo ffmpeg_LIBS	= `pkg-config --libs libavcodec libavutil libswscale libavformat`   >> $(WORKSRC)/config.mak
	@$(MAKECOOKIE)

pre-install:
	@#Purge previous configuation
	@rm -rf $(DESTDIR)/etc/mms-1.1.0/ 
	@$(MAKECOOKIE)
