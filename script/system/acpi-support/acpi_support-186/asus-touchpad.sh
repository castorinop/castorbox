#!/bin/sh
[ -f /usr/share/acpi-support/state-funcs ] || exit 0 

. /usr/share/acpi-support/power-funcs

# if this is the right behavior, then this should be moved out of acpi-support
# to hal (or whatever is replacing hal for such events)
getXconsole

XINPUTNUM=`xinput list | grep 'SynPS/2 Synaptics TouchPad' | sed -n -e's/.*id=\([0-9]\+\).*/\1/p'`

# get the current state of the touchpad
TPSTATUS=`xinput list-props $XINPUTNUM | awk '/Synaptics Off/ { print $NF }'`

# if getting the status failed, exit
test -z $TPSTATUS && exit 1

if [ $TPSTATUS = 0 ]; then
   xinput set-int-prop $XINPUTNUM "Synaptics Off" 8 1
else
   xinput set-int-prop $XINPUTNUM "Synaptics Off" 8 0
fi
