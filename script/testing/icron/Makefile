GARNAME = incron
GARVERSION = 0.5.7
CATEGORIES = lib
MASTER_SITES = http://inotify.aiken.cz/download/incron/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx 

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS = CXX="$(CXX)" \
	CXXFLAGS="$(CXXFLAGS)" \
	LDFLAGS="$(LDFLAGS)"
INSTALL_ARGS = USER="$(USER)" \
	PREFIX="$(DESTDIR)" \
	USERDATADIR="$(DESTDIR)$(localstatedir)/spool/incron" \
	SYSDATADIR="$(DESTDIR)$(sysconfdir)/incron.d" \
	CFGDIR="$(DESTDIR)$(sysconfdir)" \
	MANPATH="$(DESTDIR)$(mandir)"

include ../../gar.mk

