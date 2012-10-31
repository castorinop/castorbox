GARNAME = service.watchdog
GARVERSION = 739e683a7d
CATEGORIES = themes
#MASTER_SITES = git://github.com/BigNoid/Aeon-Nox.git/
MASTER_SITES = https://github.com/downloads/takoi/xbmc-addon-library-watchdog/
#MASTER_SITES = git://lirc.git.sourceforge.net/gitroot/lirc/lirc/
DISTNAME := $(GARNAME)
DISTFILES = $(DISTNAME).zip
#PATCHFILES = \
#	$(DISTNAME)-lirc_xbox.patch \
#	$(DISTNAME)-disable_lirc_i2c.patch \
#	$(DISTNAME)-remove_smp_lock_h.patch \
#	$(DISTNAME)-bit_le_fix.patch \
#	$(DISTNAME)-kfifo_fix.patch \
#	$(DISTNAME)-uinput_key_fix.patch \
#	$(DISTNAME)-input_map.patch.gar
LICENSE = GPL3

DESCRIPTION =
define BLURB
endef

#DEPENDS = lang/c kernel/kernel lib/alsa-lib lib/libftdi lib/libirman lib/libusb-compat xorg/xorg

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
#BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(includedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--enable-shared \
	--disable-static \
	--enable-sandboxed \
	--with-gnu-ld \
	--with-x \
	--with-kerneldir="$(DESTDIR)$(LINUX_SOURCEDIR)" \
	--with-moduledir="$(LINUX_MODULESDIR)/misc/lirc" \
	--with-driver=all \
	--with-transmitter \
	--with-syslog
BUILD_ARGS     = $(LINUX_MAKE_ARGS)
INSTALL_ARGS   = $(LINUX_MAKE_ARGS)

CONFIGURE_ENV = $(LINUX_MAKE_ENV)
BUILD_ENV     = $(LINUX_MAKE_ENV)
INSTALL_ENV   = $(LINUX_MAKE_ENV)

GAR_EXTRA_CONF += kernel-$(mm_KERNEL_VERSION)/linux/package-api.mk
include ../../gar.mk

PARALLELMFLAGS := -j1

git//%$(DISTNAME).tar.bz2:
	@$(call FETCH_GIT, $*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

x-checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

install-custom:
	mkdir -p $(DESTDIR)$(datadir)/xbmc/addons/$(GARNAME)
	cp -a $(WORKSRC)/* $(DESTDIR)$(datadir)/xbmc/addons/$(GARNAME)/
	$(MAKECOOKIE)

