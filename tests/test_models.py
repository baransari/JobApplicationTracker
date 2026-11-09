import unittest
from models import JobApplication
from datetime import date


class TestModels(unittest.TestCase):
    def test_valid_job_application_uses_applied_status(self):
        application = JobApplication(
            application_id="APP-TEST",
            company_name="Example Corp",
            position_title="Python Developer",
            applied_on=date(2025, 10, 11),
        )

        self.assertEqual(application.status, "applied")

    def test_job_application_rejects_blank_application_id(self):
        with self.assertRaises(ValueError):
            JobApplication(
                application_id="",
                company_name="Example Corp",
                position_title="Python Developer",
                applied_on=date(2025, 10, 11),
            )

    def test_job_application_rejects_blank_company_name(self):
        with self.assertRaises(ValueError):
            JobApplication(
                application_id="APP-TEST",
                company_name="",
                position_title="Python Developer",
                applied_on=date(2025, 10, 11),
            )

    def test_job_application_rejects_blank_position_title(self):
        with self.assertRaises(ValueError):
            JobApplication(
                application_id="APP-TEST",
                company_name="Example Corp",
                position_title="",
                applied_on=date(2025, 10, 11),
            )

    def test_job_application_rejects_invalid_status(self):
        with self.assertRaises(ValueError):
            JobApplication(
                application_id="APP-TEST",
                company_name="Example Corp",
                position_title="Python Developer",
                applied_on=date(2025, 10, 11),
                status="intervew",
            )

    def test_job_application_rejects_non_date_applied_on(self):
        with self.assertRaises(TypeError):
            JobApplication(
                application_id="APP-TEST",
                company_name="Example Corp",
                position_title="Python Developer",
                applied_on="TIME",
            )
