GARNAME = xorg
GARVERSION = $(XORG_VERSION)
CATEGORIES = $(CATEGORY)
LICENSE =

DESCRIPTION = 
define BLURB
endef

DEPENDS = \
	$(CATEGORY)/font-alias \
	$(CATEGORY)/font-bh-ttf \
	$(CATEGORY)/font-cursor-misc \
	$(CATEGORY)/font-misc-misc \
	$(CATEGORY)/freeglut \
	$(CATEGORY)/glew \
	$(CATEGORY)/iceauth \
	$(CATEGORY)/libX11 \
	$(CATEGORY)/libXdamage \
	$(CATEGORY)/libXext \
	$(CATEGORY)/libXfixes \
	$(CATEGORY)/libXft \
	$(CATEGORY)/libXinerama \
	$(CATEGORY)/libXmu \
	$(CATEGORY)/libXpm \
	$(CATEGORY)/libXrandr \
	$(CATEGORY)/libXrender \
	$(CATEGORY)/libXres \
	$(CATEGORY)/libXt \
	$(CATEGORY)/libXtst \
	$(CATEGORY)/Mesa \
	$(CATEGORY)/mesa-demos \
	$(CATEGORY)/mkfontdir \
	$(CATEGORY)/mkfontscale \
	$(CATEGORY)/rgb \
	$(CATEGORY)/xcb-util-keysyms \
	$(CATEGORY)/xdpyinfo \
	$(CATEGORY)/xev \
	$(if $(filter-out build, $(DESTIMG)), \
		$(CATEGORY)/xf86-input-evdev \
		$(CATEGORY)/xf86-input-void \
		$(CATEGORY)/xf86-video-ati \
		$(if $(filter i386  ,$(GARCH_FAMILY)), $(CATEGORY)/xf86-video-geode) \
		$(CATEGORY)/xf86-video-intel \
		$(CATEGORY)/xf86-video-nouveau \
		$(CATEGORY)/xf86-video-openchrome \
		$(CATEGORY)/xf86-video-savage \
		$(CATEGORY)/xf86-video-sis \
		$(CATEGORY)/xf86-video-vmware \
	) \
	$(CATEGORY)/xinit \
	$(CATEGORY)/xkbcomp \
	$(CATEGORY)/xkeyboard-config \
	$(CATEGORY)/xlsclients \
	$(CATEGORY)/xmodmap \
	$(CATEGORY)/xorg-server \
	$(CATEGORY)/xrandr \
	$(CATEGORY)/xset \
	$(CATEGORY)/xsetroot

CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

include ../../gar.mk

post-install:
	@rm -rf $(DESTDIR)$(versiondir)/$(GARNAME)
	@rm -rf $(DESTDIR)$(licensedir)/$(GARNAME)
	@$(MAKECOOKIE)
