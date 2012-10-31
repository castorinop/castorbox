#!/bin/bash
# TODO:  Above should be /bin/sh

test -f /usr/share/acpi-support/state-funcs || exit 0

. /etc/default/acpi-support

if [ x$ACPI_HIBERNATE != xtrue ] && [ x$1 != xforce ]; then
  exit;
fi

pm-hibernate
