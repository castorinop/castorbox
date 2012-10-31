GARNAME = php
GARVERSION = 5.3.2
CATEGORIES = lang
MASTER_SITES =  http://www.php.net/distributions/
DISTFILES = $(DISTNAME).tar.bz2
# php-5.2.5-systzdata.patch 
#PATCHFILES = php-shared.diff \
#	php-phpbuilddir.diff \
#	php-libtool.diff \
#        php-posix-autoconf-2.62_fix.diff \
#	php-dlopen.diff \
#	php-filter-shared.diff 
#	php-no_libedit.diff \

PATCHFILES =  $(DISTNAME).patch.gar \
	php-init.diff \
	php-shared.diff \
	php-libtool.diff \
	php-no_egg.diff \
	php-phpize.diff \
	php-phpbuilddir.diff \
	php5-apache2-filters.diff \
	php-xmlrpc_epi.patch \
	php-xmlrpc_no_rpath.diff \
	php-really_external_sqlite2.diff \
	php-mail.diff \
	php-filter-shared.diff \
	php-dba-link.patch \
	php-5.2.8-bdb4.7_fix.diff \
	php-zlib-for-getimagesize.patch \
	php-zlib.patch \
	php-session.save_path.diff \
	php-exif_nesting_level.diff \
	php-cxx.diff \
	php-install.diff \
	php-umask.diff \
	php-shutdown.diff \
	php-libc-client.diff \
	php-no_pam_in_c-client.diff \
	php-dlopen.diff \
	php-tests-wddx.diff \
	php-bug43221.diff \
	php-bug43589.diff \
	php-5.1.0RC6-CVE-2005-3388.diff \
	php-no-fvisibility_hidden_fix.diff \
	php-5.3.0RC1-enchant_lib64_fix.diff \
	php-5.3.0RC2-xmlrpc-epi_fix.diff \
	php-5.3.2-aconf26x.patch \
	php-post_configure_libdl.patch 

LICENSE = PHP
PHP_LICENSE_TEXT = $(WORKSRC)/LICENSE
DESCRIPTION =
define BLURB
endef

LIBDEPS =  lib/libstdcxx lib/ncurses lib/openssl lib/zlib db/sqlite lib/libxml2 lib/readline lib/pcre lib/zlib utils/bzip2 net/curl 

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom 
INSTALL_SCRIPTS = custom 

CONFIGURE_ENV= READLINE_SHARED_LIBADD="$READLINE_SHARED_LIBADD -lhistory -lreadline -lncurses" \
	EXTENSION_DIR="$(libdir)/php/extensions" \
	oldstyleextdir=yes


BUILD_ARGS = oldstyleextdir=yes \
	EXTENSION_DIR="$(libdir)/php/extensions" \
	$(COFIGURE_ENV) \
	INSTALL_ROOT="$(DESTDIR)" \
	DESTDIR="$(DESTDIR)"

INSTALL_ARGS = $(BUILD_ARGS) \
	INSTALL_IT="\$$(LIBTOOL) --mode=install install libphp5_common.la $(DESTDIR)$(libdir)/" \
	INSTALL_CLI="\$$(LIBTOOL) --silent --mode=install install sapi/cli/php $(DESTDIR)$(bindir)/php" install

MODES = php cgi


