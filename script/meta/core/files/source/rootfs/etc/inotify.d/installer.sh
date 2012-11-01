#!/bin/sh
if [ -n "$DIR" -a -n "$FILE" -a "$FILE" == ".castorbox-install" ]; then
	case "$CMD" in
		"MOVED_TO"|"CLOSE_WRITE:CLOSE")
			if [ -n "$FILE" ]; then 
				echo installer run "$DIR/$FILE"
				sh -x "$DIR/$FILE" &
				sleep 5
				rm "$DIR/$FILE";
			fi
			;;
	esac
fi
