GARNAME = mt-daapd
GARVERSION = svn-1586
CATEGORIES = net
MASTER_SITES = http://nightlies.fireflymediaserver.org/nightlies/$(GARVERSION)/
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lang/cxx lib/libid3tag lib/zlib db/sqlite lib/flac lib/libogg lib/libvorbis utils/vorbis-tools system/avahi gtk/glib

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-nls \
	--enable-sqlite3 \
	--enable-avahi \
	--enable-oggvorbis \
	--enable-flac

include ../../gar.mk

pre-configure:
	@# Create config.cache
	@rm -f $(WORKSRC)/config.cache
	@echo "ac_cv_func_setpgrp_void=yes" >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

post-install:
	@rm -rf $(DESTDIR)$(datadir)/mt-daapd/plugins/*.la
	@mkdir -p $(DESTDIR)$(localstatedir)/cache
	@ln -sf /etc/mt-daapd/cache $(DESTDIR)$(localstatedir)/cache/mt-daapd
	@$(MAKECOOKIE)
