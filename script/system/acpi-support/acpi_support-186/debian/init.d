#!/bin/bash
# INIT script to check whether we're on batteries, and so start with laptop 
# mode etc enabled.

# BUGS: unless we start *really* late, we have no way of throttling 
# xscreensaver, since it won't be there to command.
. /usr/share/acpi-support/power-funcs

test -f /lib/lsb/init-functions || exit 1
. /lib/lsb/init-functions

test -d /var/lib/acpi-support || exit 0

shopt -s nullglob

case "$1" in
  start)
    log_begin_msg "Checking battery state..."
    /etc/acpi/power.sh
    log_end_msg 0
    ;;
  stop)
    log_begin_msg "Disabling power management..."
    /etc/acpi/power.sh false
    log_end_msg 0
    ;;
  *)
  ;;
esac
        

