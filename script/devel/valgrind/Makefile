GARNAME = valgrind
GARVERSION = 3.2.1
CATEGORIES = devel
MASTER_SITES = http://valgrind.org/downloads/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c devel/gdb

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	$(if $(filter x86_64,$(GARCH_FAMILY)),--enable-only64bit) \
	$(if $(filter i386,  $(GARCH_FAMILY)),--enable-only32bit) \
	--enable-tls
BUILD_ARGS     = \
	AR="$(AR)"
INSTALL_ARGS   = \
	AR="$(AR)"

CONFIGURE_ENV = \
	GDB=$(DESTDIR)$(bindir)/gdb

include ../../gar.mk
