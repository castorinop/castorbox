mm_NAME ?= core

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

mm_VERSION_BUILD = $(shell cat $(HOME)/.castorbox/.BUILD)

mm_RELEASE = $(mm_VERSION_BASE)-r$(mm_VERSION_SVN)-b$(mm_VERSION_BUILD)

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

$(top_build)/stage/image/initrd: $(top_build)/stage/image/$(mm_NAME)
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~ $@~/etc/splash
	@INSTALL_LOADER=$@~ make -C $(mm_HOME)/script/utils/loader install
	@#Copy splash theme.
	@cp -a $(top_build)/image/core/etc/splash/CastorBOX $@~/etc/splash
	@rm -r $@~/etc/splash/CastorBOX/animations
	@mv $@~ $@

$(top_build)/image/$(mm_NAME): $(build_DESTDIR)$(build_rootdir) $(DESTDIR)$(rootdir) $(top_source)
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@# Copy source.
	@mkdir -p $@~$(sourcedir)
	@#cp -pdR $(top_build)/stage/gar-$(mm_NAME).tar.bz2 $@~$(sourcedir)/gar-$(mm_NAME).tar.bz2
	@# Copy versions.
	@mkdir -p $@~$(versiondir)-build
	@cp -pdR $(build_DESTDIR)$(build_versiondir)/* $@~$(versiondir)-build
	@mkdir -p $@~$(versiondir)
	@cp -pdR $(DESTDIR)$(versiondir)/* $@~$(versiondir)
	@rm -rf $@~$(versiondir)/castorbox
	@mkdir -p $@~$(extras_versiondir)
	@cp -pdR $(DESTDIR)$(extras_versiondir)/* $@~$(extras_versiondir)
	@# Copy licenses.
	@mkdir -p $@~$(licensedir)-build
	@cp -pdR $(build_DESTDIR)$(build_licensedir)/* $@~$(licensedir)-build
	@mkdir -p $@~$(licensedir)
	@cp -pdR $(DESTDIR)$(licensedir)/* $@~$(licensedir)
	@rm -rf $@~$(licensedir)/castorbox
	@mkdir -p $@~$(extras_licensedir)
	@cp -pdR $(DESTDIR)$(extras_licensedir)/* $@~$(extras_licensedir)
	@# Install busybox.
	@echo "installing busybox"
	@main_DESTDIR=$@~ $(MAKE) -C $(mm_HOME)/script/utils/busybox DESTIMG=$(DESTIMG) USE_INSTALL_COOKIE=true install
	@# Copy binaries.
	@$(call COPY_FILES, "binaries", "binary", $(DESTDIR), $@~, $(bindirs), $(MM_BINS))
	@# Copy etcs.
	@$(call COPY_FILES, "etcs", "etc", $(DESTDIR), $@~, $(etcdirs), $(MM_ETCS))
	@# Copy libraries.
	@$(call COPY_FILES, "libraries", "library", $(DESTDIR), $@~, $(libdirs), $(MM_LIBS))
	@# Copy shares.
	@$(call COPY_FILES, "shares", "share", $(DESTDIR), $@~, $(sharedirs), $(MM_SHARES))
	@# Copy vars.
	@$(call COPY_FILES, "vars", "var", $(DESTDIR), $@~, $(vardirs), $(MM_VARS))
	@# Copy package rootfs files.
	@find $(top_source)/rootfs -depth -type d \
		| sed -e 's%^\$(top_source)/rootfs%$@~%' \
		| xargs -n 1  mkdir -m 0755 -p
	@find $(top_source)/rootfs -depth -type f ! -name "*~" \
		| sed -e 's%^\(\$(top_source)/rootfs\)/\(.*\)$$%\1/\2 $@~/\2%' \
		| xargs -n 2 cp -fpd
	@find $(top_source)/rootfs -depth -type l ! -name "*~" \
		| sed -e 's%^\(\$(top_source)/rootfs\)/\(.*\)$$%\1/\2 $@~/\2%' \
		| xargs -n 2 cp -fpd
	@# Copy install scripts.
	@cp  -pd $(top_source)/installer/castorbox-install $@~/usr/bin/castorbox-install
	@chmod 0755 $@~/usr/bin/castorbox-install
	@#cp  -pd $(top_source)/mm_local/mm_local_helper $@~/usr/bin/mm_local_helper_old
	@# Substitute values for variables in files
	@sed -i 's%@MM_VERSION@%$(mm_VERSION)%g'                   $@~$(sysconfdir)/conf.d/core
	@sed -i 's%@MM_VERSION_MYTH@%$(mm_VERSION_MYTH)%g'         $@~$(sysconfdir)/conf.d/core
	@sed -i 's%@MM_VERSION_MINIMYTH@%$(mm_VERSION_MINIMYTH)%g' $@~$(sysconfdir)/conf.d/core
	@sed -i 's%@MM_CONF_VERSION@%$(mm_CONF_VERSION)%g'         $@~$(sysconfdir)/conf.d/core
	@sed -i 's%@PATH@%$(call MAKE_PATH,$(bindirs_base))%g'     $@~$(sysconfdir)/conf.d/core
	@sed -i 's%@GAR_libdir@%$(libdir)%g'                       $@~$(sysconfdir)/fonts/local.conf
	@echo "$(mm_VERSION_BASE) $(mm_VERSION_SVN)-$(mm_VERSION_BUILD)" > $@~$(sysconfdir)/release
	@sed -i 's%@GAR_VERSION@%$(mm_FULL_VERSION)%g'             $@~$(sysconfdir)/motd
	@# Create the castorbox build configuration file.
	@rm -rf   $@~$(versiondir)/castorbox.conf.mk
	@mkdir -m 0755 -p $@~$(versiondir)
	@$(foreach build_var,$(build_vars), \
		echo "$(build_var)='$(strip $($(build_var)))'" >> $@~$(versiondir)/castorbox.conf.mk ; )
	@# Create the loader configuration file.
	@rm -f $@~$(sysconfdir)/ld.so.conf
	@echo include /etc/ld.so.conf.d/*.conf >> $@~$(sysconfdir)/ld.so.conf ;
	@$(foreach dir, $(libdirs_base), \
		echo $(dir) >> $@~$(sysconfdir)/ld.so.conf ; )
	@rm -f $@~$(sysconfdir)/ld.so.cache{,~}
	@# Make font file links.
	@#for font in `cd $@~$(datadir)/fonts/X11/TTF ; ls -1 *.{TTF,ttf} 2> /dev/null` ; do \
	 #	ln -sf $(patsubst /%,%,$(call DIRSTODOTS,$(datadir)/mms/fonts))$(datadir)/fonts/X11/TTF/$${font} \
	#	       $@~$(datadir)/mms/fonts/$${font} ; \
	# done
	@ln -sf $(patsubst /%,%,$(call DIRSTODOTS,$(sysconfdir)/splash/CastorBOX))$(datadir)/fonts/X11/TTF/LiberationSans-Italic.ttf \
			$@~$(sysconfdir)/splash/CastorBOX/luxisri.ttf
	@# Remove unneeded perl files.
	@echo 'removing unneeded perl files'
	@#dirs'$(PERL_libdir)' ; \
	 for dir in $${dirs} ; do \
		if [ -e $@~$${dir} ] ; then \
			cd $@~$${dir} ; \
			find . -depth -type f -name '.*'    -exec rm -rf '{}' \; ; \
			find . -depth -type f -name '*.bs'  -exec rm -rf '{}' \; ; \
			find . -depth -type f -name '*.e2x' -exec rm -rf '{}' \; ; \
			find . -depth -type f -name '*.eg'  -exec rm -rf '{}' \; ; \
			find . -depth -type f -name '*.h'   -exec rm -rf '{}' \; ; \
			find . -depth -type f -name '*.pod' -exec rm -rf '{}' \; ; \
			while [ `find . -depth -type d -empty | wc -l` -gt 0 ] ; do \
				find . -depth -type d -empty -exec rm -rf '{}' \; ; \
			done ; \
		fi ; \
	 done
	@# Remove unneeded python files.
	@echo 'removing unneeded python files'
	@dirs='$(PYTHON_libdir) $(datadir)' ; \
		for dir in $${dirs} ; do \
			if [ -e $@~$${dir} ] ; then \
				cd $@~$${dir} ; \
				find . -depth -type f -name 'EGG-INFO' -exec rm -rf '{}' \; ; \
				find . -depth -type f -name '*.egg-info' -exec rm -rf '{}' \; ; \
				find . -depth -type f -name '*.pyc' -exec rm -rf '{}' \; ; \
				find . -depth -type f -name '*.pyo' -exec rm -rf '{}' \; ; \
			fi ; \
		done

	@# Remove unwanted binaries, etcs, shares and libraries.
	@echo 'removing unwanted files'
	@for file_item in $(addprefix $@~,$(MM_REMOVES)) ; do \
		if echo $${file_item} | grep -q -e '/$$' > /dev/null 2>&1 ; then \
			file_list=`ls -d1 $${file_item} 2> /dev/null` ; \
			for file in $${file_list} ; do \
				if [ -d $${file} ] ; then \
					rm -rf $${file} ; \
				fi ; \
			done ; \
		else \
			file_list=`ls -d1 $${file_item} 2> /dev/null` ; \
			for file in $${file_list} ; do \
				if [ -f $${file} ] ; then \
					rm -rf $X${file} ; \
				fi ; \
			done ; \
		fi ; \
	 done
	@# Copy dependent libraries.
	@echo 'copying dependent libraries'
	@new_filter_path="\(`echo $(strip $(libdirs)) | sed -e 's%//*%/%g' -e 's% /% %g' -e 's%^/%%' -e 's%  *%\\\\|%g'`\)" ; \
	 pass=0 ; \
	 lib_count=1 ; \
	 old_list="" ; \
	 lib_list=`find $@~ -depth -exec file '{}' \; \
		| grep -E -i 'ELF ..-bit LSB executable|ELF ..-bit LSB shared object' \
		| sed -e 's%:.*%%' \
		| sed -e :a -e '$!N;s/\n/ /;ta' -e 'P;D'` ; \
	 while [ $${lib_count} -gt 0 ] ; do \
		pass=$$(($${pass}+1)) ; \
		old_list=`echo $${old_list} $${lib_list} \
			| sed -e 's%[^ ]*/%%g' \
			      -e 's% %\n%g' \
			| sort -u \
			| sed -e :a -e '$!N;s/\n/ /;ta' -e 'P;D'` ; \
		old_filter="\(`echo $${old_list} | sed -e 's%\([.+]\)%\\1%g' | sed -e 's%  *%\\\\|%g'`\)" ; \
		new_list=`$(OBJDUMP) -x $${lib_list} 2> /dev/null \
			| grep -e '^ *NEEDED  *' \
			| sort -u \
			| sed -e 's%^ *NEEDED  *%%' \
			      -e 's%  *$$%%' \
			      -e "s%^$${old_filter}$$%%g" \
			| sed -e :a -e '$!N;s/\n/ /;ta' -e 'P;D'` ; \
		lib_count=`echo "$${new_list}" | wc -w` ; \
		echo "copying dependent libraries: pass $${pass} found $${lib_count} libraries to copy" ; \
		if [ "$(mm_DEBUG_BUILD)" = "yes" ] ; then \
			echo "    lib_list : $${lib_list}" ; \
			echo "    old_list : $${old_list}" ; \
			echo "    new_list : $${new_list}" ; \
		fi ; \
		lib_list="" ; \
		if [ $${lib_count} -gt 0 ] ; then \
			new_filter_file="\(`echo $${new_list} | sed -e 's%\([.+]\)%\\\\\\1%g' | sed -e 's%  *%\\\\|%g'`\)" ; \
			new_filter="$${new_filter_path}/$${new_filter_file}" ; \
			new_list=`cd $(DESTDIR) ; find * -depth -regex "$${new_filter}"` ; \
			for lib in $${new_list} ; do \
				dir=`echo $${lib} | sed -e 's%[^/]*$$%%'` ; \
				mkdir -p $@~/$${dir} ; \
				cp -p $(DESTDIR)/$${lib} $@~/$${dir} ; \
				chmod -R u+w $@~/$${lib} ; \
				lib_list="$${lib_list} $@~/$${lib}" ; \
			done ; \
		fi ; \
	 done
	@# Copy dependent kernel modules.
	@echo 'copying dependent kernel modules'
	@depmod -b "$(DESTDIR)$(rootdir)" "$(LINUX_FULL_VERSION)"
	@find $@~$(LINUX_MODULESDIR) -depth -name '*.ko' | sed -e 's%^$@~$(LINUX_MODULESDIR)%/%' -e 's%//*%/%g' -e 's%^/%%' | \
	 while read module ; do \
		module_deps=`cat $(DESTDIR)$(LINUX_MODULESDIR)/modules.dep | grep -e "^$${module}:" | sed -e 's%[^:]*: *%%'` ; \
		for module_dep in $${module_deps} ; do \
			if [ ! -e $@~$(LINUX_MODULESDIR)/$${module_dep} ] ; then \
				mkdir -p `dirname $@~$(LINUX_MODULESDIR)/$${module_dep}` ; \
				cp -pd $(DESTDIR)$(LINUX_MODULESDIR)/$${module_dep} $@~$(LINUX_MODULESDIR)/$${module_dep} ; \
			fi ; \
		done ; \
	 done
	@# Remove unwanted binaries, etcs, shares and libraries.
	@echo 'removing unwanted files'
	@for file_item in $(addprefix $@~,$(MM_REMOVES)) ; do \
		if echo $${file_item} | grep -q -e '/$$' > /dev/null 2>&1 ; then \
			file_list=`ls -d1 $${file_item} 2> /dev/null` ; \
			for file in $${file_list} ; do \
				if [ -d $${file} ] ; then \
					rm -rf $${file} ; \
				fi ; \
			done ; \
		else \
			file_list=`ls -d1 $${file_item} 2> /dev/null` ; \
			for file in $${file_list} ; do \
				if [ -f $${file} ] ; then \
					rm -rf $${file} ; \
				fi ; \
			done ; \
		fi ; \
	 done
	@# Generate kernel files.
	@depmod -b "$@~$(rootdir)" "$(LINUX_FULL_VERSION)"
	@# Generate font files.
	@cd $@~$(datadir)/fonts/X11/misc ; mkfontscale . ; mkfontdir .
	@cd $@~$(datadir)/fonts/X11/TTF  ; mkfontscale . ; mkfontdir .
	@# Strip binaries and shared libraries.
	@if [ ! $(mm_DEBUG) = yes ] ; then \
		echo 'stripping binaries and shared libraries' ; \
		find $@~ -depth -exec file '{}' \; \
			| grep -E -i 'ELF ..-bit LSB executable|ELF ..-bit LSB shared object' \
			| sed -e 's%:.*%%' \
			| xargs $(STRIP) --strip-all -R .note -R .comment ; \
	 fi
	@# Clean up permissions (at least somewhat)
	@find $@~ -depth -exec file '{}' \; \
		| grep -i 'ELF ..-bit LSB executable' \
		| sed -e 's%:.*%%' \
		| xargs chmod 0755
	@find $@~ -depth -exec file '{}' \; \
		| grep -i 'ELF ..-bit LSB shared object' \
		| sed -e 's%:.*%%' \
		| grep -v '*' \
		| grep -v '/libc.so.[0-9]\+$$' \
		| grep -v '/ld-linux.so.[0-9]\+$$' \
		| grep -v '/ld-linux-x86-64.so.[0-9]\+$$' \
		| grep -v '/portmap$$' \
		| xargs chmod 0644
	@$(call SET_PERMISSIONS,$@~)
	@chmod 0600 $@~/etc/ssh/ssh_host* 
	@chmod 0755 $@~/usr/bin/dbus-daemon
	@chmod 4755 $@~/usr/libexec/dbus-daemon-launch-helper
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/image/$(mm_NAME): $(top_build)/image/$(mm_NAME)
	@echo "making core image directory"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@# Create the read-only core image from the base file system.
	@# Copy the base file system to the read-only core image location.
	@# Remove extras directory items because they is included in the extras file system image.
	@# Remove the non-menu themes and non-default themes because they are included in the themes file system.
	@cp -pdR $</* $@~
	@rm -rf           $@~/$(extras_rootdir)
	@mkdir -m 0755 -p $@~/$(extras_rootdir)
	@# Create the rest for core image.
	@mkdir -m755 -p                     $@~/config
	@mkdir -m755 -p                     $@~/bin
	@mkdir -m755 -p                     $@~/root
	@mkdir -m755 -p                     $@~/dev
	@mkdir -m755 -p                     $@~/initrd
	@mkdir -m755 -p                     $@~/lib
	@mkdir -m755 -p                     $@~/sbin
	@mkdir -m755 -p                     $@~/proc
	@mkdir -m755 -p                     $@~/sys
	@mkdir -m755 -p                     $@~/var
	@mkdir -m755 -p                     $@~/var/log
	@mkdir -m755 -p                     $@~/var/lib
	@mkdir -m755 -p                     $@~/var/run
	@mkdir -m755 -p                     $@~/var/tmp
	@mkdir -m755 -p                     $@~/var/empty
	@mkdir -m755 -p                     $@~/var/lock/pmount
	@mkdir -m755 -p                     $@~/media/CastorBOX
	@mkdir -m755 -p                     $@~/mnt/cdrom
	@mkdir -m755 -p                     $@~/mnt/removable
	@mkdir -m755 -p                     $@~/mnt/system
	@mkdir -m755 -p                     $@~/mnt/tmp
	@ln -s                              ../media/CastorBOX $@~/mnt/local
	@mkdir -m755 -p                     $@~/tmp
	@$(call SET_PERMISSIONS,$@~)
	@chmod 600 $@~/etc/ssh/ssh_host* 
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/image/$(mm_NAME).fakeroot: $(top_build)/stage/image/$(mm_NAME)
	@echo "making core image directory fakeroot configuration file"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot -s $@~ sh -c                                             " \
		rm -rf           $</$(rootdir)/dev               ; \
		mkdir -m 0755 -p $</$(rootdir)/dev               ; \
		mknod -m 0600    $</$(rootdir)/dev/console c 5 1 ; \
		mknod -m 0600    $</$(rootdir)/dev/initctl p     "
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/image/initrd.fakeroot: $(top_build)/stage/image/initrd
	@echo "making initrd image directory fakeroot configuration file"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot -s $@~ sh -c                                             " \
		rm -rf           $</$(rootdir)/dev               ; \
		mkdir -m 0755 -p $</$(rootdir)/dev               ; \
		mknod -m 0600    $</$(rootdir)/dev/console c 5 1 ; \
		mknod -m 0600    $</$(rootdir)/dev/null c 1 3	 ; \
		mknod -m 0600    $</$(rootdir)/dev/tty1 c 4 1	 ; \
		mknod -m 0600    $</$(rootdir)/dev/tty2 c 4 2	 ; \
		mknod -m 0600    $</$(rootdir)/dev/tty3 c 4 3	 ; \
		mknod -m 0600    $</$(rootdir)/dev/tty4 c 4 4    ; \
		mknod -m 0600    $</$(rootdir)/dev/initctl p	 "
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/image/themes: $(top_build)/image/$(mm_NAME)
	@echo "making themes file system directory"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@cp -pdR $</usr/share/mythtv/themes/* $@~
	@# Remove the menu themes and default themes because they are included in the core image.
	@for theme in `cd $@~ ; ls -1` ; do \
		if [ -e $@~/$${theme}/mainmenu.xml ] || \
		   [ "$${theme}" = "default"       ] || \
		   [ "$${theme}" = "default-wide"  ] ; then \
			rm -rf $@~/$${theme} ; \
		fi ; \
	 done
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/image/extras: $(top_build)/image/$(mm_NAME)
	@echo "making extras file system directory"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@cp -pdR $</$(extras_rootdir)/* $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/helper: \
		$(top_source)/mm_local/mm_local_helper
	@echo "making helper directory"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@cp -pdR $^ $@~
	@cd $@~ ; for file in `ls -1` ; do  \
		md5sum $${file} > $${file}.md5 ; \
	 done
	@find $@~ -depth -type d -exec chmod 0755 '{}' \;
	@find $@~ -depth -type f -exec chmod 0644 '{}' \;
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/html: $(top_source)/html
	@echo "copying HTML documentation"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@cp -pdR $^ $@~
	@find $@~ -depth -type d -exec chmod 0755 '{}' \;
	@find $@~ -depth -type f -exec chmod 0644 '{}' \;
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/version:
	@echo "making version file"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@touch $@~
	@echo "$(mm_FULL_VERSION)" > $@~
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/scripts: \
		$(top_source)/installer/castorbox-install
	@echo "making scripts directory"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@cp -pdR $^ $@~
	@cp -pdR $(DESTDIR)$(esbindir)/extlinux $@~
	@find $@~ -depth -exec chmod 0755 '{}' \;
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/changelog.txt: $(top_source)/html/document-changelog.txt
	@echo "copying changelog file"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@cp -pdR $< $@~
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/readme.txt: $(top_source)/share-readme.txt
	@echo "copying readme file"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@cp -pdR $< $@~
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

$(top_build)/stage/kernel: $(DESTDIR)/$(LINUX_DIR)/vmlinuz
	@echo "copying kernel file"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@cp -pdR $< $@~
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/castorbox-$(mm_NAME).sfs: $(top_build)/stage/image/$(mm_NAME) $(top_build)/stage/image/$(mm_NAME).fakeroot
	@echo "making the squashfs version of the core image"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot -i $<.fakeroot sh -c "mksquashfs $< $@~ -no-exports -no-progress -processors 1 -no-fragments > /dev/null 2>&1"
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/initrd.sfs: $(top_build)/stage/image/initrd $(top_build)/stage/image/initrd.fakeroot
	@echo "making the squashfs version of the initrd image"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot -i $<.fakeroot sh -c "mksquashfs $< $@~ -no-exports -no-progress -processors 1 -no-fragments > /dev/null 2>&1"
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@


$(top_build)/stage/extras.sfs: $(top_build)/stage/image/extras
	@echo "making the squashfs version of the extras file system"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot                sh -c "mksquashfs $< $@~ -no-exports -no-progress -processors 1 -no-fragments > /dev/null 2>&1"
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/themes: $(top_build)/stage/image/themes
	@echo "making the squashfs version of the themes file system"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@mkdir -m 0755 -p $@~
	@for theme in `cd $< ; ls -1` ; do                                                    \
		fakeroot         sh -c "mksquashfs $</$${theme} $@~/$${theme}.sfs -no-exports -no-progress -processors 1 -no-fragments > /dev/null 2>&1" ; \
	 done
	@find $@~ -depth -type d -exec chmod 0755 '{}' \;
	@find $@~ -depth -type f -exec chmod 0644 '{}' \;
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/rootfs.tar.bz2: $(top_build)/stage/image/$(mm_NAME) $(top_build)/stage/image/$(mm_NAME).fakeroot
	@echo "making the tarball version of the core image"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot -i $<.fakeroot sh -c "tar -C $(<D) -jcf $@~ $(<F)"
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/extras.tar.bz2: $(top_build)/stage/image/extras
	@echo "making the tarball version of the extras file system"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot sh -c "tar -C $(<D) -jcf $@~ $(<F)"
	@chmod 0644 $@~
	@touch $@~
	@mv $@~ $@

$(top_build)/stage/themes.tar.bz2: $(top_build)/stage/image/themes
	@echo "making the tarball version of the themes file system"
	@mkdir -m 0755 -p $(@D)
	@rm -rf $@ $@~
	@fakeroot 	sh -c "tar -C $(<D) -jcf $@~ $(<F)"
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


$(top_share)/$(mm_NAME): \
		$(top_build)/stage/version			$(top_build)/stage/version.md5                  \
		$(top_build)/stage/kernel			$(top_build)/stage/kernel.md5			\
		$(top_build)/stage/initrd.sfs			$(top_build)/stage/initrd.sfs.md5		\
		$(top_build)/stage/castorbox-$(mm_NAME).sfs	$(top_build)/stage/castorbox-$(mm_NAME).sfs.md5		\
		$(top_build)/stage/scripts
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
	@cp -af $(top_share)/$*/* $(mm_HOME)/images/castorbox/$*/$(mm_RELEASE)/
	@echo $(mm_RELEASE) > $(mm_HOME)/images/castorbox/$*/latest

.PHONY: all build install 
