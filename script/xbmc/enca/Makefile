GARNAME = enca
GARVERSION = 1.13
CATEGORIES = lib
MASTER_SITES = http://www.sfr-fresh.com/unix/privat/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = tools $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-external \
	--with-gnu-ld \
	-C 

include ../../gar.mk

pre-configure:
	@echo "ac_cv_file__dev_random=yes" >> $(WORKSRC)/config.cache
	@echo "ac_cv_file__dev_urandom=yes" >> $(WORKSRC)/config.cache
	@echo "ac_cv_file__dev_srandom=yes" >> $(WORKSRC)/config.cache
	@echo "ac_cv_file__dev_arandom=yes" >> $(WORKSRC)/config.cache
	$(MAKECOOKIE)

build-tools:
	CC=$(build_CC) make -C $(WORKSRC)/tools make_hash
	cd $(WORKSRC)/tools && $(build_CC) -o make_hash make_hash.c || die "failed build native tools"
	$(MAKECOOKIE)
