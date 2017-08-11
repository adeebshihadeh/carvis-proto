import time
import requests
import os
import cmds
import ups

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')

@app.route('/command', methods=['GET', 'POST'])
def command():
  if request.method == 'POST':
    print "post request"
    print request.form.get('cmd')
    cmds.handleCmd(request.form.get('cmd'))
  return "ok"

@app.route('/update', methods=['GET', 'POST'])
def update():
  os.system("git pull")
  return render_template('index.html')


if __name__ == '__main__':
  ups.init()
  app.run(debug=True, host= 'localhost')