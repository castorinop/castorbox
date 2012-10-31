GARNAME    ?= castorbox
GARVERSION ?= $(mm_VERSION)

all: mm-all

GAR_EXTRA_CONF += kernel-$(mm_KERNEL_VERSION)/linux/package-api.mk devel/build-system-bins/package-api.mk meta/castorbox/version.mk
include ../../gar.mk

mm-all:
	@echo "checking ..."
	@# Check build environment.
	@echo "  build system binaries ..."
	@$(foreach pkg,$(build_system_bins), \
		$(foreach bin,$(sort $(build_system_bins_$(subst -,_,$(pkg)))), \
			echo "    '$(bin)' (from package '$(pkg)')" ; \
			if [ ! "$$?" = "0" ] ; then \
				echo "error: your system does not contain the program '$(bin)' (from package '$(pkg)')." ; \
				exit 1 ; \
			fi ; \
		) \
	)
	@echo "  build user uid and gid"
	@if [ `id -u` -eq 0 ] || [ `id -g` -eq 0 ] ; then \
		echo "error: gar-minimyth cannot be run by the user 'root'." ; \
		exit 1 ; \
	fi
	@echo "  / and /usr directory access"
	@for dir in /          /lib                              /bin           /sbin \
	            /usr       /usr/lib       /usr/libexec       /usr/bin       /usr/sbin \
	            /usr/local /usr/local/lib /usr/local/libexec /usr/local/bin /usr/local/sbin\
	            /opt ; do \
		if [ -e "$${dir}" ] && [ -w "$${dir}" ] ; then \
			echo "error: gar-minimyth cannot be run by a user with write access to '$${dir}'." ; \
			exit 1 ; \
		fi ; \
	done
	@echo "  build system binaries ... done"
	@# Check for obsolete parameters and parameter values.
	@echo "  obsolete parameters and parameter values ..."
	@echo "    mm_CHIPSETS"
	@if [ -n "$(mm_CHIPSETS)" ] ; then \
		echo "error: mm_CHIPSETS is obsolete." ; \
		exit 1 ; \
	fi
	@echo "    mm_INSTALL_TFTP_BOOT"
	@if [ -n "$(mm_INSTALL_TFTP_BOOT)" ] ; then \
		echo "error: mm_INSTALL_TFTP_BOOT should be replaced with mm_INSTALL_RAM_BOOT." ; \
		exit 1 ; \
	fi
	@echo "    mm_INSTALL_CRAMFS"
	@if [ -n "$(mm_INSTALL_CRAMFS)" ] ; then \
		echo "error: mm_INSTALL_CRAMFS should be replaced with mm_INSTALL_RAM_BOOT." ; \
		exit 1 ; \
	fi
	@echo "    mm_INSTALL_NFS"
	@if [ -n "$(mm_INSTALL_NFS)" ] ; then \
		echo "error: mm_INSTALL_NFS should be replaced with mm_INSTALL_NFS_BOOT." ; \
		exit 1 ; \
	fi
	@if [ -n "$(mm_MYTH_SVN_VERSION)" ] ; then \
		echo "error: mm_MYTH_SVN_VERSION should be replaced with mm_MYTH_TRUNK_VERSION." ; \
		exit 1 ; \
	fi
	@echo "    mm_XORG_VERSION='old'"
	@if [ "$(mm_XORG_VERSION)" = "old" ] ; then \
		echo "error: mm_XORG_VERSION=\"old\" should be replaced with mm_XORG_VERSION=\"6.8\"." ; \
		exit 1 ; \
	fi
	@echo "    mm_XORG_VERSION='new'"
	@if [ "$(mm_XORG_VERSION)" = "new" ] ; then \
		echo "error: mm_XORG_VERSION=\"new\" should be replaced with mm_XORG_VERSION=\"7.0\"." ; \
		exit 1 ; \
	fi
	@echo "  obsolete parameters and parameter values ... done"
	@# Check build parameters.
	@echo "  build parameters ..."
	@echo "    HOME"
	@if [ ! -e $(HOME)/.castorbox/castorbox.conf.mk ] ; then \
		echo "error: configuration file '$(HOME)/.castorbox/castorbox.conf.mk' is missing." ; \
		exit 1 ; \
	fi
	@echo "    mm_GARCH"
	@if [ ! "$(mm_GARCH)" = "c3"          ] && \
	    [ ! "$(mm_GARCH)" = "c3-2"        ] && \
	    [ ! "$(mm_GARCH)" = "pentium-mmx" ] && \
	    [ ! "$(mm_GARCH)" = "x86-64"      ] ; then \
		echo "error: mm_GARCH=\"$(mm_GARCH)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "    mm_HOME"
	@if [ ! "$(mm_HOME)" = "`cd $(GARDIR)/.. ; pwd`" ] ; then \
		echo "error: mm_HOME must be set to \"`cd $(GARDIR)/.. ; pwd`\" but has been set to \"$(mm_HOME)\"."; \
		exit 1 ; \
	fi
	@if [ "$(firstword $(strip $(subst /, ,$(mm_HOME))))" = "$(firstword $(strip $(subst /, ,$(qt3prefix))))" ] ; then \
		echo "error: MiniMyth cannot be built in a subdirectory of \"/$(firstword $(strip $(subst /, ,$(qt3prefix))))\"."; \
		exit 1 ; \
	fi
	@if [ "$(firstword $(strip $(subst /, ,$(mm_HOME))))" = "$(firstword $(strip $(subst /, ,$(qt4prefix))))" ] ; then \
		echo "error: MiniMyth cannot be built in a subdirectory of \"/$(firstword $(strip $(subst /, ,$(qt4prefix))))\"."; \
		exit 1 ; \
	fi
	@echo "    mm_DEBUG"
	@if [ ! "$(mm_DEBUG)" = "yes" ] && [ ! "$(mm_DEBUG)" = "no" ] ; then \
		echo "error: mm_DEBUG=\"$(mm_DEBUG)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "    mm_DEBUG_BUILD"
	@if [ ! "$(mm_DEBUG_BUILD)" = "yes" ] && [ ! "$(mm_DEBUG_BUILD)" = "no" ] ; then \
		echo "error: mm_DEBUG_BUILD=\"$(mm_DEBUG_BUILD)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "    mm_GRAPHICS"
	@for graphic in $(mm_GRAPHICS) ; do \
		if [ ! "$${graphic}" = "intel"      ] && \
		   [ ! "$${graphic}" = "nvidia"     ] && \
		   [ ! "$${graphic}" = "openchrome" ] && \
		   [ ! "$${graphic}" = "radeon"     ] && \
		   [ ! "$${graphic}" = "radeonhd"   ] && \
		   [ ! "$${graphic}" = "savage"     ] && \
		   [ ! "$${graphic}" = "sis"        ] && \
		   [ ! "$${graphic}" = "virtualbox" ] && \
		   [ ! "$${graphic}" = "vmware"     ] ; then \
			echo "error: mm_GRAPHICS=\"$${graphic}\" is an invalid value." ; \
			exit 1 ; \
		fi ; \
	done
	@echo "    mm_KERNEL_HEADERS_VERSION"
	@if [ ! "$(mm_KERNEL_HEADERS_VERSION)" = "3.0" ] && \
	    [ ! "$(mm_KERNEL_HEADERS_VERSION)" = "3.0" ] ; then \
		echo "error: mm_KERNEL_HEADERS_VERSION=\"$(mm_KERNEL_HEADERS_VERSION)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "    mm_KERNEL_VERSION"
	@if [ ! "$(mm_KERNEL_VERSION)" = "3.0" ] && \
	    [ ! "$(mm_KERNEL_VERSION)" = "3.0" ] ; then \
		echo "error: mm_KERNEL_VERSION=\"$(mm_KERNEL_VERSION)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "    mm_KERNEL_VERSION >= mm_KERNEL_HEADERS_VERSION"
	@if [ `echo ${mm_KERNEL_HEADERS_VERSION} | sed 's%2\.6\.\(.*\)%\1%'` -gt \
	      `echo ${mm_KERNEL_VERSION}         | sed 's%2\.6\.\(.*\)%\1%'`     ] ; then \
		echo "error: mm_KERNEL_HEADERS_VERSION is greater than mm_KERNEL_VERSION." ; \
		exit 1 ; \
	fi
	@echo "    mm_MMS_VERSION"
	@if [ ! "$(mm_MMS_VERSION)" = "castorbox-1.1.x" ] && \
	    [ ! "$(mm_MMS_VERSION)" = "trunk"        ] ; then \
		echo "error: mm_MMS_VERSION=\"$(mm_MMS_VERSION)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "    mm_NVIDIA_VERSION"
	@if [ ! "$(mm_NVIDIA_VERSION)" = "96.43.19"  ] && \
	    [ ! "$(mm_NVIDIA_VERSION)" = "173.14.28" ] && \
	    [ ! "$(mm_NVIDIA_VERSION)" = "302.17" ] ; then \
		echo "error: mm_NVIDIA_VERSION=\"$(mm_NVIDIA_VERSION)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "    mm_XORG_VERSION"
	@if [ ! "$(mm_XORG_VERSION)" = "7.4" ] && \
	    [ ! "$(mm_XORG_VERSION)" = "7.6" ] ; then \
		echo "error: mm_XORG_VERSION=\"$(mm_XORG_VERSION)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "  build parameters ... done"
	@# Check build system parameters.
	@echo "  build system parameters ..."
	@if [ ! "$(build_GARCH_FAMILY)" = "i386"   ] && \
            [ ! "$(build_GARCH_FAMILY)" = "x86_64" ] ; then \
		echo "error: build_GARCH_FAMILY=\"$(build_GARCH_FAMILY)\" is an invalid value." ; \
		exit 1 ; \
	fi
	@echo "  distribution parameters ... done"
	@echo "checking ... done"

.PHONY: all mm-all
