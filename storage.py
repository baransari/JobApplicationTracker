import sqlite3


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
