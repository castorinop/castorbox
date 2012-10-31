GARNAME = xerces-c
GARVERSION = 2.7.0
CATEGORIES = lib
MASTER_SITES = http://www.apache.org/dist/xml/xerces-c/source/
DISTNAME = $(GARNAME)-src_$(subst .,_,$(GARVERSION))
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx lib/openssl

WORKSRC = $(WORKDIR)/$(DISTNAME)/src/xercesc

BUILD_ENV = XERCESCROOT=$(PWD)/$(WORKSRC)
BUILD_ARGS = Q=""
MAKE_FLAGS = XERCESCROOT=$(PWD)/$(WORKSRC) 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-aligned \
	--disable-debug \
	--with-gnu-ld 

include ../../gar.mk

PARALLELMFLAGS := -j1

pre-configure:
	@cd $(WORKSRC); autoconf

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libtorrent.la
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/libtorrent.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/libtorrent.pc
	@$(MAKECOOKIE)
