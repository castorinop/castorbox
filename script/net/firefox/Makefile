GARNAME = firefox
GARVERSION = 2.0.0.16
CATEGORIES = net
MASTER_SITES = ftp://ftp.mozilla.org/pub/firefox/releases/$(GARVERSION)/source/
DISTFILES = $(DISTNAME)-source.tar.bz2

#LICENSE = MPL

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c 
LIBDEPS = lib/openssl lib/libIDL gtk/gtk
BUILDDEPS = utils/zip

WORKSRC = $(WORKDIR)/mozilla

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile


CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--target=i686-pc-linux \
	--enable-application=xulrunner \
	--disable-javaxpcom \
	--enable-libxul \
 	--disable-64bit \
	--with-gnu-ld

include ../../gar.mk
