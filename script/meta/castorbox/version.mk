
# Version 

#yymm_VERSION_VCS = $(shell if [ -d ".git" ]; then echo `LC_ALL=C gitversion -c $(mm_HOME) |cut -d ":" -f 2`; else echo "noVCS"; fi)

mm_VERSION_GIT = $(shell if [ -d "$(mm_HOME)/.git" ]; then echo `LC_ALL=C git rev-parse --short HEAD `; else echo "noVCS"; fi)

mm_VERSION_BRANCH ?= $(shell if [ -d "$(mm_HOME)/.git" ]; then \
	     	git branch  |grep \* |cut -d " " -f 2; \
	        fi)

mm_VERSION_VCS = $(mm_VERSION_BRANCH)-$(mm_VERSION_GIT)

# The version of Castorbox.
mm_VERSION_BASE      ?= ng
mm_VERSION_EXTRA     ?= $(strip \
                            $(if $(filter yes,$(mm_DEBUG)),-debug) \
	               )

mm_VERSION := $(mm_VERSION_BASE)-$(mm_VERSION_VCS)
