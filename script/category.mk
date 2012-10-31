# This makefile is to be included from Makefiles in each category
# directory.

include ../castorbox.conf.mk
#include ../castorbox.lib.mk

PKGS_ADD =$(strip `diff -u . $(strip $(1))/ |grep Only |grep minimyth |cut -d ':' -f 2`)
PKGS_DEL =$(strip `diff -u . $(strip $(1))/ |grep Only |grep -v minimyth |cut -d ':' -f 2`)

merge-diffs:
	@find -maxdepth 2 -name merge.diff; 

category-diff:
	@echo missing packs: $(call PKGS_ADD, $(MINIMYTH_PATH)/$(LOCAL_PATH));
	@echo extras packs: $(call PKGS_DEL, $(MINIMYTH_PATH)/$(LOCAL_PATH));  


category-sync:
	@for i in $(call PKGS_ADD, $(MINIMYTH_PATH)/$(LOCAL_PATH)); do \
		rsync -auvC $(MINIMYTH_PATH)/$(LOCAL_PATH)/$(strip $$i)/ $(strip $$i); \
	done

%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* ; \
	done

paranoid-%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || exit 2; \
	done

export BUILDLOG ?= $(shell pwd)/buildlog.txt

report-%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || echo "	*** make $* in $$i failed ***" >> $(BUILDLOG); \
	done
