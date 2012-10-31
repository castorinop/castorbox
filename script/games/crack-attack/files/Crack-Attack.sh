#!/bin/sh
. /mnt/store/games/game_config
xsetroot -solid black &
xli -geometry 800x600 /mnt/store/games/black.jpg &
crack-attack -1  --name "CastorBOX" --res 600 &
sleep 2
joy2key 'Crack Attack!' -rcfile /mnt/store/common/joy2keyrc -config crackattack
killall xli

