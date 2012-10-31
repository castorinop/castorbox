GARNAME = libmng-mini
GARVERSION = $(LIBMNG_VERSION)
CATEGORIES = lib
SOURCEPKG = lib/libmng
PATCHFILES = libmng-$(GARVERSION)-no_jpeg.patch
LICENSE = libmng
libmng_LICENSE_TEXT = $(WORKSRC)/LICENSE

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/zlib

WORKSRC = $(WORKDIR)/libmng-$(GARVERSION)

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld \
	--without-zlib \
	--without-lcms \
	--without-jpeg

GAR_EXTRA_CONF += lib/libmng/package-api.mk
include ../../gar.mk

pre-configure:
	@cp $(WORKSRC)/makefiles/configure.in $(WORKSRC)
	@cp $(WORKSRC)/makefiles/Makefile.am $(WORKSRC)
	@cd $(WORKSRC) ; autoreconf --verbose --install --force
	@$(MAKECOOKIE)

install-custom:
	@install -m 0755 $(WORKSRC)/.libs/libmng.a $(DESTDIR)$(libdir)/libmng-mini.a
	@$(MAKECOOKIE)
