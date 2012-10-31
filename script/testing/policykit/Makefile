GARNAME = PolicyKit
GARVERSION = 0.9
CATEGORIES = lib
MASTER_SITES = http://ftp.de.debian.org/debian/pool/main/p/policykit/
DISTFILES = policykit_$(GARVERSION).orig.tar.gz
PATCHFILES= $(DISTNAME)-pam-headers.patch $(DISTNAME)-pk_debug.patch
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/COPYING

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/glib lib/dbus-glib lib/expat

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-authdb=dummy \
	--with-authfw=none \
	--with-os-type=redhat \
	--with-polkit-user=nobody \
	--with-polkit-group=nogroup \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libpolkit-dbus.la
	@rm -f $(DESTDIR)$(libdir)/libpolkit-grant.la
	@rm -f $(DESTDIR)$(libdir)/libpolkit.la
	@$(MAKECOOKIE)
	

