GARNAME = swig
GARVERSION = 1.3.31
CATEGORIES = lang
MASTER_SITES = http://download.sourceforge.net/$(GARNAME)/
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz 
#PATCHFILES = gar-base.diff
#PATCHFILES = $(DISTNAME).patch.gar
LICENSE = PSF
PSF_LICENSE_TEXT = $(WORKSRC)/LICENSE

define BLURB
endef

LIBDEPS = devel/glibc lib/libstdcxx lib/ncurses utils/readline lib/zlib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

BUILD_ARGS = LDFLAGS="$(LDFLAGS) -L$(DESTDIR)$(libdir)"

INCLUDEDIR = $(games_includedir)
MANDIR = $(games_mandir)
#INSTALL_OVERRIDE_DIRS = MANDIR INCLUDEDIR

CONFIGURE_ARGS = $(DIRPATHS)  --build=$(GARBUILD) --host=$(GARHOST) \
	LDFLAGS="$(LDFLAGS) -L$(DESTDIR)$(libdir)" \
	--x-includes="$(DESTDIR)$(includedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--without-lua \
	--without-perl \
	--with-python=$(DESTDIR)$(games_bindir)/python \
	--with-gnu-ld

include ../../gar.mk
include ../games.mk
