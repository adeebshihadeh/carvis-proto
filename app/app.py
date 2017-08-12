import time
import requests
import os
import cmds
import audio

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


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

@app.route('/update', methods=['POST'])
def update():
  os.system("git pull")
  return render_template('index.html')


@app.route('/audio', methods=['POST'])
def handle_audio():
  audio.handle_request()
  request.form.get('cmd')
  return "ok"


if __name__ == '__main__':
  app.run(debug=True, host= 'localhost', port=8080)