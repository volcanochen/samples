import os
import re
import csv
import pandas as pd
import numpy as np


def sortedDictValue(adict):
    keys = adict.keys()
    keys.sort()
    return [adict[key] for key in keys] 


class Datas:
    def __init__(self):

        self.cars = {} # {carId: Car, ...}
        
    def initFromFolder(self, folder):
        for parent, dirnames, filenames in os.walk(folder):  
            for filename in filenames:
                pattern = re.compile(r'.*\.csv')
                isCSV = pattern.match(filename)
                if not isCSV:
                    print "%s is non csv format" %(filename)
                    continue

                pattern = re.compile(r'(.*)\.trip_(\d+)\.csv')
                isTripCSV = pattern.match(filename)
                if not isTripCSV:
                    print "%s is not trip csv, by pass" %(filename)
                    continue     
                carId = isTripCSV.group(1)   
                tripId = isTripCSV.group(2)   
                print("carId, TripId : (%s, %s)"%(carId, tripId))
                filefullname = os.path.join(parent, filename)
                #print ( "proccessing file : " + filefullname)
                
                if self.cars.has_key(carId):
                    self.cars[carId].trips[tripId] = Trip(carId, tripId, filefullname)
                else:
                    self.cars[carId] = Car(carId, folder)
                    self.cars[carId].trips[tripId] = Trip(carId, tripId, filefullname)

    def show(self):
        for i in self.cars:
            self.cars[i].show()
        
    def analyseAll(self):
        for carId in self.cars:
            self.cars[carId].analyse()

    def cvsExportIdleMax(self, outfile):
        outputfile = open(outfile, 'wb')
        
        line = ''
        idDataTitle = "%s,%s,%s,%s" %("cardId", "tripId","startTime", "endTime")
        line += "%s,"%idDataTitle
        line += "%s,"%"idleMax"
        outputfile.write(line+ "\n")
        
        
        for ca  in self.cars:  #{carid : Datas_car}
            for tr in self.cars[ca].trips: # {tripid: Data_trip}
                cardid = ca
                tripid = tr
                starttime = self.cars[ca].trips[tr].tripInfo.starttime
                endtime = self.cars[ca].trips[tr].tripInfo.endtime
  
                line = ""
                line += "%s,%s,%s,%s," %(cardid, tripid,starttime, endtime)

                line += "%f,"%self.cars[ca].trips[tr].idleCountMax

                outputfile.write(line+ "\n")
   
        outputfile.close()
    def cvsExportHeading(self, outfile):
        outputfile = open(outfile, 'wb')
        
        line = ''
        idDataTitle = "%s,%s,%s,%s" %("cardId", "tripId","startTime", "endTime")
        line += "%s,"%idDataTitle
        line += "%s,"%"headingPercentage"
        outputfile.write(line+ "\n")
        
        
        for ca  in self.cars:  #{carid : Datas_car}
            for tr in self.cars[ca].trips: # {tripid: Data_trip}
                cardid = ca
                tripid = tr
                starttime = self.cars[ca].trips[tr].tripInfo.starttime
                endtime = self.cars[ca].trips[tr].tripInfo.endtime
  
                line = ""
                line += "%s,%s,%s,%s," %(cardid, tripid,starttime, endtime)

                line += "%f,"%self.cars[ca].trips[tr].heading_midDist.midDistPr

                outputfile.write(line+ "\n")
   
        outputfile.close()  
    def cvsExportAcc(self, outfile):
        outputfile = open(outfile, 'wb')
        
        an_segs_title = {}
        for i  in self.cars:  #{carid : Datas_car}
            for j in self.cars[i].trips: # {tripid: Data_trip}
                an_segs_title = self.cars[i].trips[j].acc.an_segs_title
                an_midD_title = self.cars[i].trips[j].acc_midDist.title
                break;

        #print an_segs_title
        
        line = ''
        idDataTitle = "%s,%s,%s,%s" %("cardId", "tripId","startTime", "endTime")
        line += "%s,"%idDataTitle
        for i in sortedDictValue(an_segs_title):
            line += "%s,"%i
        for i in sortedDictValue(an_segs_title):
            line += "%sp,"%i
            
        line += "%s,"%"mean"
        line += "%s,"%"var"
        line += "%s,"%an_midD_title
        line += "%s,"%"VSP"
        outputfile.write(line+ "\n")
        
        
        for ca  in self.cars:  #{carid : Datas_car}
            for tr in self.cars[ca].trips: # {tripid: Data_trip}
                cardid = ca
                tripid = tr
                starttime = self.cars[ca].trips[tr].tripInfo.starttime
                endtime = self.cars[ca].trips[tr].tripInfo.endtime
                
                tripData1 = self.cars[ca].trips[tr].acc.an_segs
                tripData2 = self.cars[ca].trips[tr].acc.an_segs_persentage
                line = ""
                line += "%s,%s,%s,%s," %(cardid, tripid,starttime, endtime)
                for i in sortedDictValue(tripData1):
                    line += "%s,"%i
                for i in sortedDictValue(tripData2):
                    line += "%f,"%i
                    
                line += "%f,"%self.cars[ca].trips[tr].acc_var.mean
                line += "%f,"%self.cars[ca].trips[tr].acc_var.var
                line += "%f,"%self.cars[ca].trips[tr].acc_midDist.midDistPr
                line += "%f,"%self.cars[ca].trips[tr].vspMean
                outputfile.write(line+ "\n")
   
        outputfile.close()
    def cvsExportAccacc(self, outfile):
        outputfile = open(outfile, 'wb')
        
        an_segs_title = {}
        for i  in self.cars:  #{carid : Datas_car}
            for j in self.cars[i].trips: # {tripid: Data_trip}
                an_segs_title = self.cars[i].trips[j].accacc.an_segs_title
                an_midD_title = self.cars[i].trips[j].accacc_midDist.title
                break;

        #print an_segs_title
        
        line = ''
        idDataTitle = "%s,%s,%s,%s" %("cardId", "tripId","startTime", "endTime")
        line += "%s,"%idDataTitle
        for i in sortedDictValue(an_segs_title):
            line += "%s,"%i
        for i in sortedDictValue(an_segs_title):
            line += "%sp,"%i
            
        line += "%s,"%"mean"
        line += "%s,"%"var"
        line += "%s,"%an_midD_title
        outputfile.write(line+ "\n")
        
        
        for ca  in self.cars:  #{carid : Datas_car}
            for tr in self.cars[ca].trips: # {tripid: Data_trip}
                cardid = ca
                tripid = tr
                starttime = self.cars[ca].trips[tr].tripInfo.starttime
                endtime = self.cars[ca].trips[tr].tripInfo.endtime
                
                tripData1 = self.cars[ca].trips[tr].accacc.an_segs
                tripData2 = self.cars[ca].trips[tr].accacc.an_segs_persentage
                line = ""
                line += "%s,%s,%s,%s," %(cardid, tripid,starttime, endtime)
                for i in sortedDictValue(tripData1):
                    line += "%s,"%i
                for i in sortedDictValue(tripData2):
                    line += "%f,"%i
                    
                line += "%f,"%self.cars[ca].trips[tr].accacc_var.mean
                line += "%f,"%self.cars[ca].trips[tr].accacc_var.var
                line += "%f,"%self.cars[ca].trips[tr].accacc_midDist.midDistPr
                outputfile.write(line+ "\n")
   
        outputfile.close()   
