GARNAME    ?= castorbox
GARVERSION ?= $(mm_VERSION)

all: mm-all

GAR_EXTRA_CONF += kernel-$(mm_KERNEL_VERSION)/linux/package-api.mk perl/perl/package-api.mk meta/castorbox/version.mk
include ../../gar.mk


build_vars := $(sort \
	$(shell cat $(mm_HOME)/script/castorbox.conf.mk | grep -e '^mm_' | sed -e 's%[ =].*%%') \
	$(shell cat $(mm_HOME)/script/meta/castorbox/version.mk | grep -e '^mm_' | sed -e 's%[ =].*%%') \
	)

bindirs_base := \
	$(extras_sbindir) \
	$(extras_bindir) \
	$(esbindir) \
	$(ebindir) \
	$(sbindir) \
	$(bindir) \
	$(libexecdir) 
bindirs := \
	$(bindirs_base) \
	$(libexecdir)
libdirs_base := \
	$(extras_libdir) \
	$(elibdir) \
	$(libdir) \
	$(libexecdir) \
	$(libdir)/mysql 

libdirs := \
	$(libdirs_base) \
	$(libdir)/xorg/modules \
	$(if $(filter $(mm_GRAPHICS),nvidia),$(libdir)/nvidia)
etcdirs := \
	$(extras_sysconfdir) \
	$(sysconfdir)
sharedirs := \
	$(extras_datadir) \
	$(datadir)
vardirs := \
	$(extras_localstatedir) \
	$(localstatedir)

MM_CONFIG_VARS = \
	bindir \
	bindirs \
	bindirs_base \
	build_bindir \
	build_DESTDIR \
	build_licensedir \
	build_rootdir \
	build_system_bins \
	build_vars \
	$(build_vars) \
	build_versiondir \
	datadir \
	DESTDIR \
	DESTIMG \
	ebindir \
	elibdir \
	esbindir \
	etcdirs \
	extras_licensedir \
	extras_rootdir \
	extras_versiondir \
	libdir \
	libdirs \
	libdirs_base \
	vardirs \
	licensedir \
	LINUX_DIR \
	LINUX_FULL_VERSION \
	LINUX_MODULESDIR \
	mm_GRAPHICS \
	mm_CONF_VERSION \
	mm_DEBUG \
	mm_DEBUG_BUILD \
	mm_DESTDIR \
	mm_HOME \
	mm_INSTALL_LATEST \
	mm_MMS_VERSION \
	mm_USER_BIN_LIST \
	mm_USER_ETC_LIST \
	mm_USER_LIB_LIST \
	mm_USER_REMOVE_LIST \
	mm_USER_SHARE_LIST \
	mm_VERSION_CASTORBOX \
	mm_VERSION \
	mm_VERSION_BASE \
	mm_VERSION_VCS \
	mm_HOST \
	mm_HTTP_HOST \
	mm_INSTALL_METHOD \
	mm_BRANCH \
	OBJDUMP \
	PERL_libdir \
	rootdir \
	sharedirs \
	sourcedir \
	STRIP \
	sysconfdir \
	versiondir

mm-all: $(WORKSRC)/build/config.mk

$(WORKSRC)/build/config.mk:
	@mkdir -p $(dir $@)
	@rm -rf $@~
	@$(foreach var,$(MM_CONFIG_VARS), echo $(var) = $($(var)) >> $@~ ; )
	@if [ -e $@ ] ; then \
		diff -q $@ $@~ 2>&1 > /dev/null ; \
		if [ $$? -ne 0 ] ; then \
			rm -rf $@ ; \
		fi ; \
	fi
	@if [ ! -e $@ ] ; then \
		cp -f $@~ $@ ; \
	fi
	@rm -f $@~

.PHONY: all mm-all
