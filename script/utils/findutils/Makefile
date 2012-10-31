GARNAME = findutils
GARVERSION = 4.4.2
CATEGORIES = utils
MASTER_SITES = ftp://ftp.gnu.org/gnu/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES= $(DISTNAME)-perl.patch.gar
LICENSE = GPL3

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-rpath \
	--enable-leaf-optimisation \
	--enable-d_type-optimization \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@$(call FIX_LIBTOOL_LIBPATH,$(WORKSRC),configure)
	@echo "gl_cv_header_working_fcntl_h=yes" >> $(WORKSRC)/config.cache
	@echo "ac_cv_func_fnmatch_gnu=yes" >> $(WORKSRC)/config.cache
	@echo "gl_cv_func_wcwidth_works=yes" >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)
