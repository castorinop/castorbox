GARNAME = brutalchess
GARVERSION = 0.5.2
CATEGORIES = games
MASTER_SITES =  http://easynews.dl.sourceforge.net/sourceforge/$(GARNAME)/
DISTFILES = $(GARNAME)-alpha-$(GARVERSION)-src.tar.gz 
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c 

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--x-includes="$(DESTDIR)$(incdludedir)" \
	--x-libraries="$(DESTDIR)$(libdir)" \
	--with-sdl-prefix=$(DESTDIR) \
	--with-sdl-exec-prefix=$(DESTDIR)/usr \
	--with-gnu-ld \
	LIBS="-L$(DESTDIR)/$(games_libdir) $(LDFLAGS)" \

include ../../gar.mk
include ../games.mk

