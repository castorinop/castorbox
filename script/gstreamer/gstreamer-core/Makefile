GARNAME = gstreamer
GARVERSION = 0.10.29
CATEGORIES = lib
MASTER_SITES = http://gstreamer.freedesktop.org/src/gstreamer/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2_1

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c gtk/glib lib/libxml2 lib/liboil lib/check

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-tests \
	--disable-examples \
	--disable-nls \
	--disable-dependency-tracking \
	--enable-debug \
	--with-checklibname=check \
	--with-configdir=$(sysconfdir)/gstreamer \
	--with-cachedir=$(localstatedir)/cache/gstreamer-0.10 \
	--with-gnu-ld 

include ../../gar.mk

pre-configure:
	@for i in lt_cv_dlopen_self=yes lt_cv_dlopen_self_static=yes ac_cv_func_mmap_fixed_mapped=yes; do \
		echo "$$i" >> $(WORKSRC)/config.cache; \
	done
	@$(MAKECOOKIE)

post-install:
	@#$(DESTDIR)$(bindir)/chrpath -d $(DESTDIR)$(bindir)/gst-{inspect,launch,typefind,xmlinspect,xmllaunch}-0.10
	@#$(DESTDIR)$(bindir)/chrpath -d $(DESTDIR)$(libdir)/{*.so,gstreamer-0.10/*.so}
	@mkdir -p $(DESTDIR)$(localstatedir)/cache/gstreamer-0.10
	@rm -fv $(DESTDIR)$(libdir)/libgstreamer-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgstcontroller-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgstnet-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstcoreelements.la
	@rm -fv $(DESTDIR)$(libdir)/gstreamer-0.10/libgstcoreindexers.la
	@rm -fv $(DESTDIR)$(libdir)/libgstbase-0.10.la
	@rm -fv $(DESTDIR)$(libdir)/libgstdataprotocol-0.10.la
	@$(MAKECOOKIE)
