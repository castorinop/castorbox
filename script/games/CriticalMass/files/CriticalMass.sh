#!/bin/sh
. /mnt/store/games/game_config
killall unclutter&
critter &
sleep 2
joy2key 'Critical Mass' -rcfile /mnt/store/common/joy2keyrc -config criticalmass

sh -c "unclutter -idle 0.1 -root&" &
