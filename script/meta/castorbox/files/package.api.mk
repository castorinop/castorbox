mm_NAME ?= noname

top        = ../
top_source = ./
top_build  = ../build/
top_share = ../share/

top        := $(shell cd $(top)        ; pwd)
top_source := $(shell cd $(top_source) ; pwd)
top_build  := $(shell cd $(top_build)  ; pwd)
top_share  := $(shell cd $(top_share)  ; pwd)

cookiedir  := $(top_build)/cookie

include $(top_build)/config.mk

mm_FILES = version version.md5 castorbox-$(mm_NAME).sfs	castorbox-$(mm_NAME).sfs.md5

mm_VERSION_BUILD = $(shell cat $(HOME)/.castorbox/.BUILD)

mm_RELEASE = $(mm_VERSION_BASE)-$(mm_VERSION_VCS)-b$(mm_VERSION_BUILD)

mm_FULL_VERSION = $(mm_NAME)-$(mm_RELEASE)

MM_BIN_FILES    := $(strip \
	$(if $(wildcard                     lists/castorbox-bin-list   ),                     lists/castorbox-bin-list   ) \
	$(if $(wildcard                lists/extras/extras-bin-list   ),                lists/extras/extras-bin-list   ) \
	$(filter $(patsubst %,lists/graphics/castorbox-bin-list.%,$(mm_GRAPHICS)),$(wildcard lists/graphics/castorbox-bin-list.*)))
MM_LIB_FILES    := $(strip \
	$(if $(wildcard                     lists/castorbox-lib-list   ),                     lists/castorbox-lib-list   ) \
	$(if $(wildcard                lists/extras/extras-lib-list   ),                lists/extras/extras-lib-list   ) \
	$(filter $(patsubst %,lists/graphics/castorbox-lib-list.%,$(mm_GRAPHICS)),$(wildcard lists/graphics/castorbox-lib-list.*)))
MM_ETC_FILES    := $(strip \
	$(if $(wildcard                     lists/castorbox-etc-list   ),                     lists/castorbox-etc-list   ) \
	$(if $(wildcard                lists/extras/extras-etc-list   ),                lists/extras/extras-etc-list   ) \
	$(filter $(patsubst %,lists/graphics/castorbox-etc-list.%,$(mm_GRAPHICS)),$(wildcard lists/graphics/castorbox-etc-list.*)))
MM_SHARE_FILES  := $(strip \
	$(if $(wildcard                     lists/castorbox-share-list ),                     lists/castorbox-share-list ) \
	$(if $(wildcard                lists/extras/extras-share-list ),                lists/extras/extras-share-list ) \
	$(filter $(patsubst %,lists/graphics/castorbox-share-list.%,$(mm_GRAPHICS)),$(wildcard lists/graphics/castorbox-share-list.*)))
MM_VAR_FILES  := $(strip \
	$(if $(wildcard               lists/castorbox-var-list ),               lists/castorbox-var-list ) \
	$(if $(wildcard    	      lists/extras/extras-var-list     ),        lists/extras/extras-var-list ) \
	$(filter $(patsubst %,lists/graphics/castorbox-var-list.%,$(mm_GRAPHICS)),$(wildcard lists/graphics/castorbox-var-list.*)))

MM_REMOVE_FILES := $(strip \
	$(if $(wildcard                     lists/castorbox-remove-list),                     lists/castorbox-remove-list) \
	$(filter $(patsubst %,lists/graphics/castorbox-remove-list.%,$(mm_GRAPHICS)),$(wildcard lists/graphics/castorbox-remove-list.*)))

MM_BIN_DEBUG    := $(strip $(if $(filter yes,$(mm_DEBUG)), \
	gdb \
	strace \
	xdpyinfo \
	))
MM_LIB_DEBUG    := $(strip $(if $(filter yes,$(mm_DEBUG)), \
	))
MM_ETC_DEBUG    := $(strip $(if $(filter yes,$(mm_DEBUG)), \
	))
MM_SHARE_DEBUG  := $(strip $(if $(filter yes,$(mm_DEBUG)), \
	))
MM_REMOVE_DEBUG := $(strip $(if $(filter yes,$(mm_DEBUG)), \
	))

