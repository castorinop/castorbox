GARNAME = aeon-nox
GARVERSION = bb4c242793
CATEGORIES = themes
MASTER_SITES = git://github.com/BigNoid/Aeon-Nox.git/
#MASTER_SITES = http://www.lirc.org/software/snapshots/
#MASTER_SITES = git://lirc.git.sourceforge.net/gitroot/lirc/lirc/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

#DEPENDS = lang/c kernel/kernel lib/alsa-lib lib/libftdi lib/libirman lib/libusb-compat xorg/xorg

INSTALL_SCRIPTS   = custom 

include ../../gar.mk


git//%$(DISTNAME).tar.bz2:
	@$(call FETCH_GIT, $*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

x-checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

install-custom:
	mkdir -p $(DESTDIR)$(datadir)/xbmc/addons/skin.$(GARNAME)
	cp -a $(WORKSRC)/* $(DESTDIR)$(datadir)/xbmc/addons/skin.$(GARNAME)/
	$(MAKECOOKIE)