class Trip:
    def __init__(self, carId, tripId, f):
        
        self.tripInfo = TripInfo(carId, tripId, f)
        self.acc = None
        self.acc_var = None
        self.acc_midDist = None
        self.accacc = None
        self.accacc_var = None
        self.accacc_midDist = None
        self.heading_midDist = None
        self.idleCountMax = 0
        self.vspMean = 0
        
    def show(self):
        print(50*"=")
        print(50*"=")
        self.tripInfo.show() 
        print(">>>>> acc >>>>>")
        self.acc.show()
        print(">>>>> accacc >>>>>")
        self.accacc.show()
        self.heading_midDist.show()
        
        print("idle max : %d"%self.idleCountMax)
        print("VSP mean : %f"%self.vspMean)
        
    def analyse(self):
        
        f = CSVFile(self.tripInfo.file) #per trip file
        acclist, accacclist, headingList, vspList = f.readData()

        # trip
        self.tripInfo.starttime = f.starttime
        self.tripInfo.endtime = f.endtime
        
        #idle counter max
        self.idleCountMax = f.idleCount
        
        #trip acc
        acc = DistributeMethod()
        #acc.an_seg_size = 0.5
        acc.analyse(acclist)
        self.acc = acc
        
        #trip acc_midDist
        m = MidDistributeMethod()
        m.analyse(acclist)
        self.acc_midDist = m
        
        var = VarianceMethod()
        var.analyse(acclist)
        self.acc_var = var
        
        #trip accacc
        accacc = DistributeMethod()
        accacc.analyse(accacclist)
        self.accacc = accacc   
        
        
        #trip acc_midDist
        accacc_m = MidDistributeMethod()
        accacc_m.analyse(accacclist)
        self.accacc_midDist = accacc_m
        
        accacc_var = VarianceMethod()
        accacc_var.analyse(accacclist)
        self.accacc_var = accacc_var
        
        #heading
        heading = MidDistributeMethod()
        heading.n = 5
        heading.analyse(headingList)
        self.heading_midDist = heading
        
        
        #vsp
        self.vspMean = np.mean(vspList)
        
        