MM_BINS    := $(sort $(if $(MM_BIN_FILES),    $(shell cat $(MM_BIN_FILES)    | sed 's%[ \t]*\#.*%%')) $(MM_BIN_DEBUG)    $(mm_USER_BIN_LIST))
MM_LIBS    := $(sort $(if $(MM_LIB_FILES),    $(shell cat $(MM_LIB_FILES)    | sed 's%[ \t]*\#.*%%')) $(MM_LIB_DEBUG)    $(mm_USER_LIB_LIST))
MM_ETCS    := $(sort $(if $(MM_ETC_FILES),    $(shell cat $(MM_ETC_FILES)    | sed 's%[ \t]*\#.*%%')) $(MM_ETC_DEBUG)    $(mm_USER_ETC_LIST))
MM_SHARES  := $(sort $(if $(MM_SHARE_FILES),  $(shell cat $(MM_SHARE_FILES)  | sed 's%[ \t]*\#.*%%')) $(MM_SHARE_DEBUG)  $(mm_USER_SHARE_LIST))
MM_VARS    := $(sort $(if $(MM_VAR_FILES),    $(shell cat $(MM_VAR_FILES)    | sed 's%[ \t]*\#.*%%')) $(MM_VAR_DEBUG)    $(mm_USER_VAR_LIST))
MM_REMOVES := $(sort $(if $(MM_REMOVE_FILES), $(shell cat $(MM_REMOVE_FILES) | sed 's%[ \t]*\#.*%%')) $(MM_REMOVE_DEBUG) $(mm_USER_REMOVE_LIST))

MAKE_PATH = \
	$(patsubst @%@,%,$(subst @ @,:, $(strip $(patsubst %,@%@,$(1)))))

DIRSTODOTS = \
	$(subst . /,./,$(patsubst %,/..,$(subst /, ,/$(1))))

# $1 = file type label plural.
# $2 = file type label singular.
# $3 = source destdir.
# $4 = target destdir.
# $5 = file directories.
# $6 = files.
COPY_FILES = \
	echo "copying $(strip $(1))" ; \
	for dir in $(strip $(5)) ; do \
		mkdir -p $(strip $(4))/$${dir} ; \
	done ; \
	for file_item in $(strip $(6)) ; do \
		found="" ; \
		for dir in $(strip $(5)) ; do \
			file_list="" ; \
			if [ -e $(3)/$${dir} ] ; then \
				if echo $${file_item} | grep -q -e '/$$' > /dev/null 2>&1 ; then \
					file_list=`cd $(3)/$${dir} ; find -L $${file_item} -maxdepth 0 -type d 2> /dev/null` ; \
				else \
					file_list=`cd $(3)/$${dir} ; find -L $${file_item} -maxdepth 0 -type f 2> /dev/null` ; \
				fi; \
			fi ; \
			for file in $${file_list} ; do \
				if [ -e $(3)/$${dir}/$${file} ] ; then \
					found="true" ; \
					source_file="$(3)/$${dir}/$${file}" ; \
					target_file="$(strip $(4))/$${dir}/$${file}" ; \
					if [ ! -e $${target_file} ] ; then \
						cp_flags=""                ; \
						cp_flags="$${cp_flags} -p" ; \
						file -L $${source_file} | grep -i -q 'ELF ..-bit LSB shared object' ; \
						if [ $$? -ne 0 ] ; then \
							cp_flags="$${cp_flags} -d" ; \
						fi ; \
						if [ -d $${source_file} ] ; then \
							cp_flags="$${cp_flags} -R" ; \
						fi ; \
						target_dir=`dirname $${target_file}` ; \
						mkdir -p $${target_dir} ; \
						cp $${cp_flags} $${source_file} $${target_file} ; \
						while file $${target_file} | grep -i -q 'symbolic link to' ; do \
							link="`file $${source_file} | \
								sed -e 's%^.* %%' -e 's%^.%%' -e 's%.$$%%'`" ; \
							source_file="`dirname $${source_file}`/$${link}" ; \
							target_file="`dirname $${target_file}`/$${link}" ; \
							if [ ! -e $${source_file} ] ; then \
								echo "error: $${source_file} not found." ; \
								exit 1 ; \
							fi ; \
							if [ ! -e $${target_file} ] ; then \
								target_dir=`dirname $${target_file}` ; \
								mkdir -p $${target_dir} ; \
								cp $${cp_flags} $${source_file} $${target_file} ; \
								chmod -R u+w $${target_file} ; \
							fi ; \
						done ; \
						chmod -R u+w $${target_file} ; \
					fi ; \
				fi ; \
			done ; \
		done ; \
		if [ -z $${found} ] ; then \
			echo "copying $(strip $(1)): warning: $(strip $(2)) \"$${file_item}\" not found." ; \
		fi ; \
	done

# $1 = file/directory
SET_PERMISSIONS = \
	chmod -R -s   $(strip $(1))                                                   ; \
	chmod -R -t   $(strip $(1))                                                   ; \
	chmod -R +r   $(strip $(1))                                                   ; \
	chmod -R u+w  $(strip $(1))                                                   ; \
	chmod -R go-w $(strip $(1))                                                   ; \
	find          $(strip $(1)) -depth -type d             -exec chmod +x '{}' \; ; \
	find          $(strip $(1)) -depth -type f -perm /0100 -exec chmod +x '{}' \;

all: build

build:  $(top_share)/$(mm_NAME)
	$(MAKECOOKIE)

