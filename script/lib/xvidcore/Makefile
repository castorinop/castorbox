GARNAME = xvidcore
GARVERSION = 1.3.2
CATEGORIES = lib
MASTER_SITES = http://downloads.xvid.org/downloads/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME).patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/c
BUILDDEPS = devel/nasm

WORKSRC = $(WORKDIR)/$(GARNAME)

CONFIGURE_SCRIPTS = $(WORKSRC)/build/generic/configure
BUILD_SCRIPTS     = $(WORKSRC)/build/generic/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/build/generic/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST)

include ../../gar.mk

API_MAJOR = $(shell cat $(WORKSRC)/build/generic/platform.inc | grep '^API_MAJOR=' | sed 's%^API_MAJOR=%%')
API_MINOR = $(shell cat $(WORKSRC)/build/generic/platform.inc | grep '^API_MINOR=' | sed 's%^API_MINOR=%%')

post-install:
	@rm -f $(DESTDIR)$(libdir)/libxvidcore.a
	@ln -sf libxvidcore.so.$(API_MAJOR).$(API_MINOR) $(DESTDIR)$(libdir)/libxvidcore.so.$(API_MAJOR)
	@ln -sf libxvidcore.so.$(API_MAJOR)              $(DESTDIR)$(libdir)/libxvidcore.so
	@$(MAKECOOKIE)
