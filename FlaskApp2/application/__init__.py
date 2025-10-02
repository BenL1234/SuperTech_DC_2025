#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
from flask import Flask

# Create Flask object
app = Flask(__name__)

from . import routes

