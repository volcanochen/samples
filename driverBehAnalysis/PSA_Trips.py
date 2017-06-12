'''
Created on Jun 12, 2017

@author: eliiyui
'''
import csv
from copy import deepcopy
import pandas as pd  
import numpy as np 
from numpy import sort
import re
import os 
import os.path

class PSA_Trips(object):
    def __init__(self, inputPath):
        self.tripInterval = 30  # 30 min
        self.path = inputPath
        self.title = [
            "timeOffset",
            "dateOfCollection",
            "second",
            "ts",
            "ts_str",
            "date_str",
            "time_str",
            "heading",
            "latitude",
            "longitude",
            "altitude",
            "quality",
            "type",
            "frontFogLampsStatus",
            "rearFogLampsStatus",
            "driverBeltStatus",
            "outsideTemperature",
            "recommendedGearIndicator",
            "fuelInstantConsumption",
            "fuelTotalConsumption",
            "ignition",
            "gearboxMode",
            "engineRpm",
            "speed",
            "luminosity",
            "hybridMode",
            "odometer",
            "fuelLevel",
            "oilTemperature",
            "gmpStatus",
            "exceedingSpeed"
            ]
        
        
        self.titleStr   = "" 
        self.speedInterval = 10  # km/h
        self.speedStart = 0
        self.speedBucketNumber  = 15  
        
        #        value =  "%s,%s,%s,%s," %(carId , tripId, startTime, endTime)

        self.speedTitle = "carId,tripId,startTime,endTime,zeroNumber,"\
                        +"0_9,10_19,20_29,30_39,40_49,50_59,60_69,70_79,80_89,90_99,100_109,110_119,120_129,130_139,140_,"\
                        +"0_9p,10_19p,20_29p,30_39p,40_49p,50_59p,60_69p,70_79p,80_89p,90_99p,100_109p,110_119p,120_129p,130_139p,140_p"
        
 
            
        for i in range(len(self.title)):
            self.titleStr += self.title[i]+","
            
        return        


    def read_sort_SingleCSV(self,inputFile):
        csvfile = open(self.path+inputFile, 'rb')
        reader  = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        
        m = re.match(r'(.*)\.csv', inputFile)
        carid = m.group(1)      
        
        resultDict = dict()                  
        for row in reader:
            key = row['ts']
            #print key
            
            #print row 
            value = "";
            for i in range(len(self.title)):                    
                  value += row[self.title[i]]+","
            resultDict[key] = value
               

        outputfile = open(self.path+inputFile+'.sort.csv', 'wb')
        
        #print resultDict.keys()
        #print np.sort( resultDict.keys())
        outputfile.write(self.titleStr+"\n")
        for key in np.sort( resultDict.keys()):
            outputfile.write(resultDict[key]+"\n")
        csvfile.close()       
       #     print '%s,%s' % (key, self.resultDict[key])  
    
    def cal_geo_single(self):
        return
    
    def cal_speed_distribution(self):
        outputfile = open(self.path+'Table_speed.csv', 'wb')
        outputfile.write(self.speedTitle+"\n")
        rootdir = self.path  
        for parent, dirnames, filenames in os.walk(rootdir):  
        # case 1:   
            #for dirname in dirnames:  
            #   print ( " parent is: " + parent)  
            #   print ( " dirname is: " + dirname)  
        # case 2   
            for filename in filenames:
                
       
                pattern = re.compile(r'.*\.csv')
                isCSV = pattern.match(filename)
                if not isCSV:
                    print "%s is non csv format" %(filename)
                    continue
                
                pattern = re.compile(r'.*\.trip_\d+.csv')
                isTripCSV = pattern.match(filename)
                if not isTripCSV:
                    print "%s is not trip csv, by pass" %(filename)
                    continue     
                

                
                print ( "proccessing file : " + os.path.join(parent, filename))
                record = self.cal_speed_distribution_single(filename)
                outputfile.write(record + "\n")
        outputfile.close()
        
    def cal_speed_distribution_single(self,inputFile):
        record_value = ""
        csvfile = open(self.path+inputFile, 'rb')
        reader  = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        
        m = re.match(r'(.*).trip_(\d+)\.csv', inputFile)
        
        carId = m.group(1)   
        tripId = m.group(2)   
        
        #print  "car Id : %s" %(carId)
        #print  "trip Id : %s" %(tripId)
        startTime= 0
        endTime = 0
        
        #init
        resultDict = dict()  
        for i in  range(self.speedBucketNumber):
            resultDict[i] = 0
        
        NonZeroTotal = 0.0
        zeroNumber = 0
        for row in reader:
            
            key = long(row['ts'])
            if startTime == 0:
                startTime = key
            if key > endTime:
                endTime = key
            speed = float(row['speed'])
            if speed == 0:
                zeroNumber += 1
                continue
            
            NonZeroTotal += 1
            bucket =  int(speed / self.speedInterval)
            if(bucket  > self.speedBucketNumber - 1):
                bucket =  self.speedBucketNumber - 1
                 
            if resultDict.has_key(bucket):
                #print "#1"
                resultDict[bucket] = resultDict[bucket] + 1
         
            else:       
                #print "(key %s speed %s bucket %s)" %(key,speed, bucket)       
                resultDict[bucket] = 1            
            #print "(key %s speed %s bucket %s)" %(key,speed, bucket) 
        
        record_value =  "%s,%s,%s,%s,%s" %(carId , tripId, startTime, endTime, zeroNumber)
        
        
        for i in  range(self.speedBucketNumber):
            #print "(bucket %s number %s )" %(i,resultDict[i])
            record_value = "%s,%s" %(record_value ,str(resultDict[i]) ) 
            
        
        for i in  range(self.speedBucketNumber):
            #print "(bucket %s number %s total %s )" %(i,resultDict[i],total)
            if NonZeroTotal > 0:
                record_value = "%s,%.3f" %(record_value ,float(resultDict[i]/NonZeroTotal) )
            else:
                record_value = "%s,%.3f" %(record_value ,0) 
        #print record_value
        csvfile.close()
        return record_value

    def splitTrps_SingleCSV(self,inputFile):
        csvfile = open(self.path+inputFile, 'rb')
        reader  = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        
        m = re.match(r'(.*)\.csv', inputFile)
        carId = m.group(1)      
        
        resultDict = dict()                  
        for row in reader:
            key = row['ts']
            #print key
            
            #print row 
            value = "";
            for i in range(len(self.title)):                    
                  value += row[self.title[i]]+","
            resultDict[key] = value
        
        lastkey = 0
        tripId = 0
        
        
        for key in np.sort( resultDict.keys()):
            key_value = long(key)
            if ( key_value - lastkey ) /1000 /60 > self.tripInterval :
                #print "found a trip: %d" %(tripId)
                outputfile = open(self.path+carId+'.trip_'+str(tripId)+'.csv', 'wb')
                outputfile.write(self.titleStr+"\n")
                tripId = tripId + 1
 
            outputfile.write(resultDict[key]+"\n")
            lastkey = key_value
             
               
       #     print '%s,%s' % (key, self.resultDict[key])  

            
    
    def splitTrips(self):
        
        rootdir = self.path  
        for parent, dirnames, filenames in os.walk(rootdir):  
        # case 1:   
            #for dirname in dirnames:  
            #   print ( " parent is: " + parent)  
            #   print ( " dirname is: " + dirname)  
        # case 2   
            for filename in filenames:
                
       
                pattern = re.compile(r'.*\.csv')
                isCSV = pattern.match(filename)
                if not isCSV:
                    print "%s is non csv format" %(filename)
                    continue
                
                pattern = re.compile(r'.*\.trip_\d+.csv')
                isTripCSV = pattern.match(filename)
                if isTripCSV:
                    print "%s is trip csv, by pass" %(filename)
                    continue            
                
                pattern = re.compile(r'Table.*\.csv')
                isTripCSV = pattern.match(filename)
                if isTripCSV:
                    print "%s is Table csv, by pass" %(filename)
                    continue     
                
                print ( "proccessing file : " + os.path.join(parent, filename))
                self.splitTrps_SingleCSV(filename)
                                