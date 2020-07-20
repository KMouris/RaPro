import os, glob
import pandas as pd
import csv
import datetime

try:
    import numpy as np
except:
    print("ERROR: Package numpy not installed (make sure to use the provided Conda environment).")
import config
from functools import partial

# ----Check Function: Checks if folder path exists-----#
def CheckPath(file_dir):
    if os.path.exists(file_dir) == True:
        pass
    else:
        sys.exit("ERROR: The file directory doesn't exist")

def Prec(name, storm_array_mean, tdm, i):  # recieves name of file (to get date), the mean prec from the .txt file the file iteration number
    date = GetDate(name)  # send file name to function to get the date and time of the file values
    value = storm_array_mean
    tdm = TwoDArray_Precipitation(date, value, tdm, i)
    return tdm

def TwoDArray_Precipitation(date, value, tdm, i):
    tdm[i,0:4]=date #fill columns 1 to 4
    tdm[i,4]=value #fill column 5 with mean value
    #print(tdm)
    return tdm

# ----Function: Get Date#
###Function recieves file name (which is the date) and saves each value [year, month, day, hour, minute, second] in an array
def GetDate(name):
    date = np.zeros(4)  # Initialize an array with 6 values, will be a float array
    date[0] = float(name[0:4])  # year
    date[1] = float(name[4:6])  # month
    date[2] = float(name[6:8])  # day
    date[3] = float(name[10:12])  # hour
    return date
