
LDFLAGS += -fwhole-program

extract-$(CONFIGFILE):
	@cat $(DOWNLOADDIR)/$(CONFIGFILE) \
		| sed -e 's%@GAR_rootdir@%$(rootdir)%g' \
		| sed -e 's%@GAR_sysconfdir@%$(sysconfdir)%g' \
		> $(WORKDIR)/$(CONFIGFILE)
	@$(MAKECOOKIE)

pre-configure:
	@rm -rf   $(WORKSRC)/arch/$(GARCH_FAMILY)
	@mkdir -p $(WORKSRC)/arch/$(GARCH_FAMILY)
	@echo "CPPFLAGS += $(CPPFLAGS)" >> $(WORKSRC)/arch/$(GARCH_FAMILY)/Makefile
	@echo "CFLAGS   += $(CFLAGS)"   >> $(WORKSRC)/arch/$(GARCH_FAMILY)/Makefile
	@$(MAKECOOKIE)

configure-custom:
	@$(CONFIGURE_ENV) $(MAKE) $(CONFIGURE_ARGS) -C $(WORKSRC) mrproper
	@cp $(WORKDIR)/$(CONFIGFILE) $(WORKSRC)/.config
	@$(CONFIGURE_ENV) $(MAKE) $(CONFIGURE_ARGS) -C $(WORKSRC) oldconfig
	@$(CONFIGURE_ENV) $(MAKE) $(CONFIGURE_ARGS) -C $(WORKSRC) clean
	
	@$(MAKECOOKIE)

install-custom:
	@if [ -n "$(USE_INSTALL_COOKIE)" ]; then \
		$(INSTALL_ENV) $(MAKE) $(INSTALL_ARGS) -C $(WORKSRC) CONFIG_PREFIX="$(CONFIG_PREFIX)" install; \
	fi
	
