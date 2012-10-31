GARNAME = dropbear
GARVERSION = 0.49
CATEGORIES = net
MASTER_SITES = http://matt.ucc.asn.au/dropbear/releases/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-urandom.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/zlib

CONFIGURE_SCRIPTS  = $(WORKSRC)/configure
BUILD_SCRIPTS      = $(WORKSRC)/Makefile
INSTALL_SCRIPTS    = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST)

include ../../gar.mk
