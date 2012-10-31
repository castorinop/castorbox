#-*- mode: Fundamental; tab-width: 4; -*-
# ex:ts=4

# This file contains configuration variables that are global to
# the GAR system.  Users wishing to make a change on a
# per-package basis should edit the category/package/Makefile, or
# specify environment variables on the make command-line.

# Variables that define the default *actions* (rather than just
# default data) of the system will remain in bbc.gar.mk
# (bbc.port.mk)

# Setting this variable will cause the results of your builds to
# be cleaned out after being installed.  Uncomment only if you
# desire this behavior!

# export BUILD_CLEAN = true

ALL_DESTIMGS = main build rootbin lnximg singularity

# These are the standard directory name variables from all GNU
# makefiles.  They're also used by autoconf, and can be adapted
# for a variety of build systems.
# 
# TODO: set $(SYSCONFDIR) and $(LOCALSTATEDIR) to never use
# /usr/etc or /usr/var

# Directory config for the "main" image
main_prefix ?= /
main_exec_prefix = $(prefix)
main_bindir = $(exec_prefix)/bin
main_sbindir = $(exec_prefix)/sbin
main_libexecdir = $(exec_prefix)/libexec
main_datadir = $(prefix)/share
main_sysconfdir = $(prefix)/etc
main_sharedstatedir = $(prefix)/share
main_localstatedir = $(prefix)/var
main_libdir = $(exec_prefix)/lib
main_infodir = $(prefix)/info
main_lispdir = $(prefix)/share/emacs/site-lisp
main_includedir = $(prefix)/include
main_mandir = $(prefix)/man
main_docdir = $(prefix)/share/doc
main_sourcedir = $(prefix)/src
main_licensedir = $(prefix)/licenses

# Directory config for the "build" image
build_prefix ?= /tmp/build
build_exec_prefix = $(build_prefix)
build_bindir = $(build_exec_prefix)/bin
build_sbindir = $(build_exec_prefix)/sbin
build_libexecdir = $(build_exec_prefix)/libexec
build_datadir = $(build_prefix)/share
build_sysconfdir = $(build_prefix)/etc
build_sharedstatedir = $(build_prefix)/share
build_localstatedir = $(build_prefix)/var
build_libdir = $(build_exec_prefix)/lib
build_infodir = $(build_prefix)/info
build_lispdir = $(build_prefix)/share/emacs/site-lisp
build_includedir = $(build_prefix)/include
build_mandir = $(build_prefix)/man
build_docdir = $(build_prefix)/share/doc
build_sourcedir = $(build_prefix)/src
build_licensedir = $(build_prefix)/licenses

# the DESTDIR is used at INSTALL TIME ONLY to determine what the
# filesystem root should be.  Each different DESTIMG has its own
# DESTDIR.
main_DESTDIR ?= /tmp/gar
build_DESTDIR ?= /
build_chroot_DESTDIR ?= /tmp/chroot

# allow us to link to libraries we installed
#main_CPPFLAGS += -nostdinc
#main_CFLAGS += -nostdinc -nostdlib
#main_LDFLAGS += -nostdlib
main_CPPFLAGS += -I$(DESTDIR)$(includedir) 
main_CFLAGS += -Os -I$(DESTDIR)$(includedir) -L$(DESTDIR)$(libdir) 
#main_CXXFLAGS += -Os -I$(DESTDIR)$(includedir) -L$(DESTDIR)$(libdir) 
main_LDFLAGS += -L$(DESTDIR)$(libdir) 
main_CPPFLAGS += -I$(GCC_INCLUDEDIR) -I$(CROSS_GCC_INCLUDEDIR)
main_CFLAGS += -I$(GCC_INCLUDEDIR) -I$(CROSS_GCC_INCLUDEDIR) -L$(GCC_LIBDIR) -L$(CROSS_GCC_LIBDIR)
#main_CXXFLAGS += -I$(GCC_INCLUDEDIR) -I$(CROSS_GCC_INCLUDEDIR) -L$(GCC_LIBDIR) -L$(CROSS_GCC_LIBDIR)
main_LDFLAGS += -L$(GCC_LIBDIR) -L$(CROSS_GCC_LIBDIR)

# allow us to link to libraries we installed
build_CPPFLAGS += -I$(DESTDIR)$(includedir) 
build_CFLAGS += -Os -I$(DESTDIR)$(includedir) -L$(DESTDIR)$(libdir) 
#build_CXXFLAGS += -Os -I$(DESTDIR)$(includedir) -L$(DESTDIR)$(libdir) 
build_LDFLAGS += -L$(DESTDIR)$(libdir) 

# Default main_CC to gcc, $(DESTIMG)_CC to main_CC and set CC based on $(DESTIMG)
main_CC ?= $(GARHOST)-gcc
main_CXX ?= g++
main_LD ?= $(GARHOST)-ld
build_CC ?= gcc
build_CXX ?= g++
build_LD ?= ld

# GARCH and GARHOST for main.  Override these for cross-compilation
main_GARCH ?= i386
main_GARHOST ?= i386-pc-linux-gnu

# GARCH and GARHOST for build.  Do not change these.
build_GARCH := $(shell arch)
build_GARHOST := $(GARBUILD)

# Don't build these packages as in the build image
build_NODEPEND = devel/glibc devel/gcc-primitives

# This is for foo-config chaos
PKG_CONFIG_PATH=$(DESTDIR)$(libdir)/pkgconfig/

# Put these variables in the environment during the
# configure build and install stages
STAGE_EXPORTS = DESTDIR prefix exec_prefix bindir sbindir libexecdir datadir
STAGE_EXPORTS += sysconfdir sharedstatedir localstatedir libdir infodir lispdir
STAGE_EXPORTS += includedir mandir docdir sourcedir
STAGE_EXPORTS += CPPFLAGS CFLAGS LDFLAGS
STAGE_EXPORTS += CC CXX

CONFIGURE_ENV += $(foreach TTT,$(STAGE_EXPORTS),$(TTT)="$($(TTT))")
BUILD_ENV += $(foreach TTT,$(STAGE_EXPORTS),$(TTT)="$($(TTT))")
INSTALL_ENV += $(foreach TTT,$(STAGE_EXPORTS),$(TTT)="$($(TTT))")
MANIFEST_ENV += $(foreach TTT,$(STAGE_EXPORTS),$(TTT)="$($(TTT))")

# Global environment
export GARBUILD
export PATH LD_LIBRARY_PATH #LD_PRELOAD
export PKG_CONFIG_PATH

GARCHIVEROOT ?= /var/www/garchive
GARCHIVEDIR = $(GARCHIVEROOT)/$(DISTNAME)
GARPKGROOT ?= /var/www/garpkg
GARPKGDIR = $(GARPKGROOT)/$(GARNAME)

# prepend the local file listing
FILE_SITES = file://$(FILEDIR)/ file://$(GARCHIVEDIR)/

#append the public archive
MASTER_SITES += http://www.lnx-bbc.org/garchive/$(DISTNAME)/ http://garchive.movealong.org/$(DISTNAME)/ http://build.lnx-bbc.org/garchive/$(DISTNAME)/

# Extra configuration for the lnx-bbc build
GAR_EXTRA_CONF += devel/gcc/package-api.mk
GAR_EXTRA_CONF += meta/singularity/singularity.conf.mk
GAR_EXTRA_CONF += meta/lnx.img/lnx.img.conf.mk
GAR_EXTRA_CONF += meta/root.bin/root.bin.conf.mk

# Extra libs to include with gar.mk
GAR_EXTRA_LIBS += bbc.lib.mk
