import os
import re
import csv
import pandas as pd


def sortedDictValue(adict):
    keys = adict.keys()
    keys.sort()
    return [adict[key] for key in keys] 


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
            
    def cvsExportAcc(self, outfile):
        outputfile = open(outfile, 'wb')
        
        an_segs_title = {}
        for i  in self.datas_card:  #{carid : Datas_car}
            for j in self.datas_card[i].datas_trips_acc: # {tripid: Data_trip}
                an_segs_title = self.datas_card[i].datas_trips_acc[j].an_segs_title
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
            for tr in self.datas_card[ca].datas_trips_acc: # {tripid: Data_trip}
                cardid = ca
                tripid = tr
                starttime = self.datas_card[ca].datas_trips[tr].starttime
                endtime = self.datas_card[ca].datas_trips[tr].endtime
                tripData1 = self.datas_card[ca].datas_trips_acc[tr].an_segs
                tripData2 = self.datas_card[ca].datas_trips_acc[tr].an_segs_persentage
                line = ""
                line += "%s,%s,%s,%s," %(cardid, tripid,starttime, endtime)
                for i in sortedDictValue(tripData1):
                    line += "%s,"%i
                for i in sortedDictValue(tripData2):
                    line += "%f,"%i
                outputfile.write(line+ "\n")
   
        outputfile.close()
    def cvsExportAccacc(self, outfile):
        outputfile = open(outfile, 'wb')
        
        an_segs_title = {}
        for i  in self.datas_card:  #{carid : Datas_car}
            for j in self.datas_card[i].datas_trips_accacc: # {tripid: Data_trip}
                an_segs_title = self.datas_card[i].datas_trips_accacc[j].an_segs_title
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
            for tr in self.datas_card[ca].datas_trips_accacc: # {tripid: Data_trip}
                cardid = ca
                tripid = tr
                starttime = self.datas_card[ca].datas_trips[tr].starttime
                endtime = self.datas_card[ca].datas_trips[tr].endtime
                tripData1 = self.datas_card[ca].datas_trips_accacc[tr].an_segs
                tripData2 = self.datas_card[ca].datas_trips_accacc[tr].an_segs_persentage
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
        self.datas_trips_acc = dict() # {1: data_trip_acc}
        self.datas_trips_accacc = dict() # {1: data_trip_accacc}
        
    def analyse(self):
        print("in analysing "+ self.carId)
        for trip in self.trip_file_dict:
            
            f = csvFile(self.trip_file_dict[trip]) #per trip file
            acclist, accacclist = f.readData()
            #print acclist
           # print accacclist
            
            # trip
            a = Data_trip(self.carId, trip, self.trip_file_dict[trip], f.starttime, f.endtime)
            self.datas_trips[trip]=a
            
            #trip acc
            acc = Data_trip_acc()
            acc.analyse(acclist)
            self.datas_trips_acc[trip]=acc
            
            #trip accacc
            accacc = Data_trip_accacc()
            accacc.analyse(accacclist)
            self.datas_trips_accacc[trip]=accacc
  

class csvFile: 
    def __init__(self, file):
        self.starttime = 0
        self.endtime = 0
        self.file = file
    def calStartEndTime(self, min, max):
        if self.starttime == 0:
            self.starttime = min
        if max > self.endtime:
            self.endtime = max

    def readData(self):
        print "processing %s"%self.file
        accelerate = []
        acc_accelerate = []
        self.tsColumn = 3
        self.speedColumn = 23
        
        df = pd.read_csv(self.file ,sep=",")
        column_count =  df.shape[1]  
        row_count = df.shape[0]
        print "column X row : %d * %d" % (column_count, row_count)
        last_acc_ts = 0
        last_acc = 0
        for i in range (row_count - 1):
            t1 = df.loc[i][self.tsColumn] #timestamp
            t2 = df.loc[i + 1][self.tsColumn]

            self.calStartEndTime(t1,t2)

            speed1 = df.loc[i][self.speedColumn] #speed
            speed2 = df.loc[i + 1][self.speedColumn]  

            
            if t2 - t1 == 1000:
                if speed2 != 0 or speed1 != 0:
                    acc = speed2 - speed1
                    accelerate.append (acc) 
                    if t2 - last_acc_ts == 1000:
                        acc_accelerate.append (acc - last_acc) 
                    else :
                        print "accacc - time diff error - %d" % (t2 - last_acc_ts)
                    last_acc_ts = t2
                    last_acc = acc
            else:
                print "accelerate - time diff error - %d" % (t2 -t1)
    
        #print accelerate 
        return accelerate, acc_accelerate
    
class Data_trip:
    def __init__(self, cardId , trip, file, starttime, endtime):
        self.carId = cardId
        self.tripId = trip
        self.file = file
        self.starttime = starttime
        self.endtime = endtime
        
class Data_trip_acc:
        
    def __init__(self):
        print "init"

        self.an_seg_size = 1
        self.an_seg_count = 20
        self.an_segs = dict()  # {seg_id : count}
        self.an_segs_persentage = dict() # {seg_id : 0.02}
        self.an_segs_title = dict()  # {seg_id : seg_title}
        self.total_data = 0


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
        
    def analyse(self, acc_data_list):
        
        if isinstance(self.an_seg_size,float):
            titleFormat = "(%.2f-%.2f)"
            titleEdge1Format = "(%.2f-)"
            titleEdge2Format = "(-%.2f)"
        else:
            titleFormat = "(%d-%d)"
            titleEdge1Format = "(%d-)"
            titleEdge2Format = "(-%d)"
        
        
        seg_distr_count_dict = dict()
        
        for item in acc_data_list:
            seg_distr = int(float(item)/self.an_seg_size) + (1 if (float(item))>0 else -1) #  -2 -1 1 2
            if seg_distr_count_dict.has_key(seg_distr):
                num = seg_distr_count_dict[seg_distr] + 1
                seg_distr_count_dict[seg_distr] = num
            else:
                seg_distr_count_dict[seg_distr] = 1

        self.total_data = float(len(acc_data_list))
        
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

class Data_trip_accacc:
        
    def __init__(self):
        print "init"

        self.an_seg_size = 1
        self.an_seg_count = 20
        self.an_segs = dict()  # {seg_id : count}
        self.an_segs_persentage = dict() # {seg_id : 0.02}
        self.an_segs_title = dict()  # {seg_id : seg_title}
        self.total_data = 0

        
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

