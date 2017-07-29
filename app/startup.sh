#!/bin/bash

exec ./rotate.sh

python /home/pi/carvis-proto/app/app.py &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences

chromium-browser http://localhost:5000 &
