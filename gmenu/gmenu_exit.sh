#!/bin/bash

# echo "__exit" > /tmp/myfifo

progpid=$(pgrep -f "python3 ./gmenu.py")
if [[ "$progpid" -gt "0" ]]
then
    kill -USR2 $progpid
fi
