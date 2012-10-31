GARNAME = libcap
GARVERSION = 2.17
CATEGORIES = net
MASTER_SITES = http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES += $(DISTNAME)-buildfix.patch
#PATCHFILES += $(DISTNAME)-remove-kernel-headers-workaround.patch

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

BUILD_ARGS = CC=$(CC) \
	CFLAGS="$(CFLAGS) -I$(DESTDIR)$(includedir)" \
	LDFLAGS="$(LDFLAGS)" \
	SYSTEM_HEADERS="$(DESTDIR)$(includedir)"

include ../../gar.mk

post-install:
	@mv $(DESTDIR)$(bindir)/transmissioncli $(DESTDIR)$(bindir)/transmission-cli
	@$(MAKECOOKIE)
