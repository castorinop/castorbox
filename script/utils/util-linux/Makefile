GARNAME = util-linux
GARVERSION = 2.22.1
CATEGORIES = utils
MASTER_SITES  = ftp://ftp.kernel.org/pub/linux/utils/util-linux/v2.22/
MASTER_SITES += ftp://ftp.infradead.org/pub/util-linux/v2.22/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-agetty_2.19.1.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/ncursesw lib/zlib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--bindir=$(ebindir) \
	--sbindir=$(esbindir) \
	--libdir=$(elibdir) \
	--cache-file=config.cache \
	--disable-silent-rules \
	--enable-shared \
	--disable-static \
	--disable-gtk-doc \
	--enable-nls \
	--disable-rpath \
	--enable-tls \
	--enable-libuuid \
	--enable-libblkid \
	--enable-libmount \
	--disable-deprecated-mount \
	--enable-mount \
	--disable-fsck \
	--disable-partx \
	--enable-uuidd \
	--disable-mountpoint \
	--disable-fallocate \
	--disable-unshare \
	--enable-arch \
	--disable-ddate \
	--disable-eject \
	--enable-agetty \
	--enable-cramfs \
	--enable-switch-root \
	--disable-pivot-root \
	--disable-elvtune \
	--disable-kill \
	--disable-last \
	--disable-utmpdump \
	--disable-line \
	--disable-mesg \
	--disable-raw \
	--enable-rename \
	--disable-reset \
	--disable-vipw \
	--disable-newgrp \
	--disable-chfn-chsh \
	--enable-chsh-only-listed \
	--disable-login \
	--disable-login-chown-vcs \
	--disable-login-stat-mail \
	--disable-sulogin \
	--disable-su \
	--disable-schedutils \
	--disable-wall \
	--disable-write \
	--disable-chkdupexe \
	--disable-socket-activation \
	--enable-pg-bell \
	--enable-require-password \
	--disable-use-tty-group \
	--disable-makeinstall-chown \
	--disable-makeinstall-setuid \
	--with-gnu-ld \
	--without-selinux \
	--without-audit \
	--without-udev \
	--without-slang \
	--without-utempter \
	--without-systemdsystemunitdir

BUILD_ARGS     = \
	usrbinexecdir=$(bindir) \
	usrsbinexecdir=$(sbindir)
INSTALL_ARGS   = \
	usrbinexecdir=$(bindir) \
	usrsbinexecdir=$(sbindir)

include ../../gar.mk

pre-configure:
	@$(call RUN_GETTEXTIZE)
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(if $(filter-out build,$(DESTIMG)),echo "scanf_cv_type_modifier=ms" >> $(WORKSRC)/config.cache)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libblkid.la
	@rm -f $(DESTDIR)$(libdir)/libmount.la
	@rm -f $(DESTDIR)$(libdir)/libuuid.la
	@$(MAKECOOKIE)
