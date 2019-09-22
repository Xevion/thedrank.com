from app import app
from flask import render_template
from multiprocessing import Value
import os
import sys

viewcountpath = os.path.join('app', 'static', 'viewcount.dat')
counter = Value('i', int(open(viewcountpath, 'r').read()))

def getIncrement(n=1):
    with counter.get_lock():
        counter.value += n
    open(viewcountpath, 'w').write(str(counter.value))
    return counter.value

@app.route('/')
def index():
    return render_template('index.html', viewcount=getIncrement())

@app.route('/keybase.txt')
@app.route('/.well-known/keybase.txt')
def keybase():
    return app.send_static_file('keybase.txt')