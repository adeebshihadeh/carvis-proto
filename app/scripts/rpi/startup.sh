#!/bin/bash

xinput --set-prop 'ILITEK ILITEK Multi-Touch' 'Coordinate Transformation Matrix'  0 1 0 -1 0 1 0 0 1

python /home/pi/carvis-proto/app/app.py &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences &
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences &

chromium-browser --noerrdialogs http://localhost:8080 &
#chromium-browser --noerrdialogs --kiosk http://localhost:8080 &

exit 0