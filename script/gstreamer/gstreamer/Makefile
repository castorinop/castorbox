GARNAME = gstreamer
GARVERSION = 0.10.x
CATEGORIES = lib

DEPENDS = gstreamer/gstreamer-core \
	gstreamer/gst-plugins-base \
	gstreamer/gst-plugins-good \
	gstreamer/gst-plugins-ugly
#	lib/gst-ffmpeg

include ../../gar.mk

clean-all: $(addprefix clean-,$(subst /,_,$(DEPENDS)))
	@rm -rf $(DESTDIR)$(libdir)/libgst*
	@rm -rf $(DESTDIR)$(libdir)/gstreamer-0.10
	@$(MAKE) clean

clean-%:
	@$(MAKE) -C $(GARDIR)/$(subst _,/,$*) clean


