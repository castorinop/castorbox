#-------------------------------------------------------------------------------
# Values in this file can be overridden by including the desired value in
# '$(HOME)/.castorbox/castorbox.conf.mk'.
#-------------------------------------------------------------------------------
-include $(HOME)/.castorbox/castorbox.conf.mk

# Configuration file (castorbox.conf) version.
mm_CONF_VERSION           ?= 35

mm_INSTALL_METHOD 	  ?= scp
#-------------------------------------------------------------------------------
# Variables that you are likely to be override based on your environment.
#-------------------------------------------------------------------------------
# Indicates whether or not to enable debugging in the image.
# Valid values for mm_DEBUG are 'yes' and 'no'.
mm_DEBUG                  ?= no
# Indicates whether or not to enable debugging in the build system.
# Valid values for mm_DEBUG_BUILD are 'yes' and 'no'.
mm_DEBUG_BUILD            ?= no
# Lists the graphics drivers supported.
# Valid values for mm_GRAPHICS are one or more of 'intel', 'nvidia',
# 'openchrome', 'radeon', 'savage', 'sis', 'virtualbox' and 'vmware'.
mm_GRAPHICS               ?= intel nvidia openchrome radeon radeonhd virtualbox 
#virtualbox
# Lists the software to be supported.
# Valid values for MM_SOFTWARE are zero or more of 'mythbrowser', 'mythgallery',
# 'mythgame', 'mythmusic', 'mythnews', 'mythphone', 'mythstream', 'mythvideo',
# 'mythweather', 'mythzoneminder', 'mplayer', 'mplayer-svn' (experimental and
# may be removed in the future without warning), 'vlc' (experimental and may be
# removed in the future without warning), 'xine', 'perl', 'transcode', 'mame',
# 'wiimote', 'backend' and 'debug'.
mm_SOFTWARE               ?= $(if $(filter $(mm_MYTH_VERSION),0.21),mythbrowser) \
                             mythgallery \
                             mythgame \
                             mythmusic \
                             mythnews \
                             mythphone \
                             mythstream \
                             mythvideo \
                             mythweather \
                             mythzoneminder \
                             mplayer \
                             mplayer-svn \
                             vlc \
                             xine \
                             perl \
                             backend \
                             $(if $(filter $(mm_DEBUG),yes),debug)
# Indicates the microprocessor architecture.
# Valid values for mm_GARCH are 'c3', 'c3-2', 'pentium-mmx' and 'x86-64'.
mm_GARCH                  ?= pentium-mmx
# Castorbox distribution download directory.
# Valid values for mm_INSTALL_LATEST are 'yes' and 'no'.
mm_INSTALL_LATEST         ?= no
# Indicates the directory where the GAR Castorbox build system is installed.
mm_HOME                   ?= $(HOME)/gar-castorbox
# The version of kernel headers to use.
# Valid values are '2.6.27', '2.6.28', '2.6.29' and '2.6.30'.
mm_KERNEL_HEADERS_VERSION ?= 3.0
# The version of kernel to use.
# Valid values are '2.6.27', '2.6.28', '2.6.29' and '2.6.30'.
mm_KERNEL_VERSION         ?= 3.0
# The kernel configuration file to use.
# When set, the kernel configuration file $(HOME)/.castorbox/$(mm_KERNEL_CONFIG) will be used.
# When not set, a built-in kernel configuration file will be used.
mm_KERNEL_CONFIG          ?=
# The version of MMS to use.
# Valid values are '1.1.0', and 'trunk'.
mm_MMS_VERSION		?= castorbox-1.1.x
# The version of the NVIDIA driver.
# Valid values are '71.86.09' (legacy), '96.43.11' (legacy), '169.12' (legacy),
# '173.14.18' (legacy), '180.51', '185.18.08' (beta).
#mm_NVIDIA_VERSION         ?= 275.21
mm_NVIDIA_VERSION         ?= 302.17

