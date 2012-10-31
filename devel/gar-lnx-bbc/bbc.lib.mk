# Copyright (C) 2002 Nate Riffe
# 
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.

BUILD_SCRIPTS += $(addprefix user-,$(GARUSERS))
INSTALL_SCRIPTS += $(addprefix user-,$(GARUSERS))

#### MACROS

# Take out the extra slashes in a path
NORM_PATH = $(shell echo $(1) | sed -e 's~/\+~/~g')

#### EXTRACT TARGETS

# EXTRACTING GARUSERS
# get the .passwd, .group, and .bootstrap files into their correct locations
$(foreach OOZER,$(GARUSERS),$(addprefix extract-$(OOZER),.passwd .group .bootstrap)):
	@echo " ==> Copying $(subst extract-,$(DOWNLOADDIR)/,$@)"
	@cp $(subst extract-,$(DOWNLOADDIR)/,$@) $(WORKDIR)/
	@$(MAKECOOKIE)

##### BUILD TARGETS

# BUILDING GARUSERS
# Dummy rule which a maintainer can override in cases where a user's home
# directory must actually contain stuff.
user-%:
	@echo 

# rule to create the garuser tarball
user-$(WORKDIR)/%.tar.gz:
	@cp $(WORKDIR)/$*.bootstrap $(WORKDIR)/$*/.bootstrap
	@chmod 755 $(WORKDIR)/$*/.bootstrap
	@(cd $(WORKDIR); tar zcf $*.tar.gz $* $*.passwd $*.group)

# rule to create directory which will be in /home at runtime
user-$(WORKDIR)/%:
	@mkdir -p $(subst user-,,$@)

# Umbrella rule which is triggered as a dependency of "build"
build-user-%: user-$(WORKDIR)/% user-% user-$(WORKDIR)/%.tar.gz
	@$(MAKECOOKIE)

##### INSTALL TARGETS

# INSTALLING GARUSERS
# Put the user tarball into $(DESTDIR)/home
install-user-%:
	@mkdir -p $(DESTDIR)/home
	@cp -f $(WORKDIR)/$*.tar.gz $(DESTDIR)/home
	@$(MAKECOOKIE)

INSTALL_SCRIPTS += $(addprefix /setuid/,$(SETUID_PROGRAMS))
# INSTALLING SETUID
install-/setuid/%:
	@mkdir -p $(DESTDIR)/setuid
	@if test -L $(DESTDIR)/$*; then \
	  echo "Undoing previous setuid install on $*"; \
	  rm $(DESTDIR)/$*; \
	  mkdir -p $$(dirname $(DESTDIR)$*); \
	  mv $(DESTDIR)/setuid/$* $(DESTDIR)/$*; \
	fi
	@mkdir -p $$(dirname $(DESTDIR)/setuid/$*)
	@mv $(DESTDIR)/$* $(DESTDIR)/setuid/$*
	@ln -sf $(call NORM_PATH,/mnt/rw/setuid/$*) $(DESTDIR)/$*
