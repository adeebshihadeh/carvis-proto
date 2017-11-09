import requests
import json
import os
import core
import eventlet

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app)

core = core.core

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')

@socketio.on('cmd')
def handle_msg(msg):
  print "new msg: " + msg
  core.handle_msg(msg)
  update(json.dumps(core.get_state()))


def update(state):
  socketio.emit("msg", state)
  print "emitted new state\n\n"
core.set_update_function(update)

def loop():
  while True:
    update(json.dumps(core.get_state()))
    eventlet.sleep(0.05)

eventlet.spawn(loop)

if __name__ == '__main__':
  socketio.run(app, host='localhost', debug=True, port=8080)