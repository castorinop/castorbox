GARNAME = busybox
GARVERSION = $(BUSYBOX_VERSION)
CATEGORIES = utils
MASTER_SITES = http://www.busybox.net/downloads/
MASTER_SITES += http://www.busybox.net/downloads/fixes-$(GARVERSION)/
CONFIGFILE = $(DISTNAME).config
DISTFILES = $(DISTNAME).tar.bz2 $(CONFIGFILE)
PATCHFILES  =
PATCHFILES += $(DISTNAME)-check_cc.patch $(DISTNAME)-dhcp_log_server.patch $(DISTNAME)-dhcp_tcode.patch $(DISTNAME)-tftp_timeout.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

GAR_EXTRA_CONF += utils/busybox/package-api.mk

include ../../gar.mk
include build-api.mk
