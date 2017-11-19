#!/bin/bash

python ~/carvis-proto/app/app.py &

spotify & 

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/Default/Preferences &
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences &

chromium-browser ~/carvis-proto/app/loading.html

exit 0
