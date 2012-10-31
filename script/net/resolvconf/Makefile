GARNAME = resolvconf
GARVERSION = 1.44
MASTER_SITES = http://ftp.de.debian.org/debian/pool/main/r/resolvconf/
CATEGORIES = net
DISTFILES = $(GARNAME)_$(GARVERSION).tar.gz
PATCHFILES = $(DISTNAME)-busybox.patch \
	$(DISTNAME)-path.patch
LICENSE = LGPL2

DESCRIPTION = 
define BLURB
endef

INSTALL_SCRIPTS = custom

include ../../gar.mk

install-custom:
	@mkdir -p $(DESTDIR)$(elibdir)/resolvconf
	@mkdir -p $(DESTDIR)$(sysconfdir)/resolvconf/run/interface
	@cp -a $(WORKSRC)/etc/* $(DESTDIR)$(sysconfdir)
	@cp -a $(WORKSRC)/bin/resolvconf $(DESTDIR)$(esbindir)/
	@cp -a $(WORKSRC)/bin/list-records $(DESTDIR)$(elibdir)/resolvconf
	@touch $(DESTDIR)$(sysconfdir)/resolvconf/run/enable-updates
	@$(MAKECOOKIE)


	
