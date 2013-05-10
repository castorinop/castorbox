GARNAME = mozjs
GARVERSION = 17.0.0
MAJOR = 1
CATEGORIES = net
MASTER_SITES = ftp://ftp.mozilla.org/pub/mozilla.org/js/
DISTNAME=$(GARNAME)$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz libjs.pc
#PATCHFILES = $(DISTNAME)-make.patch $(DISTNAME)-threadsafe.patch $(DISTNAME)-fix_strings.patch $(DISTNAME)-shlib.patch $(DISTNAME)-editline.patch
#LICENSE = MPL

DESCRIPTION = 
define BLURB
endef

DEPENDS = lang/c lib/nspr lib/readline


CONFIGURE_SCRIPTS = $(WORKSRC)/js/src/configure
BUILD_SCRIPTS     = $(WORKSRC)/js/src/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/js/src/Makefile 

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
		 --enable-threadsafe  

include ../../gar.mk

extract-libjs.pc:
	@cp $(DOWNLOADDIR)/libjs.pc $(WORKSRC)
	@sed -i "s|@GAR_prefix@|$(prefix)|g" $(WORKSRC)/libjs.pc
	@sed -i "s|@GAR_libdir@|$(libdir)|g" $(WORKSRC)/libjs.pc
	@sed -i "s|@GAR_includedir@|$(includedir)|g" $(WORKSRC)/libjs.pc
	@sed -i "s|@GARVERSION@|$(GARVERSION)|g" $(WORKSRC)/libjs.pc
	@$(MAKECOOKIE)
	

build-custom:
	$(BUILD_ENV) make -C $(WORKSRC)/src -f Makefile.ref \
	CPU_ARCH="$(GARCH)" \
	JS_THREADSAFE="1" \
	BUILD_OPT="1" \
	JS_READLINE="1" \
	LD=$(LD) \
	CC=$(CC) \
	CFLAGS="$(CFLAGS) -DXP_UNIX" \
	LDFLAGS="$(LDFLAGS)" \
	OBJDIR=$(WORKSRC)_build \
	jscpucfg jsautocfg.h all
	@$(MAKECOOKIE)

install-custom:
	install -d $(DESTDIR)$(bindir)
	install -d $(DESTDIR)$(libdir)
	install -d $(DESTDIR)$(includedir)/js-$(GARVERSION)
	# install headers
	install -m0644 $(WORKSRC)/src/*.h $(DESTDIR)$(includedir)/js-$(GARVERSION)/
	install -m0644 $(WORKSRC)/src/js.msg $(DESTDIR)$(includedir)/js-$(GARVERSION)/
	install -m0644 $(WORKSRC)/src/*.tbl $(DESTDIR)$(includedir)/js-$(GARVERSION)/
	install -m0644 $(WORKSRC)/src/Linux_All_OPT.OBJ/jsautocfg.h $(DESTDIR)$(includedir)/js-$(GARVERSION)/
	# install shared library
	install -m0755 $(WORKSRC)/src/Linux_All_OPT.OBJ/lib$(GARNAME).so \
	    $(DESTDIR)$(libdir)/lib$(GARNAME).so.$(MAJOR)
	ln -snf lib$(GARNAME).so.$(MAJOR) $(DESTDIR)$(libdir)/lib$(GARNAME).so
	# install pkgconfig file
	mkdir -p $(DESTDIR)$(libdir)/pkgconfig/
	install -m0644 $(WORKSRC)/libjs.pc $(DESTDIR)$(libdir)/pkgconfig/



