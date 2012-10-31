GARNAME = boost-jam
GARVERSION = 3.1.14
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/boost/
DISTFILES = $(DISTNAME).tgz

LICENSE = boost
boost_LICENSE_TEXT = $(WORKSRC)/LICENSE_1_0.txt

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

BUILD_SCRIPTS     = custom
INSTALL_SCRIPTS   = custom

BUILD_ARGS   = \
	CC="$(CC)" \
	AR="$(AR)" \
	RANLIB="$(RANLIB)" \
	CFLAGS="" \
	LDFLAGS="$(LDFLAGS)" \
	DESTDIR="$(DESTDIR)" \
	prefix="$(prefix)" \
	bindir="$(bindir)" \
	libdir="$(libdir)" \
	includedir="$(includedir)" \
	mandir="$(mandir)"

include ../../gar.mk

build-custom:
	cd $(WORKSRC) && $(BUILD_ARGS) ./build.sh cc
	@$(MAKECOOKIE)

install-custom:
	@cp -f $(WORKSRC)/bin.linux*/bjam $(DESTDIR)$(bindir)/
	@$(MAKECOOKIE)
