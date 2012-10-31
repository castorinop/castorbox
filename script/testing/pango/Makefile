GARNAME = pango
GARVERSION = 1.10.4
CATEGORIES = net
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pango/1.10/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/SDL

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/libpango-1.0.la
	@rm -f $(DESTDIR)$(libdir)/libpangoft2-1.0.la
	@rm -f $(DESTDIR)$(libdir)/libpangoxft-1.0.la
	@rm -f $(DESTDIR)$(libdir)/libpangox-1.0.la
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/pango.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/pango.pc
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/pangoft2.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/pangoft2.pc
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/pangoxft.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/pangoxft.pc
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/pangox.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/pangox.pc
	@$(MAKECOOKIE)

