#!/bin/sh

test -f /usr/share/acpi-support/state-funcs || exit 0

. /etc/default/acpi-support
. /usr/share/acpi-support/power-funcs

getXconsole;
if [ x"$XAUTHORITY" != x"" ]; then
    . /usr/share/acpi-support/key-constants
    acpi_fakekey $KEY_MAIL   # [was: 236]
fi
