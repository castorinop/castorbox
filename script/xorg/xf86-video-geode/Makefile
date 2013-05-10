GARNAME = xf86-video-geode
#GARVERSION_TYPE = git
GARVERSION = $(strip $(if $(filter git,$(GARVERSION_TYPE)) , \
	20120829-4a20e8a, \
	2.11.14 ))
CATEGORIES = $(CATEGORY)
MASTER_SITES = $(strip $(if $(filter git,$(GARVERSION_TYPE)) , \
	git://anongit.freedesktop.org/git/xorg/driver/xf86-video-geode/ , \
	$(XORG_MASTER_SITES) ))
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/COPYING

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c \
	$(CATEGORY)/fontsproto \
	$(CATEGORY)/libpciaccess \
	$(CATEGORY)/randrproto \
	$(CATEGORY)/renderproto \
	$(CATEGORY)/util-macros \
	$(CATEGORY)/videoproto \
	$(CATEGORY)/xextproto \
	$(CATEGORY)/xorg-server \
	$(CATEGORY)/xproto
BUILDDEPS = \
	$(CATEGORY)/xorg-sgml-doctools

CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-silent-rules \
	--enable-shared \
	--disable-static \
  	--enable-geodegx-panel \
  	--disable-werror \
  	--enable-visibility \
	--with-gnu-ld

GAR_EXTRA_CONF += $(CATEGORY)/xorg/package-api.mk
include ../../gar.mk

git//%$(DISTNAME).tar.bz2:
	@$(call FETCH_GIT, $*, $(word 2,$(subst -, ,$(GARVERSION))), $(DISTNAME))
	@$(MAKECOOKIE)

x-checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE) 

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/drivers/geode_drv.la
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/drivers/ztv_drv.la
	@$(MAKECOOKIE)
