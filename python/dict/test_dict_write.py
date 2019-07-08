#!/usr/bin/python
#coding: utf8

import csv
import json
import pickle

dict = {
'Msg1' : 'Message1',
'Msg2' : 'Message2',
'Msg3' : 'Message3'
}

# export dictionary in three different formats

w = csv.writer(open("dict.csv", "w"))
for key, val in dict.items():
    w.writerow([key, val])

json = json.dumps(dict)
f = open("dict.json","w")
f.write(json)
f.close()

f = open("dict.pkl","wb")
pickle.dump(dict,f)
f.close()
