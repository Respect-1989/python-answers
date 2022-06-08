import unittest
from name import get_full_name

class NameTest(unittest.TestCase): #Create class with NaeTest name 
    def test_toliq_ism(self):        # Create new function 
        name=get_full_name("alijon","valiev")
        self.assertEqual(name,'Alijon Valiev')
    def test_toliq_otasi(self):
        name=get_full_name("alijon","valiev","olimovich")
        self.assertEquals(name,"Alijon Olimovich Valiev")
    
unittest.main()

