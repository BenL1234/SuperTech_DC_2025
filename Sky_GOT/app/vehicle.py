#! /usr/bin/env python3
# Author: DCameron
# Description: This is a BASE class of Vehicle
"""
    Vehicle Base Class for Tanks, Jeeps and Trucks
"""

class Vehicle:
    def __init__(self, country, model):
        self.country = country # Public var
        self.model = model # Public var

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None