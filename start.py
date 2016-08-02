#!/usr/bin/env python3
from flask import *
app = Flask(__name__)
things_i_like = "test"
projects = "test2"
@app.route('/')
def start_page():
    return render_template('./index.html', things_i_like=things_i_like, projects=projects)
    
@app.route('/<name>')
def hello_name(name):
    return "Hello, {}".format(name)