$(top_build)/stage/version:
	@echo "making version file"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@touch $@~
	@echo "$(mm_FULL_VERSION)" > $@~
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/gar-$(mm_NAME): $(top_source)/gar-castorbox
	@echo "copying build system source directory"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@cp -pdR $< $@~
	@$(call SET_PERMISSIONS,$@~)
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/castorbox-$(mm_NAME).sfs: $(top_build)/stage/image/$(mm_NAME) $(top_build)/stage/image/$(mm_NAME).fakeroot
	@echo "making the squashfs version of the $(mm_NAME) image"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot -i $<.fakeroot sh -c "mksquashfs $< $@~ -no-exports -no-progress -processors 1 -no-fragments > /dev/null 2>&1"
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/%.md5: $(top_build)/stage/%
	@echo "making the checksum file for $(patsubst $(top)%,[...]%,$<)"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@(cd $(<D) ; find $(<F) -depth -type f -exec md5sum '{}' \; | sort -k 2) > $@~
	@chmod 644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/%.tar.bz2: $(top_build)/stage/%
	@echo "making the tarball file of $(patsubst $(top)%,[...]%,$<)"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot 	sh -c "tar -C $(<D) -jcf $@~ $(<F)"
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/starge/images/%:
	@echo "  making $* squashfs image file"
	@rm -rf $(mm_STAGEDIR)/distro/$(call IMGNAME,$*).sfs
	@fakeroot sh -c                                                                              " \
		chown -R $(call GET_UID,root):$(call GET_GID,root) $(mm_STAGEDIR)/$* > /dev/null 2>&1                    ; \
		chmod -R go-w $(mm_STAGEDIR)/$*                                                        ; \
		mksquashfs $(mm_STAGEDIR)/$* $(mm_STAGEDIR)/distro/$(call IMGNAME,$*).sfs > /dev/null 2>&1 "
	@chmod 644 $(mm_STAGEDIR)/distro/$(call IMGNAME,$*).sfs
	@cd $(mm_STAGEDIR)/distro/; md5sum $(call IMGNAME,$*).sfs > $(call IMGNAME,$*).sfs.md5

$(top_build)/stage/image/$(mm_NAME).fakeroot: $(top_build)/stage/image/$(mm_NAME)
	@echo "making $(mm_NAME) image directory fakeroot configuration file"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot -s $@~ sh -c                                             " \
		rm -rf           $</$(rootdir)/dev               ; \
		mkdir -m 0755 -p $</$(rootdir)/dev               ; \
		mknod -m 0600    $</$(rootdir)/dev/console c 5 1 ; \
		mknod -m 0600    $</$(rootdir)/dev/initctl p     "
	@touch $@~
	@mv $@~ $@

$(top_share)/$(mm_NAME): $(addprefix $(top_build)/stage/,$(mm_FILES)) \
		$(top_build)/stage/version			$(top_build)/stage/version.md5                  \
		$(top_build)/stage/castorbox-$(mm_NAME).sfs	$(top_build)/stage/castorbox-$(mm_NAME).sfs.md5
#		$(top_build)/stage/gar-$(mm_NAME).tar.bz2 $(top_build)/stage/gar-$(mm_NAME).tar.bz2.md5
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@cp -pdR $^ $@~
	@rm -f $@~/$(mm_NAME).md5
	@rm -f $@~~$(mm_NAME).md5~
	@(cd $@~ ; find -depth -type f -exec md5sum '{}' \; | sed -e 's%\./%%' | sort -k 2) > $@~~$(mm_NAME).md5~
	@mv -f $@~~$(mm_NAME).md5~ $@~/$(mm_NAME).md5
	@chmod 0644 $@~/$(mm_NAME).md5
	@touch $@~
	@mv $@~ $@
	@echo "made share distribution"

$(top_share)/%/$(mm_NAME).md5: $(top_share)/%
	@echo "making $(patsubst $(top)%,[...]%,$@)"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@cp -pdR $^ $@~
	@rm -f $@~/$(mm_NAME).md5
	@rm -f $@~~$(mm_NAME).md5~
	@(cd $@~ ; find -depth -type f -exec md5sum '{}' \; | sed -e 's%\./%%' | sort -k 2) > $@~~$(mm_NAME).md5~
	@mv -f $@~~$(mm_NAME).md5~ $@~/$(mm_NAME).md5
	@chmod 0644 $@~/$(mm_NAME).md5
	@touch $@~
	@mv $@~ $@

install: build $(addprefix install-,$(mm_NAME))

install-%:
	@mkdir -p $(mm_HOME)/images/castorbox/$*/$(mm_RELEASE)/
	@ln -sf $(top_share)/$*/* $(mm_HOME)/images/castorbox/$*/$(mm_RELEASE)/
	@echo $(mm_RELEASE) > $(mm_HOME)/images/castorbox/$*/latest

.PHONY: all build install 
