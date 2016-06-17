import unittest
from exercise1 import Calculator

class mytest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        caltor = Calculator('3*4.0+(-3+5*+3+(4+4+4))/2')
        self.assertEqual(caltor.get_res(), '24.0', 'test 1 fail')

    def test2(self):
        caltor = Calculator('3*4.0+(-3+5*+3+(4+-4+4))/2')
        self.assertEqual(caltor.get_res(), '20.0', 'test 2 fail')

    def test3(self):
        caltor = Calculator('1 -2 * ((60-30+123*99)-(-4*3)/ (16-3*2))')
        self.assertEqual(caltor.get_res(), '-24415.4', 'test 3 fail')


if __name__ =='__main__':
    unittest.main()