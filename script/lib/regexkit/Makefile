GARNAME = pcre++
GARVERSION = 0.9.5
CATEGORIES = lib
MASTER_SITES = http://www.daemon.de/files/mirror/ftp.daemon.de/scip/Apps/pcre++/
DISTFILES = $(DISTNAME).tar.gz 

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = \
	--prefix=$(prefix) \
	--exec_prefix=$(exec_prefix) \
     	--libdir=$(libdir) \
	--includedir=$(includedir) \
	--shared
BUILD_ARGS     = \
	LIBS="libz.a libz.so.1.2.3"
INSTALL_ARGS   = \
	LIBS="libz.a libz.so.1.2.3"

INSTALL_OVERRIDE_DIRS = prefix exec_prefix libdir includedir mandir

include ../../gar.mk

CFLAGS := $(CFLAGS) -fPIC
AR     := $(AR) -rc
