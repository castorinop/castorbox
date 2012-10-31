#ifndef MMS_CONFIG_H
#define MMS_CONFIG_H  1

/* this recaps any configure option supplied by usr */
#define MMS_CONFIG_OPTIONS "--prefix=/home/pablo/bin/mms-1.1.0 --config=/home/pablo/bin/mms-1.1.0/etc/mms --disable-alsaplayer --disable-epg --enable-gst-audio --enable-opengl --enable-notify-area --enable-clock --enable-media-rss --enable-ffmpeg-thumb --enable-python --enable-game --enable-evdev --enable-debug"

/* prefix (where to find configuration, and theme files */
#define mms_prefix "/usr/"
#define mms_config "/etc/mms-1.1.0/"

/* gcc version */
#define gcc_ver_major_3 1


/* Music support */
#define c_music 1
#define music_radio 1

/* fancy audio support */
#define use_graphical_audio 1

/* Movie support */
#define c_movie 1

/* fancy movie support */
#define use_graphical_movie 1

/* ffmpeg thumbnailer */
#define use_ffmpeg_thumbnailer 1

/* FFMPEG include split */
#define ffmpeg_include_split 1

/* Picture support */
#define c_picture 1

/* Game support */
//#define c_game 0


/* IMMS support */
//#define use_imms 0

/* graphical game support */
#define use_graphical_game 1

/* EPG support */



/* Notification Area support */
#define use_notify_area 1

/* WEATHER support */


/* VBOX support */


/* Media RSS support */
#define use_media_rss 1

/* Tv */


/* Resolution */


/* lirc */
#define use_lirc 1

/* evdev */

/* mouse */

#define use_x11 1

/* Output */

#define use_sdl 1
#define use_opengl 1



#define ffmpeg_type_external 1

/* DPMS */
#define use_dpms 1

/* sqlite */
#define use_sqlite 1

/* Python support */
//#define use_python 0

/* libfs++ */


/* inotify support */
#define use_inotify 1

/* gettext */
#define use_nls 1
#define use_iconv 1

/* benchmark */


/* debug */

#endif
