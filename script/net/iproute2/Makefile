GARNAME = iproute2
GARVERSION = 2.6.29
CATEGORIES = net
MASTER_SITES = http://devresources.linux-foundation.org/dev/iproute2/download/
DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES = $(DISTNAME)-cross_compiling.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile



GAR_EXTRA_CONF += kernel-headers/linux-headers-$(KERNEL_VERSION)/linux/package-api.mk

CONFIGURE_ARGS = $(DESTDIR)$(includedir)/linux
BUILD_ARGS = CC="$(CC)" HOSTCC="$(CC)" CCOPTS="$(CFLAGS) -I$(DESTDIR)$(includedir)" LDFLAGS="$(LDFLAGS)" KERNEL_INCLUDE="$(DESTDIR)$(includedir)/linux"
INSTALL_ARGS = DESTDIR=$(DESTDIR)$(prefix)

include ../../gar.mk
