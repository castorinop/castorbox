GARNAME = libgcrypt
GARVERSION = 1.4.5
CATEGORIES = utils
MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)_notests.patch
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c testing/libgpg-error

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gpg-error-prefix=$(DESTDIR)$(prefix) \
	--with-gnu-ld

include ../../gar.mk

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libgcrypt.la
	@$(MAKECOOKIE)
