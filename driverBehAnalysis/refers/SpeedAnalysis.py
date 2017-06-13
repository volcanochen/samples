import pandas as pd
import numpy as np
import math
#import psycopg2
from datetime import *  
import time
import random

class OutputUtil:
    def __init__(self):
        pass
    @staticmethod
    def basicTitle():
        return "carId,tripId,startTime,endTime,zeroNumber"
        
class SpeedAnalysis:

    
    def __init__(self, file,  segment):
        self.segment = segment
        self.anyliseAcc(file)

    def anyliseAcc(self, file):
        
        self.accelerate = []
        self.tsColumn = 3
        self.speedColumn = 23
        
        df = pd.read_csv(file ,sep=",")
        
        print "column X row : %d * %d" % (df.shape[0], df.shape[1])#column
        
        for i in range (df.shape[0] - 1):
            t1 = df.loc[i][self.tsColumn] #timestamp
            t2 = df.loc[i + 1][self.tsColumn]

            speed1 = df.loc[i][self.speedColumn] #speed
            speed2 = df.loc[i + 1][self.speedColumn]  
            
            if t2 - t1 == 1000:
                if speed2 != 0 and speed1 != 0:
                    self.accelerate.append (speed2 - speed1) 
            else:
                print "time diff error - %d" % (t2 -t1)
            
        print self.accelerate    
   
    def anyliseSpeed(self, file):
        
        self.accelerate = []
        self.tsColumn = 3
        self.speedColumn = 23
        
        
        
        speedCat = []  # 0---> max , interval = n, count
        anylMaxSpeed = 145
        anylInterval = 10
        anylCount = 15
        n = 0
        while(n < anylCount -1):
            catTitle  += "%d-%d,"%(anylInterval * n ,( n +1)* anylInterval)
            n += 1
            
        catTitle  += "%d-"%(anylInterval * n)
           

        
        df = pd.read_csv(file ,sep=",")
        
        print "column X row : %d * %d" % (df.shape[0], df.shape[1])#column
        
        for i in range (df.shape[0] - 1):

            speed = df.loc[i][self.speedColumn]  
            
            if t2 - t1 == 1000:
                if speed2 != 0 and speed1 != 0:
                    self.accelerate.append (speed2 - speed1) 
            else:
                print "time diff error - %d" % (t2 -t1)
            
        print self.accelerate        

        
        
    def export(self, file):
        title = "%s,%s"%(OutputUtil.basicTitle() , catTitle())
        outputfile = open(file, 'wb')
        outputfile.write(title+"\n")
        pass

    def catTitle(self):
        return "0_9,10_19,20_29,30_39,40_49,50_59,60_69,70_79,80_89,90_99,100_109,110_119,120_129,130_139,140_";
       





