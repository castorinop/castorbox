GARNAME = core

include ../castorbox/package.api.mk

DEPENDS = \
	system/acpid \
 	utils/alsa-utils \
	utils/busybox \
	net/ifplugd \
	net/resolvconf \
	utils/loader \
	utils/ethtool \
	devel/fakeroot \
	kernel/kernel \
	fonts/liberation-fonts \
	system/lirc \
	utils/lm_sensors \
	system/powernowd \
	X11/ratpoison \
	utils/regionset \
	system/splashutils \
	net/syslinux \
	utils/squashfs \
	system/udev \
	system/avahi \
	system/zoneinfo \
	utils/usbutils \
	utils/util-linux \
	X11/vdpau-video \
        X11/vdpauinfo \
	X11/x11vnc \
	X11/xmacro \
	X11/unclutter \
	X11/xvattr \
	xorg/xorg \
	$(if $(filter nvidia,$(mm_GRAPHICS)), \
	                nvidia/nvidia-$(mm_NVIDIA_VERSION)) \
	$(if $(filter virtualbox,$(mm_GRAPHICS)), \
	                utils/virtualbox) \
	utils/mixerosd \
	utils/inotify-tools \
	utils/module-init-tools \
	utils/pmount \
	utils/unzip \
	utils/gzip \
	utils/unzip \
	utils/mp3gain \
	utils/util-linux \
	utils/coreutils \
	utils/findutils \
	utils/rsync \
	net/firefly \
	net/openssh \
	net/lighttpd \
	net/miniupnpc \
	net/dyndns \
	net/syslinux \
	net/xbnbt \
	lang/php \
	lib/nss_mdns \
	$(addprefix extras/,$(filter-out Makefile extras-% extras.%, $(shell cd ../../extras ; ls))) \
	net/transmission \
	net/amule \
	net/wget \
	xbmc/xbmc-stable \
	$(mm_USER_PACKAGES)
BUILDDEPS = \
	utils/coreutils \
	devel/fakeroot \
	utils/file \
	utils/findutils \
	utils/squashfs \
	utils/tar \
	utils/unzip \
	utils/util-linux \
	xorg/xorg


include ../../gar.mk

include ../castorbox/build.api.mk

