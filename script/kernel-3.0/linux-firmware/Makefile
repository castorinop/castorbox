GARNAME = linux-firmware
GARVERSION = 20110709
CATEGORIES = kernel-3.0
MASTER_SITES = http://www.kernel.org/pub/linux/kernel/people/dwmw2/firmware/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE =

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c kernel-3.0/linux

INSTALL_SCRIPTS = custom

include ../../gar.mk

install-custom:
	@mkdir -p $(DESTDIR)$(elibdir)/firmware/
	@cp -Rdf $(WORKSRC)/* $(DESTDIR)$(elibdir)/firmware/
	@$(MAKECOOKIE)
