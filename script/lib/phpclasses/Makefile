GARNAME = phpclasses
GARVERSION = pkg
CATEGORIES = lib
MASTER_SITES  = http://www.phpclasses.org/
DISTFILES = class.sendmusiclastfm.php

DESCRIPTION =
define BLURB
endef

DEPENDS   = lang/php


INSTALL_SCRIPTS   = custom
INSTALL_DIR = $(DESTDIR)$(datadir)/php/$(GARNAME)

include ../../gar.mk

install-custom: dir_install $(addprefix install_file-,$(DISTFILES))
	@$(MAKECOOKIE)

dir_install:
	@mkdir -p $(INSTALL_DIR)
	@$(MAKECOOKIE)

install_file-%:
	@cp $(WORKDIR)/$* $(INSTALL_DIR)/
	@$(MAKECOOKIE)
