# coding=utf-8
'''
author:马维畅
time：2018/9/28 13:40
'''

from flask_wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default=False)