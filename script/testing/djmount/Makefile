GARNAME = djmount

GARVERSION = 0.71
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
CATEGORIES = net

DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-fix_cross.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libupnp testing/fuse

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	-C \
	--enable-shared=yes \
	--enable-static=no \
	--with-external-libupnp \
	--with-gnu-ld 

include ../../gar.mk

pre-configure:
	@#echo "vl_cv_lib_readline='-lreadline -lncurses'" > $(WORKSRC)/config.cache
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)


