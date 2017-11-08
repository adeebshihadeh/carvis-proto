import core
import json

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

core = core.core


@socketio.on("msg")
def handle_msg(msg):
  core.handle_msg(msg)
  update_if()


def update_if(state):
  print "got a thing"
  socketio.emit("msg", state)
core.set_update_function(update_if)

if __name__ == '__main__':
  socketio.run(app, host='localhost', debug=True, port=8080)