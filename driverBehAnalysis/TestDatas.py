import unittest
from Datas import *

class DatasTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_analyse(self):
        data_list = [-6.69,
                     -0.5,
                     -0.69 ,
                     -0.1,
                     0.2,
                     0.5,
                     2.68,
                     4.7,
                     4.98,
                     5.87,
                     6.67,
                     8.3 ]
        a = DistributeMethod()
        a.an_seg_size = 0.5
        a.an_seg_count = 4
        a.analyse(data_list)
        a.show()



    @unittest.skip("demonstrating skipping")       
    def test_MidDistributeMethod_analyse(self):
        a = MidDistributeMethod()
        a.analyse([1,0.1,0,0.2,0.4])
        a.show()
        assert a.midDistPr == 0.6
    @unittest.skip("demonstrating skipping")     
    def test_VarianceMethod_analyse(self):    
        a  =VarianceMethod()
        a.analyse([1,2,3])
        a.show()
        assert a.mean == 2
        assert a.var == 2/float(3)
        
    
    def test_NOT_A_TEST(self):
        a= Datas()
        folder = r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880"

        a.initFromFolder(folder)
        a.analyseAll()
        #a.show()
        a.cvsExportIdleMax      (r"%s\total.export.table_idle.csv"%folder)
        a.cvsExportAcc          (r"%s\total.export.table_acc.csv"%folder)
        a.cvsExportAccacc       (r"%s\total.export.table_accacc.csv"%folder)
        a.cvsExportHeading      (r"%s\total.export.table_heading.csv"%folder)
    @unittest.skip("demonstrating skipping")      
    def test_Datas_mainflow(self):
        a= Datas()
        
        folder = r"C:\+work\++ 2017 ++\NGCVC\analysis\VF3CU9HP0EY156880TEST"
        a.initFromFolder(folder)
        a.analyseAll()
        a.show()
        a.cvsExportIdleMax      (r"%s\total.export.table_idle.csv"%folder)
        #a.cvsExportAcc          (r"%s\total.export.table_acc.csv"%folder)
        #a.cvsExportAccacc       (r"%s\total.export.table_accacc.csv"%folder)
        a.cvsExportHeading      (r"%s\total.export.table_heading.csv"%folder)



def suite():
    suite = unittest.TestSuite()
    suite.addTest(DatasTest("test_Data_trip_readdata"))