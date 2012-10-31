#!/bin/sh
. /mnt/store/games/game_config
export NEVERBALL_DATA=/games/share/neverball
neverball
sh -c "unclutter -idle 0.1 -root&" &
