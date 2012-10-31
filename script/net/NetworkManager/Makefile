GARNAME = NetworkManager
GARVERSION_TYPE= no_git
ifneq ("$(GARVERSION_TYPE)","git")
GARVERSION = 0.7.1
MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/$(GARNAME)/0.7/
PATCHFILES = \
	$(DISTNAME)-busybox_distro.patch \
	$(DISTNAME)-strip_doc.patch \
	$(DISTNAME)-polkit_disable.patch
else
GARVERSION = f43fdd9e154bac11dc4065f191d2b90afc9c43e3
MASTER_SITES = git://anongit.freedesktop.org/NetworkManager/NetworkManager.git/ 
PATCHFILES = \
	$(GARNAME)-strip_doc.patch \
	$(GARNAME)-polkit_disable.patch
endif

CATEGORIES = net
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
LICENSE = LGPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = system/hal utils/wireless-tools net/pppd net/supplicant net/dhcp
LIBDEPS = lib/libnl lib/nss disk/e2fsprogs lib/dbus-glib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-distro=debian \
	-C \
	--with-gnu-ld

include ../../gar.mk

git//%$(DISTNAME).tar.bz2:
	@$(call FETCH_GIT, $*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

x-checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE) 

x-pre-configure:
	@rm -f $(WORKSRC)/acinclude.m4
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)


post-install:
	@rm -f $(DESTDIR)$(libdir)/libnm_glib.la
	@rm -f $(DESTDIR)$(libdir)/libnm_glib_vpn.la
	@rm -f $(DESTDIR)$(libdir)/libnm-util.la
	@rm -f $(DESTDIR)$(libdir)/NetworkManager/libnm-settings-plugin-ifupdown.la
	@rm -f $(DESTDIR)$(libdir)/NetworkManager/libnm-settings-plugin-keyfile.la
	@rm -f $(DESTDIR)$(libdir)/pppd/*/nm-pppd-plugin.la
	@$(MAKECOOKIE)


	
