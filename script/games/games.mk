# Include AFTER gar.lib.mk

include ../../games/games.conf.mk

versiondir := $(games_versiondir)
licensedir := $(games_licensedir)

CPPFLAGS := -I$(DESTDIR)$(games_includedir) $(CPPFLAGS)
CFLAGS   := -I$(DESTDIR)$(games_includedir) $(CFLAGS)
CFLAGS   := -L$(DESTDIR)$(games_libdir)     $(CFLAGS)
LDFLAGS  := -L$(DESTDIR)$(games_libdir)     $(LDFLAGS)

# Change TMP_DIRPATHS so that DIRPATHS will use games directories.
TMP_DIRPATHS := \
	--prefix=$(games_prefix) \
	--exec_prefix=$(games_exec_prefix) \
	--bindir=$(games_bindir) \
	--sbindir=$(games_sbindir) \
	--libexecdir=$(games_libexecdir) \
	--datadir=$(games_datadir) \
	--sysconfdir=$(games_sysconfdir) \
	--sharedstatedir=$(games_sharedstatedir) \
	--localstatedir=$(games_localstatedir) \
	--libdir=$(games_libdir) \
	--infodir=$(games_infodir) \
	--includedir=$(games_includedir) \
	--oldincludedir=$(games_oldincludedir) \
	--mandir=$(games_mandir)

# Change STAGE_EXPORTS so that it does not include directories.
STAGE_EXPROTS :=
STAGE_EXPORTS += CC CXX LD CPP AR AS NM RANLIB STRIP OBJCOPY OBJDUMP

DESTDIR:=$(games_DESTDIR)

INSTALL_SCRIPTS := install-gamesdirs $(INSTALL_SCRIPTS)

install-gamesdirs:
	echo installing gamedir
	read algo
	mkdir -p $(games_rootdir)
	@mkdir -p $(games_prefix)
	@mkdir -p $(games_launcher)
	@mkdir -p $(games_exec_prefix)
	@mkdir -p $(games_ebindir)
	@mkdir -p $(games_esbindir)
	@mkdir -p $(games_elibdir)
	@mkdir -p $(games_sysconfdir)
	@mkdir -p $(games_localstatedir)
	@mkdir -p $(games_bindir)
	@mkdir -p $(games_sbindir)
	@mkdir -p $(games_libexecdir)
	@mkdir -p $(games_datadir)
	@mkdir -p $(games_sharedstatedir)
	@mkdir -p $(games_libdir)
	@mkdir -p $(games_infodir)
	@mkdir -p $(games_lispdir)
	@mkdir -p $(games_includedir)
	@mkdir -p $(games_oldincludedir)
	@mkdir -p $(games_mandir)
	@mkdir -p $(games_docdir)
	@mkdir -p $(games_sourcedir)
	@mkdir -p $(games_versiondir)
	@mkdir -p $(games_licensedir)
	@$(MAKECOOKIE)
