import os
import re
import csv
import pandas as pd


class Datas:
    def __init__(self):
        self.car_trip_dict = {}#  {card1 : {0 : path,1:xx ,2:xx }, card2 : {0:xx}}
        self.datas_card = {}
        
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
                if self.car_trip_dict.has_key(carId):
                    self.car_trip_dict[carId][tripId]=filefullname
                else:
                    self.car_trip_dict[carId]= {tripId:filefullname}
        print self.car_trip_dict
        
    def analyseAll(self):
        for carId in self.car_trip_dict:
            car = Datas_car(carId, self.car_trip_dict[carId])
            car.analyse()
            self.datas_card[carId] = car
            
    def cvsExport(self, outfile):
        outputfile = open(outfile, 'wb')
        
        an_segs_title = {}
        for i  in self.datas_card:  #{carid : Datas_car}
            for j in self.datas_card[i].datas_trips: # {tripid: Data_trip}
                an_segs_title = self.datas_card[i].datas_trips[j].an_segs_title
                break;

        #print an_segs_title
        
        line = ''
        idDataTitle = "%s,%s,%s,%s" %("cardId", "tripId","startTime", "endTime")
        line += "%s,"%idDataTitle
        for i in sortedDictValue(an_segs_title):
            line += "%s,"%i
        for i in sortedDictValue(an_segs_title):
            line += "%sp,"%i
        outputfile.write(line+ "\n")
        
        
        for ca  in self.datas_card:  #{carid : Datas_car}
            for tr in self.datas_card[ca].datas_trips: # {tripid: Data_trip}
                cardid = ca
                tripid = tr
                starttime = self.datas_card[ca].datas_trips[tr].starttime
                endtime = self.datas_card[ca].datas_trips[tr].endtime
                tripData1 = self.datas_card[ca].datas_trips[tr].an_segs
                tripData2 = self.datas_card[ca].datas_trips[tr].an_segs_persentage
                line = ""
                line += "%s,%s,%s,%s," %(cardid, tripid,starttime, endtime)
                for i in sortedDictValue(tripData1):
                    line += "%s,"%i
                for i in sortedDictValue(tripData2):
                    line += "%f,"%i
                outputfile.write(line+ "\n")
   
        outputfile.close()
class Datas_car:
    def __init__(self, carId, trip_file_dict):
        
        self.carId = carId
        self.trip_file_dict = trip_file_dict
        self.datas_trips = dict() # {1: data_trip}
        
    def analyse(self):
        print("in analysing "+ self.carId)
        for trip in self.trip_file_dict:
            a = Data_trip(self.carId, trip, self.trip_file_dict[trip])
            a.start()
            self.datas_trips[trip]=a
            
                
