import unittest
import tempfile
from storage import initialize_database
import sqlite3


class TestStorage(unittest.TestCase):
    def test_initialize_database_creates_job_applications_table(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = f"{temp_dir}/test.db"
            initialize_database(db_path)

            connection = sqlite3.connect(db_path)

            rows = connection.execute("SELECT * FROM job_applications").fetchall()

            connection.close()

            self.assertEqual(rows, [])
