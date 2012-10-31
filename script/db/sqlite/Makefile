GARNAME = sqlite
GARVERSION = 3.6.21
CATEGORIES = db
MASTER_SITES = http://www.sqlite.org/
DISTFILES = $(DISTNAME).tar.gz
LICENSE =

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c
BUILDDEPS = utils/tcl

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-shared \
	--disable-static \
	--enable-largefile \
	--enable-threadsafe \
	--disable-cross-thread-connections \
	--disable-threads-override-locks \
	--disable-releasemode \
	--enable-tempstore=no \
	--disable-tcl \
	--disable-readline \
	--disable-debug \
	--enable-amalgamation \
	--disable-load-extension \
	--disable-gcov  \
	--with-gnu-ld

include ../../gar.mk

pre-configure:
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(call FIX_LIBTOOL,$(WORKSRC),configure)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libsqlite3.la
	@$(MAKECOOKIE)
