import pandas as pd
import numpy as np
import math
#import psycopg2
from datetime import *  
import time
import random

from SpeedAnalysis import *


def testcase1():
    infile = r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\VF3CU9HP0EY156880.trip_0.csv";
    outfile = r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\VF3CU9HP0EY156880.trip_0.speed.csv";
    dd = SpeedAnalysis(infile,10)
    dd.export(outfile)





if __name__ == '__main__':
    testcase1()