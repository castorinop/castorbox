GARNAME = clinkcc
GARVERSION = 1.7.1
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(GARNAME)$(subst .,,$(GARVERSION)).tar.gz
LICENSE = BSD

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx extras/xerces-c 

WORKSRC = $(WORKDIR)/CyberLink

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-aligned \
	--disable-debug \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libtorrent.la
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/libtorrent.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/libtorrent.pc
	@$(MAKECOOKIE)
