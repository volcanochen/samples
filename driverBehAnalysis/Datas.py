import os
import re
import csv
import pandas as pd
import numpy as np
from compiler.ast import Pass
from multiprocessing import Pool

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

    def analyseAll_parallel(self):
        
        #files
        files = []
        for carId in self.cars:
            for tripId in self.cars[carId].trips:
                files.append(self.cars[carId].trips[tripId].tripInfo.file)
                
        p = Pool(5)
        result = p.map(processTripFile, files)

        for carId in self.cars:
            for tripId in self.cars[carId].trips:
                (t1, t2 ,e,d,c,t,d,t,u,n,o) = result.pop()
                print t1, t2
        
        

    def analyseAll(self):
        for carId in self.cars:
            self.cars[carId].analyse()

    def cvsExportIdleMax(self, outfile):
        outputfile = open(outfile, 'wb')
        
        line = ''
        idDataTitle = "%s,%s,%s,%s" %("cardId", "tripId","startTime", "endTime")
        line += "%s,"%idDataTitle
        line += "%s,"%"idleMax"
        line += "%s,"%"idleMax_score"
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
                line += "%f,"%self.cars[ca].trips[tr].score.idle
                
                outputfile.write(line+ "\n")
   
        outputfile.close()
    def cvsExportHeading(self, outfile):
        outputfile = open(outfile, 'wb')
        
        line = ''
        idDataTitle = "%s,%s,%s,%s" %("cardId", "tripId","startTime", "endTime")
        line += "%s,"%idDataTitle
        line += "%s,"%"headingPercentage"
        line += "%s_%s,"%("headingPercentage","score")
        
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
                line += "%f,"%self.cars[ca].trips[tr].score.heading_midDist
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
        line += "%s,"%"VSP"
        line += "%s,"%"VSP_score"
        
        line += "%s,"%an_midD_title
        line += "%s,"%"hard_acc_p"
        line += "%s,"%"hard_brake_p"

        line += "%s_%s,"%(an_midD_title,"score")
        line += "%s,"%"hard_acc_score"
        line += "%s,"%"hard_brake_score"

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
                line += "%f,"%self.cars[ca].trips[tr].vspMean
                line += "%f,"%self.cars[ca].trips[tr].score.vsp
                
                line += "%f,"%self.cars[ca].trips[tr].acc_midDist.midDistPr
                line += "%f,"%self.cars[ca].trips[tr].acc.plusEdge
                line += "%f,"%self.cars[ca].trips[tr].acc.minusEdge
                
                line += "%f,"%self.cars[ca].trips[tr].score.acc_midDist
                line += "%f,"%self.cars[ca].trips[tr].score.acc_hardacc
                line += "%f,"%self.cars[ca].trips[tr].score.acc_hardbrake

                
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
        line += "%s_%s,"%(an_midD_title,"score")
        
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
                line += "%f,"%self.cars[ca].trips[tr].score.accacc_midDist
                outputfile.write(line+ "\n")
   
        outputfile.close()  
         
   

class Score:
    def __init__(self):
        self.acc_midDist = 0
        self.accacc_midDist = 0
        self.acc_hardacc = 0
        self.acc_hardbrake = 0
        self.heading_midDist = 0
        self.idle = 0
        self.vsp = 0
        
    def show(self):
        print ("acc_midDist %f"%self.acc_midDist)
        print ("accacc_midDist %f"%self.accacc_midDist)
        print ("acc_hardacc %f"%self.acc_hardacc)
        print ("acc_hardbrake %f"%self.acc_hardbrake)
        print ("heading_midDist %f"%self.heading_midDist)
        print ("idle %f"%self.idle)
        print ("vsp %f"%self.vsp)

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
        

        self.score = Score()

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
        
        (starttime, endtime,idleCount,acc,acc_m,acc_var,accacc,accacc_m,accacc_var,heading,vspMean) = processTripFile(self.tripInfo.file)
        
        # trip
        self.tripInfo.starttime = starttime
        self.tripInfo.endtime = endtime
        self.idleCountMax = idleCount
        self.acc = acc
        self.acc_midDist = acc_m
        self.acc_var = acc_var
        self.accacc = accacc   
        self.accacc_midDist = accacc_m
        self.accacc_var = accacc_var
        self.heading_midDist = heading
        self.vspMean = vspMean
        
