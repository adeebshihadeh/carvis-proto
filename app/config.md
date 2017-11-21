# ubuntu config

## enable ssh

`sudo apt-get install openssh-server`

after this, the rest can be done remotely over ssh

## update & upgrade

`sudo apt-get update & sudo apt-get upgrade -y`

## install dependencies

`sudo apt-get install chromium git python-pip`

`pip install flask flask-socketio eventlet requests`

download [sp](https://gist.github.com/wandernauta/6800547)

### spotify

https://www.spotify.com/us/download/linux/

## clone this repo

clone to home dir

`git clone https://github.com/quillford/carvis-proto.git`

## startup scripts

add `rotate.sh` and `carvis-start.sh` to startup

## system settings

### brightness & lock

* disable `dim screen to save power`
* set `turn screen off when inactive for` to `never`
* turn off lock
* disable `require my pasword when waking from suspend`

### power

* set `suspend when inactive for` to `5 minutes` on battery and `don't suspend` when plugged in
* set `when power is critically low` to `power off`
* set `when the lid is closed` to `do nothing`

## optimizing boot time

rcconf
