GARNAME = mediatomb
STABLE="YES"

ifeq ($(STABLE), "YES")
GARVERSION = 0.12.1
MASTER_SITES = http://downloads.sourceforge.net/sourceforge/$(GARNAME)/
else
GARVERSION = 2035
MASTER_SITES = svn+https://svn.mediatomb.cc/svnroot/mediatomb/trunk/mediatomb/
endif

CATEGORIES = net
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-cfg_castorbox.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx lib/libexif lib/js lib/taglib lib/zlib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-db-autocreate \
	--enable-sqlite-backup-defaults \
	--with-exif-h=$(DESTDIR)$(includedir) \
	--with-exif-libs=$(DESTDIR)$(libdir) \
	--with-js-h=$(DESTDIR)$(includedir)/js-1.7.0/ \
	--with-js-libs=$(DESTDIR)$(libdir) \
	--with-zlib-h=$(DESTDIR)$(includedir) \
	--with-zlib-libs=$(DESTDIR)$(libdir) \
	--enable-inotify \
	--with-inotify-h=$(DESTDIR)$(includedir) \
	--with-curl-cfg=$(DESTDIR)$(bindir)-config/curl-config \
	--with-taglib-cfg=$(DESTDIR)$(bindir)-config/taglib-config \
	--disable-rpl-malloc \
	--with-gnu-ld 

include ../../gar.mk

svn+https//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_SVN, https://$*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@$(MAKECOOKIE)


