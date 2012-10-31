GARNAME = cvt
GARVERSION =
CATEGORIES = X11
MASTER_SITES =
DISTFILES = cvt.c
LICENSE = BSD

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c 

BUILD_SCRIPTS   = custom
INSTALL_SCRIPTS = custom

include ../../gar.mk

extract-$(GARNAME).c:
	@mkdir -p $(WORKSRC)
	@cp $(DOWNLOADDIR)/$(GARNAME).c $(WORKSRC)/
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) ; $(CC) $(CFLAGS) $(GARNAME).c -o $(GARNAME) -lm -Wall
	@$(MAKECOOKIE)

install-custom:
	@mkdir -p $(DESTDIR)$(bindir)
	@cp -f $(WORKSRC)/$(GARNAME) $(DESTDIR)$(bindir)/$(GARNAME)
	@$(MAKECOOKIE)