class Car:
    def __init__(self, carId, file_dict):
        
        self.carId = carId
        self.dictory = file_dict
        self.trips = dict() # {trip id : Datas_trip, ...}
        
    def show(self):
        print(20*"=" +self.dictory + 20*"=")

        for i in self.trips:
            self.trips[i].show()  

    def analyse(self):
        print("in analysing "+ self.carId)
        for i in self.trips:
            self.trips[i].analyse()
            
def isValidData(dat):
    a = "%f"%dat
    return (a != "nan")

class CSVFile: 
    def __init__(self, f):
        self.starttime = 0
        self.endtime = 0
        self.file = f
        self.idleCount = 0
        
        self.ifVSP = True
        self.ifHeading = True
        self.ifIdleTime = True
        
    def calStartEndTime(self, mi, ma):
        if self.starttime == 0:
            self.starttime = mi
        if ma > self.endtime:
            self.endtime = ma
    def calMaxIdleCounter(self, ma):
        print ("record idle time: %d" %ma)
        if ma > self.idleCount:
            self.idleCount = ma
            
            
    def headingDiff(self, h1, h2):
        dif = h2 - h1
        if dif > 180:
            dif = dif -360
        elif dif < -180:
            dif = dif +360
        return dif    
            
            
        
    def readData(self):
        print "processing %s"%self.file
        
        accelerate = []
        acc_accelerate = []
        dif_heading  = []
        vsplist = []
        
        self.tsColumn = 3
        self.speedColumn = 23
        self.rpmColumn = 22
        self.headingColumn = 7
        
        df = pd.read_csv(self.file ,sep=",")
        column_count =  df.shape[1]  
        row_count = df.shape[0]
        print "column X row : %d * %d" % (column_count, row_count)
        last_acc_ts = 0
        last_acc = 0
        rpm = 0 # mean invalid data
        idleStartTs = 0
        last_idle_ts = 0
        
        for i in range (row_count - 1):

            
            t1 = df.loc[i][self.tsColumn] #timestamp
            t2 = df.loc[i + 1][self.tsColumn]
            
            
            if last_idle_ts == 0:
                last_idle_ts = t1 
                
            if last_acc_ts == 0:
                last_acc_ts = t2
                
            #print t1, t2
            self.calStartEndTime(t1,t2)

            #==================== speed =======================
            speed1 = df.loc[i][self.speedColumn] #speed
            speed2 = df.loc[i + 1][self.speedColumn]  
            # ============= heading ==================
            
            heading1 = df.loc[i][self.headingColumn] 
            heading2 = df.loc[i + 1][self.headingColumn]    
                 
            if t2 - t1 == 1000:
                if speed2 != 0 or speed1 != 0:
                    acc = speed2 - speed1
                    accelerate.append (acc) 
                    
                    
                    #calculate VSP
                    if self.ifVSP :
                        #speed -> mile per hour 
                        s2 = speed2 * 0.44704 # m/s
                        a2 = acc * 0.44704  # m/s^2
                        vsp = (a2*1.1 + 0.132) * s2  +0.000302 * (s2 ** 3)
                        vsplist.append(vsp)
                    
                    if t2 - last_acc_ts == 1000:
                        acc_accelerate.append (acc - last_acc) 
                    else :
                        print "time diff error - accacc %d @ %d" % (t2 - last_acc_ts, last_acc_ts)
                    last_acc_ts = t2
                    last_acc = acc
                    
                    #heading
                    if self.ifHeading:
                        if heading1 != 0 or heading2 != 0:
                            
                            heading_acc = self.headingDiff(heading1,heading2)
                            #print "((%d -> %d) %d)"%(heading1,heading2, heading_acc)
                            dif_heading.append(heading_acc)  
                    
            else:
                print ("time diff error - acc %d @ %d" % (t2 - t1,  t1))
                
            
            if self.ifIdleTime:
                # ===========  rpm =============================
                if  isValidData(df.loc[i][self.rpmColumn]):#rpm
                    ####### not considering ts diff > 5s ######
                    rpm = df.loc[i][self.rpmColumn]
                    #print ("set rpm %f" % rpm)
                    
                #print "ts %d  rpm %f , speed %f" %(t1, rpm,speed1)
                if rpm != 0 and speed1 == 0: # meet condition
                    if idleStartTs == 0 :
                        #print ("start at %d" % t1)
                        idleStartTs  = t1
                    else: # if started
                        if t1 - last_idle_ts > 5000: #5 second
                            print ("stop  at %d >5s" % t1)
                            self.calMaxIdleCounter(last_idle_ts - idleStartTs)
                            idleStartTs = 0
                else: # end of idle
                    if idleStartTs != 0: ## if started
                        if t1 - last_idle_ts > 5000: #5 second
                            stopTimeTs = last_idle_ts
                            print ("stop  at rpm=0 or speed !=0, but at %d diff >5s" % t1)
                        else:
                            stopTimeTs = t1
                        #print ("stop  at %d" % t1)
                        self.calMaxIdleCounter(stopTimeTs - idleStartTs)
                        idleStartTs = 0
    
                last_idle_ts = t1 
            # ==============-==============================

        #print accelerate 
        return accelerate, acc_accelerate, dif_heading, vsplist
    
