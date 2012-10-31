
pre-everything:
	@$(MAKE) -f ../../meta/castorbox/files/check.mk DESTIMG=$(DESTIMG) GARNAME=$(GARNAME)
	@# There is no MAKECOOKIE so that this runs every time.

$(DOWNLOADDIR)/$(DISTNAME).tar.bz2:
	@if [ ! -e $(DOWNLOADDIR)/$(DISTNAME).tar.bz2 ] ; then \
		$(MAKE) -f ../../meta/castorbox/files/distfile.mk DESTIMG=$(DESTIMG) GARNAME=$(GARNAME) ; \
	fi

pre-build:
	@if test ! -f cookies/$(DESTIMG).d/pre-build; then \
		NUM=$$((`cat $(HOME)/.castorbox/.BUILD`+1)); \
		echo $$NUM > $(HOME)/.castorbox/.BUILD; fi
	@$(MAKECOOKIE)


checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

configure-custom:
	@$(MAKE) -f ../../meta/castorbox/files/configure.mk DESTIMG=$(DESTIMG) GARNAME=$(GARNAME)
	@$(MAKECOOKIE)

install-%/Makefile:
	@echo " ==> Running make install in $*"
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $* $(INSTALL_ARGS) install

version: 
	@echo $(mm_VERSION) svn: $(mm_VERSION_SVN) base: $(mm_VERSION_BASE)


svn: $(SVN_DEPS)

