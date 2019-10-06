#! /usr/bin/python
# -*- encoding: utf-8 -*-

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')
app.config['SECRET_KEY'] = 'ines'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('./index.html')

@socketio.on('connected')
def conn(msg):
	return {'data':'Ok'}

@socketio.on('client_message')
def receive_message(data):
	emit('server_message', data, broadcast=True)

if __name__ == '__main__':
	socketio.run(app, debug=True)
