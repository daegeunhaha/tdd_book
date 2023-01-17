import unittest
from dollar import Dollar
from franc import Franc

class Test(unittest.TestCase):

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')

    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('teardownclass')

    def testMultiplication(self):
        five = Dollar(5)
        self.assertTrue(Dollar(10) == five.times(2))
        self.assertTrue(Dollar(15) == five.times(3))

    def testEquality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
        self.assertTrue(Franc(5) == Franc(5))
        self.assertFalse(Franc(5) == Franc(6))
        self.assertFalse(Dollar(5) == Franc(5))

    def testFrancMultiplication(self):
        five = Franc(5)
        self.assertTrue(Franc(10) == five.times(2))
        self.assertTrue(Franc(15) == five.times(3))
