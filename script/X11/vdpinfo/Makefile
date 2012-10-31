GARNAME = vdpinfo
GARVERSION = 0.0.5
CATEGORIES = X11
MASTER_SITES = http://www.cs.rug.nl/~wladimir/vdpinfo/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = $(GARNAME)
$(GARNAME)_LICENSE_TEXT = $(WORKSRC)/LICENSE

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c xorg/xorg X11/vdpau

WORKSRC = $(WORKDIR)/$(GARNAME)

BUILD_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = custom

BUILD_ARGS = \
	CXXFLAGS="$(CXXFLAGS)" \
	LDFLAGS="$(LDFLAGS) -lvdpau -lX11"

include ../../gar.mk

install-custom:
	@mkdir -p $(DESTDIR)$(bindir)
	@cp -f $(WORKSRC)/vdpinfo $(DESTDIR)$(bindir)/vdpinfo
	@chmod 0755 $(DESTDIR)$(bindir)/vdpinfo
	@$(MAKECOOKIE)
