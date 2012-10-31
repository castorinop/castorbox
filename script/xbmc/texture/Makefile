GARNAME=TexturePacker
DISTNAME=xbmc-10.1
SOURCEPKG = xbmc/xbmc-stable
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef


WORKSRC=$(WORKDIR)/$(DISTNAME)
#CONFIGURE_SCRIPTS =  $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/tools/TexturePacker/Makefile 
BUILD_ARGS = TexturePacker
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	-C \
	--enable-external-libraries \
	--disable-optimizations \
	--disable-non-free

#no
#	--disable-debug \
#	--disable-ccache \
#	--enable-external-python \
#	--disable-dvdcss \
#	--enable-goom 


include ../../gar.mk

configure-custom:
	$(MAKECOOKIE)

pre-configure:
	# remove prebuilt libraries
	find $(WORKSRC) -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -delete
	cd $(WORKSRC) && ./bootstrap
	echo "ac_cv_prog_HAVE_ZIP=true" > $(WORKSRC)/config.cache
	$(MAKECOOKIE)

build-tools:
	$(MAKE) CXX=$(build_CXX) CXXFLAGS="$(CXXFLAGS)" -C $(WORKSRC)/tools//TexturePacker TexturePacker 
	$(MAKECOOKIE)
