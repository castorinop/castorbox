GARNAME = speex
GARVERSION = 1.2rc1
CATEGORIES = lib
MASTER_SITES = http://downloads.xiph.org/releases/speex/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-strip_owner.patch
LICENSE = MIT_Modified

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS  = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld

INSTALL_ARGS = INSTALL_ROOT="$(DESTDIR)"

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/libspeex.la
	@rm -f $(DESTDIR)$(libdir)/libspeexdsp.la
	@$(MAKECOOKIE)
