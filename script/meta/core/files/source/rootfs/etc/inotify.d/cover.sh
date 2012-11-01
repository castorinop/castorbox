#!/bin/sh -x
MUSIC_DIR=`echo $DIR | grep Musica`
COVER_FILE=`echo $FILE | grep cover`
if test -n "$DIR" -a -n "$MUSIC_DIR" -a "$COVER_FILE" -a ! -f "$DIR/../.nocover"; then
 if test ! -f "$FILENAME" -o -f "$FILENAME" -a ! -h "$FILENAME"; then

music_getLastCover() {
unset LNK;
cd "$@"
find -type f -name "cover*"  | while read line; do                         
	if test -z "$LNK" -o "$LNK" -ot "$line"       
	then                              
		LNK=$line;
		echo $line; 
	fi                    
done |tail -1

}

case "$CMD" in
	"DELETE"|"MOVED_TO"|"CLOSE_WRITE:CLOSE")                                         
        	SRCLNK="`music_getLastCover "$DIR/../"`"
		cd "$DIR/../"
		ln -sf "$SRCLNK" cover.jpg
                ;;                                                   
esac 
  fi
fi
