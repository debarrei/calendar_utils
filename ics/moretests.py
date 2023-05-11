from datetime import datetime
import ics
import unittest

class Test(unittest.TestCase):


#@unittest.skip("da error?")
    def test_empty_summary(self):
        self.assertEqual(ics.generate_text("", "description", datetime(2023,3,18,13,30,00), datetime(2023,3,18,14,30,00)), -1)

    def test_empty_description(self):
        self.assertEqual(ics.generate_text("summary", "", datetime(2023,3,18,13,30,00), datetime(2023,3,18,14,30,00)), -1)

    def test_empty_startdate(self):
        self.assertEqual(ics.generate_text("summary", "description", "", datetime(2023,3,18,14,30,00)), -1)

    def test_empty_enddate(self):
        self.assertEqual(ics.generate_text("summary", "description", datetime(2023,3,18,13,30,00), ""), -1)