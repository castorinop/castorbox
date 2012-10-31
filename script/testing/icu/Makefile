GARNAME = icu4c
GARVERSION = 4.2.1
CATEGORIES = testing
MASTER_SITES = http://download.icu-project.org/files/icu4c/$(GARVERSION)/
DISTFILES = $(subst .,_,$(DISTNAME))-src.tgz
LICENSE =

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c

WORKSRC = $(WORKDIR)/icu/source
WORKBLD = $(WORKDIR)/icu_build

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-cross-build=$(PWD)/$(WORKSRC) \
	--with-gnu-ld

include ../../gar.mk

configure-custom:
	@mkdir -p $(WORKBLD)
	@cd $(WORKBLD) && $(CONFIGURE_ENV) ./$(call DIRSTODOTS,$(WORKBLD))/$(WORKSRC)/configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libsqlite3.la
	@$(MAKECOOKIE)
