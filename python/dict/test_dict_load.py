#!/usr/bin/python

import pickle

# open and dump dictionary in pickle format
f = open("dict.pkl","rb")
dict = pickle.load(f)
f.close()

# dump dictionary
for key, val in dict.items():
    print key, ';', val

print(dict.keys())
print(dict.values())
