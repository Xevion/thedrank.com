from app import app
from flask import render_template
import os
import sys

viewcountpath = os.path.join('app', 'static', 'viewcount.dat')
i = int(open(viewcountpath, 'r').read())
def getIncrement(n=1):
    global i
    i += n
    open(viewcountpath, 'w').write(str(i))
    return i

@app.route('/')
def index():
    return render_template('index.html', viewcount=getIncrement())

@app.route('/keybase.txt')
@app.route('/.well-known/keybase.txt')
def keybase():
    return app.send_static_file('keybase.txt')