import unittest
import tempfile
from storage import (
    initialize_database,
    insert_application,
    get_all_applications,
    update_application_status,
)
import sqlite3
from models import JobApplication
from datetime import date


class TestStorage(unittest.TestCase):
    def test_initialize_database_creates_job_applications_table(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = f"{temp_dir}/test.db"
            initialize_database(db_path)

            connection = sqlite3.connect(db_path)

            rows = connection.execute("SELECT * FROM job_applications").fetchall()

            connection.close()

            self.assertEqual(rows, [])

    def test_insert_application_saves_application_to_database(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = f"{temp_dir}/test.db"
            initialize_database(db_path)

            application = JobApplication(
                application_id="APP-TEST",
                company_name="Example Corp",
                position_title="Python Developer",
                applied_on=date(2025, 10, 11),
            )

            insert_application(application, db_path)

            connection = sqlite3.connect(db_path)
            row = connection.execute("SELECT * FROM job_applications").fetchone()
            connection.close()

            self.assertEqual(row[0], "APP-TEST")
            self.assertEqual(row[1], "Example Corp")
            self.assertEqual(row[2], "Python Developer")
            self.assertEqual(row[3], "2025-10-11")

    def test_get_all_applications_returns_saved_applications(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = f"{temp_dir}/test.db"
            initialize_database(db_path)

            application1 = JobApplication(
                application_id="APP-1",
                company_name="Example Corp",
                position_title="Python Developer",
                applied_on=date(2025, 10, 11),
            )

            application2 = JobApplication(
                application_id="APP-2",
                company_name="Example Corp",
                position_title="React Developer",
                applied_on=date(2025, 11, 12),
            )

            insert_application(application1, db_path)
            insert_application(application2, db_path)

            load_applications = get_all_applications(db_path)

            self.assertEqual(len(load_applications), 2)

            applications_id = []

            for application in load_applications:
                applications_id.append(application.application_id)

            self.assertIn("APP-1", applications_id)
            self.assertIn("APP-2", applications_id)

            found_application = None

            for application in load_applications:
                if application.application_id == "APP-1":
                    found_application = application
                    break

            self.assertIsNotNone(found_application)
            self.assertEqual(found_application.company_name, "Example Corp")
            self.assertEqual(found_application.position_title, "Python Developer")
            self.assertEqual(found_application.applied_on, date(2025, 10, 11))

    def test_update_application_status_changes_saved_status(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = f"{temp_dir}/test.db"
            initialize_database(db_path)

            application = JobApplication(
                application_id="APP-UPDATE",
                company_name="Example Corp",
                position_title="Python Developer",
                applied_on=date(2025, 10, 11),
            )

            insert_application(application, db_path)
            update_application_status("APP-UPDATE", "interview", db_path)

            connection = sqlite3.connect(db_path)
            row = connection.execute(
                "SELECT status FROM job_applications WHERE application_id = ?",
                ("APP-UPDATE",),
            ).fetchone()

            connection.close()

            self.assertEqual(row[0], "interview")
