GARNAME = boost
GARVERSION = $(BOOST_VERSION)
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(DISTNAME).tar.bz2
PATCHFILES = $(DISTNAME)-fix-include.patch  $(DISTNAME)-libname.patch 
PATCHFILES += $(DISTNAME)-soname.patch $(DISTNAME)-ssize_t.patch    


LICENSE = boost
boost_LICENSE_TEXT = $(WORKSRC)/LICENSE_1_0.txt

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx 
BUILDDEPS = testing/boost-jam

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = custom 
INSTALL_SCRIPTS   = custom

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-toolset=cc \
	--without-python \
	--enable-aligned \
	--disable-debug \
	--with-gnu-ld 

BUILD_ENV   = \
	CC="$(CC)" \
        CXX="$(CXX)" \
	AR="$(AR)" \
	RANLIB="$(RANLIB)" \
	BOOST_BUILD_PATH="$(DESTDIR)$(bindir)" \
	USER_OPTIONS="$(CFLAGS)" 


include ../../gar.mk

build-custom:
	cd $(WORKSRC) && $(BUILD_ENV) bjam \
		-sTOOLS=gcc -sGXX=$(CXX) -sGCC=$(CC) \
		-sC++FLAGS="$(CXXFLAGS)" -sCFLAGS="$(CFLAGS)" \
		-q -jx -d1
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) && $(BUILD_ENV) bjam \
		-sTOOLS=gcc -sGXX=$(CXX) -sGCC=$(CC) \
		-sC++FLAGS="$(CXXFLAGS)" -sCFLAGS="$(CFLAGS)" \
		--prefix="$(DESTDIR)$(prefix)" --libdir="$(DESTDIR)$(prefix)" install
	@$(MAKECOOKIE)


post-install:
	@#rm -rf $(DESTDIR)$(libdir)/libtorrent.la
	@#sed -i 's%$${libdir}%$(DESTDIR)$${libdir}%g'         $(DESTDIR)$(libdir)/pkgconfig/libtorrent.pc
	@#sed -i 's%$${includedir}%$(DESTDIR)$${includedir}%g' $(DESTDIR)$(libdir)/pkgconfig/libtorrent.pc
	@$(MAKECOOKIE)
