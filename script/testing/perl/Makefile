GARNAME = perl
GARVERSION = 5.8.8
CATEGORIES = utils
MASTER_SITES = http://ftp.funet.fi/pub/CPAN/src/5.0/
MASTER_SITES += ftp://ftp.cpan.org/pub/CPAN/src/5.0/
DISTFILES = $(DISTNAME).tar.gz 
LICENSE = artistic
artistic_LICENSE_TEXT = $(WORKSRC)/Artistic

define BLURB
endef

DEPENDS = lang/c 
BUILDDEPS = testing/perl

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = custom 
#$(WORKSRC)/Makefile

NODIRPATHS = --exec_prefix --bindir --sbindir --libexecdir --datadir --infodir --sysconfdir --sharedstatedir --localstatedir --libdir --includedir --mandir --oldincludedir

CONFIGURE_ARGS = $(DIRPATHS) -Dman1dir=" " \
    -Dcf_by='GARGARGAR!' -Dmyhostname=localhost -Dperladmin=gar@localhost \
    -Uinstallusrbinperl -Ui_db
#BUILD_ARGS = 
INSTALL_ARGS = install.perl STRIPFLAGS=-p

ARCHLIB = $(shell perl -ne 'print $$1 if /^archlib=(.*)/' $(WORKSRC)/config.sh)
PERLLIB = $(shell perl -ne 'print $$1 if /^privlib=(.*)/' $(WORKSRC)/config.sh)
PERL = LD_LIBRARY_PATH=$(ARCHLIB)/CORE PERL5LIB=$(PERLLIB) $(WORKSRC)/perl

include ../../gar.mk

$(DESTIMG)_NODEPEND += testing/perl
export $(DESTIMG)_NODEPEND

pre-configure:
	@cp -pf $(WORKSRC)/configure.gnu $(WORKSRC)/configure
	chmod 755 $(WORKSRC)/configure
	# throw away big bulky useless modules
	find \
	    $(WORKSRC)/ext/Encode/[A-Z][A-Z] \
	    $(WORKSRC)/ext/Unicode \
	    -print |perl -nl -e unlink
	perl -pi -e ' \
	    s|^ext/Encode/[A-Z][A-Z]/.*||; \
	    s|^ext/Unicode/.*||; ' $(WORKSRC)/MANIFEST
	$(MAKECOOKIE)

# display some handy variables
post-configure:
	perl -pi -e ' \
	    s|^ext/Encode/[A-Z][A-Z]/.*||; \
	    s|^ext/Unicode/.*||; ' $(WORKSRC)/MANIFEST
	$(WORKSRC)/myconfig
	$(MAKECOOKIE)

# throw away any tests broken due to eliminated module above
test: build
	$(PERL) -pi -e ' \
	    s|^ext/Encode/t/Aliases.*||;\
	    s|^ext/Encode/t/at-.*||;	\
	    s|^ext/Encode/t/CJKT.*||;	\
	    s|^ext/Encode/t/guess.*||;	\
	    s|^ext/Encode/t/jperl.*||;	\
	    s|^ext/Encode/t/perlio.*||;	\
	    ' $(WORKSRC)/MANIFEST
	cd $(WORKSRC) ; $(MAKE) test
	$(MAKECOOKIE)

# disabled cause it wastes precious build time
#pre-install: test
#	$(MAKECOOKIE)

install-custom: 
	$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR)  -C $(WORKSRC) install.perl
	$(MAKECOOKIE)

post-install:
	test "$(DESTDIR)" = "/" || $(PERL) -pi -e 's|$(DESTDIR)||g' $(DESTDIR)$(ARCHLIB)/Config.pm $(DESTDIR)$(ARCHLIB)/.packlist
	$(MAKECOOKIE)
