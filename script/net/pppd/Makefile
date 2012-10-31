GARNAME = ppp
GARVERSION = 2.4.4
CATEGORIES = lib
MASTER_SITES = ftp://ftp.samba.org/pub/ppp/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
LICENSE = LGPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld

BUILD_ARGS = CC="$(CC)" COPTS="$(CFLAGS)"
INSTALL_ARGS = $(BUILD_ARGS) DESTDIR=$(DESTDIR)$(prefix)  BINDIR=$(DESTDIR)$(esbindir) INCDIR=$(DESTDIR)$(includedir) ETCDIR=$(INSTROOT)$(sysconfdir)/ppp


include ../../gar.mk