class TripInfo:
    def __init__(self, cardId , trip, f):
        self.carId = cardId
        self.tripId = trip
        self.file = f
        self.starttime = 0
        self.endtime = 0
    def show(self):
        print("carId: " +self.carId)
        print("tripId: " +self.tripId)
        print("file: " +self.file)
        print("time: %d  -- %d"%(self.starttime,self.endtime))

        
class VarianceMethod:
    def __init__(self):
        pass
    def analyse(self, data_list):
        if len(data_list) == 0 :
            print "empty!!!!!!!!"
            return
        self.mean = np.mean(data_list)
        self.var = np.var(data_list)
    def show(self):
        print ("mean: %f   var: %f"%(self.mean, self.var))
        
class MidDistributeMethod:
    def __init__(self):
        self.n = 0.5  # means [-0.5, 0.5]
        self.title = "[%.2f _ %.2f]"%(-self.n, self.n)
        self.midDistPr = 0
        
    def analyse(self, data_list):
        if len(data_list) == 0 :
            print "empty!!!!!!!!"
            return
        counter = 0
        for it in data_list:
            if it != 0 and it >= -self.n and it <= self.n:
                counter += 1
        if len(data_list) != 0: 
            self.midDistPr = float(counter) / len(data_list)
            
    def show(self):
        print self.title
        print "percentage: %f"%self.midDistPr    
           
