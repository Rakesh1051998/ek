import os
import random
#import socket
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

from os import environ

from datetime import datetime
from flask import render_template , Flask
#from flask import Flask
#import EkFlaskJade1.views

app = Flask(__name__)

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')


@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.jade',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.jade',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.jade',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/sai')
def sai():
    directory = os.getcwd()
    y = np.array([35, 25, 25, 15])
    plt.pie(y)
    s = directory + '\ekflaskjade1\static\eksai11.jpg'
    plt.savefig(s)
    return "<h1>" + s + "</h1><img src='static/eksai11.jpg' />"




@app.route('/ek/<string:name>', methods=['GET'])
def ek(name):
    
    if isBlank(name):
        name="10,20,30"


    s = name.split(",")
    directory = os.getcwd()
    y = np.array(s)
    plt.pie(y)
    s = "E:\EkPython\EkFlaskTest\EkFlaskJade1\static\eksai31.jpg"
    plt.savefig(s)
    #plt.draw
    HOST = environ.get('SERVER_HOST', 'localhost')
    PORT = environ.get('SERVER_PORT', '5555')
    url="http://" + HOST + ":" + PORT + "/static/eksai31.jpg?rnd=" + str(random.random())
    #return s + " ## " + url    
    return url + "<img src='" + url + "' />"

def isBlank (myString):
    return not (myString and myString.strip())





#from os import environ
#from EkFlaskJade1 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
