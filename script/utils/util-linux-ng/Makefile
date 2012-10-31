GARNAME = util-linux-ng
GARVERSION = 2.16.1
CATEGORIES = utils
MASTER_SITES = ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.16/
DISTFILES = $(DISTNAME).tar.bz2
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
	--enable-shared \
	--disable-static \
	--enable-tls \
	--enable-mount \
	--enable-fsck \
	--enable-uuidd \
	--enable-libblkid \
	--enable-nls \
	--disable-rpath \
	--enable-arch \
	--enable-agetty \
	--enable-cramfs \
	--enable-switch-root \
	--disable-elvtune \
	--disable-init \
	--disable-kill \
	--disable-last \
	--disable-mesg \
	--disable-partx \
	--disable-raw \
	--disable-rdev \
	--enable-rename \
	--disable-reset \
	--disable-login-utils \
	--enable-schedutils \
	--enable-wall \
	--disable-write \
	--enable-chsh-only-listed \
	--disable-login-chown-vcs \
	--disable-login-stat-mail \
	--enable-pg-bell \
	--enable-require-password \
	--disable-use-tty-group \
	--disable-makeinstall-chown \
	--with-gnu-ld

BUILD_ARGS     = \
	usrbinexecdir=$(bindir) \
	usrsbinexecdir=$(sbindir)
INSTALL_ARGS   = \
	usrbinexecdir=$(bindir) \
	usrsbinexecdir=$(sbindir)

include ../../gar.mk

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libblkid.la
	@rm -f $(DESTDIR)$(libdir)/libuuid.la
	@$(MAKECOOKIE)
