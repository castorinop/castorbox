GARNAME = inotify-tools
GARVERSION = 3.14
CATEGORIES = utils
MASTER_SITES = http://github.com/downloads/rvoicilas/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-cross.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache

include ../../gar.mk

pre-configure:
	@echo "ac_cv_header_sys_inotify_h=yes" > $(WORKSRC)/config.cache
	@echo "ac_cv_header_sys_inotify_h_works=yes" >> $(WORKSRC)/config.cache
	@cd $(WORKSRC) && autoreconf --force --install 
	@$(MAKECOOKIE)

extract-config.cache.$(GARCH_FAMILY):
	@cp $(DOWNLOADDIR)/config.cache.$(GARCH_FAMILY) $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

extract-usb.ids:
	@cp -f $(DOWNLOADDIR)/usb.ids $(WORKSRC)/usb.ids
	@$(MAKECOOKIE)
