GARNAME = syslinux
GARVERSION = 5.01
CATEGORIES = net
MASTER_SITES = ftp://ftp.kernel.org/pub/linux/utils/boot/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

ARCH=$(if $(filter i386  ,$(mm_GARCH_FAMILY)),-m32) \
     $(if $(filter x86_64,$(mm_GARCH_FAMILY)),-m64)  
DEPENDS   = lang/c

BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = custom

BUILD_ARGS = CC=$(CC) LD="$(LD)" OPTFLAGS='$(ARCH) -g -Os -static' LDFLAGS="-static" ISUBDIRS='libinstaller extlinux' BSUBDIRS='core mbr'

include ../../gar.mk

pre-build:
	rm -f $(WORKSRC)/extlinux/extlinux
	@$(MAKECOOKIE)

install-custom:
	@cp -f $(WORKSRC)/extlinux/extlinux $(DESTDIR)$(esbindir)
	@$(MAKECOOKIE)
