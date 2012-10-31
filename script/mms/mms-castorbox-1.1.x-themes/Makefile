GARNAME = mms-themes
GARVERSION = 1.1.0-themes
CATEGORIES = mms

#Dark Mix 2
MASTER_SITES = http://mailwurm.org/mms/themes/
DISTFILES = darkmix-2.tgz 
PATCHFILES = darkmix2-theme.patch fix-theme.patch

# Ocean 0.2.1
#MASTER_SITES += http://mms.mymediasystem.net/theme-ocean/
#DISTFILES += ocean-0.2.1.tgz
LICENSE = GPL2

DESCRIPTION = 
define BLURB
endef

WORKSRC = $(WORKDIR)
DEPENDS = mms/mms-castorbox-1.1.x

INSTALL_SCRIPTS = custom

include ../../gar.mk

install-custom:
	@cp -a $(WORKDIR)/* $(DESTDIR)$(datadir)/mms/themes
	@ln -sf ../standard/media_rss/ $(DESTDIR)$(datadir)/mms/themes/darkmix-2/
	@ln -sf ../../standard/weather/weather_com/ $(DESTDIR)$(datadir)/mms/themes/darkmix-2/weather/
	@$(MAKECOOKIE)
