import unittest
from circle import getArea,getPerimetr

class CircleTest(unittest.TestCase):
    
    
    def test_area(self):
        #self.assertEqual(getArea(5),78.53975)
        self.assertAlmostEquals(getArea(5),78.53975,2)# Nuqtadan so'ng 2 xonagacha tekshir]
    def test_perimetr(self):
        self.assertEqual(getPerimetr(5),31.4159)
            
unittest.main()