
MINIMYTH_PATH ?= /home/pablo/build/minimyth-svn/gar-minimyth
LOCAL_PATH = $(subst $(mm_HOME),,$(shell pwd))
DIFF = diff -ruP -x ".*" -x "*~"
FIX_DIFF = grep -v "^Only in" | sed  "s@$(MINIMYTH_PATH)/$(LOCAL_PATH)@new@g" | sed "s@--- ./@--- old/@g"

DIFF_FILES =  $(subst $(MINIMYTH_PATH)/$(LOCAL_PATH)/,, $(shell if test -d $(MINIMYTH_PATH)/$(LOCAL_PATH); then find $(MINIMYTH_PATH)/$(LOCAL_PATH) -maxdepth 3 -name  "Makefile" -or -name "checksums" -or -name "*mk" -or -name "files"; fi))

merge: remove-diff make-diff

remove-diff: 
	@rm -f merge.diff

make-diff:
	@if [ ! -d "$(MINIMYTH_PATH)/$(LOCAL_PATH)/" ]; then echo "$(MINIMYTH_PATH)/$(LOCAL_PATH)/" do not exist; fi
	@for i in $(DIFF_FILES); do $(DIFF) ./$$i $(MINIMYTH_PATH)/$(LOCAL_PATH)/$$i; done | $(FIX_DIFF) > merge.diff
	@if test  ! -s "merge.diff"; then echo no changes; rm -f merge.diff; else echo some changes; fi

merge-patch:
	@pwd
	@if test -s "merge.diff"; then echo patching merge...; patch -Np1 -i merge.diff && rm -f merge.diff; make clean; fi

copy-%:
	echo rsync -auvC $(shell cd $(MINIMYTH_PATH)/$(LOCAL_PATH)/../$*/ && pwd) ../$*
	echo rsync -auvC $(MINIMYTH_PATH)/script/$(CATEGORIES)/$*/ $(mm_HOME)/script/$(CATEGORIES)/$*

copy-dependences:
	echo rsync -auvC $(MINIMYTH_PATH)/$(LOCAL_PATH)/$*/ $(GARDIR)/$*

# $(call FETCH_BZR, <svn_url>, <svn_revision>, <file_base>)
FETCH_BZR = \
	mkdir -p $(PARTIALDIR)                                          ; \
	cd $(PARTIALDIR)                                                ; \
	rm -rf $(strip $(3))                                            ; \
	rm -rf $(strip $(3)).tar.bz2                                    ; \
	export PYTHONSTARTUP=/etc/pythonrc.py				; \
	echo launch bzr export -r $(strip $(2)) $(strip $(3)) $(strip $(1))         ; \
	/usr/bin/bzr export -r $(strip $(2)) $(strip $(3)) $(strip $(1))         ; \
	if [ $$? -ne 0 ] ; then                                           \
		rm -rf $(strip $(3))                                    ; \
	fi                                                              ; \
	ls -l . ; \
	if [ ! -d $(strip $(3)) ] ; then                                  \
		rm -rf $(strip $(3))                                    ; \
		rm -rf $(strip $(3)).tar.bz2                            ; \
		exit 1                                                  ; \
	fi                                                              ; \
	tar --exclude '*/.bzr' -jcf $(strip $(3)).tar.bz2 $(strip $(3)) ; \
	rm -rf $(strip $(3))

