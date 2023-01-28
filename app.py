# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 07:09:18 2023

@author: HOSSEIN
"""


from flask import Flask


app=Flask(__name__)


@app.route('/')
def home():
    return "hello"

    

















