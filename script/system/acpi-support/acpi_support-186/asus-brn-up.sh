#!/bin/sh
test -f /usr/share/acpi-support/key-constants || exit 0

. /usr/share/acpi-support/key-constants

DeviceConfig

if [ "$model" != "701" ] ; then
	# On an Eee PC (ASUSTeK model 701) the keys in the range handled by this
	# script have entirely different meanings. They are handled in separate
	# scripts.
	acpi_fakekey $KEY_BRIGHTNESSUP
fi
