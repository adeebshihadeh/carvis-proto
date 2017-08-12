sshpass -p "raspberry" ssh -o StrictHostKeyChecking=no pi@carvis-proto.local rm -rf /home/pi/carvis-proto

echo "purged directory... transferring new files" &

sshpass -p "raspberry" scp -r ../../carvis-proto/ pi@carvis-proto.local:~

echo "new files transferred" &

sshpass -p "raspberry" ssh -o StrictHostKeyChecking=no pi@carvis-proto.local &

sleep 1.5

python app.py