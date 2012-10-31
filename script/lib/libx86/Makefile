GARNAME = libx86
GARVERSION = 1.1
CATEGORIES = lib
MASTER_SITES = http://www.codon.org.uk/~mjg59/libx86/downloads/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-ifmask.patch
#PATCHFILES = $(DISTNAME)-fix_install.patch
LICENSE = GPL

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile


BUILD_ARGS = CFLAGS="$(CFLAGS)" CC="$(CC)"
BUILD_ARGS += $(if $(filter x86_64,$(GARCH_FAMILY)), BACKEND="x86emu")

include ../../gar.mk

