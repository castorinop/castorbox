GARNAME = SDL_perl
GARVERSION = 1.20.0
CATEGORIES = extras
MASTER_SITES =  http://easynews.dl.sourceforge.net/sourceforge/sdlpl/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = Artistic

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/c xorg/xorg lib/SDL perl/perl

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

BUILD_ARGS = CC="$(CC)" LD="$(LD)" AR="$(AR)" OPTIMIZE="$(CFLAGS)" 

include ../../gar.mk
include ../games.mk

configure-custom:
	sed -i 's@sdl-config@$(DESTDIR)$(bindir)/sdl-config@' $(WORKSRC)/Makefile.linux
	sed -i 's@/usr@$(DESTDIR)$(prefix)@' $(WORKSRC)/Makefile.linux
	sed -i 's@gcc@$(GARHOST)@' $(WORKSRC)/Makefile.linux
	cd $(WORKSRC) && perl Makefile.PL 
	@$(MAKECOOKIE)


