#!/bin/bash

sudo /usr/bin/python3 -m http.server 50501 -d /ritar-bms/web_ui 2> /dev/null &

while true; do
/usr/bin/python3 /ritar-bms/ritar-bms.py
sleep 6
done

#exit 0;