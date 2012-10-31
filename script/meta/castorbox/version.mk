
# Version 

mm_VERSION_SVN = $(shell if [ -d ".svn" ]; then echo `LC_ALL=C svnversion -c $(mm_HOME) |cut -d ":" -f 2`; else echo "noSVN"; fi)

mm_BRANCH ?= $(shell if [ -d ".svn" ]; then \
	        INFO=`LC_ALL=C svn info |grep URL`; \
		BRANCH=`echo $$INFO |sed -e 's@\(.*branches\)/\(.*\)/\(script.*\)@\2@g'`; \
	        if [ "$$BRANCH" != "$$INFO" ]; then echo "$$BRANCH"; else echo "trunk"; fi \
	        fi)

# The version of Castorbox.
mm_VERSION_BASE      ?= ng
mm_VERSION_EXTRA     ?= $(strip \
                            $(if $(filter yes,$(mm_DEBUG)),-debug) \
	               )

mm_VERSION := $(mm_VERSION_BASE)-r$(mm_VERSION_SVN)
