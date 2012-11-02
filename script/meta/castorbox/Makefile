GARNAME = castorbox
GARVERSION =  $(mm_VERSION)
CATEGORIES = meta
LICENSE =

DESCRIPTION = 
define BLURB
endef

PKGS = core   

DEPENDS = $(addprefix meta/, $(PKGS))

dst_HOST = "root@$(mm_HOST)"

ifneq ($(INSTALL_MOD), "")
mm_MOD=$(word 1,$(subst -, ,$(INSTALL_MOD)))
mm_RELEASE=$(if $(filter-out $(word 2,$(INSTALL_MOD)), "latest"),`cat $(mm_HOME)/images/castorbox/$(mm_MOD)/latest`, $(word 2, $(INSTALL_MOD)))
endif

#BUILD_SCRIPTS   = custom
INSTALL_SCRIPTS   = custom

GAR_EXTRA_CONF += meta/castorbox/version.mk
include ../../gar.mk

clean-all: clean
	@for dep in $(DEPENDS); do \
	echo " ==> Running make clean in $$dep "; \
	$(BUILD_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C ../../$$dep clean; \
	done

pre-build:
	@if test ! -f cookies/$(DESTIMG).d/pre-build; then \
		NUM=$$((`cat $(HOME)/.castorbox/.BUILD`+1)); \
		echo $$NUM > $(HOME)/.castorbox/.BUILD; fi
	@$(MAKECOOKIE)

build-custom:
	@for dep in $(PKGS); do \
	echo " ==> Running make in $$dep "; \
	$(BUILD_ENV) ionice -c 3  $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C ../../meta/$$dep $(BUILD_ARGS); \
	done

install-custom: $(addsuffix -latest, $(addprefix install-share-img-,$(PKGS)))

install-share-img-%:
	@$(MAKE) install-final INSTALL_MOD=$*

install-final:  install-$(mm_INSTALL_METHOD)

install-check-space:
	@RELEASE=$(mm_RELEASE); \
	IMG_SIZE=`/usr/bin/du -s -m $(mm_HOME)/images/castorbox/$(mm_MOD)/$$RELEASE |cut -f 1`; \
	HST_FREE=`/usr/bin/ssh $(dst_HOST) "df -m | grep /mnt/system | tr -s [:space:] |cut -d  ' ' -f 4"`; \
	if [ "$$IMG_SIZE" -gt "$$HST_FREE" ]; then echo "No space left on $(mm_HOST). need $${IMG_SIZE}M"; exit 1; fi

install-scp: install-check-space
	@echo mod = $(mm_MOD)
	@echo ver = $(mm_RELEASE)
	@echo "	check if installed $(mm_MOD) $(mm_RELEASE) image"
	@/usr/bin/scp -r $(mm_HOME)/images/castorbox/$(mm_MOD)/$(mm_RELEASE)/$(mm_MOD).md5  $(dst_HOST):/tmp/ > /dev/null|| exit 1
	@mod=$(mm_MOD); ver=$(mm_RELEASE); /usr/bin/ssh $(dst_HOST) "cd /mnt/system/roms/$$mod/$$ver/ 2>/dev/null && md5sum -c /tmp/$(mm_MOD).md5 > /dev/null 2>&1"; \
	if [ "$$?" != "0" ]; then \
		echo copying $(mm_MOD) $(mm_RELEASE) image; \
		/usr/bin/ssh $(dst_HOST) mkdir -p /mnt/system/roms/$(mm_MOD)/$(mm_RELEASE)/ || exit 1; \
		/usr/bin/scp -r $(mm_HOME)/images/castorbox/$(mm_MOD)/$(mm_RELEASE)/*  $(dst_HOST):/mnt/system/roms/$(mm_MOD)/$(mm_RELEASE)/ || exit 1; \
		echo "	[copy] complete for $(mm_MOD)"; \
		echo configuring $(mm_MOD) image; \
		script_PATH="roms/$(mm_MOD)/$(mm_RELEASE)/"; /usr/bin/ssh $(dst_HOST) $(ENV_INSTALL) /mnt/system/` [ $(mm_MOD) = 'core' ] && echo $$script_PATH`scripts/castorbox-install $(mm_MOD) \ $(mm_RELEASE) / || exit 1; \
		echo "	[configure] complete for $(mm_MOD)"; \
	else \
	echo "	already copied $(mm_MOD) image"; \
	fi;

install-http:
	@echo copying $(mm_MOD) $(mm_RELEASE) image
	/usr/bin/ssh $(mm_HTTP_HOST) mkdir -p ~/castorbox-imgs/$(mm_BRANCH)/$(mm_MOD)/$(mm_RELEASE)/ || exit 1
	/usr/bin/scp -r $(mm_HOME)/images/castorbox/$(mm_MOD)/$(mm_RELEASE)/*  \
		$(mm_HTTP_HOST):~/castorbox-imgs/$(mm_BRANCH)/$(mm_MOD)/$(mm_RELEASE)/ || exit 1
	@echo "	[copy] complete for $(mm_MOD)"

post-install:
	@rm -rf $(DESTDIR)$(versiondir)/$(GARNAME)
	@rm -rf $(DESTDIR)$(licensedir)/$(GARNAME)
	@$(MAKECOOKIE)

install-reboot: install 
	/usr/bin/ssh $(dst_HOST) reboot

version:
	@echo full: $(mm_VERSION) 
	@echo base: $(mm_VERSION_BASE)
	@echo rev: $(mm_VERSION_VCS)