class Data_trip:
        
    def __init__(self, cardId , trip, file):
        print "init"

        self.an_seg_size = 1
        self.an_seg_count = 20
        self.an_segs = dict()  # {seg_id : count}
        self.an_segs_persentage = dict() # {seg_id : 0.02}
        self.an_segs_title = dict()  # {seg_id : seg_title}
        
        self.carId = cardId
        self.tripId = trip
        self.file = file
        
        self.starttime = 0
        self.endtime = 0
        
        #self.start()
        
    def start(self):
        print ("start analysing "+ self.tripId)
        li = self.readData()
        self.analyse(li)
        #self.sortedPrint()
        
    def readData(self):
        print "processing %s"%self.file
        accelerate = []
        self.tsColumn = 3
        self.speedColumn = 23
        
        df = pd.read_csv(self.file ,sep=",")
        
        print "column X row : %d * %d" % (df.shape[0], df.shape[1])#column
        
        for i in range (df.shape[0] - 1):
            t1 = df.loc[i][self.tsColumn] #timestamp
            t2 = df.loc[i + 1][self.tsColumn]
            
            if self.starttime == 0:
                self.starttime = t1
            if t2 > self.endtime:
                self.endtime = t2

            speed1 = df.loc[i][self.speedColumn] #speed
            speed2 = df.loc[i + 1][self.speedColumn]  
            
            if t2 - t1 == 1000:
                if speed2 != 0 and speed1 != 0:
                    accelerate.append (speed2 - speed1) 
            else:
                print "time diff error - %d" % (t2 -t1)
            
        print accelerate 
        return accelerate 
        
    def readData_sim(self, file):
        
        
        return  [-6.69,
                     -0.5,
                     -0.69 ,
                     2.68,
                     4.7,
                     4.98,
                     5.87,
                     6.67,
                     8.3 ]   
        
    def analyse(self, data_list):
        
        if isinstance(self.an_seg_size,float):
            titleFormat = "(%.2f-%.2f)"
            titleEdge1Format = "(%.2f-)"
            titleEdge2Format = "(-%.2f)"
        else:
            titleFormat = "(%d-%d)"
            titleEdge1Format = "(%d-)"
            titleEdge2Format = "(-%d)"
        
        
        seg_distr_count_dict = dict()
        
        for item in data_list:
            seg_distr = int(float(item)/self.an_seg_size) + (1 if (float(item))>0 else -1) #  -2 -1 1 2
            if seg_distr_count_dict.has_key(seg_distr):
                num = seg_distr_count_dict[seg_distr] + 1
                seg_distr_count_dict[seg_distr] = num
            else:
                seg_distr_count_dict[seg_distr] = 1

        self.total_data = float(len(data_list))

        #
        for seg_id in range(self.an_seg_count/2 - 1):  # for plus  0 , 1

            key = seg_id  +1
            self.an_segs[key] = 0
            
            self.an_segs_title[key] = titleFormat % (key- self.an_seg_size, key )
            
            if seg_distr_count_dict.has_key(key):
                self.an_segs[key] = seg_distr_count_dict[key]
                seg_distr_count_dict.pop(key)
            self.an_segs_persentage[key] = self.an_segs[key]/self.total_data
            



        for seg_id in range(self.an_seg_count/2 - 1):  # for minus

            key = (-seg_id -1)
            self.an_segs[key] = 0
            
            self.an_segs_title[key] = titleFormat % (key, key + self.an_seg_size)

            if seg_distr_count_dict.has_key(key):
                self.an_segs[key] = seg_distr_count_dict[key]
                seg_distr_count_dict.pop(key)
                
            self.an_segs_persentage[key] = self.an_segs[key]/self.total_data

        self.an_segs_title[self.an_seg_count/2] = titleEdge1Format % (self.an_seg_count/2)
        self.an_segs_title[-self.an_seg_count/2] = titleEdge2Format % (-self.an_seg_count/2)
        self.an_segs[self.an_seg_count/2]  = 0
        self.an_segs[-self.an_seg_count/2] = 0
        for it in seg_distr_count_dict:
            if it > 0:
                self.an_segs[self.an_seg_count/2] = self.an_segs.get(self.an_seg_count/2,0) + seg_distr_count_dict[it]

            else :
                self.an_segs[-self.an_seg_count/2] = self.an_segs.get(-self.an_seg_count/2,0) + seg_distr_count_dict[it]
        self.an_segs_persentage[self.an_seg_count/2] = self.an_segs[self.an_seg_count/2]/self.total_data
        self.an_segs_persentage[-self.an_seg_count/2] = self.an_segs[-self.an_seg_count/2]/self.total_data
        
    def show(self):
        
        print (100*"=")
        print ("card id: %s "%self.carId)
        print ("trip id: %s "%self.tripId)
        print ("file: %s "%self.file)
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
        
    def sortedPrint(self):
        print sortedDictValue(self.an_segs_title)
        print sortedDictValue(self.an_segs)


def sortedDictValue(adict):
    keys = adict.keys()
    keys.sort()
    return [adict[key] for key in keys] 