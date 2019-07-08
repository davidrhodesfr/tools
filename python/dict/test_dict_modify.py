#!/usr/bin/python

import pickle

f = open("dict.pkl","rb")
dict = pickle.load(f)
f.close()

# remove one entry
dict.pop('Msg2')

for key, val in dict.items():
    print key, ';', val

f = open("dict-new.pkl","wb")
pickle.dump(dict,f)
f.close()
