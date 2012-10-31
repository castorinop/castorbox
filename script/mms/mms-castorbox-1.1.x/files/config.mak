PREFIX = /usr/
CONFIG = /etc/mms-1.1.0
CONFIGDIR = /etc/mms-1.1.0/
BINDIR = /usr/bin
DATADIR = /usr/share/mms
LIBDIR = /usr/lib
PLUGINDIR = $(LIBDIR)/mms/plugins
INSTALL = install
DESTDIR = ""

# po/Makefiles
LANGUAGES = da de cs pt sv fr ru es fi pl it lv

# commoncpp2
COMMONCPP2_LOCAL = no
COMMONCPP2_CFLAGS = -D_GNU_SOURCE  
COMMONCPP2_LIBS = -pthread -lccext2 -lz -lccgnu2 -ldl -lrt -lpcrecpp 

# debug
DEBUG = no
GCC_VER_MAJOR = 4
GCC_VER_MINOR = 3

# music support
MUSIC = yes
RADIO = yes
APLAYER_ALSA = yes
APLAYER_XINE = no
APLAYER_GST = yes

# audio
AUDIO= yes

# graphical audio
FAUDIO= yes

# imms support
IMMS = no  

# movie support
MOVIE = yes

# picture support
PICTURE = yes

# graphical movie
FMOVIE = yes

# use ffmpeg or mplayer for movie thumbnailing
FFMPEG_THUMBNAILER = no

#sqlite
SQLITE = yes

# game support
GAME = no

# graphical game
FGAME = no

# epg support
EPG = no
EPG_PIC = no

# clock support
CLOCK = yes

# notify-area support
NOTIFYAREA = yes

# weather support
WEATHER = no

# vbox support
VBOX = no

# Media RSS support
MEDIA_RSS = yes

# tv support
TV = yes

# resolution support
RESOLUTION = no

# lirc
LIRC = yes

# evdev
EVDEV = yes

# mouse
MOUSE = no

# vo
VO_DXR3 = no
VO_SDL = yes
VO_OPENGL = yes
VO_DVB = no
VO_LCD = no
VO_MPEG = no


X11 = yes
DPMS = yes

MPEG = no
FFMPEG_EXTERNAL = yes

# Python
PYTHON = no
PYTHON_VERSION = 2.5
PYTHON_INSTALL = /usr/lib/python2.5/site-packages/

# Inotify
INOTIFY = yes

# benchmark
BENCH = no

# boost
EXTERNAL_BOOST = yes
BOOST_INCLUDE=-isystem/usr/include/

BUILD_DIR = /home/pablo/build/mms/bzr-1.1.0-work

#optimize
OPTIMIZE = no
SIZE_OPTIMIZE = no

