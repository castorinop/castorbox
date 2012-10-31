GARNAME = fftw
GARVERSION = 3.1.2
CATEGORIES = lib
MASTER_SITES = http://www.fftw.org/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-taglib.patch $(DISTNAME)-destdir.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx lib/glib lib/taglib lib/pcre

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-fortran \
	--with-gnu-ld 

include ../../gar.mk

post-installa:
	@rm -rf $(DESTDIR)$(libdir)/libfftw3.la
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/fftw3.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/fftw3.pc
	@$(MAKECOOKIE)
