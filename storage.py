import sqlite3
from models import JobApplication


def initialize_database(db_path: str = "applications.db") -> None:
    connection = sqlite3.connect(db_path)
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS job_applications (
            application_id TEXT PRIMARY KEY,
            company_name TEXT NOT NULL,
            position_title TEXT NOT NULL,
            applied_on TEXT NOT NULL,
            status TEXT NOT NULL,
            notes TEXT NOT NULL DEFAULT ''
        )
    """
    )

    connection.commit()
    connection.close()


def insert_application(
    application: JobApplication, db_path: str = "applications.db"
) -> None:
    connection = sqlite3.connect(db_path)
    insert_sql = """
    INSERT INTO job_applications (
        application_id,
        company_name,
        position_title,
        applied_on,
        status,
        notes
    )

    VALUES (?, ?, ?, ?, ?, ?)
    
    """

    connection.execute(
        insert_sql,
        (
            application.application_id,
            application.company_name,
            application.position_title,
            application.applied_on.isoformat(),
            application.status,
            application.notes,
        ),
    )

    connection.commit()
    connection.close()
