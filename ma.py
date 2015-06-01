#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
import os
import sys

from merchantCategories import PayPassAPI
from merchantLoc import merchantLocApi
from merchantLoc import merchantByPostalCodeApi

import os
import pprint
import logging
from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    return 'Hello World!\n' + pprint.pformat(str(os.environ))

@app.route('/merchantCategories')
def getMerchantCategories():
        #response="Hello Sharath";
        response=PayPassAPI( 38.7887, 90.5118, 20, 20 );
        # Original Return - Did not show xmnl tree in Chrome
        #return response;
        return response, 200, {'Content-Type': 'text/css; charset=utf-8'};

@app.route('/merchantLocations')
def getMerchanLocations():
        response=merchantLocApi( 38.472, 90.2852, 0, 10 );
        print response;
        # Original Return - Did not show xmnl tree in Chrome
        #return response;
        return response, 200, {'Content-Type': 'text/css; charset=utf-8'};

@app.route('/merchantByZip')
def getMerchantByZip():
        response=merchantByPostalCodeApi(63366 , 0 , 10);
        print response;
        # Original Return - Did not show xmnl tree in Chrome
        #return response;
        return response, 200, {'Content-Type': 'text/css; charset=utf-8'};

@app.route('/test')
def getTest():
        return render_template('test.html');

@app.route('/index')
def getIndex():
        return render_template('index.html');


port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    print "port is ", port
    app.run(host='0.0.0.0', port=int(port))

