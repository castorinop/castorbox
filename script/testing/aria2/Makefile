GARNAME = aria2
GARVERSION = 1.8.1
CATEGORIES = net
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES = $(DISTNAME)-cross_compiling.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-amule-daemon \
	--enable-amulecmd \
	--enable-webserver \
	--enable-upnp \
	--disable-monolithic \
	--with-upnp-prefix=$(DESTDIR)$(prefix) \
	--with-zlib=$(DESTDIR)$(prefix) \
	--with-crypto-prefix=$(DESTDIR)$(prefix) \
	--with-wx-config=$(DESTDIR)$(bindir)/wx-config \
	--with-toolkit=base \
	--disable-debug \
	--with-gnu-ld 

include ../../gar.mk
