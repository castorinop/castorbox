GARNAME = libproxy
GARVERSION = 0.3.0
CATEGORIES = net
MASTER_SITES = http://libproxy.googlecode.com/files/
#MASTER_SITES = svn-http://libproxy.googlecode.com/svn/trunk/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-libjs.patch

LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/js

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--without-gnome \
	--without-kde \
	--with-gnu-ld 

BUILD_ARGS = LDFLAGS="$(LDFLAGS) -L$(DESTDIR)$(libdir) -L$(DESTDIR)$(elibdir)"

include ../../gar.mk

svn-http//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_SVN, http://$*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

x-checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

pre-configure:
	@cd $(WORKSRC); autoreconf --force --install --verbose
	@echo "ac_cv_func_malloc_0_nonnull=yes" >  $(WORKSRC)/config.cache
	@echo "ac_cv_func_realloc_0_nonnull=yes" >>  $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libproxy.la
	@$(MAKECOOKIE)
