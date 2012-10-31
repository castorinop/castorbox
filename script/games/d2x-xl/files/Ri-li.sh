#!/bin/sh
. /mnt/store/games/game_config
killall unclutter&
Ri_li &
sleep 2
joy2key 'Ri-li V2.0.0' -rcfile /mnt/store/common/joy2keyrc -config rili

sh -c "unclutter -idle 0.1 -root&" &
