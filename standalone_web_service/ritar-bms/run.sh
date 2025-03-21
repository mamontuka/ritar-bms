#!/bin/bash
## by Oleh Mamont (C) 2025
## free for use and modification
##
## thats lifehack needed because I know issue - if we do "cold" batteries and inverter
## restart - we will get wrong entities values to homeassistant from second battery,
## because cold restarting mean turn off inverter, turn off second battery, turn off
## first battery. do maintenance. and turn on all in upsidedown direction.
## in this moment first battery will be accessible (because must be started first),
## and second - not, so we will get wrong walues to homeassistant over API and broke
## entities for battery number 2
##
##
## inverter IP address
inverter_ip="192.168.5.2"

## start ritar-bms web service
sudo /usr/bin/python3 -m http.server 50501 -d /ritar-bms/web_ui 2> /dev/null &

while true; do
##
## if inverter online - all ok, we reading batteries and push states into API
##
if ping -c 1 "$inverter_ip" >/dev/null 2>&1; then
/usr/bin/python3 /ritar-bms/ritar-bms.py
sleep 6
## in case if inverter NOT online - we STOP reading batteries and push states into API on 60 seconds
else
sleep 60
fi
done

#exit 0;
