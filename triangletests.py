import triangle
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        assert triangle.area(3,2) == 3 #test 1 fails
            
    def test2(self):
        assert triangle.area(4,3) == 6 #test 2 fails
 

if __name__ == '__main__':
    unittest.main()