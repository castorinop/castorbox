GARNAME = cxfe
GARVERSION = 0.9.1
CATEGORIES = mediaplayers
MASTER_SITES = ftp://ftp.rtwnetwork.com/pub/
MASTER_SITES += http://gd.tuwien.ac.at/opsys/linux/gentoo/distfiles/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(GARNAME).patch.gar
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

WORKSRC = $(WORKDIR)/$(GARNAME)

DEPENDS = lang/c xorg/xorg lib/freetype lib/libpng lirc/lirc mediaplayers/xine-lib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--x-includes=$(DESTDIR)$(includedir) \
	--x-libraries=$(DESTDIR)$(libdir) \
	--with-gnu-ld \
	--with-xine-prefix=$(DESTDIR)$(prefix) \
	--with-xine-exec-prefix=$(DESTDIR)$(prefix) \
	--with-x \
	--without-readline \
	--with-aalib-prefix=$(DESTDIR)$(prefix) \
	--with-aalib-exec-prefix=$(DESTDIR)$(prefix)

include ../../gar.mk

pre-configure:
	@echo "ac_cv_path_CURL_CONFIG=no"  >  $(WORKSRC)/config.cache
	@echo "ac_cv_path_AALIB_CONFIG=no" >> $(WORKSRC)/config.cache
	@echo "ac_cv_path_CACA_CONFIG=no"  >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)
