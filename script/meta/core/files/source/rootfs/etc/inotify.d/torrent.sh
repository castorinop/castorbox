#!/bin/sh
if [ "$EXT" == "torrent" ]; then
	case "$CMD" in
		"DELETE")
                	HASH=`transmission-cli -i "$FILENAME" |grep hash | cut -d ":" -f 2`
                	if [ -n "$HASH" ]; then
                        	transmission-remote -r $HASH
                        fi
			;;
		"CLOSE_WRITE:CLOSE")
			        transmission-remote -f "$DIR"
				transmission-remote -a "$FILENAME"
			;;
	esac
fi
