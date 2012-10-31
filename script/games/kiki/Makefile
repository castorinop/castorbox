GARNAME = kiki
GARVERSION = 1.0.2
CATEGORIES = games
MASTER_SITES = http://download.sourceforge.net/$(GARNAME)/
MASTER_SITES += http://downloads.sourceforge.net/sourceforge/$(GARNAME)/
MASTER_SITES += http://kiki.cvs.sourceforge.net/*checkout*/kiki/kiki/sounds/
DISTFILES = $(DISTNAME)-src.tgz title_song.mp3 $(GARNAME)-story.txt.bz2
PATCHFILES = $(DISTNAME)-python-dynling-fix.patch
PATCHFILES += $(DISTNAME)-gcc4-fix.patch
PATCHFILES += $(DISTNAME)-define-path.patch
PATCHFILES += $(DISTNAME).patch.gar

LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

DEPENDS   = lang/cxx lang/python lib/SDL games/SDL_image games/SDL_mixer 

WORKSRC = $(WORKDIR)/$(GARNAME)

BUILD_ARGS = \
	pyincludedir="$(games_includedir)" \
	pylibdir="$(games_libdir)" \
	KIKI_HOME="$(games_datadir)/$(GARNAME)" \
	OPTFLAGS=" -L$(DESTDIR)$(games_libdir) $(CFLAGS)" \
	PYTHON_VERSION=2.4 \
	PYTHONHOME="$(DESTDIR)$(libdir)/python2.4/" \
	GLLIBS="-lglut -lGLU -lGL"

BUILD_SCRIPTS     = custom
INSTALL_SCRIPTS   = custom
include ../../gar.mk
include ../games.mk

extract-$(GARNAME)-story.txt.bz2:
	@echo " ==> Extracting $(DOWNLOADDIR)/$(GARNAME)-story.txt.bz2"
	@bzip2 -dc $(DOWNLOADDIR)/$(GARNAME)-story.txt.bz2 > $(EXTRACTDIR)/story.txt
	@$(MAKECOOKIE)

pre-build: 
	ln -sf $(DESTDIR)/games $(WORKDIR)
	rm -rf `find -type d -name CVS`
	cp -f $(WORKDIR)/story.txt $(WORKSRC)
	@$(MAKECOOKIE)

build-custom: build-$(WORKSRC)/kodilib/linux/Makefile build-$(WORKSRC)/linux/Makefile

install-custom:
	install -m755 $(WORKSRC)/linux/$(GARNAME) -D $(DESTDIR)$(games_bindir)/$(GARNAME)
	cd $(WORKSRC) && install -d $(DESTDIR)$(games_datadir)/$(GARNAME)
	cd $(WORKSRC) && cp -r sound py $(DESTDIR)$(games_datadir)/$(GARNAME)
	@install -m644 $(WORKDIR)/title_song.mp3 -D $(DESTDIR)$(games_datadir)/$(GARNAME)/sound/title_song.mp3
	@$(MAKECOOKIE)
