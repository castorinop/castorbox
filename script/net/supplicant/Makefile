GARNAME = wpa_supplicant
GARVERSION = 0.6.9
CATEGORIES = net
MASTER_SITES = http://hostap.epitest.fi/releases/
DISTFILES = $(DISTNAME).tar.gz $(DISTNAME).config
LICENSE = LGPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/openssl

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = $(WORKSRC)/wpa_supplicant/Makefile
INSTALL_SCRIPTS = custom

include ../../gar.mk

configure-custom:
	@cp $(WORKDIR)/$(DISTNAME).config $(WORKSRC)/wpa_supplicant/.config
	@$(MAKECOOKIE)

install-custom:
	@for i in wpa_cli wpa_supplicant; do \
		install -m 0755 $(WORKSRC)/wpa_supplicant/$$i  $(DESTDIR)$(bindir); \
	done
	@install -m 0644 $(WORKSRC)/wpa_supplicant/dbus-wpa_supplicant.conf $(DESTDIR)$(sysconfdir)/dbus-1/system.d/
	@install -m 0644 $(WORKSRC)/wpa_supplicant/dbus-wpa_supplicant.service $(DESTDIR)$(datadir)/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service
	@$(MAKECOOKIE)
