from app import app
from flask import render_template
import os
import sys

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/keybase.txt')
@app.route('/.well-known/keybase.txt')
def keybase():
    return app.send_static_file('keybase.txt')