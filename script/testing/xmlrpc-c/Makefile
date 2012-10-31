GARNAME = xmlrpc-c
GARVERSION = 1.06.17
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tgz
LICENSE = GPL

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libxml2 utils/curl
BUILDDEPS = lib/libxml2 utils/curl

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-libxml2-backend \
	--with-gnu-ld

include ../../gar.mk

PARALLELMFLAGS := -j1

post-install:
	@rm -f $(DESTDIR)$(libdir)/libxmlrpc_util.la
	@rm -f $(DESTDIR)$(libdir)/libxmlrpc_abyss.la
	@rm -f $(DESTDIR)$(libdir)/libxmlrpc.la
	@rm -f $(DESTDIR)$(libdir)/libxmlrpc_server.la
	@rm -f $(DESTDIR)$(libdir)/libxmlrpc_server_abyss.la
	@rm -f $(DESTDIR)$(libdir)/libxmlrpc_client.la
	@rm -f $(DESTDIR)$(libdir)/libxmlrpc_server_cgi.la
	@sed -i 's%$$libdir%$(DESTDIR)$$libdir%g'         $(DESTDIR)$(bindir)/xmlrpc-c-config
	@sed -i 's%$$includedir%$(DESTDIR)$$includedir%g' $(DESTDIR)$(bindir)/xmlrpc-c-config
	@$(MAKECOOKIE)
