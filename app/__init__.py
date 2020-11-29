# !/usr/bin/env python3
# -*- coding: utf8 -*-
"""A Flask app to store Users Information"""

from flask import Flask

app = Flask(__name__)

from app import routes 
