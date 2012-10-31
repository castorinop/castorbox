#!/bin/sh

test -f /usr/share/acpi-support/key-constants || exit 0

. /usr/share/acpi-support/policy-funcs

if [ -z "$*" ] && [ `CheckPolicy` = 0 ]; then
    exit;
fi

pm-powersave $*
