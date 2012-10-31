GARNAME = talloc
GARVERSION = 2.0.1
CATEGORIES = lib
MASTER_SITES = http://samba.org/ftp/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-autoconf_tools.patch
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/c
BUILDDEPS = lib/libxslt

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST)

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS,                                                           \
		mkdir -p $(DESTDIR)$(datadir)/aclocal                                  ; \
		cd $(WORKSRC)/libreplace                                               ; \
		autoreconf --verbose --install --force -I $(DESTDIR)$(datadir)/aclocal   \
	 )
	@$(call RUN_AUTOTOOLS,                                                                         \
		mkdir -p $(DESTDIR)$(datadir)/aclocal                                                ; \
		cd $(WORKSRC)                                                                        ; \
		autoreconf --verbose --install --force -I $(DESTDIR)$(datadir)/aclocal -I libreplace   \
	 )
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libmad.la
	@$(MAKECOOKIE)
