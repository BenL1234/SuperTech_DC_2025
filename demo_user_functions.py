#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define, name, and call
# a user function with optional parameters, default values and optional
# return value.
"""
    Docstring:
"""
# Example of a user function with optional
# parameter passing [(*,) enforces named passing]
# and DEFAULT Values. Plus ANNOTATIONS (:str/:list/:dict)- NOT ENFORCED!
def say_hello(greeting:str="Namaste", recipient:str="doston")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None


say_hello("hello", "my friends") # Positional Parameter passing
say_hello(greeting="ciao", recipient="amici") # Named parameter passing
say_hello(recipient="mi amigos", greeting="hola") # Named parameter (in different order)
say_hello("salut", recipient="mes amis") # Mixed parameter passing (positional->named)
say_hello("namaste")
say_hello()

