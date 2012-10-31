GARNAME = xbl
GARVERSION = 1.1.4
CATEGORIES = extras
MASTER_SITES = http://www710.univ-lyon1.fr/ftp/xbl/
DISTFILES = $(DISTNAME).tar.gz
#LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c xorg/xorg


CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-gtk=no \
	--enable-sound=yes \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@# Create config.cache
	@rm -f $(WORKSRC)/config.cache
	@echo "ac_cv_file__proc_self_maps=yes" >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

post-install:
	@cp -rf $(WORKDIR)/data/* $(DESTDIR)$(datadir)/$(GARNAME)/
	@$(MAKECOOKIE)
