#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
import os
import sys

from merchantCategories import PayPassAPI

import os
import pprint
import logging
from flask import Flask 

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    return 'Hello World!\n' + pprint.pformat(str(os.environ))

@app.route('/merchantCategories')
def getMerchantCategories():
        #response="Hello Sharath";
        response=PayPassAPI( 38.7887, 90.5118, 20, 20 );
        return response;

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    print "port is ", port
    app.run(host='0.0.0.0', port=int(port))