class DistributeMethod:
        
    def __init__(self):
        print "init"

        self.an_seg_size = 1
        self.an_seg_count = 20
        self.an_segs = dict()  # {seg_id : count}
        self.an_segs_persentage = dict() # {seg_id : 0.02}
        self.an_segs_title = dict()  # {seg_id : seg_title}
        self.total_data = 0

        
    def analyse(self, data_list):
        
        if len(data_list) == 0 :
            print "empty!!!!!!!!"
            return
        if isinstance(self.an_seg_size,float):
            titleFormatPlus = "[%.2f_%.2f)"
            titleFormatMinu = "(%.2f_%.2f]"
            titleFormatEdgePlus = "[%.2f_)"
            titleFormatEdgeMinu = "(_%.2f]"
        else:
            titleFormatPlus = "[%d_%d)"
            titleFormatMinu = "(%d_%d]"
            titleFormatEdgePlus = "[%d_)"
            titleFormatEdgeMinu = "(_%d]"
        
        
        seg_distr_count_dict = dict()
        
        for item in data_list:
            #
            # dist to (  ...,   -2,    -1,    1,     2    ,...)
            # mappin of  ...,(-2,-1], (-1,0), [0,1), [1,2) ,...
            #
            seg_distr = int(float(item)/self.an_seg_size) + (1 if (float(item))>=0 else -1) 
            if seg_distr_count_dict.has_key(seg_distr):
                num = seg_distr_count_dict[seg_distr] + 1
                seg_distr_count_dict[seg_distr] = num
            else:
                seg_distr_count_dict[seg_distr] = 1

        self.total_data = float(len(data_list))
        
        #
        for seg_id in range(self.an_seg_count/2 - 1):  
            key = seg_id  + 1  #  for plus  1 , 2, ...

            self.an_segs[key] = 0  #init
            
            self.an_segs_title[key] = titleFormatPlus % ((key-1)*self.an_seg_size, key*self.an_seg_size )
            
            if seg_distr_count_dict.has_key(key):
                self.an_segs[key] = seg_distr_count_dict[key]
                seg_distr_count_dict.pop(key)
            if self.total_data != 0:
                self.an_segs_persentage[key] = self.an_segs[key]/self.total_data  

        for seg_id in range(self.an_seg_count/2 - 1):  # for minus
            key = (-seg_id -1)
            
            self.an_segs[key] = 0 #init
            
            self.an_segs_title[key] = titleFormatMinu % (key*self.an_seg_size, (key + 1)*self.an_seg_size)

            if seg_distr_count_dict.has_key(key):
                self.an_segs[key] = seg_distr_count_dict[key]
                seg_distr_count_dict.pop(key)
            if self.total_data != 0:    
                self.an_segs_persentage[key] = self.an_segs[key]/self.total_data

        #for two side
        plus_side_key  = self.an_seg_count/2
        mins_side_key  = -self.an_seg_count/2
        self.an_segs_title[plus_side_key] = titleFormatEdgePlus % ((plus_side_key-1)* self.an_seg_size)
        self.an_segs_title[mins_side_key] = titleFormatEdgeMinu % ((mins_side_key+1)* self.an_seg_size )
        
        self.an_segs[plus_side_key]  = 0
        self.an_segs[mins_side_key] = 0
        for it in seg_distr_count_dict:
            if it > 0:
                self.an_segs[plus_side_key] += seg_distr_count_dict[it]

            else :
                self.an_segs[mins_side_key] +=  seg_distr_count_dict[it]
        if self.total_data != 0: 
            self.an_segs_persentage[plus_side_key] = self.an_segs[plus_side_key]/self.total_data
            self.an_segs_persentage[mins_side_key] = self.an_segs[mins_side_key]/self.total_data
        
    def show(self):
        
        print (100*"=")
        print ("seg: size * count = %f %d"%(self.an_seg_size, self.an_seg_count))
        print sortedDictValue(self.an_segs_title)
        print sortedDictValue(self.an_segs)
        print sortedDictValue(self.an_segs_persentage)
        print (100*"=")

    def csvExport(self,outfile):
        outputfile = open(outfile, 'wb')
        line = ''
        for i in sortedDictValue(self.an_segs_title):
            line += "%s,"%i
        for i in sortedDictValue(self.an_segs_title):
            line += "%sp,"%i
        outputfile.write(line+ "\n")
        line = ""
        for i in sortedDictValue(self.an_segs):
            line += "%s,"%i
        for i in sortedDictValue(self.an_segs_persentage):
            line += "%f,"%i
        outputfile.write(line+ "\n")
        outputfile.close()



