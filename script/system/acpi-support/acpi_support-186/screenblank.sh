#!/bin/sh

test -f /usr/share/acpi-support/key-constants || exit 0

. /etc/default/acpi-support
. /usr/share/acpi-support/power-funcs

for x in /tmp/.X11-unix/*; do
    displaynum=`echo $x | sed s#/tmp/.X11-unix/X##`
    getXuser;
    if [ x"$XAUTHORITY" != x"" ]; then
        export DISPLAY=":$displaynum"
	. /usr/share/acpi-support/screenblank
    fi
done
