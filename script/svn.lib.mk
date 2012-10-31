
SVN_DBG = 
SVN_IGNORE_TAGS = cookies download tmp\* work
$REPLACE_RULES =

#File list
SVN_LIST_FILES = $(patsubst %x86% %_64% %x86% %i586% %i386% ,*, \
	$(addprefix $(FILEDIR)/,$(ALLFILES)) \
	$(wildcard $(FILEDIR)/$(DISTNAME)* $(FILEDIR)/*$(GARVERSION)* $(FILEDIR)/config.cache.* *.mk) \
)

# Remove temporal, rejected, and original files.
SVN_TEST_FILES  = $(foreach TTT,$(filter-out %~ %orig ~rej,$(SVN_LIST_FILES)),$(TTT))


ifeq ("$(CATEGORY)","meta")
SVN_TEST_FILES += $(wildcard $(FILEDIR)/*mk $(FILEDIR)/Makefile  $(FILEDIR)/source)
endif
#SVN_TEST_FILES := $(foreach TTT,%x86% %_64% %x86% %i586% %i386%,$(subst $(TTT),*,$(GARDIR)/xyzzy/$(COOKIEROOTDIR)/svn))

SVN_FILES = $(shell for i in $(SVN_TEST_FILES); do if [ -f "$$i" -o -d "$$i" ]; then echo "$$i"; fi; done)
ifneq ("$(SVN_FILES)","")
SVN_DIRS += $(FILEDIR)
endif

SVN_FILES_DEL = $(filter-out $(SVN_FILES) files/gar-base.diff, $(wildcard $(FILEDIR)/*) )

SVN_ALL = $(SVN_DIRS) Makefile checksums $(SVN_FILES)

SVN_TARGETS = svn-add-package svn-add-prop $(addprefix svn-add-/,$(subst %x86% %_64% %x86$ %i586% %i386% ,\*, $(SVN_ALL))) $(addprefix svn-del-/,$(SVN_FILES_DEL))
#SVN_TARGETS = svn-add-package svn-add-prop $(addprefix svn-add-/,$(SVN_ALL)) $(addprefix svn-del-/,$(SVN_FILES_DEL))  

SVNDEP_TARGETS = $(foreach TTT,$(filter-out $($*_NODEPEND),$($*_DEPENDS)),$(subst xyzzy,$(TTT),$(GARDIR)/xyzzy/$(COOKIEROOTDIR)/svn-pkg))
SVN_IMGDEPS = $(addprefix svndep-,$(IMGDEPS))

svn-pkg: $(SVN_IMGDEPS) pre-svn $(SVN_TARGETS) post-svn
	@$(MAKECOOKIE)

svn-add-package:
	@if [ -z "`svn status -v |grep '\.$$'`" ]; then $(SVN_DBG) svn add -N  $(shell /bin/pwd); fi
	@#$(MAKECOOKIE)

svn-add-prop:
	@SVN_EDITOR="echo '`for i in $(SVN_IGNORE_TAGS); do echo "$$i"; done `' > " $(SVN_DBG) svn propedit svn:ignore . > /dev/null
	@#$(MAKECOOKIE)

svn-add-/%:
	@if [ -a  "$*" ] && [ -z "`svn status -v |grep $*$$|grep -v '^?'`" ]; then \
		echo adding $*; $(SVN_DBG) svn add -N $*; \
	fi
	@#$(MAKECOOKIE)

svn-del-/%:
	@#echo check deleting $*;
	@if [ -n "`svn status -v |grep $*$$|grep -v '^?'|grep  '^ '`" ]; then \
		echo deleting $*; \
		$(SVN_DBG) svn del $*; \
	fi
	@if [ -n "`svn status -v |grep $*$$|grep -v '^?'|grep  '^A'`" ]; then \
		echo reverting $*; \
		$(SVN_DBG) svn revert $*; \
	fi
	@#$(MAKECOOKIE)

svn-deps:
	@echo package depends $(SVN_DEPS)

svn-resume:
	@echo files to test:; for i in $(SVN_TEST_FILES); do echo $$i; done
	@echo files to add:;  for i in $(SVN_FILES); do echo $$i; done
	@echo files to del:;  for i in $(SVN_FILES_DEL); do echo $$i; done

svn-dep-/%:
	@make -C  $(GARDIR)/$* svn-pkg

svn-commit-update:
	@svn ci . -m "update $(GARNAME) $(GARVERSION)"

svn-targets: 
	@echo targets:$(SVN_TARGETS)

svndep-%:
	@$(if $(SVNDEP_TARGETS),$(MAKE) DESTIMG="$*" $(SVNDEP_TARGETS),true)
	@$(MAKECOOKIE)

$(GARDIR)/%/$(COOKIEROOTDIR)/svn-pkg:
	@echo ' ==> Versioning $* as a dependency'
	@$(MAKE) -C $(GARDIR)/$* svn-pkg

.PHONY: svn svn-deps svn-commit-update
