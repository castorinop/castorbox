GARNAME = boost
GARVERSION = 1.43.0
CATEGORIES = lib
MASTER_SITES = http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(GARNAME)_$(subst .,_,$(GARVERSION)).tar.bz2
PATCHFILES = $(DISTNAME).patch.gar
LICENSE = boost
boost_LICENSE_TEXT = $(WORKSRC)/LICENSE_1_0.txt

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/cxx utils/bzip2

WORKSRC = $(WORKDIR)/$(GARNAME)_$(subst .,_,$(GARVERSION))

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = custom
INSTALL_SCRIPTS   = custom

CONFIGURE_ARGS = \
	--with-toolset=gcc \
	--without-icu \
	--without-libraries=python \
	--prefix=$(prefix) \
	--exec-prefix=$(exec_prefix) \
	--libdir=$(libdir) \
	--includedir=$(includedir)

xINSTALL_OVERRIDE_DIRS = prefix exec_prefix libdir includedir

GAR_EXTRA_CONF += devel/gcc/package-api.mk
include ../../gar.mk

pre-configure:
	@ln -s bootstrap.sh $(WORKSRC)/configure
	@$(MAKECOOKIE)

post-configure:
	@echo "using gcc : $(GCC_MAJOR_VERSION).$(GCC_MINOR_VERSION).$(GCC_TEENY_VERSION) : $(CXX) ;" >  $(WORKSRC)/user-config.jam
	@echo "using gcc : $(GCC_MAJOR_VERSION).$(GCC_MINOR_VERSION).$(GCC_TEENY_VERSION) : $(CXX) ;" >> $(WORKSRC)/tools/build/v2/user-config.jam
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) ; ./bjam
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) ; ./bjam install --prefix=$(DESTDIR)$(prefix) --exec-prefix=$(DESTDIR)$(exec_prefix) --libdir=$(DESTDIR)$(libdir) --includedir=$(DESTDIR)$(includedir)
	@$(MAKECOOKIE)

post-install:
	@rm -f $(DESTDIR)$(libdir)/libboost_date_time.a
	@rm -f $(DESTDIR)$(libdir)/libboost_filesystem.a
	@rm -f $(DESTDIR)$(libdir)/libboost_graph.a
	@rm -f $(DESTDIR)$(libdir)/libboost_iostreams.a
	@rm -f $(DESTDIR)$(libdir)/libboost_math_c99.a
	@rm -f $(DESTDIR)$(libdir)/libboost_math_c99f.a
	@rm -f $(DESTDIR)$(libdir)/libboost_math_c99l.a
	@rm -f $(DESTDIR)$(libdir)/libboost_math_tr1.a
	@rm -f $(DESTDIR)$(libdir)/libboost_math_tr1f.a
	@rm -f $(DESTDIR)$(libdir)/libboost_math_tr1l.a
	@rm -f $(DESTDIR)$(libdir)/libboost_prg_exec_monitor.a
	@rm -f $(DESTDIR)$(libdir)/libboost_program_options.a
	@rm -f $(DESTDIR)$(libdir)/libboost_regex.a
	@rm -f $(DESTDIR)$(libdir)/libboost_serialization.a
	@rm -f $(DESTDIR)$(libdir)/libboost_signals.a
	@rm -f $(DESTDIR)$(libdir)/libboost_system.a
	@rm -f $(DESTDIR)$(libdir)/libboost_test_exec_monitor.a
	@rm -f $(DESTDIR)$(libdir)/libboost_thread.a
	@rm -f $(DESTDIR)$(libdir)/libboost_unit_test_framework.a
	@rm -f $(DESTDIR)$(libdir)/libboost_wave.a
	@rm -f $(DESTDIR)$(libdir)/libboost_wserialization.a
	@$(MAKECOOKIE)
