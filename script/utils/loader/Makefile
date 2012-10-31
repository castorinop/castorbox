GARNAME = loader
GARVERSION = 0.1
CATEGORIES = boot
SOURCEPKG = utils/busybox
INITRC = linuxrc
CONFIGFILE = busybox-$(BUSYBOX_VERSION).config
DISTFILES = $(INITRC) $(CONFIGFILE)

#ATA_MODULES = ide-disk via82cxxx piix ahci libata pata_atiixp pata_mpiix pata_sis sata_nv sata_via ata_piix pata_amd pata_marvell pata_oldpiix pata_via sata_sis sd_mod sr_mod sg
#USB_MODULES = usb-storage ehci-hcd ohci-hcd uhci-hcd 
DEF_MODULES = unionfs ext4 loop
LOADER_MODULES =  $(DEF_MODULES) $(USB_MODULES) $(ATA_MODULES)


DESCRIPTION =
define BLURB
endef

DEPENDS = kernel/kernel system/splashutils-mini

WORKIMG = $(WORKDIR)/image
CONFIG_PREFIX=../../../$(WORKIMG)
WORKSRC = $(WORKDIR)/busybox-$(BUSYBOX_VERSION)
LINUX_MODULEDEP = $(LINUX_MODULESDIR)/modules.dep

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS   = custom-loader
INSTALL_SCRIPTS = custom-loader

# Prevent reinstalations of busybox
USE_INSTALL_COOKIE = true

MODULES_DEP = \
	$(shell if test -f $(DESTDIR)$(LINUX_MODULEDEP); then \
		for mod in $(1); do \
			LIST_DEP=`cat $(DESTDIR)$(LINUX_MODULEDEP) | grep "/$$mod.ko" | sed -e "s/://"`; \
			for mod_dep in $$LIST_DEP; do \
				fNAME=$${mod_dep\#\#*/}; \
				MOD_LIST_DEP="$${fNAME%%.*} $$MOD_LIST_DEP"; done; \
		done; \
		fi; \
		echo $$MOD_LIST_DEP;)

MODULES_CLEAN = $(shell sh -c 'for i in $(call MODULES_DEP, $(1)); do \
	CHECK=`echo $$LIST | grep $$i`; \
	if [ -z "$$CHECK" ]; then LIST="$$LIST $$i"; fi \
	done; echo $$LIST')

MODULES_INSTALL = $(addprefix module-install-,$(call MODULES_CLEAN, $(LOADER_MODULES)))

GAR_EXTRA_CONF += utils/busybox/package-api.mk
GAR_EXTRA_CONF += kernel-$(mm_KERNEL_VERSION)/linux/package-api.mk

include ../../gar.mk
include ../busybox/build-api.mk

PARALLELMFLAGS := -j1

show-deps:
	@echo modules $(MODULES_CLEAN)

pre-build: pre-modules-install modules-install
	@$(MAKECOOKIE)

pre-modules-install:
	@mkdir -p $(WORKIMG)/lib
	@$(MAKECOOKIE)

modules-install: $(MODULES_INSTALL)
	@$(MAKECOOKIE)

module-install-%:
	@cp -v `find $(DESTDIR)$(LINUX_MODULESDIR) -name $*.ko` $(WORKIMG)/lib; 
	@$(MAKECOOKIE)

pre-build-custom-loader:
	@mkdir -p $(WORKIMG)/bin		
	@ln -s -f  bin $(WORKIMG)/sbin
	@$(MAKECOOKIE)

build-custom-loader: pre-build-custom-loader build-$(WORKSRC)/Makefile install-custom post-build-custom-loader
	@$(MAKECOOKIE)

post-build-custom-loader:
	@cd $(WORKIMG) && rm -rf `find -type d -empty`
	@cp $(DESTDIR)$(esbindir)/fbsplashctl-mini $(WORKIMG)/$(esbindir)/fbsplashd.static
	@cp $(DOWNLOADDIR)/$(INITRC) $(WORKIMG)$(esbindir)/init
	@sed -i 's%@DEF_MODULES@%$(call MODULES_CLEAN, $(DEF_MODULES))%g' $(WORKIMG)$(esbindir)/init
	@sed -i 's%@USB_MODULES@%$(call MODULES_CLEAN, $(USB_MODULES))%g' $(WORKIMG)$(esbindir)/init
	@sed -i 's%@ATA_MODULES@%$(call MODULES_CLEAN, $(ATA_MODULES))%g' $(WORKIMG)$(esbindir)/init
	@chmod a+x $(WORKIMG)$(esbindir)/init
	@mkdir -p $(WORKIMG)/lib		
	@mkdir -p $(WORKIMG)/dev		
	@mkdir -p $(WORKIMG)/dev/pts	
	@mkdir -p $(WORKIMG)/dev/shm	
	@mkdir -p $(WORKIMG)/proc
	@mkdir -p $(WORKIMG)/sys
	@mkdir -p $(WORKIMG)/image
	@mkdir -p $(WORKIMG)/fs
	@mkdir -p $(WORKIMG)/system
	@echo 'stripping binaries' ; \
	find $(WORKIMG) -depth -exec file '{}' \; \
		| grep -E -i 'ELF ..-bit LSB executable|ELF ..-bit LSB shared object' \
		| sed -e 's%:.*%%' \
		| xargs $(STRIP) --strip-all -R .note -R .comment ;
	@$(MAKECOOKIE)

install-custom-loader:
	@if [ -n "$(INSTALL_LOADER)" ]; then \
		cp -a $(WORKIMG)/* $(INSTALL_LOADER); \
	fi;
	
