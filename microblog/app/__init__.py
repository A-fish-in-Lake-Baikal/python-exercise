# coding=utf-8
'''
author:马维畅
time：2018/9/27 17:33
'''


from flask import Flask
from app import views

app = Flask(__name__)
app.config.from_object('config')
