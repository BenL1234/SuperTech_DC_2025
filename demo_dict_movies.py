#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define, grow, and shrink
# and access a dict=Unordered Collection with Unique keys!
# From Python 3.6 onwards, dict are in INSERTION ORDER
"""
    Docstring:
"""
import pprint

movies = {'kymran': ['indiana jones', 'bridget jones', 'mamma mia'],
          'charles': ['puss in boots', 'the last wish', 'django unchained'],
          'diren': ['top gun', 'wolf of wall street', 'rio']
}

# Grow a dict..
movies['donald'] = ['lotr', 'the hobbit', 'star wars']
movies['grace'] = ['cars', 'fast and the furious 9', 'baby driver']

# Shrink a dict..
movies.pop('charles') # Remove key+value
movies.popitem() # Removes LAST ONE INSERTED!

# Access a dictionary..
print(f"Kymran's favourite three films are: {movies['kymran']}")
print(f"Kymran's Ultimate film is: {movies['kymran'][0]}")
print(f"Kymran's bestest film: {movies.get('kymran')[0]}")

print("-" * 60)
# films = movies.copy() # Copy dict
# films.clear() # Empties dict
pprint.pprint(movies)
print("-" * 60)

# Iterate through the KEYS in a dict
# using an ITERATOR for loop and dict.keys() method
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

# Iterate through the VALUES in a dict
# using an ITERATOR for loop and dict.values() method
for films in movies.values():
    print(f"Good films = {films}")

# Iterate through the KEYS+VALUES in a dict
# using an ITERATOR for loop and dict.items() method
for (name, films) in movies.items():
    print(f"{name} LOVES the films {films}")











