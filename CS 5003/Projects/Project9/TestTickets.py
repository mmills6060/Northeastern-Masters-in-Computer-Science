# File which will hold a stack data strcture
# 4/4/2023
# Implemented by Michael Mills


# create unittest that tests stack.py which includes valid strings, invalid strings, and empty strings
#  This is the fifth test
# This is another test 

import unittest
from queue import Queue
from io import StringIO
from unittest.mock import patch
from Tickets import ticket_line, main

class TestTicketLine(unittest.TestCase):
    
    def test_ticket_line(self):
        num_people_list = []
        num_remaining, num_people_list = ticket_line(num_people_list)
        
        self.assertLessEqual(len(num_people_list), 100)
        

if __name__ == '__main__':
    unittest.main()

