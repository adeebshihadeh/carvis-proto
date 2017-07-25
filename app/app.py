import time
import requests
import cmds

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


if __name__ == '__main__':
  app.run(debug=True, host= '192.168.1.187')