GARNAME = cryptopp
GARVERSION = 5.6.2
CATEGORIES = utils
MASTER_SITES = http://www.cryptopp.com/ 
DISTFILES = $(GARNAME)$(subst .,,$(GARVERSION)).zip
LICENSE = cryptopp
cryptopp_LICENSE_TEXT = $(WORKSRC)/License.txt

define BLURB
endef

DEPENDS = lang/cxx

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS = CXXFLAGS="$(CXXFLAGS)"
INSTALL_ARGS = PREFIX="$(DESTDIR)$(prefix)"

include ../../gar.mk

# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))
 

zip-extract-$(DISTFILES):
	@echo " ==> Extracting $(DOWNLOADDIR)/$(DISTFILES)"
	@unzip $(DOWNLOADDIR)/$(DISTFILES) -d $(EXTRACTDIR)/$(DISTNAME)
	@$(MAKECOOKIE)

