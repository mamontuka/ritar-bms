Stanalone web service for two ritar batteries, working over REST API </br>

in example configuration, RS485 to ethernet gate have IP address 192.168.5.29 and listening port 50500, </br>
wired to battery number 1, by BROWN PAIR (BROWN=B, WHITE-BROWN=A), to LINE IN battery hole (RJ45 7pin=WHITE-BROWN, 8pin=BROWN), </br>
LINE OUT port wired by regular patchcord to battery number 2 LINE IN </br>
RS485 port on battery number 1, wired to Deye 6K-SG03LP1 inverter port RS485/CAN, by regular patchcord </br>
Deye inverter works with Lithium battery protocol number 12 </br>

standalone Ritar-BMS linux server have IP address 192.168.5.3, listening port 50501 (on all addresses)</br>
can be accessed over http://192.168.5.3:50501/ </br>
(192.168.5.3 = YOUR server IP, used just for example) </br>
when you will connect to this web service - you will see short manual and examples, what you can use for <br>
connect batteries to your homeassitant
