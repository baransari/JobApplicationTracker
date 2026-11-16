import unittest
from services import change_application_status


class TestServices(unittest.TestCase):
    def test_change_application_status_rejects_invalid_status(self):
        with self.assertRaises(ValueError):
            change_application_status("CORP-1", "intervew")
