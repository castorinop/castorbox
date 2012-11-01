#!/bin/sh
AMULE_DIR=`echo "$DIR" | grep amule/Incoming`
DESTPATH=""
if [ -n "$DIR" -a -n "$AMULE_DIR" -a -n "$FILE" ]; then
	case "$CMD" in
		"MOVED_TO"|"CLOSE_WRITE:CLOSE")
			echo amule.sh FILE = "'$FILE'"
			if [ -n "$FILE" ]; then 
				DESTPATH=`cat /config/helper-download-ed2k | grep "$FILE" | tail -1 | cut -d "@" -f 3`
				if [ -n "$DESTPATH" ]; then
					echo amule.sh mkdir -p "$DESTPATH"
					mkdir -p "$DESTPATH"
					mv "$FILENAME" "$DESTPATH"
					ln -s "$DESTPATH/$FILE" "$FILENAME"
					touch -m "$DESTPATH/"*
					cat /config/helper-download-ed2k | grep "$FILE" >> /config/helper-downloaded-ed2k;
					# remove a week file old
					find /config/amule/Incoming/ -mtime +7 -exec rm "{}" \;
				fi
			fi
			;;
	esac
fi
