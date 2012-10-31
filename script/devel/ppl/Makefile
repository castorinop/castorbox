GARNAME = ppl
GARVERSION = 0.11.2
CATEGORIES = devel
MASTER_SITES = http://www.cs.unipr.it/ppl/Download/ftp/releases/$(GARVERSION)/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL3

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/cxx devel/gmp
BUILDDEPS = devel-tainted/devel-tainted devel/make perl/perl

CONFIGURE_SCRIPTS  = $(WORKSRC)/configure
BUILD_SCRIPTS      = $(WORKSRC)/Makefile
INSTALL_SCRIPTS    = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-silent-rules \
	--disable-rpath \
	--enable-interfaces="c,cxx" \
	--enable-shared \
	--disable-static \
	--with-cc="$(CC)" \
	--with-cxx="$(CXX)" \
	--with-cflags="$(CFLAGS)" \
	--with-cxxflags="$(CXXFLAGS)" \
	--with-gnu-ld \
  	--with-gmp-prefix=$(DESTDIR)$(prefix)

include ../../gar.mk

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libppl.la
	@rm -f $(DESTDIR)$(libdir)/libppl_c.la
	@rm -f $(DESTDIR)$(libdir)/libpwl.la
	@$(MAKECOOKIE)
