"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess belief 1 Corbat ́o’s law
License: Proprietary
"""

import os
import os.path
from os import path


prefix = './'

def getFileHandle(filename):

    return open(prefix + filename, "a+")


def remove(filename):
    print("type ", filename ," | py -2 ./sk.py --text 30 --latex False > ", "./results/sk_"+filename)
    path_res = prefix + filename
    if path.exists(path_res):
        os.remove(path_res)
    # else:
        # print("no such file at : ",path_res)

def appendTreatment(filename, treatmentLabel, population):

    f = getFileHandle(filename)

    f.write(treatmentLabel + "\n")

    line = ''
    for p in population:
        line += str(p) + " "

    f.write(line.strip() + "\n\n")