# The version of xorg to use.
# Valid values are '7.4' and '7.5'.
mm_XORG_VERSION           ?=7.6
# Lists additional packages to build when castorbox is built.
mm_USER_PACKAGES          ?=
# Lists additional binaries to include in the Castorbox image
# by adding to the lists found in castorbox-bin-list and bins-share-list
mm_USER_BIN_LIST          ?=
# Lists additional configs to include in the Castorbox image
# by adding to the lists found in castorbox-etc-list and extras-etc-list
mm_USER_ETC_LIST          ?=
# Lists additional libraries to include in the Castorbox image
# by adding to the lists found in castorbox-lib-list and extras-lib-list
mm_USER_LIB_LIST          ?=
# Lists additional data to include in the Castorbox image
# by adding to the lists found in castorbox-share-list and extras-share-list
mm_USER_REMOVE_LIST       ?=
# Lists additional files to remove from the Castorbox image
# by adding to the lists found in castorbox-remove-list*.
mm_USER_SHARE_LIST        ?=

#-------------------------------------------------------------------------------
# Variables that you are not likely to override.
#-------------------------------------------------------------------------------
mm_GARCH_FAMILY           ?= $(strip \
                                 $(if $(filter c3         ,$(mm_GARCH)),i386  ) \
                                 $(if $(filter c3-2       ,$(mm_GARCH)),i386  ) \
                                 $(if $(filter pentium-mmx,$(mm_GARCH)),i386  ) \
                                 $(if $(filter x86-64     ,$(mm_GARCH)),x86_64) \
                              )
mm_GARHOST                ?= $(strip \
                                 $(if $(filter c3         ,$(mm_GARCH)),i586  )  \
                                 $(if $(filter c3-2       ,$(mm_GARCH)),i586  )  \
                                 $(if $(filter pentium-mmx,$(mm_GARCH)),i586  )  \
                                 $(if $(filter x86-64     ,$(mm_GARCH)),x86_64)  \
                              )-castorbox-linux-gnu
mm_CFLAGS                 ?= $(strip \
                                 -pipe                                                                                       \
				 $(if $(filter atom        ,$(mm_GARCH)),-march=atom        -mtune=atom    -O2 -mfpmath=sse -ftree-vectorize -mmovbe) \
                                 $(if $(filter c3          ,$(mm_GARCH)),-march=c3-2        -mtune=c3      -Os             ) \
                                 $(if $(filter c3-2        ,$(mm_GARCH)),-march=c3-2        -mtune=c3-2    -Os -mfpmath=sse) \
                                 $(if $(filter pentium-mmx ,$(mm_GARCH)),-march=pentium-mmx -mtune=generic -Os             ) \
                                 $(if $(filter x86-64      ,$(mm_GARCH)),-march=x86-64      -mtune=generic -O3 -mfpmath=sse) \
			-ftree-loop-distribution  \
			-floop-interchange                \
			-floop-strip-mine                        \
			-floop-block                      \
			-fgraphite-identity      \
			-flto \
                                 $(if $(filter i386  ,$(mm_GARCH_FAMILY)),-m32)                                              \
                                 $(if $(filter x86_64,$(mm_GARCH_FAMILY)),-m64)                                              \
                                 $(if $(filter yes,$(mm_DEBUG)),-g)                                                          \
                              )
mm_CXXFLAGS               ?= $(mm_CFLAGS)
mm_DESTDIR                ?= $(mm_HOME)/images/mm

#-------------------------------------------------------------------------------
# Variables that you cannot override.
#-------------------------------------------------------------------------------
# Set the language for gettext to English so the configure scripts for packages
# such as lib/libjpeg do not yield incorrect results.
LANGUAGE=en
export LANGUAGE

# Stop attempts to check out patches from perforce.
PATCH_GET=0
export PATCH_GET

# Set the number of parallel makes to the number of processors.
PARALLELMFLAGS=-j$(shell cat /proc/cpuinfo | grep -c '^processor[[:cntrl:]]*:')
export PARALLELMFLAGS

