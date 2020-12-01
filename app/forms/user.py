#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" User Form """


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    f_name = StringField("What is the user's first name?", validators=[DataRequired()])
    l_name = StringField("What is the user's last name?", validators=[DataRequired()])
    hobby = StringField("What is the this user's favorite hobby?", validators=[DataRequired()])
    submit = SubmitField("Submit")