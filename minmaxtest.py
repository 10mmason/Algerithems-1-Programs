import minmax
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        inp = [1,2,3,4,5]
        expmin = 1
        assert minmax.mini(inp) == expmin #test 1 fails
    
    def test2(self):
        inp = [2,3,4,5,6]
        expmin = 2
        assert minmax.mini(inp) == expmin #test 2 fails
if __name__ == '__main__':
    unittest.main()