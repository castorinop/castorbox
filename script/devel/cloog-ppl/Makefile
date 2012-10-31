GARNAME = cloog-ppl
GARVERSION = 0.15.11
CATEGORIES = devel
MASTER_SITES = ftp://gcc.gnu.org/pub/gcc/infrastructure/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-configure.patch
LICENSE = GPL3/LGPL3

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/cxx devel/gmp devel/ppl
BUILDDEPS = devel-tainted/devel-tainted devel/make

CONFIGURE_SCRIPTS  = $(WORKSRC)/configure
BUILD_SCRIPTS      = $(WORKSRC)/Makefile
INSTALL_SCRIPTS    = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
  --enable-shared \
  --disable-static \
  --with-gnu-ld \
  --with-ppl=$(DESTDIR)$(prefix) \
  --with-gmp=$(DESTDIR)$(prefix)

include ../../gar.mk

pre-configure:
	@cd $(WORKSRC) ; mkdir -p m4
	@cd $(WORKSRC) ; touch AUTHORS
	@cd $(WORKSRC) ; touch ChangeLog
	@cd $(WORKSRC) ; touch NEWS
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libcloog.la
	@$(MAKECOOKIE)
