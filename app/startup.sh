#!/bin/bash

exec /home/adeeb/carvis-proto/app/rotate.sh &

python /home/adeeb/carvis-proto/app/app.py &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/adeeb/.config/chromium/Default/Preferences &
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/adeeb/.config/chromium/Default/Preferences &

chromium-browser http://localhost:5000 &

exit 0
