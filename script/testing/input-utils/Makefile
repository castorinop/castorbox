GARNAME = input-utils
GARVERSION = 2359
CATEGORIES = net
MASTER_SITES = svn-https://linuxconsole.svn.sourceforge.net/svnroot/linuxconsole/trunk/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/utils/Makefile
#INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS = CC="$(CC)" CFLAGS="$(CFLAGS)" PROGRAMS=evtest

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--with-gnu-ld 

include ../../gar.mk

svn-https//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_SVN, https://$*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

x-checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

