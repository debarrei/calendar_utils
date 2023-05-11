from datetime import datetime
import ics
import unittest

class Test(unittest.TestCase):

 
    def test_ok(self):
        event_text = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
BEGIN:VEVENT
SUMMARY:summary
DTSTART;VALUE=DATE:20230318T133000
DTEND;VALUE=DATE:20230318T143000
DESCRIPTION:description
END:VEVENT
END:VCALENDAR"""
        self.assertEqual(ics.generate_text("summary", "description", datetime(2023,3,18,13,30,00), datetime(2023,3,18,14,30,00)), event_text)

    def test_empty_startdate_not_datetime(self):
        self.assertEqual(ics.generate_text("summary", "description", 4, datetime(2023,3,18,14,30,00)), -1)

    def test__enddate_not_datetime(self):
        self.assertEqual(ics.generate_text("summary", "description", datetime(2023,3,18,13,30,00), 4), -1)

    def test_past_start_date(self):
        self.assertEqual(ics.generate_text("summary", "description", datetime(2022,2,18,13,46,00), datetime(2023,2,18,15,46,00)), -1)

    def test_start_later_then_end(self):
        self.assertEqual(ics.generate_text("summary", "description", datetime(2023,3,18,13,30,00), datetime(2023,3,18,12,30,00)), -1)

    def test_none_summary(self):
        self.assertEqual(ics.generate_text(None, "description", datetime(2023,3,18,13,30,00), datetime(2023,3,18,14,30,00)), -1)

    def test_none_description(self):
        self.assertEqual(ics.generate_text("summary", None, datetime(2023,3,18,13,30,00), datetime(2023,3,18,14,30,00)), -1)

    def test_none_startdate(self):
        self.assertEqual(ics.generate_text("summary", "description", None, datetime(2023,3,18,14,30,00)), -1)

    def test_none_enddate(self):
        self.assertEqual(ics.generate_text("summary", "description", datetime(2023,3,18,13,30,00), None), -1)


if __name__ == '__main__':
    unittest.main()
    