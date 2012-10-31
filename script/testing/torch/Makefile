GARNAME = Torch
GARVERSION = 3
CATEGORIES = lib
MASTER_SITES = http://www.torch.ch/archives/
DISTFILES = $(GARNAME)$(GARVERSION)src.tgz Makefile_options_Linux
PATCHFILES = $(DISTNAME)-fix_compile.patch
#LICENSE = GPL2

DESCRIPTION =
define BLURB
endef

DEPENDS = lang/cxx 

BUILD_SCRIPTS     = $(WORKSRC)/Makefile
INSTALL_SCRIPTS   = custom

BUILD_ARGS = AR="$(AR) $(ARFLAGS)" PACKAGES="distributions gradients"

include ../../gar.mk

extract-Makefile_options_Linux:
	@cp $(DOWNLOADDIR)/Makefile_options_Linux $(WORKDIR)/Torch3
	@$(MAKECOOKIE)

post-extract:
	ln -sf Torch3 $(WORKDIR)/$(DISTNAME)
	@$(MAKECOOKIE)

install-custom:
	@mkdir -p $(DESTDIR)$(includedir)/torch
	@install $(WORKSRC)/*/*.h $(DESTDIR)/$(includedir)/torch
	@install -m 644 -D $(WORKSRC)/lib/*/libtorch.a $(DESTDIR)$(libdir)/libtorch.a
	@$(MAKECOOKIE)
