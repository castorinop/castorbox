GARNAME = fftw
GARVERSION = 3.2.2
CATEGORIES = lib
MASTER_SITES = http://www.fftw.org/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = LGPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--enable-single \
	--disable-static \
	--enable-portable-binary \
	--enable-threads \
	--with-gnu-ld \
	--with-gcc-arch=$(GARCH)

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libfftw3f.la
	@rm -f $(DESTDIR)$(libdir)/libfftw3f_threads.la
	@$(MAKECOOKIE)
