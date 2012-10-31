GARNAME = xcursor-transparent-theme
GARVERSION = 0.1.1
CATEGORIES = X11
MASTER_SITES = http://projects.o-hand.com/matchbox/sources/utils/
DISTFILES = $(DISTNAME).tar.gz index.theme
PATCHFILES = $(DISTNAME).patch.gar
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c xorg/xorg 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(MAKECOOKIE)

post-install:
	ln -sf xcursor-transparent $(DESTDIR)$(datadir)/icons/default
	@#mkdir -p $(DESTDIR)$(datadir)/icons/default
	@#cp -f $(DOWNLOADDIR)/index.theme $(DESTDIR)$(datadir)/icons/default
	@$(MAKECOOKIE)
