#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
movies = {'kymran': ['indiana jones', 'bridget jones', 'mamma mia'],
          'charles': ['puss in boots', 'the last wish', 'django unchained'],
          'diren': ['top gun', 'wolf of wall street', 'rio'],
          'donald': ['lotr', 'the hobbit', 'star wars']
}

# Open file handle for WRITING in TEXT mode
fh_out = open(r"c:\labs\projects\Sky_SuperTech_DC_2025\movies.txt", mode="wt")

# Iterate through movies KEYS and write KEYS+VALUES to file handle..
# Using an ITERATOR for loop
for name in movies.keys():
    print(f"{name} {movies[name]}", end="\n")
    fh_out.write(f"{name} {movies[name]}\n")

fh_out.close() # Flush buffers and close file handle

print("-" * 60)

# Open file handle for READING in TEXT mode
fh_in = open(r"c:\labs\projects\Sky_SuperTech_DC_2025\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into a str object! Be Careful of LARGE files!
# text = fh_in.read(30) # Read NEXT 30 chars into str object!
text = fh_in.readline() # Read NEXT LINE into str object!
print(text)

fh_in.close()