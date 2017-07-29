#!/bin/bash

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences
 

python /home/pi/carvis-proto/app/app.py &

chromium-browser http://localhost:5000 &

# rotate screen & touch input

exec ./rotate.sh

# launch chromium kiosk mode. direct to localhost:5000
# no screensaver/sleep
