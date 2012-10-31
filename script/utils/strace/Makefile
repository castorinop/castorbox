GARNAME = strace
GARVERSION = 4.4-1
CATEGORIES = utils
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
MASTER_SITES += http://unc.dl.sourceforge.net/sourceforge/strace/
DISTFILES = $(GARNAME)_$(GARVERSION).tar.gz 
LICENSE = Modified_BSD
Modified_BSD_LICENSE_TEXT = $(WORKSRC)/COPYRIGHT

PATCHFILES = gar-base.diff

WORKSRC = $(WORKDIR)/$(GARNAME)-4.4

DESCRIPTION = System call tracer
define BLURB
 #XXX: nwall package blurb goes here.
endef

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir mandir


include ../../gar.mk
