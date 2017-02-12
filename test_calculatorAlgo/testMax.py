from testlib.testcase import BaseTestCase

class testMax(TestCase):
    # testing max calculator function
    
    def setUp(self):
        self.calc = calcMax()
        
    def runTest(self):
        arr = [3,2,4,1]
        self.assertEqual(self.calc.findMax(arr),4)
        
    if __name__ == '__main__':
        unittest.main()