GARNAME = lcdproc
GARVERSION = 0.5.4
CATEGORIES = system
MASTER_SITES = http://downloads.sourceforge.net/project/$(GARNAME)/$(GARNAME)/$(GARVERSION)/
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = $(DISTNAME)-dm140_henlar_v0.2.patch
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c lib/libftdi lib/libg15render lib/libirman lib/ncurses lib/libusb-compat system/g15daemon system/lirc

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS) --build=$(GARBUILD) --host=$(GARHOST) \
	--enable-libusb \
	--enable-libftdi \
	--disable-libhid \
	--enable-ethlcd \
	--disable-doxygen \
	--disable-dot \
	--disable-html-dox \
	--disable-latex-dox \
	--enable-drivers=all

include ../../gar.mk

cvs//%/$(DISTNAME).tar.bz2:
	@$(call FETCH_CVS, $*, $(GARNAME), $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

pre-configure:
	@$(call RUN_AUTOTOOLS)
	@$(MAKECOOKIE)

clean-all:
	@$(MAKE) clean
	@rm -rf $(DESTDIR)$(bindir)/lcdexec
	@rm -rf $(DESTDIR)$(bindir)/lcdident.pl
	@rm -rf $(DESTDIR)$(bindir)/lcdmetar.pl
	@rm -rf $(DESTDIR)$(bindir)/lcdproc
	@rm -rf $(DESTDIR)$(bindir)/lcdvc
	@rm -rf $(DESTDIR)$(sbindir)/LCDd
	@rm -rf $(DESTDIR)$(libdir)/lcdproc
	@rm -rf $(DESTDIR)$(sysconfdir)/LCDd.conf
