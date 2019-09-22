from app import app
from flask import render_template
import os
import sys

i = int(open(os.path.join('app', 'static', 'viewcount.dat'), 'r').read())
def getIncrement(n=1):
    global i
    i += n
    open(os.path.join, 'w').write(str(i))
    return i

@app.route('/')
def index():
    return render_template('index.html', viewcount=getIncrement())

@app.route('/keybase.txt')
@app.route('/.well-known/keybase.txt')
def keybase():
    return app.send_static_file('keybase.txt')