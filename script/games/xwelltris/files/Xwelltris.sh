#!/bin/sh
. /mnt/store/games/game_config
xsetroot -solid black &
xwelltris&
sleep 2
joy2key 'xwelltris' -rcfile /mnt/store/common/joy2keyrc -config xwelltris
