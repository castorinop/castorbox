GARNAME = gdbm
GARVERSION = 1.8.3
CATEGORIES = lib
MASTER_SITES = ftp://ftp.gnu.org/gnu/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-strip_owner.patch
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
	@rm -f $(DESTDIR)$(libdir)/libgdbm.la
	@$(MAKECOOKIE)

