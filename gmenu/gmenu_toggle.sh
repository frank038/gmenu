#!/bin/bash

# if ! pgrep -f gmenu.py > /dev/null
# then
#     exec /FULL/PATH/gmenu/gmenu.sh &
# fi
#
# echo "__toggle" > /tmp/myfifo

progpid=$(pgrep -f "python3 ./gmenu.py")

if [[ "$progpid" -gt "0" ]]
then
    kill -USR1 $progpid
else
    exec /FULL/PATH/gmenu/gmenu.sh &
    sleep 1
    kill -USR1 $(pgrep -f "python3 ./gmenu.py")
fi
