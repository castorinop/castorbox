GARNAME = libsmbclient
GARVERSION = 3.5.9
CATEGORIES = net
DISTFILES = samba-$(GARVERSION).tar.gz
MASTER_SITES = http://us1.samba.org/samba/ftp/stable/
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

WORKSRC = $(WORKDIR)/samba-$(GARVERSION)

CONFIGURE_SCRIPTS = $(WORKSRC)/source3/configure
BUILD_SCRIPTS   = $(WORKSRC)/source3/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/source3/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
		 -C \
		 --without-ldap \
		 --with-ld

BUILD_ARGS = libsmbclient
INSTALL_ARGS = installlibwbclient

include ../../gar.mk


# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))
pre-configure:
	echo "samba_cv_CC_NEGATIVE_ENUM_VALUES=yes" >> $(WORKSRC)/source3/config.cache
	$(MAKECOOKIE)
