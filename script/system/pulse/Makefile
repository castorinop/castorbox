GARNAME = pulseaudio
HTTP_MASTER_SITES = http://0pointer.de/lennart/projects/pulseaudio/
GIT_MASTER_SITES = git://git.0pointer.de/pulseaudio.git/
GARVERSION_TYPE = http
GARVERSION = $(strip $(if $(filter git,$(GARVERSION_TYPE)) , \
            848dd378bb7fa53be7b88016335fa89d520f2ea3, \
            0.9.22 ))
CATEGORIES = system
MASTER_SITES = $(strip $(if $(filter git,$(GARVERSION_TYPE)) , \
              $(GIT_MASTER_SITES) , \
	      $(HTTP_MASTER_SITES) ))

DISTFILES = $(strip $(if $(filter git,$(GARVERSION_TYPE)) , \
              $(DISNTAME).tar.bz2 , \
	      $(DISTNAME).tar.gz ))
#DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES = $(DISTNAME)-fix_pa_drop_caps.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/liboil lib/libsamplerate lib/libsndfile lib/libatomic_ops lib/alsa-lib lib/gdbm lib/speex system/lirc

CONFIGURE_SCRIPTS   = $(WORKSRC)/configure
BUILD_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-nls \
	--with-libiconv-prefix=$(DESTDIR)$(prefix) \
	--disable-default-build-tests \
	--enable-avahi \
	--enable-bluez \
	--enable-force-preopen \
	--with-gnu-ld

include ../../gar.mk

git//%$(DISTNAME).tar.bz2:
	@$(call FETCH_GIT, $*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE) 

pre-configure:
	@#$(call RUN_AUTOTOOLS)
	@sed 's@v=UNKNOWN@v=0.9.21.x@g' -i $(WORKSRC)/git-version-gen
#	cd $(WORKSRC) && NOCONFIGURE=1 ./bootstrap.sh
	#@cp -f $(build_DESTDIR)$(build_datadir)/libtool/config/config.sub $(WORKSRC)
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	#@$(call FIX_LIBTOOL,$(WORKSRC)/ltconfig)
	#echo "lt_cv_dlopen_self=yes" > $(WORKSRC)/config.cache
	#echo "lt_cv_dlopen_self_static=yes" >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

no-pre-configure:
	@#cd $(WORKSRC); autoreconf --force --install --verbose
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	#echo "lt_cv_dlopen_self_static=yes" >> $(WORKSRC)/config.cache
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libpulsecore.la
	@rm -f $(DESTDIR)$(libdir)/libpulse.la
	@rm -f $(DESTDIR)$(libdir)/libpulse-mainloop-glib.la
	@rm -f $(DESTDIR)$(libdir)/libpulse-simple.la
	@$(MAKECOOKIE)
