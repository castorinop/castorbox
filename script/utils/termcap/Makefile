GARNAME = termcap
GARVERSION = 1.3.1
CATEGORIES = utils
MASTER_SITES = ftp://ftp.gnu.org/gnu/termcap/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
LICENSE = GPL2

# used Debian procps_2.0.7-8 to create diff -- extensive changes!

DESCRIPTION = GNU termcap
define BLURB
 #XXX: nwall package blurb goes here.
endef

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = --prefix=$(prefix) --exec_prefix=$(exec_prefix)
BUILD_OVERRIDE_DIRS = libdir includedir infodir prefix
INSTALL_OVERRIDE_DIRS = libdir includedir infodir prefix

include ../../gar.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/libtermcap.la
	@$(MAKECOOKIE)
