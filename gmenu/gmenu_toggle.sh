#!/bin/bash

if ! pgrep -f gmenu.py > /dev/null
then
    exec /FULL/PATH/gmenu/gmenu.sh &
fi

echo "__toggle" > /tmp/myfifo
