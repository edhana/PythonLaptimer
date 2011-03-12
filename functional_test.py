import unittest
from mockito import *
import os

from src import GPS # Keep Consistency with the REAL spec for this module
from src import main

class TestFunctional (unittest.TestCase):
    def setUp(self):
        self.log_file = open(main.GPS_LOG_FILE_NAME, 'w')
        
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
        
    def test_should_return_a_formated_message_when_gps_message_is_valid(self):
        when(GPS).getActualPosition().thenReturn('225109.000,1545.1554S,04752.9177W,0.6,1066.3,3,190.05,0.03,0.01,261010,10')
        gps_data = main.get_formated_gps_data()
        
        self.assertEqual(gps_data[0:10], '225109.000')

    def test_should_validate_minimum_speed(self):
        # Speed 0.03 km/h
        when(GPS).getActualPosition().thenReturn('225109.000,1545.1554S,04752.9177W,0.6,1066.3,3,190.05,0.03,0.01,261010,10')
        main.loop(self.log_file)

        # Reopens the file -- only for read
        self.log_file = self.log_file = open(main.GPS_LOG_FILE_NAME, 'r')
        
        self.assertEqual(self.log_file.readline(), '')
        
    def test_should_save_data_when_speed_is_greater_than_10kmh(self):
        # Speed 11.03 km/h
        when(GPS).getActualPosition().thenReturn('225109.000,1545.1554S,04752.9177W,0.6,1066.3,3,190.05,11.03,0.01,261010,10')
        main.loop(self.log_file)

        # Reopens the file -- only for read
        self.log_file = self.log_file = open(main.GPS_LOG_FILE_NAME, 'r')
        
        self.assertEqual(self.log_file.readline(), '225109.000,1545.1554S,04752.9177W,3,190.05,11.03\n')
        
if __name__ == '__main__':
    # unique = unittest.TestSuite()
    #     unique.addTest(TestFunctional('test_should_send_a_start_message'))
    #     unittest.TextTestRunner().run(unique)
    unittest.main()
        
        