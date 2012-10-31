GARNAME = xorg
GARVERSION = $(mm_XORG_VERSION)
CATEGORIES = xorg
LICENSE =

DESCRIPTION = 
define BLURB
endef

DEPENDS = xorg-$(mm_XORG_VERSION)/xorg

include ../../gar.mk

post-install:
	@rm -rf $(DESTDIR)$(versiondir)/$(GARNAME)
	@rm -rf $(DESTDIR)$(licensedir)/$(GARNAME)
	@$(MAKECOOKIE)
