from PSA_Package.PSA_Trips import *

if __name__ == "__main__": 

    #myCSV = PSA_Trips("C:\\local_data\\codecenter\\PSA_Project\\")
    
    #myCSV.read_splitTrps_SingleCSV("VF3CU9HP0EY156880.csv")
    #myCSV.splitTrips()
    path = "G:\\PSA\\PSA_CSV\\"
    myCSV = PSA_Trips(path)
    
    #myCSV.splitTrips()
    myCSV.cal_speed_distribution()
    #myCSV.cal_speed_distribution_single("VF30A9HR8BS348643.trip_38.csv")
    print "done"
   