CONFIGURE_ARGS = $(DIRPATHS)  --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-debug \
	--enable-inline-optimization \
	--with-exec-dir=$(bindir) \
	--enable-shared=yes \
	--enable-static=no \
	--with-config-file-path=$(sysconfdir) \
	--with-config-file-scan-dir=$(sysconfdir)/php.d \
	--with-regex=system \
	--with-pcre-regex=$(DESTDIR)$(prefix) \
	--with-freetype-dir=$(DESTDIR)$(prefix) --with-zlib=$(DESTDIR)$(prefix) \
	--with-png-dir=$(DESTDIR)$(prefix) \
	--enable-magic-quotes \
	--enable-safe-mode \
	--with-zlib=shared,$(DESTDIR)$(prefix) --with-zlib-dir=$(DESTDIR)$(prefix) \
	--with-openssl=shared,$(DESTDIR)$(prefix) \
	--enable-libxml=$(DESTDIR)$(prefix) --with-libxml-dir=$(DESTDIR)$(prefix) \
	--enable-mod_charset \
	--without-pear \
	--enable-bcmath=shared \
	--with-bz2=shared,$(DESTDIR)$(prefix) \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--with-curl=shared,$(DESTDIR)$(prefix) --without-curlwrappers \
	--enable-dba=no \
	--enable-dom=shared,$(DESTDIR)$(prefix) --with-libxml-dir=$(DESTDIR)$(prefix) \
	--enable-exif=shared \
	--enable-filter=shared --with-pcre-dir=$(DESTDIR)$(prefix) \
	--enable-json=shared \
	--with-openssl-dir=$(DESTDIR)$(prefix) --enable-ftp=shared \
	--without-gd \
	--with-gettext=shared,$(DESTDIR)$(prefix) \
	--without-gmp \
	--enable-hash=shared,$(DESTDIR)$(prefix) \
	--with-iconv=shared \
	--without-imap \
	--without-ldap \
	--enable-mbstring=shared,$(DESTDIR)$(prefix) --enable-mbregex \
	--without-mcrypt \
	--with-mhash=shared,$(DESTDIR)$(prefix) \
	--without-mssql --without-mysqli \
	--without-unixODBC \
	--enable-pcntl=shared \
	--enable-pdo=shared,$(DESTDIR)$(prefix) --with-pdo-sqlite=shared,$(DESTDIR)$(prefix) \
	--without-pgsql \
	--disable-phar \
	--enable-posix=shared \
	--without-pspell \
	--with-readline=shared,$(DESTDIR)$(prefix) \
	--without-recode \
	--enable-session=shared,$(DESTDIR)$(prefix) \
	--enable-shmop=shared,$(DESTDIR)$(prefix) \
	--enable-simplexml \
	--without-snmp \
	--enable-soap=shared,$(DESTDIR)$(prefix) --with-libxml-dir=$(DESTDIR)$(prefix) \
	--enable-sockets=shared,$(DESTDIR)$(prefix) \
	--without-sqlite \
	--with-sqlite3=shared,$(DESTDIR)$(prefix) \
	--enable-sysvmsg=shared,$(DESTDIR)$(prefix) \
	--enable-sysvsem=shared,$(DESTDIR)$(prefix) \
	--enable-sysvshm=shared,$(DESTDIR)$(prefix) \
	--without-tidy \
	--enable-tokenizer=shared,$(DESTDIR)$(prefix) \
	--enable-xml=shared,$(DESTDIR)$(prefix) \
	--enable-xmlreader=shared,$(DESTDIR)$(prefix) \
	--without-xmlrpc \
	--enable-xmlwriter=shared,$(DESTDIR)$(prefix) \
	--without-xsl \
	--enable-wddx=shared \
	--with-gnu-ld

include ../../gar.mk

# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))

patch-php-post_configure_libdl.patch:
	@$(MAKECOOKIE)

