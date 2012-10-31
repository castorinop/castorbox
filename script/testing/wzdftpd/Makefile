GARNAME = wzdftpd
GARVERSION = 0.8.3
CATEGORIES = net
MASTER_SITES = http://downloads.sourceforge.net/wzdftpd/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES += $(DISTNAME)-metainfo_title.002.patch
#PATCHFILES += $(DISTNAME)_changeset3827.patch
#PATCHFILES += $(DISTNAME)_changeset3837.patch

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/openssl

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 

BUILD_ARGS = CC=$(CC) \
	CFLAGS="$(CFLAGS)" \
	LDFLAGS="$(LDFLAGS)" \
	SYSTEM_HEADERS="$(DESTDIR)$(includedir)"


include ../../gar.mk

no-pre-configure:
	cd $(WORKSRC); autoreconf --force --install --verbose
	@$(MAKECOOKIE)

post-install:
	@mv $(DESTDIR)$(bindir)/transmissioncli $(DESTDIR)$(bindir)/transmission-cli
	@$(MAKECOOKIE)
