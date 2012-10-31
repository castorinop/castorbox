GARNAME = boolstuff
GARVERSION = 0.1.12
CATEGORIES = lib
MASTER_SITES = http://perso.b2b2c.ca/sarrazip/dev/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-fix_gcc.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/libboolstuff-0.1.la
	@$(MAKECOOKIE)

