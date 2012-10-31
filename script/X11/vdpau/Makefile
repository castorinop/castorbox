NVIDIA_MAJOR_VERSION = 185
NVIDIA_MINOR_VERSION = 18
NVIDIA_TEENY_VERSION = 31

INSTALL_SCRIPTS = includes libs

GAR_EXTRA_CONF += kernel-$(mm_KERNEL_VERSION)/linux/package-api.mk nvidia/nvidia/package-api.mk 
include ../../gar.mk

NVIDIA_FILE_LIST_LIB_SO = $(strip \
		$(if $(wildcard $(WORKSRC)/usr/lib/libvdpau.so.*), \
			libvdpau.so:/usr/lib:$(libdir)) \
	)

install-includes:
	@mkdir -p $(DESTDIR)$(includedir)
	@rm -rf $(DESTDIR)$(includedir)/vdpau
	@cp -r $(WORKSRC)/usr/include/vdpau $(DESTDIR)$(includedir)
	@$(MAKECOOKIE)

install-libs:
	@$(foreach entry,$(NVIDIA_FILE_LIST_LIB_SO), \
		rm -f \
		    $(DESTDIR)$(word 3,$(subst :, ,$(entry)))/$(word 1,$(subst :, ,$(entry))) \
		    $(DESTDIR)$(word 3,$(subst :, ,$(entry)))/$(word 1,$(subst :, ,$(entry))).* ; \
	)
	@$(foreach entry,$(NVIDIA_FILE_LIST_LIB_SO), \
		install -D \
		    $(WORKSRC)$(word 2,$(subst :, ,$(entry)))/$(word 1,$(subst :, ,$(entry))).$(word 1,$(NVIDIA_VERSION_LIST)) \
		    $(DESTDIR)$(word 3,$(subst :, ,$(entry)))/$(word 1,$(subst :, ,$(entry))).$(word 1,$(NVIDIA_VERSION_LIST)) ; \
	)
	@$(foreach entry,$(NVIDIA_FILE_LIST_LIB_SO), $(if $(word 2,$(NVIDIA_VERSION_LIST)), \
		ln -sf \
		    $(word 1,$(subst :, ,$(entry))).$(word 1,$(NVIDIA_VERSION_LIST)) \
		    $(DESTDIR)$(word 3,$(subst :, ,$(entry)))/$(word 1,$(subst :, ,$(entry))).$(word 2,$(NVIDIA_VERSION_LIST)) ; \
	))
	@$(foreach entry,$(NVIDIA_FILE_LIST_LIB_SO), $(if $(word 3,$(NVIDIA_VERSION_LIST)), \
		ln -sf \
		    $(word 1,$(subst :, ,$(entry))).$(word 2,$(NVIDIA_VERSION_LIST)) \
		    $(DESTDIR)$(word 3,$(subst :, ,$(entry)))/$(word 1,$(subst :, ,$(entry))).$(word 3,$(NVIDIA_VERSION_LIST)) ; \
	))
	@$(foreach entry,$(NVIDIA_FILE_LIST_LIB_SO), \
		ln -sf \
		    $(word 1,$(subst :, ,$(entry))).$(word $(words $(NVIDIA_VERSION_LIST)),$(NVIDIA_VERSION_LIST)) \
		    $(DESTDIR)$(word 3,$(subst :, ,$(entry)))/$(word 1,$(subst :, ,$(entry))) ; \
	)
	@$(foreach entry,$(NVIDIA_FILE_LIST_LIB_SO), $(if $(filter-out 1,$(NVIDIA_MAJOR_VERSION)), \
		ln -sf \
		    $(word 1,$(subst :, ,$(entry))).$(word $(words $(NVIDIA_VERSION_LIST)),$(NVIDIA_VERSION_LIST)) \
		    $(DESTDIR)$(word 3,$(subst :, ,$(entry)))/$(word 1,$(subst :, ,$(entry))).1 ; \
	))
	@$(foreach entry,$(NVIDIA_FILE_LIST_LIB_SO), $(if $(word 4,$(subst :, ,$(entry))), \
		ln -sf \
		    $(word 1,$(subst :, ,$(entry))) \
		    $(DESTDIR)$(word 3,$(subst :, ,$(entry)))/$(word 4,$(subst :, ,$(entry))) ; \
	))
	@$(MAKECOOKIE)

install-version: GARNAME=vdpau

install-license-%: GARNAME=vdpau
