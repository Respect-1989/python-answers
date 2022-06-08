import unittest
from max_nums import maxnum

class MaxNumTest(unittest.TestCase):
    def get_MaxNum(self):
        
        self.assertAlmostEquals(maxnum(),7)
       
unittest.main()
