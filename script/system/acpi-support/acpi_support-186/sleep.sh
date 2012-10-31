#!/bin/bash
# TODO:  Change above to /bin/sh

# This script HANDLES the sleep button (does not TRANSLATE it). It is part
# of the *suspend* side of acpi-support, not the special keys translation
# side. If this script is called, it is assumed to be the result of a suspend
# key press that can also be heard by other parts of the system. The only time
# that it actually does something is when it is determined that no other parts
# of the system are listening (this is what the CheckPolicy call does).

test -f /usr/share/acpi-support/key-constants || exit 0

. /etc/default/acpi-support
. /usr/share/acpi-support/power-funcs
. /usr/share/acpi-support/device-funcs
. /usr/share/acpi-support/policy-funcs

DeviceConfig;

if [ x$ACPI_SLEEP != xtrue ] && [ x$1 != xforce ]; then
  exit;
fi

# If gnome-power-manager or klaptopdaemon are running, let them handle policy
if [ x$1 != xforce ] && [ x$1 != xsleep ] && [ `CheckPolicy` = 0 ]; then
    exit;
fi

if [ x$LOCK_SCREEN = xtrue ]; then
    if pidof xscreensaver > /dev/null; then
	for x in /tmp/.X11-unix/*; do
	    displaynum=`echo $x | sed s#/tmp/.X11-unix/X##`
	    getXuser;
	    if [ x"$XAUTHORITY" != x"" ]; then
		export DISPLAY=":$displaynum"
		. /usr/share/acpi-support/screenblank
	    fi
	done
    fi
fi

pm-suspend
