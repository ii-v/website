#!/usr/bin/env python3
from flask import *
import markdown
app = Flask(__name__)
things_i_like = open('things_i_like.list', 'r').readlines()
projects = open('projects.list', 'r').readlines()
@app.route('/')
def start_page():
    return render_template('index.html', things_i_like=things_i_like, projects=projects)
    
@app.route('/<number>')
def hello_name(number):
    return "{0} in binary is {1}".format(number, bin(number))