def processTripFile(file):
    f = CSVFile(file)
    acclist, accacclist, headingList, vspList = f.readData()
    
    #trip acc
    acc = DistributeMethod()
    #acc.an_seg_size = 0.5
    acc.analyse(acclist)

    #trip acc_midDist
    acc_m = MidDistributeMethod()
    acc_m.analyse(acclist)
    
    acc_var = VarianceMethod()
    acc_var.analyse(acclist)
    
    #trip accacc
    accacc = DistributeMethod()
    accacc.analyse(accacclist)   
     
    #trip acc_midDist
    accacc_m = MidDistributeMethod()
    accacc_m.analyse(accacclist)  
            
    accacc_var = VarianceMethod()
    accacc_var.analyse(accacclist)  
    
    #heading
    heading = MidDistributeMethod()
    heading.n = 5
    heading.analyse(headingList)
    
    vspMean = np.mean(vspList)
    
    return (f.starttime, f.endtime, f.idleCount,acc,acc_m,acc_var,accacc,accacc_m,accacc_var,heading,vspMean)
        
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
        
        acc_midDist_List = MedianMethod()
        accacc_midDist_List = MedianMethod()
        
        hardacc_list = MedianMethod()
        hardbrake_list = MedianMethod()
        heading_List = MedianMethod()
        
        vsp_List = MedianMethod()
        idle_List = MedianMethod()
        
        for i in self.trips:
            self.trips[i].analyse()
            #continue
            
            acc_midDist_List        .append_forMedian(self.trips[i].acc_midDist.midDistPr)
            accacc_midDist_List     .append_forMedian(self.trips[i].accacc_midDist.midDistPr)
            
            hardacc_list            .append_forMedian(self.trips[i].acc.plusEdge)
            hardbrake_list          .append_forMedian(self.trips[i].acc.minusEdge)
            heading_List            .append_forMedian(self.trips[i].heading_midDist.midDistPr)
            vsp_List                .append_forMedian(self.trips[i].vspMean)
            idle_List               .append_forMedian(self.trips[i].idleCountMax)
        #return    
        # calculate median
        acc_midDist_List.calculate_median()
        hardacc_list.calculate_median()
        hardbrake_list.calculate_median()
        accacc_midDist_List.calculate_median()
        heading_List.calculate_median()
        vsp_List.calculate_median()
        idle_List.calculate_median()
        
        #median for dist to median
        for i in self.trips:
            acc_midDist_List    .append_forDistMedian(self.trips[i].acc_midDist.midDistPr)
            accacc_midDist_List .append_forDistMedian(self.trips[i].accacc_midDist.midDistPr)
            hardacc_list        .append_forDistMedian(self.trips[i].acc.plusEdge)
            hardbrake_list      .append_forDistMedian(self.trips[i].acc.minusEdge)
            heading_List        .append_forDistMedian(self.trips[i].heading_midDist.midDistPr)
            vsp_List            .append_forDistMedian(self.trips[i].vspMean)
            idle_List           .append_forDistMedian(self.trips[i].idleCountMax)
            
        # calculate median
        acc_midDist_List.calculate_distMedian()
        hardacc_list.calculate_distMedian()
        hardbrake_list.calculate_distMedian()
        accacc_midDist_List.calculate_distMedian()
        heading_List.calculate_distMedian()
        vsp_List.calculate_distMedian()
        idle_List.calculate_distMedian()
        
        for i in self.trips:
            self.trips[i].score.acc_midDist    = acc_midDist_List   .scoreEvaluate(self.trips[i].acc_midDist.midDistPr)
            self.trips[i].score.accacc_midDist = accacc_midDist_List.scoreEvaluate(self.trips[i].accacc_midDist.midDistPr)
            self.trips[i].score.acc_hardacc   = hardacc_list        .scoreEvaluate(self.trips[i].acc.plusEdge)
            self.trips[i].score.acc_hardbrake = hardbrake_list      .scoreEvaluate(self.trips[i].acc.minusEdge)
            self.trips[i].score.heading_midDist = heading_List      .scoreEvaluate(self.trips[i].heading_midDist.midDistPr)
            self.trips[i].score.vsp             = vsp_List          .scoreEvaluate(self.trips[i].vspMean)
            self.trips[i].score.idle            = idle_List         .scoreEvaluate(self.trips[i].idleCountMax)

            print (50*"!!")
            self.trips[i].score.show()

class MedianMethod:
    def __init__(self):
        self.list = []
        self.distlist = []
        self.median = None
        self.dist_median = None
        
    def append_forMedian(self, data):
        self.list.append(data)    
        
    def calculate_median(self):
        self.median = np.median(self.list)   
        #self.show()
        
    def calculate_distMedian(self):
        self.dist_median = np.median(self.distlist)   
        #self.show()    
        
    def append_forDistMedian(self, data):
        self.distlist.append(abs(data - self.median))

    def scoreEvaluate(self, data):

        if (abs(data - self.median) + self.dist_median) == 0:
            return -1
        score = self.dist_median / (abs(data - self.median) + self.dist_median)

        print ("input %f md %f dmd %f score %f"%(data,self.median,self.dist_median,score))
        return score
    
    def show(self):
        print ("median %f"%self.median)
        print ("dist median %f"%self.median)
            
def isValidData(dat):
    a = "%f"%dat
    return (a != "nan" and a!= "")

    
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
            
            if speed1 == 655.35:
                speed1 = 0
            if speed2 == 655.35:
                speed2 = 0
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
                        pass
                        #print "time diff error - accacc %d @ %d" % (t2 - last_acc_ts, last_acc_ts)
                    last_acc_ts = t2
                    last_acc = acc
                    
                    #heading
                    if self.ifHeading:
                        if heading1 != 0 or heading2 != 0:
                            
                            heading_acc = self.headingDiff(heading1,heading2)
                            #print "((%d -> %d) %d)"%(heading1,heading2, heading_acc)
                            dif_heading.append(heading_acc)  
                    
            else:
                pass
                #print ("time diff error - acc %d @ %d" % (t2 - t1,  t1))
                
            
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
                            #print ("stop  at %d >5s" % t1)
                            self.calMaxIdleCounter(last_idle_ts - idleStartTs)
                            idleStartTs = 0
                else: # end of idle
                    if idleStartTs != 0: ## if started
                        if t1 - last_idle_ts > 5000: #5 second
                            stopTimeTs = last_idle_ts
                            #print ("stop  at rpm=0 or speed !=0, but at %d diff >5s" % t1)
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
        self.mean = 0
        self.var = 0
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

        self.plusEdge = 0
        self.minusEdge = 0 
        
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
            
        # calcualte edges:
        for i in range(4):
            self.plusEdge +=  self.an_segs_persentage[plus_side_key - i]
            self.minusEdge += self.an_segs_persentage[mins_side_key + i]
        
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



