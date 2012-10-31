GARNAME = gperf
GARVERSION = 3.0.4
CATEGORIES = net
MASTER_SITES = http://ftp.gnu.org/pub/gnu/gperf/
DISTFILES = $(DISTNAME).tar.gz

LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 

include ../../gar.mk


