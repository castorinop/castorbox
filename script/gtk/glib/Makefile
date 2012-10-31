GARNAME = glib
GARVERSION = 2.28.8
CATEGORIES = gtk
MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/glib/2.28/
DISTFILES = $(DISTNAME).tar.bz2
LICENSE = LGPL2

DESCRIPTION =
define BLURB
endef

DEPENDS    = lang/c lib/pcre lib/zlib
BUILDDEPS  = gtk/gtk-doc
ifneq ($(DESTIMG),build)
BUILDDEPS += gtk/glib
endif

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--cache-file=config.cache \
	--disable-silent-rules \
	--disable-debug \
	--disable-static \
	--enable-shared \
	--disable-selinux \
	--disable-fam \
	--enable-xattr \
	--enable-regex \
	--disable-gtk-doc \
	--disable-man \
	--disable-dtrace \
	--disable-systemtap \
	--disable-gcov \
	--enable-Bsymbolic \
	--with-gnu-ld \
	--with-threads=posix \
	--with-pcre=system

CONFIGURE_ENV  =
ifneq ($(DESTIMG),build)
CONFIGURE_ENV += \
	ac_cv_func_mmap_fixed_mapped='yes' \
	ac_cv_func_posix_getpwuid_r='yes' \
	ac_cv_func_posix_getgrgid_r='yes' \
	ac_cv_func_printf_unix98='yes' \
	ac_cv_func_snprintf_c99='yes' \
	ac_cv_func_vsnprintf_c99='yes' \
	glib_cv_stack_grows='no' \
	glib_cv_uscore='no' \
	glib_cv_va_val_copy='no'
endif

include ../../gar.mk

# Fails to compile with GCC 4.5.2's link time optimization enabled, outputing the error:
# "mem-overflow.c:137:1: sorry, unimplemented: gimple bytecode streams do not support the optimization attribute".
CFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
LDFLAGS := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(call FIX_LIBTOOL,$(WORKSRC),configure)
	@$(MAKECOOKIE)

post-install:
	@rm -rf $(DESTDIR)$(libdir)/libgio-2.0.la
	@rm -rf $(DESTDIR)$(libdir)/libglib-2.0.la
	@rm -rf $(DESTDIR)$(libdir)/libgmodule-2.0.la
	@rm -rf $(DESTDIR)$(libdir)/libgobject-2.0.la
	@rm -rf $(DESTDIR)$(libdir)/libgthread-2.0.la
	@$(MAKECOOKIE)
