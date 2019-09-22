from app import app
from flask import render_template
import os
import sys

@app.route('/')
def index():
    render_template('index.html')