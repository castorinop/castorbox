#!/bin/sh

# This script is part of the KEY TRANSLATION part of acpi-support. Compare with
# sleep.sh, which is part of the SUSPEND part of acpi-support. This script is
# intended to translate a key event which is not seen as a suspend key press by
# the rest of the system.


test -f /usr/share/acpi-support/key-constants || exit 0

. /usr/share/acpi-support/key-constants
acpi_fakekey $KEY_SLEEP
