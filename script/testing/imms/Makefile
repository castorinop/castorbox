GARNAME = imms
GARVERSION = 3.0.2
CATEGORIES = lib
MASTER_SITES = http://www.luminal.org/files/imms/
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-configure.patch $(DISTNAME)-taglib.patch $(DISTNAME)-destdir.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx lib/glib lib/taglib lib/pcre db/sqlite3 testing/fftw testing/torch testing/sox

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

INSTALL_ARGS = DESTDIR="$(DESTDIR)"

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--enable-analyzer \
	--with-taglib \
	--with-id3lib \
	--with-vorbis \
	--with-gnu-ld 

include ../../gar.mk

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@echo "ac_cv_prog_have_sox=yes" > $(WORKSRC)/config.cache
	@$(MAKECOOKIE)


post-install:
	@rm -rf $(DESTDIR)$(libdir)/libtorrent.la
	@sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/libtorrent.pc
	@sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/libtorrent.pc
	@$(MAKECOOKIE)
