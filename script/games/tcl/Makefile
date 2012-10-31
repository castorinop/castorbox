GARNAME =  tcl
GARVERSION = 8.4.14
CATEGORIES = games
MASTER_SITES = http://unc.dl.sourceforge.net/sourceforge/$(GARNAME)/
MASTER_SITES += http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(GARNAME)$(GARVERSION)-src.tar.gz
PATCHFILES = 
# put your e-mail address in here, as in: 	Foo Bar <foo@bar.com>
MAINTAINER = Paul Gray <gray@cs.uni.edu>
# GPL, GPL2, BSD, MIT, etc. Or add the URL to any custom license
LICENSE = weird
weird_LICENSE_TEXT = $(WORKDIR)/$(GARNAME)$(GARVERSION)/license.terms

DESCRIPTION = Tcl is a multi-platform scripting language 
define BLURB
Tcl provides a powerful platform for creating integration applications that
tie together diverse applications, protocols, devices, and frameworks.
When paired with the Tk toolkit, Tcl provides the fastest and most powerful
way to create GUI applications that run on PCs, Unix, and the Macintosh.
Tcl can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.
endef

# Dependencies are of the form categorydir/packagedir
# LIBDEPS are for libraries, and DEPENDS are for everything else
LIBDEPS =
DEPENDS =
# Builddeps are installed in $(BUILD_PREFIX) in their entirety
BUILDDEPS =
WORKSRC=$(WORKDIR)/$(GARNAME)$(GARVERSION)/unix

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-gnu-ld
NODIRPATHS = 

# If some dirs are trying to install into /, list their names
# here, such as: prefix bindir mandir
INSTALL_ARGS = INSTALL_ROOT=$(DESTDIR)
INSTALL_OVERRIDE_DIRS = 

# This should go before any hand-made rules.
include ../../gar.mk
include ../games.mk

pre-everything:
