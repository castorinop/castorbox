#!/bin/sh

test -f /usr/share/acpi-support/key-constants || exit 0

# Lenovo rock.  They have changed the function of the Fn-F8
# combination on the LenovoPads from stretching the display (in
# hardware/BIOS) to toggling the touchpad on and off.
#
# Unfortunately they didn't bother to change the DMI strings
# consistently...  so some of the new machines say 'LENOVO' and some
# still say 'IBM'.  Yay for consistency(!).

# So:
# IBM && !Series60   => nothing
# IBM && Series60    => Touchpad toggle
# LENOVO && ThinkPad => Touchpad toggle

toggle_touchpad=0

system_manufactuer=`dmidecode -s system-manufacturer`
case "$system_manufactuer" in
    IBM*)
    system_version=`dmidecode -s system-version`
    case "$system_version" in
	ThinkPad\ [TXZ]60*)
	toggle_touchpad=1
	;;
    esac
    ;;
    LENOVO*)
    toggle_touchpad=1
    ;;
esac

if [ "$toggle_touchpad" -ne 0 -a -x /etc/acpi/asus-touchpad.sh ] ; then
    /etc/acpi/asus-touchpad.sh
fi