prepare-build_ext:
	@# "temporary" autoconf-2.62 "fixes"
	@#perl -pi -e "s|have_broken_glibc_fopen_append|have_cv_broken_glibc_fopen_append|g" *.m4
	@for i in `find "$(WORKSRC) -name "*.m4"`; do \
	    sed -i "s@cv_php_mbstring_stdarg@php_cv_mbstring_stdarg@g" $$i; \
	    sed -i "s@php_can_support_proc_open@php_cv_can_support_proc_open@g" $$i; \
	done
	#
	@mkdir -p $(WORKSRC)/php-devel/extensions
	@mkdir -p $(WORKSRC)/php-devel/sapi
	#
	# Install test files in php-devel
	@cp -a $(WORKSRC)/tests $(WORKSRC)/php-devel
	#
	@cp -dpR $(WORKSRC)/ext/* $(WORKSRC)/php-devel/extensions/
	@rm -f $(WORKSRC)/php-devel/extensions/informix/stub.c
	@rm -f $(WORKSRC)/php-devel/extensions/standard/.deps
	@rm -f $(WORKSRC)/php-devel/extensions/skeleton/EXPERIMENTAL
	@rm -f $(WORKSRC)/php-devel/extensions/ncurses/EXPERIMENTAL
	# SAPI
	@cp -dpR $(WORKSRC)/sapi/* $(WORKSRC)/php-devel/sapi/ 
	@rm -f $(WORKSRC)/php-devel/sapi/thttpd/stub.c
	@rm -f $(WORKSRC)/php-devel/sapi/cgi/php.sym
	@rm -f $(WORKSRC)/php-devel/sapi/fastcgi/php.sym
	@rm -f $(WORKSRC)/php-devel/sapi/pi3web/php.sym
	# don't ship MS Windows source
	@rm -rf $(WORKSRC)/php-devel/extensions/com_dotnet
	# likewise with these:
	@find $(WORKSRC)/php-devel -name "*.dsp" | xargs rm -f
	@find $(WORKSRC)/php-devel -name "*.mak" | xargs rm -f
	@find $(WORKSRC)/php-devel -name "*.w32" | xargs rm
	# maek sure using system libs
	@rm -rf $(WORKSRC)/ext/ereg/regex
	@rm -rf $(WORKSRC)/ext/pcre/pcrelib
	@rm -rf $(WORKSRC)/ext/pdo_sqlite/sqlite
	@rm -rf $(WORKSRC)/ext/xmlrpc/libxmlrpc
	#
	@echo \#!/bin/bash  				> $(WORKSRC)/php-devel/buildext
	@echo $(CC) -Wall -fPIC -shared $(CFLAGS) \\	>> $(WORKSRC)/php-devel/buildext
	@echo -I. \`$(DESTDIR)$(bindir)-config/php-config --includes\` \\ 	>> $(WORKSRC)/php-devel/buildext
	@echo -I$(DESTDIR)$(includedir)/libxml2 \\	>> $(WORKSRC)/php-devel/buildext
	@echo -I$(DESTDIR)$(includedir)/freetype \\	>> $(WORKSRC)/php-devel/buildext
	@echo -I$(DESTDIR)$(includedir)/openssl \\	>> $(WORKSRC)/php-devel/buildext
	@echo -I$(WORKSRC)/php-devel/ext \\		>> $(WORKSRC)/php-devel/buildext
	@echo -I$(DESTDIR)$(includedir)/\$$1 \\		>> $(WORKSRC)/php-devel/buildext
	@echo \$$4 \$$2 -o \$$1.so \$$3 -lc		>> $(WORKSRC)/php-devel/buildext
	@chmod 755 $(WORKSRC)/php-devel/buildext
	@$(MAKECOOKIE)


pre-configure: prepare-build_ext
	@# aclocal workaround - to be improved
	@cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >> $(WORKSRC)/aclocal.m4
	@# Force use of system libtool:
	@cd $(WORKSRC) && libtoolize --force --copy
	@cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 > $(WORKSRC)/build/libtool.m4
	@# Regenerate configure scripts (patches change config.m4's)
	@touch $(WORKSRC)/configure.in
	@cd $(WORKSRC) && ./buildconf --force
	@$(call FIX_LIBTOOL,$(WORKSRC)/configure)
	@echo " ==> Applying patch $(DOWNLOADDIR)/php-post_configure_libdl.patch"
	@$(GARPATCH) < $(DOWNLOADDIR)/php-post_configure_libdl.patch
	@$(MAKECOOKIE)

%-configure:
	@echo " ==> Running configure $* in $(WORKSRC)"
	@cd $(WORKSRC) && $(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS) \
		-C \
	`[ $* = cgi ] && echo --disable-cli` \
	`[ $* = php ] && echo --disable-cgi --enable-cli`
	@cp -f $(WORKSRC)/Makefile $(WORKSRC)/Makefile.$*
	@sed -i "s@-prefer-non-pic -static@@g" $(WORKSRC)/Makefile.$*
	@sed -i "s@-I$(includedir)@-I$(DESTDIR)$(includedir)@g" $(WORKSRC)/Makefile.$*
	@cp -f $(WORKSRC)/main/php_config.h $(WORKSRC)/php_config.h.$*
	@$(MAKECOOKIE)

%-build:
	@echo " ==> Running make $* in $(WORKSRC)"
	cp $(WORKSRC)/php_config.h.$* $(WORKSRC)/main/php_config.h
	cp -f $(WORKSRC)/Makefile.$* $(WORKSRC)/Makefile 
	$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(WORKSRC) -f Makefile.$* $(BUILD_ARGS)
	@$(MAKECOOKIE)

cgi-install:
	cd $(WORKSRC) && ./libtool --silent --mode=install install sapi/cgi/php-cgi $(DESTDIR)$(bindir)/php-cgi
	@$(MAKECOOKIE)

%-install:
	@echo " ==> Running make $* in $(WORKSRC)"
	cp $(WORKSRC)/php_config.h.$* $(WORKSRC)/main/php_config.h
	cp -f $(WORKSRC)/Makefile.$* $(WORKSRC)/Makefile 
	$(INSTALL_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(WORKSRC) -f Makefile.$* $(INSTALL_ARGS) install install-sapi
	@$(MAKECOOKIE)



configure-custom: $(addsuffix -configure,$(MODES)) 

build-custom: $(addsuffix -build,$(MODES))

install-custom: $(addsuffix -install,$(MODES))  

post-install:
	@rm -rf $(DESTDIR)$(libdir)$(GARNAME)$(GARVERSION)/config/lib$(GARNAME)$(GARVERSION).a
	@rm -rf $(DESTDIR)$(libdir)/php/extensions/*.a
	@rm -rf $(DESTDIR)$(sysconfdir)/php.d; 
	@mkdir -p $(DESTDIR)$(sysconfdir)/php.d
	@let count=00; for i in bz2 calendar ctype curl dba dom exif openssl zlib ftp gd gettext gmp iconv imap intl ldap mbstring mcrypt fileinfo enchant odbc pcntl posix pspell readline recode sybase_ct session shmop snmp soap sockets hash sysvmsg sysvsem sysvshm tidy tokenizer xml xmlrpc wddx xmlreader xsl xmlwriter bcmath pdo pdo_sqlite sqlite3 filter json zip; do \
	if [ -f "$(DESTDIR)$(libdir)/php/extensions/$$i.so" ]; then \
		echo "extension=$$i.so" > $(DESTDIR)$(sysconfdir)/php.d/$$(printf "%02d_%s.ini" $${count} $${i}); \
		let count=count+1; \
	fi; \
	done
	@rm -f $(DESTDIR)$(bindir)-config/php-config
	@rm -f $(DESTDIR)$(bindir)-config/$(compiler_prefix)php-config
	@mkdir -p $(DESTDIR)$(bindir)-config
	@mv $(DESTDIR)$(bindir)/php-config $(DESTDIR)$(bindir)-config/php-config
	@$(if $(compiler_prefix), ln -s php-config $(DESTDIR)$(bindir)-config/$(compiler_prefix)php-config)
	@$(MAKECOOKIE)

