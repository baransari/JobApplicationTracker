import sqlite3
from models import JobApplication
from datetime import date


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


def get_all_applications(db_path: str = "applications.db") -> list[JobApplication]:
    connection = sqlite3.connect(db_path)
    rows = connection.execute("SELECT * FROM job_applications").fetchall()

    connection.close()

    applications = []

    for row in rows:
        application = JobApplication(
            application_id=row[0],
            company_name=row[1],
            position_title=row[2],
            applied_on=date.fromisoformat(row[3]),
            status=row[4],
            notes=row[5],
        )

        applications.append(application)

    return applications


def update_application_status(
    application_id: str, new_status: str, db_path: str = "applications.db"
) -> None:
    connection = sqlite3.connect(db_path)

    update_sql = """
        UPDATE job_applications
        SET status = ?
        WHERE application_id = ?
        
    """

    connection.execute(update_sql, (new_status, application_id))

    connection.commit()
    connection.close()
