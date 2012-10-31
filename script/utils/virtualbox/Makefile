GARNAME = VirtualBox
GARVERSION = 4.1.12
CATEGORIES = utils
MASTER_SITES = http://download.virtualbox.org/virtualbox/$(GARVERSION)/
DISTFILES = $(DISTNAME).tar.bz2
#PATCHFILES = $(DISTNAME)-fix_modalias.patch
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/COPYING

DESCRIPTION = 
define BLURB
endef

WORKSRC = $(WORKDIR)/$(DISTNAME)_OSE

BUILD_TARGET = $(strip \
        $(if $(filter i386  ,$(GARCH_FAMILY)), x86   ) \
        $(if $(filter x86_64,$(GARCH_FAMILY)),amd64))


DEPENDS = lang/c xorg/xorg lib/libIDL
BUILDDEPS = python/python

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     =  custom \
	$(WORKSRC)/out/linux.$(BUILD_TARGET)/release/bin/additions/src/vboxguest/Makefile \
	$(WORKSRC)/out/linux.$(BUILD_TARGET)/release/bin/additions/src/vboxsf/Makefile \
	$(WORKSRC)/out/linux.$(BUILD_TARGET)/release/bin/additions/src/vboxvideo/Makefile 
INSTALL_SCRIPTS   = custom 

CONFIGURE_ENV += TARGET_CPU=$(BUILD_TARGET)
CONFIGURE_ARGS = --build-headless \
	--ose \
	--nofatal \
	--with-gcc=$(CC) \
	--with-g++="$(CXX)" \
	--with-openssl-dir=$(DESTDIR)$(prefix) \
	--with-linux=$(DESTDIR)$(LINUX_SOURCEDIR)

DEFAULT_ARGS = \
	$(LINUX_MAKE_ARGS)
BUILD_ARGS   = $(DEFAULT_ARGS)
INSTALL_ARGS = $(DEFAULT_ARGS)

DEFAULT_ENV = $(LINUX_MAKE_ENV) \
	VBOX_WITH_CROGL=1 \
	BUILD_TARGET_ARCH="$(BUILD_TARGET)" \
	ARCH="$(ARCH)" \
	KERN_INCL="$(DESTDIR)$(LINUX_SOURCEDIR)" \
	KERN_DIR="$(DESTDIR)$(LINUX_BUILDDIR)" \
	CFLAGS="$(CFLAGS)" \
	VBOX_WITH_PAM=0 \
	KERNELRELEASE="$(LINUX_FULL_VERSION)"
BUILD_ENV = $(DEFAULT_ENV)
INSTALL_ENV = $(DEFAULT_ENV)

GAR_EXTRA_CONF += kernel-$(mm_KERNEL_VERSION)/linux/package-api.mk
GAR_EXTRA_CONF += xorg-$(mm_XORG_VERSION)/xorg/package-api.mk

include ../../gar.mk

ifeq ($(mm_XORG_VERSION)),7.4)
	VBOX_MOD_VERSION = 16
endif	
ifeq ("x$(mm_XORG_VERSION)", "x7.6")
	VBOX_MOD_VERSION = 110
else
	VBOX_MOD_VERSION = nooooo
endif


http//%: 
	@cd $(PARTIALDIR) ; wget -c http://$* -O $(DISTFILES)

test:
	echo $(mm_XORG_VERSION) : $(VBOX_MOD_VERSION) 


post-configure:
pre-build:
	for i in VBOX_ONLY_ADDITIONS VBOX_WITH_X11_ADDITIONS VBOX_WITH_ADDITION_DRIVERS VBOX_WITH_CROGL VBOX_WITH_VIDEOHWACCEL ; do \
	echo $$i=1 >> $(WORKSRC)/LocalConfig.kmk; \
	done
	for i in VBOX_WITH_PAM ; do \
	echo $$i := >> $(WORKSRC)/LocalConfig.kmk; \
	done
	$(MAKECOOKIE)

build-custom:
	#cd $(WORKSRC) && pwd && . ./env.sh && $(BUILD_ENV) kmk additions-build-linux.$(BUILD_TARGET)
	cd $(WORKSRC) && pwd && . ./env.sh && $(BUILD_ENV) kmk
	$(MAKECOOKIE)

install-custom:
	@#Install Video Driver
	install -D $(WORKSRC)/out/linux.x86/release/bin/additions/vboxvideo_drv_$(VBOX_MOD_VERSION).so $(DESTDIR)$(libdir)/xorg/modules/drivers/vboxvideo_drv.so
	install -D $(WORKSRC)/out/linux.x86/release/bin/additions/vboxmouse_drv_$(VBOX_MOD_VERSION).so $(DESTDIR)$(libdir)/xorg/modules/input/vboxmouse_drv.so
	@install -D $(WORKSRC)/out/linux.x86/release/bin/additions/VBoxOGL*.so  $(DESTDIR)$(libdir)
	@ln -sf ../../../VBoxOGL.so $(DESTDIR)$(libdir)/xorg/modules/dri/vboxvideo_dri.so
	@#Install Kernel Extensions
	@install -d $(DESTDIR)$(LINUX_MODULESDIR)/misc/vbox/
	@install $(WORKSRC)/out/linux.x86/release/bin/additions/src/vboxguest/vboxguest.ko $(DESTDIR)$(LINUX_MODULESDIR)/misc/vbox/
	@install $(WORKSRC)/out/linux.x86/release/bin/additions/src/vboxsf/vboxsf.ko $(DESTDIR)$(LINUX_MODULESDIR)/misc/vbox/
	@install $(WORKSRC)/out/linux.x86/release/bin/additions/src/vboxvideo/vboxvideo.ko $(DESTDIR)$(LINUX_MODULESDIR)/misc/vbox/
	@depmod -b "$(DESTDIR)" "$(LINUX_FULL_VERSION)"
	@#Install command line programs
	@install -m755 $(WORKSRC)/out/linux.x86/release/bin/additions/mount.vboxsf $(DESTDIR)$(ebindir)
	@install -m755 $(WORKSRC)/out/linux.x86/release/bin/additions/VBoxClient $(DESTDIR)$(bindir)
	@install -m755 $(WORKSRC)/out/linux.x86/release/bin/additions/VBoxControl $(DESTDIR)$(bindir)
	@install -m755 $(WORKSRC)/out/linux.x86/release/bin/additions/VBoxService $(DESTDIR)$(bindir)
	@#install -m755 $(WORKSRC)/src/VBox/Additions/x11/Installer/VBoxRandR.sh $(DESTDIR)$(bindir)/VBoxRandR
	@$(MAKECOOKIE)
