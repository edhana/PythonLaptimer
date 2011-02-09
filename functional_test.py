import unittest
from mockito import *
import os

from src import GPS # Keep Consistency with the REAL spec for this module
from src import main

class TestFunctional (unittest.TestCase):
    def setUp(self):
        self.log_file = open(main.GPS_LOG_FILE_NAME, 'w')
        when(GPS).getActualPosition().thenReturn('225109.000,1545.1554S,04752.9177W,0.6,1066.3,3,190.05,0.03,0.01,261010,10')
        
    def tearDown(self):
        if self.log_file != None:
            # logfile = None

            try:
                # logfile = open(main.GPS_LOG_FILE_NAME, 'r')
            
                # Delete the file
                if self.log_file != None:
                    self.log_file.close()
                    os.remove(main.GPS_LOG_FILE_NAME)
                
            except IOError:
                print "\nThe file %s was not found"%main.GPS_LOG_FILE_NAME
                
    def test_sould_return_true_when_a_valid_message_is_passed(self):
        invalid_message = '225109.000,1545.1554S,04752.9177W,0.6,1066.3,3,190.05,0.03,0.01,261010,10'
        spl_message = invalid_message.split(',')

        self.assertTrue(main.is_valid_message(spl_message))
                    
    def test_sould_return_false_when_an_invalid_message_is_passed(self):
        invalid_message = '235948.043,,,,,0,,,,140209,00'
        spl_message = invalid_message.split(',')
        
        self.assertFalse(main.is_valid_message(spl_message))
        
        
    # def test_should_get_formated_gps_data(self):
    #     string_to_write = "Testing"
    #     readed_string = ""
    #     
    #     formated_data = main.get_formated_gps_data()
    #     self.assertTrue(formated_data != "")
    #     
        # self.assertEquals(readed_string, string_to_write)

if __name__ == '__main__':
    # unique = unittest.TestSuite()
    #     unique.addTest(TestFunctional('test_should_send_a_start_message'))
    #     unittest.TextTestRunner().run(unique)
    unittest.main()
        
        