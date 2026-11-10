import unittest
import tempfile
from storage import initialize_database, insert_application
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
