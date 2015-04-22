#!/usr/env python

import pickle
import os.path
import sys

fn = sys.argv[1]

if os.path.isfile(fn):

    try:
        print pickle.load(open( "stats2.p", "rb" ))       
    except:
        print fn + " is not a pickle file"

else:
    print fn + " does not exist"
