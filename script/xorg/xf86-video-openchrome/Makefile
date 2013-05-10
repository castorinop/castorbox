GARNAME = xf86-video-openchrome
GARVERSION_TYPE = git
GARVERSION = $(strip $(if $(filter git,$(GARVERSION_TYPE)) , \
	20121211-0db1c3c, \
	0.3.1 ))
CATEGORIES = $(CATEGORY)
MASTER_SITES = $(strip $(if $(filter git,$(GARVERSION_TYPE)) , \
	git://anongit.freedesktop.org/git/openchrome/$(GARNAME)/ , \
	$(XORG_MASTER_SITES) ))
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = \
	$(DISTNAME)-automake_1.13.patch
LICENSE = MIT

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c system/udev \
	$(CATEGORY)/fontsproto \
	$(CATEGORY)/libdrm \
	$(CATEGORY)/libpciaccess \
	$(CATEGORY)/libX11 \
	$(CATEGORY)/libXext \
	$(CATEGORY)/libXvMC \
	$(CATEGORY)/randrproto \
	$(CATEGORY)/renderproto \
	$(CATEGORY)/util-macros \
	$(CATEGORY)/videoproto \
	$(CATEGORY)/xextproto \
	$(CATEGORY)/xf86driproto \
	$(CATEGORY)/xorg-server \
	$(CATEGORY)/xproto

CATEGORY := $(shell basename $(shell dirname $(shell pwd)))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--disable-silent-rules \
	--disable-static \
	--enable-shared \
	--disable-debug \
	--disable-xv-debug \
	--disable-viaregtool \
	--with-gnu-ld

include ../../gar.mk

git//%$(DISTNAME).tar.bz2:
	@$(call FETCH_GIT, $*, $(word 2,$(subst -, ,$(GARVERSION))), $(DISTNAME))
	@$(MAKECOOKIE)

checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE) 

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/xorg/modules/drivers/openchrome_drv.la
	@rm -f $(DESTDIR)$(libdir)/libchromeXvMC.la
	@rm -f $(DESTDIR)$(libdir)/libchromeXvMCPro.la
	@$(MAKECOOKIE)
