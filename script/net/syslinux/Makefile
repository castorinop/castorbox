GARNAME = syslinux
GARVERSION = 4.05
CATEGORIES = net
MASTER_SITES = http://www.kernel.org/pub/linux/utils/boot/$(GARNAME)/4.xx/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/c

BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = custom

BUILD_ARGS = CC=$(CC) LD="$(LD)" OPTFLAGS='-m32 -g -Os -static' LDFLAGS="-static" ISUBDIRS='libinstaller extlinux' BSUBDIRS='core mbr'

include ../../gar.mk

pre-build:
	rm -f $(WORKSRC)/extlinux/extlinux
	@$(MAKECOOKIE)

install-custom:
	@cp -f $(WORKSRC)/extlinux/extlinux $(DESTDIR)$(esbindir)
	@$(MAKECOOKIE)
