GARNAME = dhcp
GARVERSION = 4.1.0
MASTER_SITES =http://ftp.isc.org/isc/$(GARNAME)/
CATEGORIES = net
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/LICENSE

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-dhcpv6 \
	--with-gnu-ld


include ../../gar.mk

pre-configure:
	@echo "ac_cv_file__dev_random=yes" > $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

install-custom:
	@cp $(WORKSRC)/client/dhclient $(DESTDIR)$(esbindir)/
	@$(MAKECOOKIE)


	
