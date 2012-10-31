GARNAME = libedit
GARVERSION = 20100424-3.0
CATEGORIES = net
MASTER_SITES  = http://www.thrysoee.dk/editline/
DISTFILES = $(DISTNAME).tar.gz
#PATCHFILES = $(DISTNAME)-abstract_socket.patch $(DISTNAME).patch
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/LICENCE

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/openssl lib/zlib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-strip \
	--disable-lastlog \
	--disable-utmp \
	--disable-utmpx \
	--disable-wtmp \
	--disable-wtmpx \
	--without-rpath \
	--with-ssl-engine \
	--without-pam

include ../../gar.mk

#CPPFLAGS   += -DX_UNIX_PATH=\\\"@/tmp/.X11-unix/X%u\\\"
#CFLAGS     += -DX_UNIX_PATH=\\\"@/tmp/.X11-unix/X%u\\\"
#CXXFLAGS   += -DX_UNIX_PATH=\\\"@/tmp/.X11-unix/X%u\\\"

LD         := $(CC)
LDFLAGS    := $(CFLAGS)

sysconfdir := $(sysconfdir)/ssh

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@rm -f $(WORKSRC)/config.cache
	@echo "ac_cv_have_space_for_dirent_d_name=yes" >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)
