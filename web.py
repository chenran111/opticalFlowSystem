#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# coding=utf-8
from flask import *
app=Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>Apache server发布成功!</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8081)