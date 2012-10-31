GARNAME = vsftpd
GARVERSION = 2.2.0
CATEGORIES = net
MASTER_SITES = ftp://vsftpd.beasts.org/users/cevans/
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
	--without-gtk \
	--with-gnu-ld 

BUILD_ARGS = CC=$(CC) CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"

include ../../gar.mk

post-install:
	@mv $(DESTDIR)$(bindir)/transmissioncli $(DESTDIR)$(bindir)/transmission-cli
	@$(MAKECOOKIE)
