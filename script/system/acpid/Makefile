GARNAME = acpid
GARVERSION = 2.0.10
CATEGORIES = system
MASTER_SITES = http://www.tedfelix.com/linux/
DISTFILES = $(DISTNAME).tar.gz
LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/c

BUILD_SCRIPTS   = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

BUILD_ARGS   = \
	OPT="$(CFLAGS)" \
	BINDIR=$(bindir) \
	SBINDIR=$(sbindir) \
	MAN8DIR=$(mandir)/man8 \
	DOCDIR=$(docdir)/acpid
INSTALL_ARGS = \
	BINDIR=$(bindir) \
	SBINDIR=$(sbindir) \
	MAN8DIR=$(mandir)/man8 \
	DOCDIR=$(docdir)/acpid

include ../../gar.mk

LDFLAGS := $(LDFLAGS) -fwhole-program

LDFLAGS := $(CFLAGS) $(LDFLAGS)

post-install:
	@chmod 755 $(DESTDIR)$(sbindir)/acpid
	@$(MAKECOOKIE)
