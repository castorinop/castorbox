#!/bin/sh
VIDEO_DIR=`echo "$DIR" | grep Videos`
if [ -n "$DIR" -a -n "$VIDEO_DIR" ]; then

video_mkcovername () {
        var="$1"
        cNAME=${var##*/}
        sNAME=${cNAME%%.*}
        echo "/config/mms/movies/${sNAME}_cover.jpg"
}

case "$CMD" in
	"DELETE")                                                   
        	rm `video_mkcovername "$FILENAME"`                        
                ;;                                                  
        "MOVED_TO")     
		#thumb_FROM_FILENAME=`video_mkcovername "$FROM_FILENAME"`                              
		#thumb_TO_FILENAME=`video_mkcovername "$FILENAME"`
                #if [ -f "$thumb_FROM_FILENAME" ]; then      
		#	echo "thumbs.sh mv $thumb_FROM_FILENAME to $thumb_TO_FILENAME"
        	#	mv "$thumb_FROM_FILENAME" "$thumb_TO_FILENAME"
                #else                               
			echo "thumbs.sh thumb-helper $FILENAME"                  
                	thumb-helper "$FILENAME" & 
                #fi                                                   
                ;;                                                   
        "CLOSE_WRITE:CLOSE")                                         
		echo "thumbs.sh thumb-helper $FILENAME"
        	thumb-helper "$FILENAME" &
                ;;                                                   
esac 
fi
