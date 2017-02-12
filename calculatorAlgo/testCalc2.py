import unittest
from calculator import simpleCalc
#import simpleCalc
#from testlib.testcase import BaseTestCase

class testCalc(unittest.TestCase):
    
    # set up the tests by instantiating a simpleCalc object as calc
    def setUp(self):
        self.calc = simpleCalc()
    
    def runTest(self):
        self.assertEqual(self.calc.subtract(7,3),4)
        #self.test_add()
        #self.test_sub()
'''
    # test a simple addition case
    def test_add(self):
        self.assertEqual(self.calc.add(5,4), 9)
    
    # test a simple subtraction case    
    def test_sub(self):
        self.assertEqual(self.calc.subtract(7,3),4)
    
    # returns the full test suite for the calculator object
    def calc_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(testCalc('test_add'))
        suite.addTest(testCalc('test_sub'))
        return suite
'''
if __name__ == '__main__':
    unittest.main()