import unittest
from mockito import *

import src.GPS # Keep's Consistency with the REAL spec for this module

class TestFunctional (unittest.TestCase):
    def setUp(self):
        pass
        # self.serialInterface = SerialInterface('karmonitor.log')
        # self.gprs = GPRS(self.serialInterface, GPRS.OPERATOR_VIVO)
        # self.kClient = MessageFactory('KAR', 1234, 4)
        # when(PropertiesLoader).get_splitted_plate().thenReturn(['TTT', 1111])
        # when(GPS).getActualPosition().thenReturn('225109.000,1545.1554S,04752.9177W,0.6,1066.3,3,190.05,0.03,0.01,261010,10')

    def test_should_send_a_message_when_everything_goes_right(self):
        pass