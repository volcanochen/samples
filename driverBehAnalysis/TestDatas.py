import unittest
from Datas import *

class DatasTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_analyse(self):
        data_list = [-6.69,
                     -0.5,
                     -0.69 ,
                     2.68,
                     4.7,
                     4.98,
                     5.87,
                     6.67,
                     8.3 ]
        a = Data_trip("test","test","")
        a.analyse(data_list)

    
    def test_Datas_mainflow(self):
        a= Datas()
        file =  r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\VF3CU9HP0EY156880.trip_0.csv"
        folder = r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880"
        a.initFromFolder(folder)
        a.analyseAll()
        a.cvsExport(r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\total.export.acc.csv")
        
    @unittest.skip("demonstrating skipping")
    def test_Data_trip(self):
        a = Data_trip("VF3CU9HP0EY156880",0,r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\VF3CU9HP0EY156880.trip_0.csv")
        a.start()
    @unittest.skip("demonstrating skipping")   
    def test_Data_show(self):
        a = Data_trip("VF3CU9HP0EY156880",0,r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\VF3CU9HP0EY156880.trip_0.csv")
        a.start()
        a.show()
        
    @unittest.skip("demonstrating skipping")
    def test_Data_trip_exportfile(self):
        a = Data_trip("VF3CU9HP0EY156880",0,r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\VF3CU9HP0EY156880.trip_0.csv")
        a.start()
        a.csvExport(r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\VF3CU9HP0EY156880.trip_0.export.csv")
        
    @unittest.skip("demonstrating skipping") 
    def test_Data_trip_readdata(self):
        a = Data_trip("VF3CU9HP0EY156880",0,r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880\VF3CU9HP0EY156880.trip_0.csv")
        a.readData()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DatasTest("test_Data_trip_readdata"))