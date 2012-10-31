GARNAME = m-feeds-cli
GARVERSION = buggy
#GARVERSION = 05ccba4ee0d46c35ba91567f4aae03ff0dc301e3
CATEGORIES = net
#MASTER_SITES =  http+git://castorinop@trac.castorinop.com.ar:80/trac/mediafeeds/dav/cli/
#MASTER_SITES = http://www.lirc.org/software/snapshots/
#MASTER_SITES = git://lirc.git.sourceforge.net/gitroot/lirc/lirc/
DISTFILES = $(DISTNAME).tar.bz2 m-feeds-cli m-feeds-list
#PATCHFILES = $(DISTNAME)-fix_store_json.patch \
#	     $(DISTNAME)-better_startdownload.patch 

LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = net/amule python/python

#CONFIGURE_SCRIPTS = $(WORKSRC)/configure
#BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom
include ../../gar.mk


PARALLELMFLAGS := -j1

git//%$(DISTNAME).tar.bz2:
	@$(call FETCH_GIT, $*, $(GARVERSION), $(DISTNAME))
	@$(MAKECOOKIE)

x-checksum-$(DISTNAME).tar.bz2:
	@$(MAKECOOKIE)

install-custom:
	@mkdir -p $(DESTDIR)$(datadir)/m-feeds-cli
	@cp -a $(WORKSRC)/{celerity,src,m-feeds-cli.py} $(DESTDIR)$(datadir)/m-feeds-cli
	@find $(DESTDIR)$(datadir)/m-feeds-cli -type d -a -name "\.*" | xargs rm -rf
	find $(DESTDIR)$(datadir)/m-feeds-cli -name "*.pyc" -delete
	@cp $(DOWNLOADDIR)/m-feeds-cli $(DESTDIR)$(bindir)/m-feeds-cli
	@cp $(DOWNLOADDIR)/m-feeds-list $(DESTDIR)$(bindir)/m-feeds-list
	@chmod 755 $(DESTDIR)$(bindir)/m-feeds-cli
	@chmod 755 $(DESTDIR)$(bindir)/m-feeds-list
	$(MAKECOOKIE)

