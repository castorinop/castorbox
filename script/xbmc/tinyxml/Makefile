GARNAME = tinyxml
GARVERSION = 2.6.2
CATEGORIES = lib
MASTER_SITES = http://downloads.sourceforge.net/$(GARNAME)/$(GARVERSION)/
DISTFILES =$(GARNAME)_$(subst .,_,$(GARVERSION)).tar.gz
PATCHFILES = $(DISTNAME)-stl.patch
#LICENSE = zlib

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

BUILD_SCRIPTS     = custom
INSTALL_SCRIPTS   = custom

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--with-gnu-ld 

include ../../gar.mk


WORKSRC := $(WORKDIR)/$(GARNAME)
# Fails to compile (for x86_64) with GCC 4.5.3's link time optimization.
CFLAGS   := $(filter-out -flto -fuse-linker-plugin, $(CFLAGS))
CXXFLAGS := $(filter-out -flto -fuse-linker-plugin, $(CXXFLAGS))
LDFLAGS  := $(filter-out -flto -fuse-linker-plugin, $(LDFLAGS))


build-custom:
	@cd $(WORKSRC);	for i in tinyxml.cpp tinystr.cpp tinyxmlerror.cpp tinyxmlparser.cpp; do \
	  $(CXX) $(CXXFLAGS) -o $$i.o -c $$i; \
	  done
	@cd $(WORKSRC); $(CXX) $(CXXFLAGS) $(LDFLAGS) -shared -o lib$(GARNAME).so.0.$(GARVERSION) \
		     -Wl,-soname,lib$(GARNAME).so.0 *.cpp.o
	@$(MAKECOOKIE)

install-custom:
	@install -m 644 $(WORKSRC)/lib$(GARNAME).so.0.$(GARVERSION) $(DESTDIR)/$(libdir)
	@install -m 644 $(WORKSRC)/*.h $(DESTDIR)/$(includedir)
	ln -sf lib$(GARNAME).so.0.$(GARVERSION) $(DESTDIR)/$(libdir)/lib$(GARNAME).so.0
	ln -sf lib$(GARNAME).so.0.$(GARVERSION) $(DESTDIR)/$(libdir)/lib$(GARNAME).so
	@$(MAKECOOKIE)
