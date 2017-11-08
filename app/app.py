import requests
import json
import os
import core

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

core = core.core

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')

@socketio.on('msg')
def handle_msg(message):
  print "new msg: " + message
  core.handle_msg(message)
  update(json.dumps(core.get_state()))


def update(state):
  socketio.emit("msg", state)
core.set_update_function(update)


if __name__ == '__main__':
  socketio.run(app, host='localhost', debug=True, port=8080)
