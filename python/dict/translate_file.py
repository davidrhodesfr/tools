#!/usr/bin/python

import pickle

# replace function
def replace_strings(src_text, dictionary):
    for key, val in dictionary.items():
        src_text = src_text.replace(key, val)
    return src_text

# dictionary
f = open("dict.pkl","rb")
dict = pickle.load(f)
f.close()

# file to translate
source = open('src.txt','rt')
tmp_text = source.read()
source.close()

# do it
tmp_text = replace_strings(tmp_text, dict)

# output
dest = open('dest.txt','wt')
dest.write(tmp_text)
dest.close()
