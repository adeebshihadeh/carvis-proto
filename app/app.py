import time
import requests
import os
import cmds
import audio

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
  if request.method == 'POST':
    print "post request"
    print request.form.get('cmd')
    cmds.handleCmd(request.form.get('cmd'))
  return "ok"

@socketio.on('audio')
def handle_audio(message):
  audio.handle_request(message)
  print "audio message: " + message



if __name__ == '__main__':
  socketio.run(app, host='localhost', debug=True, port=8080)