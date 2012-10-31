GARNAME = xkeyboard-config
GARVERSION = 1.9
CATEGORIES = $(CATEGORY)
MASTER_SITES  = http://xlibs.freedesktop.org/xkbdesc/
MASTER_SITES += http://people.freedesktop.org/~svu/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/COPYING

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c
BUILDDEPS = \
	perl/perl-XML-Parser

CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-xkbcomp-symlink \
	--enable-compat-rules \
	--enable-nls \
	--with-xkb-base="$(datadir)/X11/xkb"

CONFIGURE_ENV  = \
	XKBCOMP=$(bindir)/xkbcomp

GAR_EXTRA_CONF += $(CATEGORY)/xorg/package-api.mk
include ../../gar.mk
