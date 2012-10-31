GARNAME = regionset
GARVERSION = 0.1
CATEGORIES = utils
MASTER_SITES = http://linvdr.org/download/regionset/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

BUILD_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = custom

BUILD_ARGS = \
	CC="$(CC) $(CFLAGS)"

include ../../gar.mk

install-custom:
	@mkdir -p $(DESTDIR)$(bindir)
	@cp -f $(WORKSRC)/regionset $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)
