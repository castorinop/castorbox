GARNAME = cdparanoia
GARVERSION = III-alpha9.8
CATEGORIES = lib
MASTER_SITES = http://www.xiph.org/paranoia/download/
DISTFILES = $(DISTNAME).src.tgz config.cache.$(GARCH_FAMILY)
PATCHFILES = $(DISTNAME).patch $(DISTNAME)-gcc-3.4.x.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST)
BUILD_ARGS     = \
	CPPFLAGS="$(CPPFLAGS)" \
	FLAGS="$(CFLAGS)" \
	OPT="$(CFLAGS)" \
	LDFLAGS="$(LDFLAGS)"

INSTALL_OVERRIDE_DIRS = prefix exec_prefix BINDIR MANDIR INCLUDEDIR LIBDIR

BINDIR     = $(bindir)
MANDIR     = $(mandir)
INCLUDEDIR = $(includedir)
LIBDIR     = $(libdir)

include ../../gar.mk

extract-config.cache.$(GARCH_FAMILY):
	@cp $(DOWNLOADDIR)/config.cache.$(GARCH_FAMILY) $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

pre-configure:
	@cp -f $(build_DESTDIR)$(build_datadir)/libtool/config.sub $(WORKSRC)/configure.sub
	@$(MAKECOOKIE)
