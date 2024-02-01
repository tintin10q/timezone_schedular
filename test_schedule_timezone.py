import unittest

import schedule_timezone
import datetime as dt


class TestScheduleTimezone(unittest.TestCase):
    """ Might be wrong if summer and stuff happens """

    def test_alpha2(self):
        result = schedule_timezone.get_local_time_for_remote_time_alpha2("NL", "US", "12:00")
        hours = result.strftime("%H:%M")
        self.assertEqual(hours, "18:00")

    def test_timezone(self):
        result = schedule_timezone.get_local_time_for_remote_time("Europe/Amsterdam", "Brazil/West", "12:00")
        hours = result.strftime("%H:%M")
        self.assertEqual(hours, "17:00")

    def test_datetime(self):
        result = schedule_timezone.get_local_time_for_remote_time("Europe/Amsterdam", "Brazil/West", "12:00")
        self.assertIsInstance(result, dt.datetime)
